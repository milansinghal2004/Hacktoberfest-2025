#!/usr/bin/env python3
"""
Test runner script for factorial calculator

This script provides a simple interface for running all tests and generating reports.
Suitable for use in continuous integration environments.

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py --coverage         # Run tests with coverage
    python run_tests.py --benchmark        # Include performance benchmarks
    python run_tests.py --all              # Run everything with full reporting
"""

import sys
import subprocess
import argparse
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and return the result."""
    print(f"\n{description}")
    print("-" * len(description))
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    
    except Exception as e:
        print(f"Error running command: {e}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version_info = sys.version_info
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 6):
        print("ERROR: Python 3.6 or higher is required")
        return False
    
    print(f"Python version: {version_info.major}.{version_info.minor}.{version_info.micro}")
    return True


def run_basic_tests():
    """Run basic unit tests."""
    python_cmd = sys.executable
    return run_command(
        f"{python_cmd} -m unittest test_factorial_calculator.py -v",
        "Running Basic Unit Tests"
    )


def run_coverage_tests():
    """Run tests with coverage analysis."""
    python_cmd = sys.executable
    
    # Check if coverage is available
    coverage_check = subprocess.run(
        f"{python_cmd} -c 'import coverage'",
        shell=True,
        capture_output=True
    )
    
    if coverage_check.returncode != 0:
        print("Coverage module not available. Install with: pip install coverage")
        return False
    
    # Run coverage
    success = True
    success &= run_command(
        f"{python_cmd} -m coverage run -m unittest test_factorial_calculator.py",
        "Running Tests with Coverage Analysis"
    )
    
    success &= run_command(
        f"{python_cmd} -m coverage report -m",
        "Coverage Report"
    )
    
    return success


def run_performance_benchmarks():
    """Run performance benchmarks."""
    python_cmd = sys.executable
    return run_command(
        f"{python_cmd} test_factorial_calculator.py --benchmark",
        "Running Performance Benchmarks"
    )


def run_code_quality_checks():
    """Run code quality checks if tools are available."""
    python_cmd = sys.executable
    success = True
    
    # Check for flake8
    flake8_check = subprocess.run(
        f"{python_cmd} -c 'import flake8'",
        shell=True,
        capture_output=True
    )
    
    if flake8_check.returncode == 0:
        success &= run_command(
            f"{python_cmd} -m flake8 factorial_calculator.py test_factorial_calculator.py --max-line-length=100",
            "Code Style Check (flake8)"
        )
    else:
        print("\nCode Style Check: flake8 not available (optional)")
    
    return success


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description="Test runner for factorial calculator")
    parser.add_argument("--coverage", action="store_true", help="Run with coverage analysis")
    parser.add_argument("--benchmark", action="store_true", help="Include performance benchmarks")
    parser.add_argument("--quality", action="store_true", help="Run code quality checks")
    parser.add_argument("--all", action="store_true", help="Run all checks and tests")
    
    args = parser.parse_args()
    
    if args.all:
        args.coverage = True
        args.benchmark = True
        args.quality = True
    
    print("Factorial Calculator Test Suite")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    success = True
    
    # Run basic tests
    success &= run_basic_tests()
    
    # Run coverage if requested
    if args.coverage:
        success &= run_coverage_tests()
    
    # Run benchmarks if requested
    if args.benchmark:
        success &= run_performance_benchmarks()
    
    # Run quality checks if requested
    if args.quality:
        success &= run_code_quality_checks()
    
    # Final summary
    print("\n" + "=" * 50)
    if success:
        print("All tests and checks PASSED")
        sys.exit(0)
    else:
        print("Some tests or checks FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()