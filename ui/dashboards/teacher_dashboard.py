# ui/dashboards/teacher_dashboard.py

from PyQt6.QtWidgets import QStackedWidget
from ui.dashboards.base_dashboard import BaseDashboard

# import each of your real page‐widgets:
from ui.dashboards.teacher_home_widget       import TeacherHomeWidget
from ui.dashboards.teacher_salary_widget     import TeacherSalaryWidget
from ui.dashboards.teacher_library_widget    import TeacherLibraryWidget
from ui.dashboards.teacher_experience_widget import TeacherExperienceWidget
from ui.dashboards.teacher_schedule_widget   import TeacherScheduleWidget
from ui.dashboards.teacher_class_widget      import TeacherClassWidget
from ui.dashboards.teacher_attendance_widget import TeacherAttendanceWidget
from ui.dashboards.teacher_assignment_widget import TeacherAssignmentWidget
from ui.dashboards.teacher_result_widget     import TeacherResultWidget
from ui.dashboards.teacher_exam_widget       import TeacherExamWidget


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

        # build a QStackedWidget and add each actual page‐widget in order:
        stack = QStackedWidget()
        stack.addWidget(TeacherHomeWidget())        # index 0
        stack.addWidget(TeacherSalaryWidget())      # index 1
        stack.addWidget(TeacherLibraryWidget())     # index 2
        stack.addWidget(TeacherExperienceWidget())  # index 3
        stack.addWidget(TeacherScheduleWidget())    # index 4
        stack.addWidget(TeacherClassWidget())       # index 5
        stack.addWidget(TeacherAttendanceWidget())  # index 6
        stack.addWidget(TeacherAssignmentWidget())  # index 7
        stack.addWidget(TeacherResultWidget())      # index 8
        stack.addWidget(TeacherExamWidget())        # index 9

        super().__init__(
            user_name="Teacher Name",
            left_menus=menus,
            main_widget=stack
        )
