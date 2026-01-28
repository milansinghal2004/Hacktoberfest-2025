import requests
import json


def get_fact():
    """Fetch a random fact from the Useless Facts API."""
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    data = json.loads(response.text)
    return data["text"]


def main():
    """Main entry point for the random fact generator."""
    print("--- Welcome to my Random Fact Generator ---\n")

    try:
        n = int(input("Enter a number (1-7): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if n > 7:
        print("Maximum number of facts per execution is 7.")
    elif n <= 0:
        print("Minimum number of facts per execution is 1.")
    else:
        for _ in range(n):
            print(get_fact())
            print()


if __name__ == "__main__":
    main()
