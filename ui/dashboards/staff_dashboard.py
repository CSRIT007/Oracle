from ui.dashboards.base_dashboard import BaseDashboard
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class StaffMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Staff Dashboard Main Area"))

class StaffDashboard(BaseDashboard):
    def __init__(self):
        menus = ["Home", "Position", "Attendance", "Schedule", "Library"]
        super().__init__(user_name="Staff", left_menus=menus, main_widget=StaffMainWidget())
