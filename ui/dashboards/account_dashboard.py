# ui/dashboards/account_dashboard.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QStackedWidget
)
from ui.dashboards.base_dashboard import BaseDashboard

# — simple page with a big title —
class SimplePage(QWidget):
    def __init__(self, title: str):
        super().__init__()
        layout = QVBoxLayout(self)
        lbl = QLabel(title)
        lbl.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        layout.addWidget(lbl, 0)

class AccountDashboard(BaseDashboard):
    def __init__(self):
        # flatten all sub-sections into individual menu entries
        menus = [
            ("Home",             "resources/icons/home.png"),
            ("Student Income",   "resources/icons/income.png"),
            ("Parking Income",   "resources/icons/income.png"),
            ("Mark Income",      "resources/icons/income.png"),
            ("Restaurant Income","resources/icons/income.png"),
            ("Course Income",    "resources/icons/income.png"),
            ("Teacher Expense",  "resources/icons/expense.png"),
            ("Staff Expense",    "resources/icons/expense.png"),
            ("Book Expense",     "resources/icons/expense.png"),
            ("Utilities Expense","resources/icons/expense.png"),
            ("Reports",          "resources/icons/report.png"),
        ]

        # build one SimplePage per menu item
        self.pages = QStackedWidget()
        self.pages.addWidget(SimplePage("Welcome to Account Home"))
        self.pages.addWidget(SimplePage("Income → Student Overview"))
        self.pages.addWidget(SimplePage("Income → Parking Overview"))
        self.pages.addWidget(SimplePage("Income → Mark Overview"))
        self.pages.addWidget(SimplePage("Income → Restaurant Overview"))
        self.pages.addWidget(SimplePage("Income → Course Sorting"))
        self.pages.addWidget(SimplePage("Expense → Teacher Overview"))
        self.pages.addWidget(SimplePage("Expense → Staff Overview"))
        self.pages.addWidget(SimplePage("Expense → Book Overview"))
        self.pages.addWidget(SimplePage("Expense → Utilities Overview"))
        self.pages.addWidget(SimplePage("Financial Reports"))

        # hand off to BaseDashboard
        super().__init__(
            user_name="Account Manager",
            left_menus=menus,
            main_widget=self.pages
        )
        # BaseDashboard will automatically wire its sidebar buttons
        # so that label “Student Income” shows page index 1, etc.
