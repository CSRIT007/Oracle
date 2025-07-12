# ui/dashboards/parent_dashboard.py

from PyQt6.QtWidgets import QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

from ui.dashboards.parent_home_widget import ParentHomeWidget
from ui.dashboards.parent_payment_widget import ParentPaymentWidget
from ui.dashboards.parent_academic_progress_widget import ParentAcademicProgressWidget
from ui.dashboards.parent_experience_widget import ParentExperienceWidget
from ui.dashboards.parent_schedule_widget import ParentScheduleWidget
from ui.dashboards.parent_profile_widget import ParentProfileWidget

class ParentDashboard(BaseDashboard):
    def __init__(self):
        menus = [
            ("Home",              "resources/icons/home.png"),
            ("Payment",           "resources/icons/payments.png"),
            ("Academic Progress", "resources/icons/progress.png"),
            ("Experience",        "resources/icons/experience.png"),
            ("Schedule",          "resources/icons/schedule.png"),
            ("Profile",           "resources/icons/user.png"),
        ]

        # 1) Store the stack on self so we can refer to it later
        self.stack = QStackedWidget()
        self.stack.addWidget(ParentHomeWidget())             # index 0
        self.stack.addWidget(ParentPaymentWidget())          # index 1
        self.stack.addWidget(ParentAcademicProgressWidget()) # index 2
        self.stack.addWidget(ParentExperienceWidget())       # index 3
        self.stack.addWidget(ParentScheduleWidget())         # index 4
        self.stack.addWidget(ParentProfileWidget())          # index 5

        # 2) Initialize BaseDashboard with our stack
        super().__init__(
            user_name="Parent Name",
            left_menus=menus,
            main_widget=self.stack
        )

        # 3) Populate with real data (or demo stub)
        self.load_data()

    def load_data(self):
        """
        TODO: replace this stub with your SQLite queries.
        """
        demo_profile = {
            "Name":         "Updated Name",
            "Gender":       "Female",
            "Job":          "Engineer",
            "E_mail":       "updated@example.com",
            "Phone Number": "0123456789",
            "Address":      "123 Main St",
            "Extra Field":  "Extra Value"
        }

        # 4) Grab the Profile page from our saved stack
        profile: ParentProfileWidget = self.stack.widget(5)
        profile.update_profile({
        "Name": "Updated Name",
        "Gender": "Female",
        "Phone Number": "0123456789",
        "Extra Field": "Extra Value"
        })

