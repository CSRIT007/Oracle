from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QApplication, QMessageBox, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from logic.auth import verify_login
from ui.dashboards.admin_dashboard import AdminDashboard
from ui.dashboards.student_dashboard import StudentDashboard
from ui.dashboards.teacher_dashboard import TeacherDashboard
from ui.dashboards.staff_dashboard import StaffDashboard

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System Login")
        self.showMaximized()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Left: Banner Image ---
        image_frame = QFrame()
        image_layout = QVBoxLayout(image_frame)
        image_label = QLabel()
        pixmap = QPixmap("resources/images/login_banner.png")  # Change path if your image is different!
        if not pixmap.isNull():
            image_label.setPixmap(pixmap.scaledToWidth(700, Qt.TransformationMode.SmoothTransformation))
        else:
            image_label.setText("[IMAGE NOT FOUND]")
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_label.setStyleSheet("color: white; font-size: 18px;")
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_layout.addWidget(image_label)
        image_layout.addStretch(1)
        image_frame.setStyleSheet("background-color: #1a1e37;")
        main_layout.addWidget(image_frame, 2)

        # --- Right: Centered Login Form ---
        right_outer = QFrame()
        right_layout = QHBoxLayout(right_outer)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addStretch(1)  # Left spacer

        # Login form card
        form_frame = QFrame()
        form_frame.setFixedWidth(410)
        form_frame.setStyleSheet(
            """
            QFrame {
                background: #fff;
                
            }
            """
        )
        # Drop shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(8)
        shadow.setColor(Qt.GlobalColor.gray)
        form_frame.setGraphicsEffect(shadow)

        form_layout = QVBoxLayout(form_frame)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setContentsMargins(40, 40, 40, 40)

        # Title
        title = QLabel("Welcome to School Management System")
        title.setFont(QFont("Arial", 17, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(title)
        form_layout.addSpacing(18)
        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedHeight(42)
        self.username_input.setFont(QFont("Arial", 12))
        form_layout.addWidget(self.username_input)
        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(42)
        self.password_input.setFont(QFont("Arial", 12))
        form_layout.addWidget(self.password_input)
        # Login Button
        self.login_btn = QPushButton("Login")
        self.login_btn.setFixedHeight(44)
        self.login_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.login_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #1a1e37;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #23274a;
            }
            """
        )
        self.login_btn.clicked.connect(self.login)
        form_layout.addSpacing(12)
        form_layout.addWidget(self.login_btn)
        form_layout.addSpacing(18)
        # Credit
        credit = QLabel("© 2025 ACLEDA University of Business")
        credit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credit.setStyleSheet("color: #888; font-size: 12px;")
        form_layout.addWidget(credit)
        form_layout.addStretch(1)

        right_layout.addWidget(form_frame)
        right_layout.addStretch(1)  # Right spacer
        main_layout.addWidget(right_outer, 1)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        user = verify_login(username, password)
        if user:
            if user['role'] == 'admin':
                self.dashboard = AdminDashboard()
            elif user['role'] == 'student':
                self.dashboard = StudentDashboard()
            elif user['role'] == 'teacher':
                self.dashboard = TeacherDashboard()
            elif user['role'] == 'staff':
                self.dashboard = StaffDashboard()
            else:
                QMessageBox.warning(self, "Notice", f"Role {user['role']} not set up.")
                return
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")

# To run this file standalone for test:
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
