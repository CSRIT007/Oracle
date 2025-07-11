# ui/dashboards/teacher_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class TeacherDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",       "resources/icons/home.png"),
            ("Salary",     "resources/icons/salary.png"),
            ("Library",    "resources/icons/library.png"),
            ("Experience", "resources/icons/experience.png"),
            ("Schedule",   "resources/icons/schedule.png"),
            ("Class",      "resources/icons/class.png"),
            ("Attendance", "resources/icons/attendance.png"),
            ("Assignment", "resources/icons/assignment.png"),
            ("Result",     "resources/icons/result.png"),
            ("Exam",       "resources/icons/exam.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"Teacher → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="Teacher Name",
            left_menus=menus,
            main_widget=stack
        )
