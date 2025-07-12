# ui/dashboards/teacher_exam_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt

class TeacherExamWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        main.setSpacing(16)

        # --- Summary bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(8,8,8,8)
        bl.setSpacing(12)

        def make_circle(legend: str):
            frm = QVBoxLayout()
            circle = QFrame()
            circle.setFixedSize(60,60)
            circle.setStyleSheet("""
                QFrame { 
                    border: 4px solid lightgray; 
                    border-radius: 30px; 
                    background: transparent; 
                }
            """)
            lbl = QLabel(legend)
            lbl.setFont(QFont("Arial", 8))
            lbl.setStyleSheet("color:#ccc;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            frm.addWidget(circle, alignment=Qt.AlignmentFlag.AlignCenter)
            frm.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
            container = QFrame()
            container.setLayout(frm)
            container.setFixedHeight(80)
            return container

        def make_stat(title: str, value: str, icon_path: str):
            frm = QFrame()
            frm.setFixedHeight(80)
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            vl = QVBoxLayout(frm)
            vl.setContentsMargins(8,4,8,4)
            vl.setSpacing(4)
            t = QLabel(title)
            t.setFont(QFont("Arial", 10))
            vl.addWidget(t, alignment=Qt.AlignmentFlag.AlignLeft)
            row = QHBoxLayout()
            if icon_path:
                ico = QLabel()
                pix = QPixmap(icon_path)
                if not pix.isNull():
                    ico.setPixmap(pix.scaled(20,20,Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation))
                row.addWidget(ico)
            v = QLabel(value)
            v.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            row.addWidget(v)
            row.addStretch(1)
            vl.addLayout(row)
            return frm

        # left circle
        bl.addWidget(make_circle("Already:40%  Not yet:40%"))

        # stats
        bl.addWidget(make_stat("Student Type", "$0",          "resources/icons/user.png"))
        bl.addWidget(make_stat("Event",        "05",          "resources/icons/event.png"))
        bl.addWidget(make_stat("Attendance",   "100%",        "resources/icons/attendance.png"))
        bl.addWidget(make_stat("Subject",      "04",          "resources/icons/class.png"))

        # right circle
        bl.addWidget(make_circle("Pass:40%  Fail:40%"))

        main.addWidget(bar)

        # --- Search + Create row ---
        row = QHBoxLayout()
        row.setContentsMargins(0,0,0,0)
        row.setSpacing(8)

        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background:white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        sfl.setSpacing(8)
        lab = QLabel("Exam")
        lab.setFont(QFont("Arial", 12))
        sfl.addWidget(lab)
        le = QLineEdit()
        le.setPlaceholderText("Search Exam")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row.addWidget(sf, 1)

        btn = QPushButton("+ Create")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedHeight(32)
        btn.setStyleSheet("""
            QPushButton {
                background: #FD367E; color: white;
                border: none; border-radius:16px;
                padding: 0 16px; font-size:13px;
            }
            QPushButton:hover { background: #ff5a8f; }
        """)
        row.addWidget(btn)

        main.addLayout(row)

        # --- Exam list ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        cl = QVBoxLayout(content)
        cl.setContentsMargins(0,0,0,0)
        cl.setSpacing(12)

        # dummy data
        demo = [
            {
                "title":        "School management System",
                "dateline":     "12/Jan/2025, 12:00PM",
                "subject":      "Oracle"
            }
        ] * 6

        for item in demo:
            itm = QFrame()
            itm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel, QPushButton { color: white; }
            """)
            hl = QHBoxLayout(itm)
            hl.setContentsMargins(12,8,12,8)
            hl.setSpacing(16)

            # icon
            icon = QLabel()
            pix = QPixmap("resources/icons/exam.png")
            if not pix.isNull():
                icon.setPixmap(pix.scaled(32,32,Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation))
            hl.addWidget(icon)

            # text
            txt = QLabel(
                f"Title : {item['title']}    "
                f"Dateline: {item['dateline']}    "
                f"Subject: {item['subject']}"
            )
            txt.setFont(QFont("Arial", 11))
            hl.addWidget(txt, 1)

            # buttons
            for label in ("Edit", "View"):
                b = QPushButton(label)
                b.setCursor(Qt.CursorShape.PointingHandCursor)
                b.setFixedHeight(28)
                b.setStyleSheet("""
                    QPushButton {
                        background: none; border: 1px solid white;
                        border-radius:14px; padding:0 12px; font-size:13px;
                    }
                    QPushButton:hover { background: #255083; }
                """)
                hl.addWidget(b)

            cl.addWidget(itm)

        scroll.setWidget(content)
        main.addWidget(scroll, 1)
