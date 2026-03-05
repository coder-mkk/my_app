from my_app.qt_styles import dark, light
from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QAction, QActionGroup
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)
        self._setup_ui()

    def _setup_ui(self):
        self._create_menu_bar()

    def _create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        theme_menu = file_menu.addMenu("Theme")

        theme_group = QActionGroup(self)
        theme_group.setExclusive(True)

        dark_action = QAction("Dark", self)
        dark_action.setCheckable(True)
        dark_action.triggered.connect(lambda: self._apply_theme("dark"))
        theme_menu.addAction(dark_action)
        theme_group.addAction(dark_action)

        light_action = QAction("Light", self)
        light_action.setCheckable(True)
        light_action.triggered.connect(lambda: self._apply_theme("light"))
        theme_menu.addAction(light_action)
        theme_group.addAction(light_action)

        ui_settings = QSettings()
        if ui_settings.value("theme", "dark") == "light":
            light_action.setChecked(True)
        else:
            dark_action.setChecked(True)

        file_menu.addSeparator()

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def _apply_theme(self, theme_name):
        ui_settings = QSettings()
        ui_settings.setValue("theme", theme_name)

        app = QApplication.instance()
        if app:
            if theme_name == "light":
                app.setStyleSheet(light.STYLESHEET)
            else:
                app.setStyleSheet(dark.STYLESHEET)
