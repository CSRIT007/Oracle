# ui/dashboards/parent_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class ParentDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",             "resources/icons/home.png"),
            ("Payment",          "resources/icons/payments.png"),
            ("Academic Progress","resources/icons/progress.png"),
            ("Experience",       "resources/icons/experience.png"),
            ("Schedule",         "resources/icons/schedule.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"Parent → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="Parent Name",
            left_menus=menus,
            main_widget=stack
        )
