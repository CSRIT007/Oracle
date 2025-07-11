# ui/dashboards/manage_teacher_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class ManageTeacherDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",       "resources/icons/home.png"),
            ("All Teacher","resources/icons/teacher.png"),
            ("Attendance", "resources/icons/attendance.png"),
            ("Schedule",   "resources/icons/schedule.png"),
            ("Evaluation","resources/icons/evaluate.png"),
            ("Requests",  "resources/icons/request.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"ManageTeacher → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="TeacherMgr",
            left_menus=menus,
            main_widget=stack
        )
