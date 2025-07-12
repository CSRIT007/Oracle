# ui/dashboards/parent_home_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QFormLayout, QCalendarWidget, QPushButton, QSizePolicy
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QDate
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class ParentHomeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        outer = QVBoxLayout(self)
        outer.setSpacing(12)
        outer.setContentsMargins(0, 0, 0, 0)

        # --- 1) Profile Header ---
        profile_frame = QFrame()
        profile_frame.setStyleSheet("background: #003366; color: white;")
        pf_layout = QHBoxLayout(profile_frame)
        pf_layout.setContentsMargins(12, 6, 12, 6)

        # Avatar + Name/Tel
        avatar = QLabel()
        avatar.setPixmap(
            QPixmap("resources/icons/user.png")
            .scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        pf_layout.addWidget(avatar, 0, Qt.AlignmentFlag.AlignVCenter)

        name_tel = QVBoxLayout()
        name_lbl = QLabel("<b>Moeng Sokea</b>")
        tel_lbl  = QLabel("Tel: 0962843473")
        name_tel.addWidget(name_lbl)
        name_tel.addWidget(tel_lbl)
        pf_layout.addLayout(name_tel, 1)

        # View Profile button
        btn = QPushButton("View Profile")
        btn.setStyleSheet("""
            background: #0055aa;
            color: white;
            padding: 6px 12px;
            border-radius: 4px;
        """)
        pf_layout.addWidget(btn, 0, Qt.AlignmentFlag.AlignRight)

        outer.addWidget(profile_frame, 0)

        # --- 2) Summary + Attendance ---
        summary_frame = QFrame()
        sum_layout = QHBoxLayout(summary_frame)
        sum_layout.setContentsMargins(0, 0, 0, 0)
        sum_layout.setSpacing(8)

        # Helper to build a summary card
        def make_card(icon_path, title, value):
            card = QFrame()
            card.setStyleSheet("background: white; border: 1px solid #ccc;")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(12, 8, 12, 8)
            cl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if icon_path:
                ic = QLabel()
                ic.setPixmap(
                    QPixmap(icon_path)
                    .scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                )
                cl.addWidget(ic)
            cl.addWidget(QLabel(f"<b>{title}</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(QLabel(value), alignment=Qt.AlignmentFlag.AlignCenter)
            return card

        # Three summary cards
        sum_layout.addWidget(make_card("resources/icons/calendar.png", "Today's Class", "02 Total"), 1)
        sum_layout.addWidget(make_card("resources/icons/payments.png",    "Payment",       "$1200 Year"), 1)
        sum_layout.addWidget(make_card("resources/icons/sms.png",         "SMS",           "02 New"), 1)

        # Attendance donut chart
        chart_frame = QFrame()
        chart_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        cl = QVBoxLayout(chart_frame)
        cl.setContentsMargins(12, 8, 12, 8)
        cl.addWidget(QLabel("<b>Attendance</b>"), alignment=Qt.AlignmentFlag.AlignHCenter)

        fig = Figure(figsize=(2, 2))
        ax = fig.add_subplot(111)
        data  = [40, 40, 20]  # example: Absent, Present, Late
        labels= ['A', 'P', 'L']
        ax.pie(data, labels=labels, autopct='%1.0f%%', startangle=90, pctdistance=0.8)
        ax.axis('equal')
        canvas = FigureCanvas(fig)
        cl.addWidget(canvas)

        sum_layout.addWidget(chart_frame, 1)
        outer.addWidget(summary_frame, 0)

        # --- 3) Calendar & Holidays ---
        bottom_frame = QWidget()
        bf_layout = QHBoxLayout(bottom_frame)
        bf_layout.setContentsMargins(0, 0, 0, 0)
        bf_layout.setSpacing(12)

        # Event Calendar panel
        cal_frame = QFrame()
        cal_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        cal_layout = QVBoxLayout(cal_frame)
        cal_layout.setContentsMargins(12, 8, 12, 8)

        # Navigation header
        nav = QHBoxLayout()
        prev = QPushButton("⟨")
        prev.setFixedWidth(24)
        next = QPushButton("⟩")
        next.setFixedWidth(24)
        self.current_date = QLabel(QDate.currentDate().toString("dd MMM, yyyy"))
        self.current_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav.addWidget(prev)
        nav.addStretch()
        nav.addWidget(self.current_date)
        nav.addStretch()
        nav.addWidget(next)
        cal_layout.addLayout(nav)

        # Actual calendar widget
        cal = QCalendarWidget()
        cal.setGridVisible(True)
        cal_layout.addWidget(cal)
        bf_layout.addWidget(cal_frame, 2)

        # School Holiday panel
        hol_frame = QFrame()
        hol_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        hol_layout = QVBoxLayout(hol_frame)
        hol_layout.setContentsMargins(12, 8, 12, 8)
        hol_layout.addWidget(QLabel("<b>School Holiday</b>"))

        # Example holiday entries
        for i in range(5):
            row = QHBoxLayout()
            row.addWidget(QLabel("Stop Day"), 1)
            row.addWidget(QLabel("Date: 12/Jan/2025 to 13/Jan/2025"), 2)
            view_btn = QPushButton("View")
            view_btn.setFixedWidth(48)
            row.addWidget(view_btn)
            hol_layout.addLayout(row)

        bf_layout.addWidget(hol_frame, 1)

        outer.addWidget(bottom_frame, 1)

    # You can add slots to move calendar date back/forward, etc.
