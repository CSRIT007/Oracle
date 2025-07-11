# ui/dashboards/student_experience_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QLineEdit,
    QScrollArea, QPushButton, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class ExperienceItem(QFrame):
    def __init__(self, title, dateline, subject, icon_path="resources/icons/certificate.png"):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background: #1B3452;
                color: white;
                border-radius: 6px;
            }
        """)
        self.setFixedHeight(80)
        hl = QHBoxLayout(self)
        hl.setContentsMargins(12, 8, 12, 8)
        hl.setSpacing(16)

        # icon
        ic = QLabel()
        pix = QPixmap(icon_path)
        if not pix.isNull():
            ic.setPixmap(pix.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, 
                                     Qt.TransformationMode.SmoothTransformation))
        ic.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        hl.addWidget(ic)

        # text block
        txt = QVBoxLayout()
        lbl_title = QLabel(f"<b>Title:</b> {title}")
        lbl_title.setFont(QFont("Arial", 10))
        txt.addWidget(lbl_title)
        lbl_date = QLabel(f"<b>Dateline:</b> {dateline}")
        lbl_date.setFont(QFont("Arial", 9))
        txt.addWidget(lbl_date)
        lbl_subj = QLabel(f"<b>Subject:</b> {subject}")
        lbl_subj.setFont(QFont("Arial", 9))
        txt.addWidget(lbl_subj)
        hl.addLayout(txt, 1)

        # view button
        btn = QPushButton("View")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: #FD367E;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 14px;
                font-size: 10px;
            }
            QPushButton:hover {
                background: #ff5a8f;
            }
        """)
        hl.addWidget(btn)


class StudentExperienceWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_l = QVBoxLayout(self)
        main_l.setContentsMargins(12,12,12,12)
        main_l.setSpacing(16)

        # --- Top summary cards + title ---
        top = QFrame()
        th = QHBoxLayout(top)
        th.setContentsMargins(0,0,0,0)
        th.setSpacing(10)

        def card(icon, label, value, width=120):
            f = QFrame()
            f.setFixedSize(width, 80)
            f.setStyleSheet("""
                background: #1B3452;
                color: white;
                border-radius: 6px;
            """)
            cl = QVBoxLayout(f)
            cl.setContentsMargins(8,8,8,8)
            cl.setSpacing(4)
            # icon + label row
            row = QHBoxLayout()
            ic = QLabel()
            pix = QPixmap(icon)
            if not pix.isNull():
                ic.setPixmap(pix.scaled(20,20,Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation))
            row.addWidget(ic)
            row.addWidget(QLabel(label))
            cl.addLayout(row)
            # big value
            v = QLabel(str(value))
            v.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            v.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(v, 1)
            return f

        th.addWidget(card("resources/icons/experience.png", "Experience", 4))
        th.addWidget(card("resources/icons/event.png",      "Events",    5))
        th.addWidget(card("resources/icons/subject.png",    "Subjects",  "100%"), 1)
        th.addWidget(card("resources/icons/type.png",       "Type",      "$0"), 1)

        # center title
        title = QLabel("Experience")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #1B3452;")
        th.addWidget(title, 1)

        main_l.addWidget(top)

        # --- Search bar ---
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        inp = QLineEdit()
        inp.setPlaceholderText("Search Experience")
        inp.setFrame(False)
        inp.setStyleSheet("font-size: 13px;")
        sfl.addWidget(QLabel("Experience"))
        sfl.addWidget(inp, 1)
        sfl.addWidget(QLabel("🔍"))
        main_l.addWidget(sf)

        # --- List of experiences (scrollable) ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        vl = QVBoxLayout(container)
        vl.setContentsMargins(0,0,0,0)
        vl.setSpacing(12)

        # demo entries, replace with real data
        demo = [
            ("School management System", "12/Jan/2025, 12:00PM", "Oracle"),
            ("Library Helper Program",    "05/Feb/2025, 03:30PM", "SQL"),
            ("Internship ABC",            "20/Mar/2025, 10:00AM", "Python"),
            ("Volunteering Day",          "15/Apr/2025, 09:00AM", "Community"),
        ]
        for title, date, subj in demo:
            vl.addWidget(ExperienceItem(title, date, subj))

        vl.addStretch(1)
        scroll.setWidget(container)
        main_l.addWidget(scroll, 1)
