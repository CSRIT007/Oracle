from PyQt6.QtWidgets import QApplication
<<<<<<< HEAD
from ui.login import ParentDashboard
=======
from ui.login import ManageStudentParentDashboard
>>>>>>> 9d061739c0120a66709c2d439cfc25c773e4d8c2
from database.db import initialize_db
import sys

def main():
    initialize_db()
    app = QApplication(sys.argv)
<<<<<<< HEAD
    window = ParentDashboard()
=======
    window = ManageStudentParentDashboard()
>>>>>>> 9d061739c0120a66709c2d439cfc25c773e4d8c2
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
