# PyQt6 Boilerplate

A professional, feature-rich boilerplate for building modern desktop applications with Python and PyQt6. This template provides a solid foundation with essential features already built-in, allowing you to focus on your application's core logic.

It is designed to be easily customizable and ready for packaging with PyInstaller.

## ✨ Features

This boilerplate comes packed with features to accelerate your development process:

*   **Project Renaming Script**: A simple, one-time script (`scripts/rename_project.py`) to rename the entire project from the default `my_app` to your custom project name.
*   **Modern Theming**:
    *   Includes beautiful pre-built **dark** and **light** themes.
    *   A theme manager (`qt_styles.manager`) to easily apply themes across your application.
*   **SVG Icon Management**:
    *   A powerful `IconManager` that automatically serves theme-appropriate (dark/light) icons.
    *   Icons are cached for performance.
    *   Dozens of convenience functions (`get_save_icon()`, `get_folder_icon()`, etc.) for easy access.
*   **PyInstaller Ready**:
    *   Includes a `.spec` file for easy building.
    *   A smart asset path utility (`utils.paths.get_asset_path`) that works seamlessly in both development and "frozen" (packaged) modes.
*   **Configuration Management**: Uses `.env` files for easy and secure management of application settings and secrets.
*   **Robust Exception Handling**: A global exception hook that catches unhandled errors, logs them, and displays a user-friendly crash report dialog.
*   **Testing Framework**: Pre-configured with `pytest` and `pytest-qt` for writing and running unit tests.
*   **Sensible Project Structure**: A clean and scalable `src/` layout.
*   **Developer Scripts**: Includes helper scripts, such as a Lines of Code (LOC) counter.

## 🚀 Getting Started

Follow these steps to get your new project up and running.

### 1. Clone the Repository

Start by cloning this repository to your local machine.

```bash
git clone https://github.com/coder-mkk/pyqt6-boilerplate.git my-new-project
cd my-new-project
```

### 2. Set Up a Virtual Environment

It's highly recommended to use a virtual environment. On Windows, use `.venv\Scripts\activate` to activate the environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

This project uses `uv` for fast package management. The dependencies include development tools like `pytest`.

```bash
pip install uv
uv pip install -e .[dev]
```

### 4. Rename the Project

This is the most important step. Run the interactive renaming script to customize the boilerplate for your project.

```bash
python3 scripts/rename_project.py
```

The script will prompt you for a new project name (e.g., "Super Tool") and will automatically:
*   Rename the package directory (`src/my_app` -> `src/super_tool`).
*   Rename the PyInstaller spec file (`my-app.spec` -> `super-tool.spec`).
*   Replace all internal import paths and references.

**Note:** The script will delete itself after running successfully.

### 5. Run the Application

After renaming the project, use the provided development script to run the application. This ensures all paths are correctly configured for development.

```bash
uv run scripts/run_dev.py
```

## 📘 Usage Guide

### Theming

You can apply a theme with a single function call, typically in your `main.py` file before you show the main window.

```python
# In your main application entry point
from my_app.qt_styles.manager import apply_theme

# ... create QApplication instance ...
app = QApplication(sys.argv)

# Apply the dark theme
apply_theme('dark') # or 'light'

# ... create and show your main window ...
```

### Icon Management

The `IconManager` makes it trivial to use icons in your UI. You can use the global convenience functions.

```python
from PyQt6.QtWidgets import QPushButton
from my_app.qt_styles import icon_manager

# Get a specific icon (theme is detected automatically)
save_icon = icon_manager.get_save_icon()

# Use it on a widget
my_button = QPushButton("Save")
my_button.setIcon(save_icon)
```

### Configuration (`.env`)

Create a `.env` file in the project root to manage your settings. A `.env.example` file can be provided to guide users.

```ini
# .env file
APP_NAME="My Awesome App"
LOG_LEVEL="DEBUG"
API_KEY="your-secret-api-key"
```

These settings are loaded in `src/my_app/config/settings.py` and can be accessed throughout your application.

### Asset Handling

When referencing assets like images, data files, or icons that need to be included in your final build, always use the `get_asset_path` utility. This ensures your app can find them whether it's running from source or as a packaged executable.

```python
from my_app.utils.paths import get_asset_path

# The path is relative to the project root
icon_path = get_asset_path("assets/images/logo.png") 
```

## 📦 Building for Distribution

This boilerplate is set up for easy packaging with PyInstaller.

1.  Make sure you have run the `rename_project.py` script.
2.  Install PyInstaller: `uv pip install pyinstaller`.
3.  Run the build command using the `.spec` file that was renamed for you.

```bash
pyinstaller your-project-name.spec
```

The final executable will be located in the `dist/` directory.

## 🧪 Running Tests

The project is configured to use `pytest`. To run the test suite:

```bash
pytest
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.