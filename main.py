from PyQt6.QtWidgets import QApplication
from ui.login import ManageStudentParentDashboard
from database.db import initialize_db
import sys

def main():
    initialize_db()
    app = QApplication(sys.argv)
    window = ManageStudentParentDashboard()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
