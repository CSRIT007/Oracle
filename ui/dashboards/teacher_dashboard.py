# ui/dashboards/teacher_dashboard.py
from ui.dashboards.base_dashboard import BaseDashboard
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class TeacherMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Teacher Home: Schedule, Salary, Results, Attendance, etc."))

class TeacherDashboard(BaseDashboard):
    def __init__(self):
        menus = ["Home", "Salary", "Library", "Experience", "Schedule", "Class", "Attendance", "Assignment", "Result", "Exam"]
        super().__init__(user_name="Teacher Name", left_menus=menus, main_widget=TeacherMainWidget())
