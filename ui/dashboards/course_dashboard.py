# ui/dashboards/course_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class CourseDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",              "resources/icons/home.png"),
            ("All Course",        "resources/icons/course.png"),
            ("Schedule",          "resources/icons/schedule.png"),
            ("Local Course",      "resources/icons/local.png"),
            ("International",     "resources/icons/global.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"Course → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="CourseMgr",
            left_menus=menus,
            main_widget=stack
        )
