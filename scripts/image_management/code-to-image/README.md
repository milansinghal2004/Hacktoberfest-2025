# ✨ Code-to-Image (Carbon Clone)

A high-performance Python CLI tool that transforms raw source code into professional, "designer" screenshots. Stop sharing messy terminal snippets and start sharing polished, high-fidelity images with syntax highlighting, dynamic backgrounds, and a sleek macOS-style aesthetic.

## 🚀 Key Features

-   **🎨 Dynamic "Formal" Backgrounds**: Every image generated features a unique, randomized gradient. The colors are algorithmically selected to be subtle and dark, ensuring they "vibe" perfectly with dark-themed code without being distracting.
-   **🌈 Intelligent Syntax Highlighting**: Powered by the industry-standard `Pygments` engine. It automatically detects the programming language and applies a beautiful theme (defaulting to Monokai).
-   **🖥️ Premium Window UI**: Features a macOS-inspired window frame with signature "Traffic Light" buttons (Red/Yellow/Green) and beautifully rounded corners.
-   **☁️ Soft Rounded Shadows**: Unlike basic tools that use sharp box shadows, this clone implements a custom rounded-rect shadow engine to ensure the depth effect matches the window's curvature.
-   **⌨️ Dual Interface Modes**:
    -   **Interactive Menu**: A user-friendly "wizard" mode that guides you through file selection and customization.
    -   **Advanced CLI**: A powerful command-line interface for power users and automation scripts.
-   **🛡️ Robust Error Handling**: Built-in protection against binary file accidental reads (like trying to "convert" an image) and full UTF-8 support for modern codebases.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Pip (Python Package Manager)

### Step-by-Step Installation
1.  **Clone the Repository**:
    ```powershell
    git clone <your-repo-url>
    cd code-to-image
    ```
2.  **Set up a Virtual Environment** (Highly Recommended):
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Install Required Packages**:
    ```powershell
    pip install pygments pillow
    ```

## 📖 Usage Guide

### 1. The Interactive Wizard (Easiest)
Simply type the command with no arguments. It will ask you for your file path, your preferred theme, and the output name.
```powershell
python code_to_image.py
```

### 2. Direct Command Line (Fastest)
Generate an image in one go by providing the filename:
```powershell
python code_to_image.py my_script.py --output post.png
```

### 3. Sharing Snippets Without Files
You can pass raw code directly via the console:
```powershell
python code_to_image.py --code "print('Hello World')" --theme dracula
```

## ⚙️ Configuration Flags

| Flag | Description | Default |
| :--- | :--- | :--- |
| `input` | Position argument for the source file. | N/A |
| `--code` | Raw string of code to render. | N/A |
| `--output` | The filename for the final image. | `code_snippet.png` |
| `--theme` | Pygments style (`monokai`, `dracula`, `friendly`). | `monokai` |
| `--lang` | Explicitly set the language (e.g., `python`, `js`). | Auto-detected |

## 🧪 Troubleshooting
- **UnicodeDecodeError**: Ensure your file is saved with UTF-8 encoding. The tool will warn you if you accidentally try to read a binary file.
- **Font Issues**: The tool looks for `consola.ttf` (Windows standard). If not found, it falls back to common Linux mono fonts or the system default.

## 🤝 Contributing
Feel free to fork this project and add new features like custom font support, social media presets, or more elaborate gradient algorithms!
