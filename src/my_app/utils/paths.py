import sys
from pathlib import Path

# This is the root directory of the project.
# It's calculated by going up 3 levels from this file's location:
# paths.py -> utils -> my_app -> src -> PROJECT_ROOT
PROJECT_ROOT = Path(__file__).resolve().parents[3]

__all__ = ["get_asset_path"]


def get_asset_path(relative_path: str | Path) -> Path:
    """
    Get the absolute path to an asset, handling PyInstaller's temp folder.

    The relative_path should be relative to the project root.

    Example: get_asset_path("src/my_app/qt_styles/icons")
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        # We are running in a normal Python environment
        base_path = PROJECT_ROOT

    return base_path / relative_path
