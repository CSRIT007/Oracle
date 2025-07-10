from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome, Admin!"))
        # You can add more widgets and logic here later
        self.setLayout(layout)
