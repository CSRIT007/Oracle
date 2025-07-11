# ui/dashboards/student_dashboard.py

from PyQt6.QtWidgets import QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

# import your actual page widgets:
from ui.dashboards.student_home_widget       import StudentHomeWidget
from ui.dashboards.student_profile_widget    import StudentProfileWidget
from ui.dashboards.student_payment_widget    import StudentPaymentWidget
from ui.dashboards.student_library_widget    import StudentLibraryWidget
from ui.dashboards.student_experience_widget import StudentExperienceWidget
from ui.dashboards.student_schedule_widget   import StudentScheduleWidget
from ui.dashboards.student_class_widget      import StudentClassWidget
from ui.dashboards.student_attendance_widget import StudentAttendanceWidget
from ui.dashboards.student_assignment_widget import StudentAssignmentWidget
from ui.dashboards.student_result_widget     import StudentResultWidget
from ui.dashboards.student_exam_widget       import StudentExamWidget

class StudentDashboard(BaseDashboard):
    def __init__(self):
        # sidebar labels + icons
        menus = [
            ("Home",       "resources/icons/home.png"),
            ("Profile",    "resources/icons/user.png"),
            ("Payment",    "resources/icons/payments.png"),
            ("Library",    "resources/icons/library.png"),
            ("Experience", "resources/icons/experience.png"),
            ("Schedule",   "resources/icons/schedule.png"),
            ("Class",      "resources/icons/class.png"),
            ("Attendance", "resources/icons/attendance.png"),
            ("Assignment", "resources/icons/assignment.png"),
            ("Result",     "resources/icons/result.png"),
            ("Exam",       "resources/icons/exam.png"),
        ]

        # build the stacked widget with each page
        stack = QStackedWidget()
        stack.addWidget(StudentHomeWidget())         # index 0
        stack.addWidget(StudentProfileWidget())      # index 1
        stack.addWidget(StudentPaymentWidget())      # index 2
        stack.addWidget(StudentLibraryWidget())      # index 3
        stack.addWidget(StudentExperienceWidget())   # index 4
        stack.addWidget(StudentScheduleWidget())     # index 5
        stack.addWidget(StudentClassWidget())        # index 6
        stack.addWidget(StudentAttendanceWidget())   # index 7
        stack.addWidget(StudentAssignmentWidget())   # index 8
        stack.addWidget(StudentResultWidget())       # index 9
        stack.addWidget(StudentExamWidget())         # index 10

        # hand off to BaseDashboard
        super().__init__(
            user_name="Student Name",
            left_menus=menus,
            main_widget=stack
        )
