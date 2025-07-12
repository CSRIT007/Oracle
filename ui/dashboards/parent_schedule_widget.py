# ui/dashboards/parent_schedule_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QLineEdit, QGridLayout, QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ParentScheduleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(12)

        # --- 1) Top summary bar ---
        top = QFrame()
        top.setStyleSheet("background: #003366; color: white;")
        t_layout = QHBoxLayout(top)
        t_layout.setContentsMargins(12, 6, 12, 6)
        t_layout.setSpacing(24)

        # Today's Course card
        today_card = QFrame()
        today_card.setStyleSheet("background: white;")
        td = QVBoxLayout(today_card)
        td.setContentsMargins(12, 8, 12, 8)
        td.setAlignment(Qt.AlignmentFlag.AlignTop)
        # icon + count
        ic = QLabel()
        ic.setPixmap(
            QPixmap("resources/icons/schedule.png")
            .scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        td.addWidget(ic, alignment=Qt.AlignmentFlag.AlignLeft)
        td.addWidget(QLabel("<b>Today's Course</b>"), alignment=Qt.AlignmentFlag.AlignLeft)
        td.addWidget(QLabel("<span style='font-size:16pt;'>02</span>"), alignment=Qt.AlignmentFlag.AlignLeft)
        td.addWidget(QLabel("<span style='color: green;'>Now: On Studying Oracle (CS412)<br>8:00 AM – 11:00 AM</span>"), alignment=Qt.AlignmentFlag.AlignLeft)
        t_layout.addWidget(today_card, 2)

        # Student summary card
        profile_card = QFrame()
        profile_card.setStyleSheet("background: white;")
        pd = QHBoxLayout(profile_card)
        pd.setContentsMargins(12, 8, 12, 8)
        pd.setSpacing(12)
        # avatar
        avatar = QLabel()
        avatar.setPixmap(
            QPixmap("resources/icons/user.png")
            .scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        pd.addWidget(avatar)
        # details
        details = QVBoxLayout()
        details.addWidget(QLabel("<b>Student :</b> Moeng Kimheang"))
        details.addWidget(QLabel("<b>Batch   :</b> 08"))
        details.addWidget(QLabel("<b>Major   :</b> Computer Science and Engineering"))
        pd.addLayout(details)
        t_layout.addWidget(profile_card, 3)

        root.addWidget(top, 0)

        # --- 2) Search bar ---
        search_bar = QFrame()
        sb = QHBoxLayout(search_bar)
        sb.setContentsMargins(0, 0, 0, 0)
        sb.setSpacing(8)
        lbl = QLabel("<b>Course</b>")
        lbl.setStyleSheet("padding:4px 8px; background:#0055aa; color:white; border-top-left-radius:4px; border-bottom-left-radius:4px;")
        sb.addWidget(lbl)
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Course")
        sb.addWidget(self.search, 1)
        sb.addWidget(QLabel("<b>All 〉</b>"), alignment=Qt.AlignmentFlag.AlignRight)
        root.addWidget(search_bar, 0)

        # --- 3) Course cards grid ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        grid = QGridLayout(container)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(12)

        # sample courses
        sample = [
            ("CS412", "Oracle",     "12/Jan/2025", "8:00 AM - 9:30 AM",   "Brassat Banteay Kdei", "Build “B”"),
            ("CS412", "Oracle",     "12/Jan/2025", "9:30 AM - 11:00 AM",  "Brassat Banteay Kdei", "Build “B”"),
            ("CS413", "Mobile App", "12/Jan/2025", "12:00 PM - 1:30 PM",  "Brassat Banteay Kdei", "Build “B”"),
            ("CS413", "Mobile App", "12/Jan/2025", "1:30 PM - 3:00 PM",   "Brassat Banteay Kdei", "Build “B”"),
            ("CS413", "Mobile App", "12/Jan/2025", "3:00 PM - 4:30 PM",   "Brassat Banteay Kdei", "Build “B”"),
            ("CS413", "Mobile App", "12/Jan/2025", "4:30 PM - 6:00 PM",   "Brassat Banteay Kdei", "Build “B”"),
        ]

        for idx, (cid, subj, date, time, cls, bld) in enumerate(sample):
            card = QFrame()
            # alternate colors
            bg = "#28a745" if idx % 2 == 0 else "#6f42c1"
            card.setStyleSheet(f"background: {bg}; color: white; border-radius:4px;")
            cd = QVBoxLayout(card)
            cd.setContentsMargins(12, 8, 12, 8)
            # fields
            cd.addWidget(QLabel(f"<b>ID :</b> {cid}"))
            cd.addWidget(QLabel(f"<b>Subject :</b> {subj}"))
            cd.addWidget(QLabel(f"<b>Date :</b> {date}"))
            cd.addWidget(QLabel(f"<b>Time :</b> {time}"))
            cd.addWidget(QLabel(f"<b>Class :</b> {cls}"))
            cd.addWidget(QLabel(f"<b>Building :</b> {bld}"))
            row = idx // 3
            col = idx % 3
            grid.addWidget(card, row, col)

        container.setLayout(grid)
        scroll.setWidget(container)
        root.addWidget(scroll, 1)

    def load_data(self, today_info: dict, courses: list[tuple]):
        """
        :param today_info: {
            'count': str,
            'current': str
        }
        :param courses: list of tuples (id, subject, date, time, class, building)
        """
        # TODO: update today's card & rebuild grid from `courses`
        pass
