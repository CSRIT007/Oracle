from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class StudentDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome, Student!"))
        self.setLayout(layout)
