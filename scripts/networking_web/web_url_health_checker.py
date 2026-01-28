#!/usr/bin/env python3
"""
Web URL Health Checker

A Python script to monitor website health by checking if URLs are accessible,
measuring response times, and saving results to a file. This tool is useful
for monitoring website uptime, server health, and detecting connectivity issues.

Author: Sukarth
Created for: Hacktoberfest 2025
Date: October 2025
"""

import requests
import time
import json
import csv
from datetime import datetime
from typing import List, Dict, Tuple
import sys
import argparse


class URLHealthChecker:
    """A class to check the health status of URLs."""

    def __init__(self, timeout: int = 10):
        """
        Initialize the URL Health Checker.

        Args:
            timeout (int): Request timeout in seconds (default: 10)
        """
        self.timeout = timeout
        self.results = []

    def check_url(self, url: str) -> Dict:
        """
        Check the health of a single URL.

        Args:
            url (str): The URL to check

        Returns:
            Dict: Dictionary containing check results with keys:
                  - url: The checked URL
                  - status: 'UP' or 'DOWN'
                  - status_code: HTTP status code (or None if failed)
                  - response_time: Response time in milliseconds
                  - timestamp: Check timestamp
                  - error: Error message (if any)
        """
        result = {
            'url': url,
            'status': 'DOWN',
            'status_code': None,
            'response_time': None,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'error': None
        }

        # Ensure URL has a scheme
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            result['url'] = url

        try:
            start_time = time.time()
            response = requests.get(url, timeout=self.timeout, allow_redirects=True)
            end_time = time.time()

            # Calculate response time in milliseconds
            response_time = round((end_time - start_time) * 1000, 2)

            result['status_code'] = response.status_code
            result['response_time'] = response_time

            # Consider 2xx and 3xx status codes as UP
            if 200 <= response.status_code < 400:
                result['status'] = 'UP'
            else:
                result['status'] = 'DOWN'
                result['error'] = f'HTTP {response.status_code}'

        except requests.exceptions.Timeout:
            result['error'] = 'Request timeout'
        except requests.exceptions.ConnectionError:
            result['error'] = 'Connection error'
        except requests.exceptions.TooManyRedirects:
            result['error'] = 'Too many redirects'
        except requests.exceptions.RequestException as e:
            result['error'] = f'Request failed: {str(e)}'
        except Exception as e:
            result['error'] = f'Unexpected error: {str(e)}'

        return result

    def check_urls(self, urls: List[str]) -> List[Dict]:
        """
        Check the health of multiple URLs.

        Args:
            urls (List[str]): List of URLs to check

        Returns:
            List[Dict]: List of check results for all URLs
        """
        self.results = []
        print(f"\nChecking {len(urls)} URL(s)...\n")
        print("-" * 80)

        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] Checking: {url}")
            result = self.check_url(url)
            self.results.append(result)

            # Display result
            status_symbol = "✓" if result['status'] == 'UP' else "✗"
            print(f"{status_symbol} Status: {result['status']}")

            if result['status_code']:
                print(f"  HTTP Status: {result['status_code']}")
            if result['response_time']:
                print(f"  Response Time: {result['response_time']} ms")
            if result['error']:
                print(f"  Error: {result['error']}")
            print("-" * 80)

        return self.results

    def save_to_json(self, filename: str = 'url_health_report.json'):
        """
        Save results to a JSON file.

        Args:
            filename (str): Output filename (default: 'url_health_report.json')
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            print(f"\n✓ Results saved to {filename}")
        except Exception as e:
            print(f"\n✗ Error saving JSON file: {e}")

    def save_to_csv(self, filename: str = 'url_health_report.csv'):
        """
        Save results to a CSV file.

        Args:
            filename (str): Output filename (default: 'url_health_report.csv')
        """
        try:
            if not self.results:
                print("\n✗ No results to save")
                return

            with open(filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['url', 'status', 'status_code', 'response_time', 'timestamp', 'error']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.results)
            print(f"✓ Results saved to {filename}")
        except Exception as e:
            print(f"\n✗ Error saving CSV file: {e}")

    def print_summary(self):
        """
        Print a summary of the health check results.
        """
        if not self.results:
            print("\nNo results to summarize.")
            return

        total = len(self.results)
        up_count = sum(1 for r in self.results if r['status'] == 'UP')
        down_count = total - up_count

        # Calculate average response time for UP URLs
        response_times = [r['response_time'] for r in self.results if r['response_time']]
        avg_response_time = round(sum(response_times) / len(response_times), 2) if response_times else 0

        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print(f"Total URLs checked: {total}")
        print(f"✓ UP: {up_count} ({(up_count/total*100):.1f}%)")
        print(f"✗ DOWN: {down_count} ({(down_count/total*100):.1f}%)")
        if avg_response_time > 0:
            print(f"Average Response Time: {avg_response_time} ms")
        print("="*80)


def read_urls_from_file(filename: str) -> List[str]:
    """
    Read URLs from a text file (one URL per line).

    Args:
        filename (str): Path to the file containing URLs

    Returns:
        List[str]: List of URLs
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return urls
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def main():
    """
    Main function to run the URL Health Checker.
    """
    parser = argparse.ArgumentParser(
        description='Web URL Health Checker - Monitor website uptime and performance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check a single URL
  python web_url_health_checker.py -u https://www.google.com

  # Check multiple URLs
  python web_url_health_checker.py -u https://www.google.com https://github.com

  # Check URLs from a file
  python web_url_health_checker.py -f urls.txt

  # Save results to custom files
  python web_url_health_checker.py -u https://example.com -o custom_report

  # Set custom timeout
  python web_url_health_checker.py -u https://example.com -t 20
        """
    )

    parser.add_argument('-u', '--urls', nargs='+', help='URL(s) to check')
    parser.add_argument('-f', '--file', help='File containing URLs (one per line)')
    parser.add_argument('-o', '--output', default='url_health_report',
                        help='Output filename prefix (default: url_health_report)')
    parser.add_argument('-t', '--timeout', type=int, default=10,
                        help='Request timeout in seconds (default: 10)')
    parser.add_argument('--json', action='store_true', help='Save results as JSON')
    parser.add_argument('--csv', action='store_true', help='Save results as CSV')

    args = parser.parse_args()

    # Collect URLs
    urls = []
    if args.urls:
        urls.extend(args.urls)
    if args.file:
        urls.extend(read_urls_from_file(args.file))

    # If no URLs provided, use example URLs
    if not urls:
        print("No URLs provided. Using example URLs for demonstration...\n")
        urls = [
            'https://www.google.com',
            'https://github.com',
            'https://www.python.org',
            'https://this-site-definitely-does-not-exist-12345.com'
        ]

    # Remove duplicates while preserving order
    urls = list(dict.fromkeys(urls))

    # Create checker and run checks
    checker = URLHealthChecker(timeout=args.timeout)
    checker.check_urls(urls)

    # Print summary
    checker.print_summary()

    # Save results
    if args.json or (not args.json and not args.csv):
        checker.save_to_json(f"{args.output}.json")
    if args.csv or (not args.json and not args.csv):
        checker.save_to_csv(f"{args.output}.csv")

    # Return exit code based on results
    down_count = sum(1 for r in checker.results if r['status'] == 'DOWN')
    return 1 if down_count > 0 else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
