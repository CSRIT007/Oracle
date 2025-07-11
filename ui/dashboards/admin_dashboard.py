# ui/dashboards/admin_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class AdminDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",        "resources/icons/home.png"),
            ("Student",     "resources/icons/student.png"),
            ("Teacher",     "resources/icons/teacher.png"),
            ("Staff",       "resources/icons/staff.png"),
            ("Library",     "resources/icons/library.png"),
            ("Schedule",    "resources/icons/schedule.png"),
            ("Income",    "resources/icons/tracking.png"),
            ("Expense",      "resources/icons/course.png"),
            ("Tracking",    "resources/icons/tracking.png"),
            ("Course",      "resources/icons/course.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"Admin → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="Admin User",
            left_menus=menus,
            main_widget=stack
        )
