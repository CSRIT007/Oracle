# ui/dashboards/admin_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from ui.login import LoginWindow

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome, Admin!"))
        self.logout_btn = QPushButton("Logout")
        self.logout_btn.clicked.connect(self.logout)
        layout.addWidget(self.logout_btn)
        self.setLayout(layout)

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
