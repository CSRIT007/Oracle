# ui/dashboards/manage_student_parent_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class ManageStudentParentDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",             "resources/icons/home.png"),
            ("All Student",      "resources/icons/student.png"),
            ("Result Student",   "resources/icons/result.png"),
            ("Achievement",      "resources/icons/award.png"),
            ("Survey",           "resources/icons/survey.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"ManageStud/Parent → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="Manager",
            left_menus=menus,
            main_widget=stack
        )
