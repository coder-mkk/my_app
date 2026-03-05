"""
Icon Manager for PyQt6 Themes
Provides easy access to theme-appropriate icons.
"""

import os

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication

from my_app.utils.paths import get_asset_path


class IconManager:
    """Manages theme-appropriate icons for PyQt6 applications."""

    def __init__(self):
        self.icon_dir = get_asset_path("src/my_app/qt_styles/icons")
        self._cache = {}

    def get_icon(self, icon_name, theme=None):
        """
        Get an icon with appropriate theme coloring.

        Args:
            icon_name (str): Base name of the icon (e.g., 'folder', 'save', 'edit')
            theme (str, optional): 'dark' or 'light'. If None, uses current theme.

        Returns:
            QIcon: The themed icon
        """
        if theme is None:
            # Try to detect current theme from application stylesheet
            app = QApplication.instance()
            if app and app.styleSheet():
                theme = (
                    "dark"
                    if "background-color: #1E1E1E" in app.styleSheet()
                    else "light"
                )
            else:
                theme = "dark"  # Default to dark theme

        cache_key = f"{icon_name}_{theme}"

        if cache_key not in self._cache:
            icon_path = os.path.join(self.icon_dir, f"{icon_name}_{theme}.svg")
            if os.path.exists(icon_path):
                self._cache[cache_key] = QIcon(icon_path)
            else:
                # Fallback to dark theme if light version doesn't exist
                dark_path = os.path.join(self.icon_dir, f"{icon_name}_dark.svg")
                self._cache[cache_key] = (
                    QIcon(dark_path) if os.path.exists(dark_path) else QIcon()
                )

        return self._cache[cache_key]

    def get_folder_icon(self, theme=None):
        """Get folder icon."""
        return self.get_icon("folder", theme)

    def get_file_icon(self, theme=None):
        """Get file icon."""
        return self.get_icon("file", theme)

    def get_save_icon(self, theme=None):
        """Get save icon."""
        return self.get_icon("save", theme)

    def get_open_icon(self, theme=None):
        """Get open icon."""
        return self.get_icon("open", theme)

    def get_close_icon(self, theme=None):
        """Get close icon."""
        return self.get_icon("close", theme)

    def get_settings_icon(self, theme=None):
        """Get settings icon."""
        return self.get_icon("settings", theme)

    def get_search_icon(self, theme=None):
        """Get search icon."""
        return self.get_icon("search", theme)

    def get_add_icon(self, theme=None):
        """Get add icon."""
        return self.get_icon("add", theme)

    def get_delete_icon(self, theme=None):
        """Get delete icon."""
        return self.get_icon("delete", theme)

    def get_edit_icon(self, theme=None):
        """Get edit icon."""
        return self.get_icon("edit", theme)

    def get_copy_icon(self, theme=None):
        """Get copy icon."""
        return self.get_icon("copy", theme)

    def get_paste_icon(self, theme=None):
        """Get paste icon."""
        return self.get_icon("paste", theme)

    def get_play_icon(self, theme=None):
        """Get play icon."""
        return self.get_icon("play", theme)

    def get_pause_icon(self, theme=None):
        """Get pause icon."""
        return self.get_icon("pause", theme)

    def get_stop_icon(self, theme=None):
        """Get stop icon."""
        return self.get_icon("stop", theme)

    def get_refresh_icon(self, theme=None):
        """Get refresh icon."""
        return self.get_icon("refresh", theme)

    def get_download_icon(self, theme=None):
        """Get download icon."""
        return self.get_icon("download", theme)

    def get_upload_icon(self, theme=None):
        """Get upload icon."""
        return self.get_icon("upload", theme)

    def get_info_icon(self, theme=None):
        """Get info icon."""
        return self.get_icon("info", theme)

    def get_warning_icon(self, theme=None):
        """Get warning icon."""
        return self.get_icon("warning", theme)

    def get_error_icon(self, theme=None):
        """Get error icon."""
        return self.get_icon("error", theme)

    def get_heart_icon(self, theme=None):
        """Get heart icon."""
        return self.get_icon("heart", theme)

    def get_star_icon(self, theme=None):
        """Get star icon."""
        return self.get_icon("star", theme)

    def get_home_icon(self, theme=None):
        """Get home icon."""
        return self.get_icon("home", theme)

    def list_available_icons(self):
        """List all available icon names."""
        icons = set()
        for file in os.listdir(self.icon_dir):
            if file.endswith(".svg"):
                name = file.replace("_dark.svg", "").replace("_light.svg", "")
                icons.add(name)
        return sorted(list(icons))


# Global instance for easy access
icon_manager = IconManager()


def get_icon(icon_name, theme=None):
    """Convenience function to get an icon."""
    return icon_manager.get_icon(icon_name, theme)


def get_folder_icon(theme=None):
    """Convenience function to get folder icon."""
    return icon_manager.get_folder_icon(theme)


def get_file_icon(theme=None):
    """Convenience function to get file icon."""
    return icon_manager.get_file_icon(theme)


def get_save_icon(theme=None):
    """Convenience function to get save icon."""
    return icon_manager.get_save_icon(theme)


def get_settings_icon(theme=None):
    """Convenience function to get settings icon."""
    return icon_manager.get_settings_icon(theme)


def get_search_icon(theme=None):
    """Convenience function to get search icon."""
    return icon_manager.get_search_icon(theme)


def get_add_icon(theme=None):
    """Convenience function to get add icon."""
    return icon_manager.get_add_icon(theme)


def get_delete_icon(theme=None):
    """Convenience function to get delete icon."""
    return icon_manager.get_delete_icon(theme)


def get_edit_icon(theme=None):
    """Convenience function to get edit icon."""
    return icon_manager.get_edit_icon(theme)


