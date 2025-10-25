# Python Scripts Collection

![Hacktoberfest 2025](https://img.shields.io/badge/Hacktoberfest-2025-orange.svg)
![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains Python scripts designed to automate common tasks. It is beginner-friendly and open for contributions during Hacktoberfest 2025.

## Table of Contents

1. [About](#about)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Project Structure](#project-structure)
6. [Contributors](#contributors)
7. [Contact](#contact)

## About

The repository currently contains the following scripts:

- `file_renamer.py` — Rename all files in a folder with a specific prefix and optional extension filter.
- `image_compressor.py` — Compress images individually or in bulk using Pillow.
- `factorial_calculator.py` — Calculate the factorial of a non-negative integer.
- `password_generator.py` — Generate strong, random passwords with customizable criteria.
- `Folder Cleaner`- Delete files older than n days.
- `PDF Merger` - Merge multiple PDFs into one.
- `Bulk Image Resizer` - Resize all images to a fixed width.
- `CSV to Excel Converter` - Convert all CSV files in a folder to Excel.
- `To Do List` - A simple Python-based To-Do List Manager to add, view, and remove tasks directly from the terminal.
- `Emotion Detection` - Detect emotions from webcam feed using deep learning.
- `Object Detection` - Detects Objects from webcam feed using AI/ML.
- `TicTacToe` - In this game the player has to play through the 3X3 grid on 3X3 where firt player will play the turn and subsequently the secong player moves would be restricted in that child board.
- `Wordle Game` - A Python implementation of Wordle where you guess a 5-letter word in 6 attempts with feedback for correct letters and positions.
- `Email Sender` - Send emails to multiple recipients with optional attachments, including logging and error handling.
- `Library Management System` - A Python program to manage books, track borrowing/returning, and store data persistently.
  
This collection aims to help users automate repetitive tasks efficiently and serve as an introduction to Python scripting and open-source contributions.

## Getting Started

### Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.9+
- Git
- Optional: Node.js (for additional scripts or integration)

### Installation

1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/Hacktoberfest-2025.git
cd Hacktoberfest-2025
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If using Node.js scripts:

```bash
npm install
```

## Usage

1. File Renamer

```bash
from Scripts.file_renamer import rename_files
rename_files("documents", prefix="report", extension=".txt")
```

2. Image Compressor

```bash
from Scripts.image_compressor import compress_folder
compress_folder("images","compressed_images",quality=60)
```

3. Factorial Calculator

```bash
from Scripts.factorial_calculator import factorial
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
```

4. Password Generator

```bash
from Scripts.password_generator import generate_password
print(f"Generated password: {generate_password(length=16, use_symbols=False)}")
```

Both scripts include detailed docstrings and inline comments to guide usage.

5. Emotion Detection
- make sure you are running it on Python 3.9 or above till 3.11.5
- make sure you have keras, tensorflow, opencv-python, numpy installed. You can install them using:
```bash
pip install keras tensorflow opencv-python numpy
```
in terminal.
- run the script using:
```bash
python Scripts/Emotion_Detection/EmotionDetection.py
```
in terminal

6. Object Detection
- make sure you are running it on Python 3.9 or above
- make sure you have tkinter, opencv-python, numpy, Pillow. You can install them using:
- ```bash
  pip install tkinter opencv-python numpy Pillow
  ```
- make sure you download YOLOV3.weights file, check readme file in ` /scripts/Object-Detection-System/ `.
- run the script using:
  ```bash
  python Scripts/Object-Detection-System/main.py
  ```

## Contributing

We welcome contributions of all kinds from improving documentation to adding new scripts.

1. Review the [CONTRIBUTION.md]
   guide.
2. Create a new branch for your changes:

```bash
git checkout -b feat/your-feature-name
```

3. Commit your changes with a descriptive message:

```bash
git commit -m "docs: improve README and add usage examples"
```

4. Push your branch and open a Pull Request.

## CI/CD Automation

This repository uses [GitHub Actions](https://github.com/features/actions) to automate code quality checks and ensure consistency. All automations are defined in the `.github/workflows` directory.

### Python Linter

We have a workflow that automatically runs the `flake8` linter on every pull request. This process checks the Python code for common programming errors, style issues, and complexity.

1.  When a pull request is opened, the workflow is triggered automatically.
2.  It installs Python and the project's dependencies.
3.  It runs `flake8` to analyze the code.

If the linter finds any critical errors, the workflow will fail. A "pass" or "fail" status will be reported on the pull request page. All checks must pass before a pull request can be merged. This ensures that all contributions adhere to our project's coding standards.

## Project Structure
```
.
├── Scripts/ # Contains Python scripts
│ ├── file_renamer.py
│ └── image_compressor.py
├── .gitignore # Files to ignore in Git
├── CONTRIBUTING.md # Contribution guidelines
├── LICENSE # MIT License file
├── README.md # This file
└── WORKFLOW.md # Git and GitHub workflow guide
```

## Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/milansinghal2004>
            <img src=https://avatars.githubusercontent.com/u/118826647?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=MILAN SINGHAL/>
            <br />
            <sub style="font-size:14px"><b>MILAN SINGHAL</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/strikkerJalaj-25>
            <img src=https://avatars.githubusercontent.com/u/205951485?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=strikkerJalaj-25/>
            <br />
            <sub style="font-size:14px"><b>strikkerJalaj-25</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/ArnavP2305>
            <img src=https://avatars.githubusercontent.com/u/153117709?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Arnav Parmar/>
            <br />
            <sub style="font-size:14px"><b>Arnav Parmar</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Vedansh-Rawat>
            <img src=https://avatars.githubusercontent.com/u/207315559?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Vedansh/>
            <br />
            <sub style="font-size:14px"><b>Vedansh</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/devanshsonii>
            <img src=https://avatars.githubusercontent.com/u/139559687?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=runn3r/>
            <br />
            <sub style="font-size:14px"><b>runn3r</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Spartan1-1-7>
            <img src=https://avatars.githubusercontent.com/u/121613262?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Arindam Shukla/>
            <br />
            <sub style="font-size:14px"><b>Arindam Shukla</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Anshul-Bartwal>
            <img src=https://avatars.githubusercontent.com/u/223218288?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Anshul-Bartwal/>
            <br />
            <sub style="font-size:14px"><b>Anshul-Bartwal</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/jalaj-25>
            <img src=https://avatars.githubusercontent.com/u/115914764?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Jalaj Singhal/>
            <br />
            <sub style="font-size:14px"><b>Jalaj Singhal</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/992manav>
            <img src=https://avatars.githubusercontent.com/u/170462638?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Manav Desai/>
            <br />
            <sub style="font-size:14px"><b>Manav Desai</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/csr76>
            <img src=https://avatars.githubusercontent.com/u/138115920?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=csr76/>
            <br />
            <sub style="font-size:14px"><b>csr76</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Jay-1409>
            <img src=https://avatars.githubusercontent.com/u/166749819?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Jay shah/>
            <br />
            <sub style="font-size:14px"><b>Jay shah</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Harshrathore994>
            <img src=https://avatars.githubusercontent.com/u/91665121?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Harsh Rathore/>
            <br />
            <sub style="font-size:14px"><b>Harsh Rathore</b></sub>
        </a>
    </td>
</tr>
</table>

Thanks to these wonderful people for their contributions!

<table>
  <tr>
    </tr>
</table>

## Contact

For questions or support, open an issue and tag the maintainer **@milansinghal2004**.
