from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from logic.auth import verify_login
from ui.dashboards.admin_dashboard import AdminDashboard

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        self.setLayout(layout)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        user = verify_login(username, password)
        if user:
            QMessageBox.information(self, "Success", f"Logged in as {user['role']}")
            if user['role'] == 'admin':
                self.dashboard = AdminDashboard()
                self.dashboard.show()
                self.close()
            else:
                QMessageBox.warning(self, "Notice", f"Role {user['role']} not set up yet.")
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
