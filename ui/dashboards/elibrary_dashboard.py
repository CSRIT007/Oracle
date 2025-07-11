# ui/dashboards/elibrary_dashboard.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

class ELibraryDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",         "resources/icons/home.png"),
            ("All Book",     "resources/icons/book.png"),
            ("History",      "resources/icons/history.png"),
            ("Student Book", "resources/icons/student.png"),
            ("Student Owe",  "resources/icons/owe.png"),
            ("Owe Student",  "resources/icons/owe_student.png"),
        ]
        stack = QStackedWidget()
        for name, _ in menus:
            w = QWidget(); l = QVBoxLayout(w)
            l.addWidget(QLabel(f"E-Library → {name}"))
            stack.addWidget(w)

        super().__init__(
            user_name="eLibrary User",
            left_menus=menus,
            main_widget=stack
        )