def get_open_icon(theme=None):
    """Convenience function to get open icon."""
    return icon_manager.get_open_icon(theme)


def get_close_icon(theme=None):
    """Convenience function to get close icon."""
    return icon_manager.get_close_icon(theme)


def get_copy_icon(theme=None):
    """Convenience function to get copy icon."""
    return icon_manager.get_copy_icon(theme)


def get_paste_icon(theme=None):
    """Convenience function to get paste icon."""
    return icon_manager.get_paste_icon(theme)


def get_play_icon(theme=None):
    """Convenience function to get play icon."""
    return icon_manager.get_play_icon(theme)


def get_pause_icon(theme=None):
    """Convenience function to get pause icon."""
    return icon_manager.get_pause_icon(theme)


def get_stop_icon(theme=None):
    """Convenience function to get stop icon."""
    return icon_manager.get_stop_icon(theme)


def get_refresh_icon(theme=None):
    """Convenience function to get refresh icon."""
    return icon_manager.get_refresh_icon(theme)


def get_download_icon(theme=None):
    """Convenience function to get download icon."""
    return icon_manager.get_download_icon(theme)


def get_upload_icon(theme=None):
    """Convenience function to get upload icon."""
    return icon_manager.get_upload_icon(theme)


def get_info_icon(theme=None):
    """Convenience function to get info icon."""
    return icon_manager.get_info_icon(theme)


def get_warning_icon(theme=None):
    """Convenience function to get warning icon."""
    return icon_manager.get_warning_icon(theme)


def get_error_icon(theme=None):
    """Convenience function to get error icon."""
    return icon_manager.get_error_icon(theme)


def get_heart_icon(theme=None):
    """Convenience function to get heart icon."""
    return icon_manager.get_heart_icon(theme)


def get_star_icon(theme=None):
    """Convenience function to get star icon."""
    return icon_manager.get_star_icon(theme)


def get_home_icon(theme=None):
    """Convenience function to get home icon."""
    return icon_manager.get_home_icon(theme)


# Bulk icon assignment functions
def get_all_file_icons(theme=None):
    """Get all file-related icons in one call."""
    return {
        "folder": icon_manager.get_folder_icon(theme),
        "file": icon_manager.get_file_icon(theme),
        "save": icon_manager.get_save_icon(theme),
        "open": icon_manager.get_open_icon(theme),
        "close": icon_manager.get_close_icon(theme),
    }


def get_all_action_icons(theme=None):
    """Get all action-related icons in one call."""
    return {
        "edit": icon_manager.get_edit_icon(theme),
        "copy": icon_manager.get_copy_icon(theme),
        "paste": icon_manager.get_paste_icon(theme),
        "delete": icon_manager.get_delete_icon(theme),
        "add": icon_manager.get_add_icon(theme),
        "search": icon_manager.get_search_icon(theme),
        "refresh": icon_manager.get_refresh_icon(theme),
    }


def get_all_media_icons(theme=None):
    """Get all media control icons in one call."""
    return {
        "play": icon_manager.get_play_icon(theme),
        "pause": icon_manager.get_pause_icon(theme),
        "stop": icon_manager.get_stop_icon(theme),
    }


def get_all_status_icons(theme=None):
    """Get all status/notification icons in one call."""
    return {
        "info": icon_manager.get_info_icon(theme),
        "warning": icon_manager.get_warning_icon(theme),
        "error": icon_manager.get_error_icon(theme),
        "heart": icon_manager.get_heart_icon(theme),
        "star": icon_manager.get_star_icon(theme),
    }


def get_all_system_icons(theme=None):
    """Get all system-related icons in one call."""
    return {
        "settings": icon_manager.get_settings_icon(theme),
        "download": icon_manager.get_download_icon(theme),
        "upload": icon_manager.get_upload_icon(theme),
        "home": icon_manager.get_home_icon(theme),
    }


def get_all_icons(theme=None):
    """Get ALL available icons in one call."""
    return {
        **get_all_file_icons(theme),
        **get_all_action_icons(theme),
        **get_all_media_icons(theme),
        **get_all_status_icons(theme),
        **get_all_system_icons(theme),
    }


def apply_icons_to_widgets(widgets, icon_mapping, theme=None):
    """
    Apply icons to multiple widgets at once.

    Args:
        widgets: Dict of {widget_name: widget_object}
        icon_mapping: Dict of {widget_name: icon_name}
        theme: Optional theme override

    Example:
        widgets = {'save_btn': save_button, 'open_btn': open_button}
        icon_mapping = {'save_btn': 'save', 'open_btn': 'open'}
        apply_icons_to_widgets(widgets, icon_mapping)
    """
    all_icons = get_all_icons(theme)

    for widget_name, icon_name in icon_mapping.items():
        if widget_name in widgets and icon_name in all_icons:
            widgets[widget_name].setIcon(all_icons[icon_name])


def create_toolbar_with_icons(toolbar, icon_list, theme=None, parent=None):
    """
    Create a toolbar with multiple icons at once.

    Args:
        toolbar: QToolBar object
        icon_list: List of (icon_name, action_text, callback) tuples
        theme: Optional theme override
        parent: Optional parent widget for QAction objects

    Example:
        icons = [
            ('save', 'Save', self.save_file),
            ('open', 'Open', self.open_file),
            ('edit', 'Edit', self.edit_file),
        ]
        create_toolbar_with_icons(toolbar, icons, parent=self)
    """
    all_icons = get_all_icons(theme)

    for icon_name, action_text, callback in icon_list:
        if icon_name in all_icons:
            action = QAction(all_icons[icon_name], action_text, parent)
            action.triggered.connect(callback)
            toolbar.addAction(action)
