# ui/dashboards/student_assignment_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class StudentAssignmentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(12, 12, 12, 12)
        outer.setSpacing(16)

        # --- Top row: two donuts + cards ---
        top = QHBoxLayout()
        top.setSpacing(12)

        def make_donut(color_light, color_dark):
            d = QFrame()
            d.setFixedSize(100,100)
            d.setStyleSheet(f"""
                QFrame {{
                    border: 12px solid {color_light};
                    border-top: 12px solid {color_dark};
                    border-radius: 50px;
                }}
            """)
            return d

        def make_card(icon_path, label, value):
            card = QFrame()
            card.setFixedHeight(80)
            card.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius: 6px; }
                QLabel { color: white; }
            """)
            v = QVBoxLayout(card)
            v.setContentsMargins(8,4,8,4)
            v.setSpacing(4)

            row = QHBoxLayout()
            if icon_path:
                ico = QLabel()
                pix = QPixmap(icon_path)
                if not pix.isNull():
                    ico.setPixmap(pix.scaled(20,20, Qt.AspectRatioMode.KeepAspectRatio,
                                             Qt.TransformationMode.SmoothTransformation))
                row.addWidget(ico)
            lbl = QLabel(label)
            row.addWidget(lbl)
            row.addStretch(1)
            v.addLayout(row)

            val = QLabel(str(value))
            val.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            bottom = QHBoxLayout()
            bottom.addStretch(1)
            bottom.addWidget(val)
            v.addLayout(bottom)

            return card

        # left donut
        top.addWidget(make_donut("#ffffff", "#D52462"))

        # cards
        cards = QHBoxLayout()
        cards.setSpacing(8)
        cards.addWidget(make_card("resources/icons/student.png", "Student Type", "$0"))
        cards.addWidget(make_card("resources/icons/event.png",       "Event",        "05"))
        cards.addWidget(make_card("resources/icons/attendance.png",  "Attendance",   "100%"))
        cards.addWidget(make_card("resources/icons/exam.png",        "Subject",      "04"))

        top.addLayout(cards, stretch=1)

        # right donut
        top.addWidget(make_donut("#404040", "#D52462"))

        outer.addLayout(top)

        # --- Search bar ---
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(4)
        search_icon = QLabel("🔍")
        search_icon.setFont(QFont("Arial", 12))
        sfl.addWidget(search_icon)
        le = QLineEdit()
        le.setPlaceholderText("Search Experience")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        outer.addWidget(sf)

        # --- Scrollable list of assignments ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QFrame()
        vlist = QVBoxLayout(container)
        vlist.setContentsMargins(0,0,0,0)
        vlist.setSpacing(8)

        # dummy data
        for i in range(6):
            row = QFrame()
            row.setStyleSheet("""
                QFrame { background: #1B3452; border-radius:6px; color: white; }
                QPushButton { 
                    background: none; border: 1px solid white; border-radius:4px; 
                    color: white; padding:2px 8px;
                }
                QPushButton:hover { background: #D52462; border-color: #D52462; }
            """)
            row.setFixedHeight(60)
            hl = QHBoxLayout(row)
            hl.setContentsMargins(8,8,8,8)
            hl.setSpacing(12)

            # icon
            ico = QLabel()
            pix = QPixmap("resources/icons/award.png")
            if not pix.isNull():
                ico.setPixmap(pix.scaled(24,24,Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation))
            hl.addWidget(ico)

            # text
            txt = QLabel("School management System    Dateline: 12/Jan/2025, 12:00PM    Subject: Oracle    Point: 20/20 pts")
            txt.setStyleSheet("color:white;")
            txt.setFont(QFont("Arial", 12))
            hl.addWidget(txt, 1)

            # action button
            btn = QPushButton("Do")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            hl.addWidget(btn)

            vlist.addWidget(row)

        vlist.addStretch(1)
        scroll.setWidget(container)
        outer.addWidget(scroll, 1)
