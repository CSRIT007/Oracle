# ui/dashboards/admin_dashboard.py
from ui.dashboards.base_dashboard import BaseDashboard
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class AdminMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Admin Home: Show statistics, batch buttons, charts here"))
        # Add summary boxes, graphs, and batch navigation logic!
        # Add tables for students, staff, teachers etc, with detail/delete logic.

class AdminDashboard(BaseDashboard):
    def __init__(self):
        menus = ["Home", "Student", "Teacher", "Staff", "Library", "Schedule", "Tracking", "Course"]
        super().__init__(user_name="Admin", left_menus=menus, main_widget=AdminMainWidget())
