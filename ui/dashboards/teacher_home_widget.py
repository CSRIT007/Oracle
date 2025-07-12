# ui/dashboards/teacher_home_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QCalendarWidget, QScrollArea, QLineEdit
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class TeacherHomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        # — overall layout —
        outer = QVBoxLayout(self)
        outer.setContentsMargins(12, 12, 12, 12)
        outer.setSpacing(16)

        # 1) Profile header
        header = QFrame()
        header.setStyleSheet("background: #1B3452; border-radius: 6px;")
        header.setFixedHeight(100)
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(16, 8, 16, 8)
        hlay.setSpacing(12)

        # avatar
        avatar = QLabel()
        pix = QPixmap("resources/images/person.png")
        avatar.setPixmap(pix.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio, 
                                    Qt.TransformationMode.SmoothTransformation))
        hlay.addWidget(avatar)

        # name + location + dept
        info = QVBoxLayout()
        name = QLabel("Teacher Name")
        name.setStyleSheet("color:white; font-size:18px; font-weight:600;")
        info.addWidget(name)
        loc = QLabel("📍 Location")
        loc.setStyleSheet("color:white; font-size:12px;")
        info.addWidget(loc)
        dept = QLabel("Computer Science and engineering")
        dept.setStyleSheet("color:white; font-size:12px;")
        info.addWidget(dept)
        hlay.addLayout(info)

        hlay.addStretch(1)

        # View Profile button
        btn = QPushButton("View Profile")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                color: white;
                border: 1px solid white;
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 13px;
                background: transparent;
            }
            QPushButton:hover {
                background: rgba(255,255,255,0.2);
            }
        """)
        hlay.addWidget(btn)

        outer.addWidget(header)

        # 2) Summary cards + attendance donut
        summary = QFrame()
        slay = QHBoxLayout(summary)
        slay.setSpacing(12)
        summary.setFixedHeight(100)

        def make_card(title, value, icon=None):
            f = QFrame()
            f.setStyleSheet("background:white; border-radius:6px;")
            f.setFixedHeight(80)
            lay = QHBoxLayout(f)
            lay.setContentsMargins(12, 0, 12, 0)
            lay.setSpacing(8)
            if icon:
                ic = QLabel()
                px = QPixmap(icon)
                ic.setPixmap(px.scaled(24,24, Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
                lay.addWidget(ic)
            val = QLabel(str(value))
            val.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            lay.addWidget(val)
            lay.addStretch(1)
            txt = QLabel(title)
            txt.setFont(QFont("Arial", 10))
            lay.addWidget(txt)
            return f

        slay.addWidget(make_card("Today's Class", 4, "resources/icons/class.png"))
        slay.addWidget(make_card("Salary", "$1,200", "resources/icons/salary.png"))
        slay.addWidget(make_card("My Work", 5, "resources/icons/assignment.png"))

        # attendance donut placeholder
        donut = QFrame()
        donut.setStyleSheet("background:white; border-radius:6px;")
        donut.setFixedSize(100, 100)
        # you can draw a real pie here; for now just a label
        dl = QVBoxLayout(donut)
        dl.setContentsMargins(0,0,0,0)
        dl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dl.addWidget(QLabel("Attendance"))
        slay.addWidget(donut)

        outer.addWidget(summary)

        # 3) Calendar & Notifications
        bottom = QFrame()
        blay = QHBoxLayout(bottom)
        blay.setSpacing(12)

        # 3a) calendar panel
        cal_panel = QFrame()
        cal_layout = QVBoxLayout(cal_panel)
        cal_layout.setContentsMargins(0,0,0,0)
        title = QLabel("Event Calendar")
        title.setStyleSheet("""
            background: #1B3452; color: white;
            padding: 4px; font-weight:600;
        """)
        title.setFixedHeight(30)
        cal_layout.addWidget(title)
        cal = QCalendarWidget()
        cal_layout.addWidget(cal)
        blay.addWidget(cal_panel, 2)

        # 3b) notification panel
        notif_panel = QFrame()
        notif_layout = QVBoxLayout(notif_panel)
        notif_layout.setContentsMargins(0,0,0,0)
        ntitle = QLabel("Notification")
        ntitle.setStyleSheet("""
            background: #1B3452; color: white;
            padding: 4px; font-weight:600;
        """)
        ntitle.setFixedHeight(30)
        notif_layout.addWidget(ntitle)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        ivlay = QVBoxLayout(inner)
        ivlay.setContentsMargins(8,8,8,8)
        ivlay.setSpacing(6)

        # example rows
        for _ in range(6):
            row = QFrame()
            row.setStyleSheet("background: white; border-radius:4px;")
            rlay = QHBoxLayout(row)
            rlay.setContentsMargins(8,4,8,4)
            rlay.addWidget(QLabel("Stop Day"))
            rlay.addStretch(1)
            rlay.addWidget(QLabel("Date: 12/Jan/2025 to 13/Jan/2025"))
            rlay.addStretch(1)
            view = QPushButton("View")
            view.setCursor(Qt.CursorShape.PointingHandCursor)
            view.setFixedSize(60,24)
            view.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius:4px;
                }
                QPushButton:hover {
                    background: #255083;
                }
            """)
            rlay.addWidget(view)
            ivlay.addWidget(row)

        scroll.setWidget(inner)
        notif_layout.addWidget(scroll)
        blay.addWidget(notif_panel, 1)

        outer.addWidget(bottom)
