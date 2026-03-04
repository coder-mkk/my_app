
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QTextEdit, QSplitter, QPushButton,
    QLineEdit, QInputDialog, QMessageBox, QLabel
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)
        self._setup_ui()

    def _setup_ui(self):
        pass  # UI setup will be implemented here in the future