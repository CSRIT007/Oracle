from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QApplication, QFrame, QGraphicsDropShadowEffect, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from logic.auth import verify_login

from ui.dashboards.admin_dashboard import AdminDashboard
from ui.dashboards.student_dashboard import StudentDashboard
from ui.dashboards.teacher_dashboard import TeacherDashboard
from ui.dashboards.account_dashboard import AccountDashboard
from ui.dashboards.course_dashboard import CourseDashboard
from ui.dashboards.elibrary_dashboard import ELibraryDashboard
from ui.dashboards.manage_student_parent_dashboard import ManageStudentParentDashboard
from ui.dashboards.manage_teacher_dashboard import ManageTeacherDashboard
from ui.dashboards.parent_dashboard import ParentDashboard

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login | School Management System")
        self.showFullScreen()
        self.setStyleSheet("background-color: #232946;")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setFixedWidth(400)
        card.setStyleSheet("""
            QFrame {
                background: #fff;
                border-radius: 16px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setXOffset(0)
        shadow.setYOffset(12)
        shadow.setColor(Qt.GlobalColor.gray)
        card.setGraphicsEffect(shadow)

        form_layout = QVBoxLayout(card)
        form_layout.setContentsMargins(36, 44, 36, 44)
        form_layout.setSpacing(22)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Sign in to your account")
        title.setFont(QFont("Arial", 19, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #232946;")
        form_layout.addWidget(title)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setFixedHeight(42)
        self.username_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d6d6d6;
                border-radius: 8px;
                background: #f3f3f3;
                padding-left: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #2d6cdf;
            }
        """)
        form_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setFixedHeight(42)
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d6d6d6;
                border-radius: 8px;
                background: #f3f3f3;
                padding-left: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #2d6cdf;
            }
        """)
        form_layout.addWidget(self.password_input)

        self.login_btn = QPushButton("Login")
        self.login_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.login_btn.setFixedHeight(44)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2d6cdf;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #4476c6;
            }
        """)
        self.login_btn.clicked.connect(self.do_login)
        form_layout.addWidget(self.login_btn)

        copyright = QLabel("© 2025 School Management System")
        copyright.setFont(QFont("Arial", 10))
        copyright.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyright.setStyleSheet("color: #8c8c8c; margin-top:14px;")
        form_layout.addWidget(copyright)

        main_layout.addWidget(card)

    def do_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if not username or not password:
            QMessageBox.warning(self, "Login", "Please enter both username and password.")
            return
        role = verify_login(username, password)
        if role == "admin":
            self.dashboard = AdminDashboard()
        elif role == "student":
            self.dashboard = StudentDashboard()
        elif role == "teacher":
            self.dashboard = TeacherDashboard()
        elif role == "course":
            self.dashboard = CourseDashboard()
        elif role == "account":
            self.dashboard = AccountDashboard()
        elif role == "elibrary":
            self.dashboard = ELibraryDashboard()
        elif role == "manage_teacher":
            self.dashboard = ManageTeacherDashboard()
        elif role == "manage_student_parent":
            self.dashboard = ManageStudentParentDashboard()
        elif role == "parent":
            self.dashboard = ParentDashboard()
        elif role:
            QMessageBox.warning(self, "Login", f"Unknown role: {role}")
            return
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")
            return
        self.dashboard.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
