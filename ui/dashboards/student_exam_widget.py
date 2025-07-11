# ui/dashboards/student_exam_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QScrollArea
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class StudentExamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(16)

        # --- Top row: Fail donut, cards, Pass donut ---
        top = QHBoxLayout()
        top.setSpacing(12)

        def donut(light, dark):
            d = QFrame()
            d.setFixedSize(100, 100)
            d.setStyleSheet(f"""
                QFrame {{
                  border: 12px solid {light};
                  border-top: 12px solid {dark};
                  border-radius: 50px;
                }}
            """)
            return d

        def card(icon, text, value):
            c = QFrame()
            c.setFixedHeight(80)
            c.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius: 6px; }
            """)
            v = QVBoxLayout(c)
            v.setContentsMargins(8, 4, 8, 4)
            v.setSpacing(4)
            h = QHBoxLayout()
            if icon:
                ico = QLabel()
                p = QPixmap(icon)
                if not p.isNull():
                    ico.setPixmap(p.scaled(20,20,Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation))
                h.addWidget(ico)
            lbl = QLabel(text)
            h.addWidget(lbl)
            h.addStretch(1)
            v.addLayout(h)
            val = QLabel(str(value))
            val.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            hb = QHBoxLayout()
            hb.addStretch(1)
            hb.addWidget(val)
            v.addLayout(hb)
            return c

        top.addWidget(donut("#D52462", "#a21f46"))  # Fail: 40%
        mid = QHBoxLayout()
        mid.setSpacing(8)
        mid.addWidget(card("resources/icons/student.png",   "Student Type", "$0"))
        mid.addWidget(card("resources/icons/event.png",     "Event",        "05"))
        mid.addWidget(card("resources/icons/attendance.png","Attendance",   "100%"))
        mid.addWidget(card("resources/icons/exam.png",      "Subject",      "04"))
        top.addLayout(mid, stretch=1)
        top.addWidget(donut("#ffffff", "#255083"))  # Pass: 40%

        root.addLayout(top)

        # --- Search bar ---
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background:white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(6)
        icon = QLabel("🔍")
        icon.setFont(QFont("Arial", 12))
        sfl.addWidget(icon)
        le = QLineEdit()
        le.setPlaceholderText("Search Exam")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        root.addWidget(sf)

        # --- Scrollable Exam List ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QFrame()
        vl = QVBoxLayout(container)
        vl.setContentsMargins(0,0,0,0)
        vl.setSpacing(8)

        # sample rows
        for i in range(6):
            row = QFrame()
            row.setFixedHeight(60)
            row.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QPushButton {
                  background: none; border: 1px solid white; border-radius:4px;
                  color: white; padding:2px 8px;
                }
                QPushButton:hover {
                  background: #D52462; border-color: #D52462;
                }
            """)
            h = QHBoxLayout(row)
            h.setContentsMargins(8,8,8,8)
            h.setSpacing(12)

            # icon
            ico = QLabel()
            p = QPixmap("resources/icons/award.png")
            if not p.isNull():
                ico.setPixmap(p.scaled(24,24,Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
            h.addWidget(ico)

            # text
            txt = QLabel(
                "School management system    "
                "Dateline: 12/Jan/2025, 12:00PM    "
                "Subject: Oracle    Point: 20/20 pts"
            )
            txt.setStyleSheet("color:white;")
            txt.setFont(QFont("Arial", 12))
            h.addWidget(txt, 1)

            # action
            btn = QPushButton("Do")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            h.addWidget(btn)

            vl.addWidget(row)

        vl.addStretch(1)
        scroll.setWidget(container)
        root.addWidget(scroll, 1)
