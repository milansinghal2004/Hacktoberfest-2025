# Scripts Repository

This directory contains various utility scripts categorized by their functionality. The repository is structured to be clean, well-maintained, and easy to navigate.

## Directory Structure

The scripts are organized into the following categories:

- [ai_ml/](file:///ai_ml/): AI and Machine Learning related scripts (Emotion Detection, Object Detection).
- [data_processing/](file:///data_processing/): Scripts for converting or merging data files (CSV, PDF, Text).
- [development_tools/](file:///development_tools/): Tools for development, testing, and CI/CD.
- [games/](file:///games/): Simple logic-based games (Wordle, Tic-Tac-Toe).
- [image_management/](file:///image_management/): Scripts for image processing (Resizing, Compression, Code-to-Image).
- [management_systems/](file:///management_systems/): Application-like management scripts (Library Management, To-Do List).
- [math_calculators/](file:///math_calculators/): Mathematical and logic calculators.
- [networking_web/](file:///networking_web/): Scripts for web APIs, networking, and information retrieval.
- [security_tools/](file:///security_tools/): Password generators and security-related scripts.
- [system_utilities/](file:///system_utilities/): System automation, file management, and cleaning scripts.

## How to Contribute

We welcome contributions! Please follow these steps:

1.  Find or create a suitable category folder for your script.
2.  Ensure your script is well-documented with docstrings.
3.  If your script has specific dependencies, add them to a `requirements.txt` in your script's folder or the root `requirements.txt` if applicable.
4.  Add a `README.md` in your script's folder if it's a complex project.
5.  Follow the existing naming convention (snake_case).

For more details on contributing to specific tools (like the Factorial Calculator), refer to the `README.md` within their respective folders.

## Running Tests

Some scripts include automated tests. You can find them in the `development_tools/` folder.
To run the main test suite:
```bash
cd development_tools
python run_tests.py
```
