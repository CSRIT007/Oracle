from PyQt6.QtWidgets import QApplication
from ui.login import LoginWindow
from database.db import initialize_db
import sys

def main():
    initialize_db()
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
