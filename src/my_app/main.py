
import sys
import os
from PyQt6.QtWidgets import QApplication
from my_app.presentation.main_window import MainWindow

def main():
    # Ensure we can find resources if needed
    os.environ["APP_NAME"] = "MyApp"  # Example of setting an environment variable for resource paths
    
    app = QApplication(sys.argv)
    
    # Apply global styles here if you have a .qss file in resources/styles
    # with open("resources/styles/main.qss", "r") as f:
    #     app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()