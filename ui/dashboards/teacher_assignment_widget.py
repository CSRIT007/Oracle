# ui/dashboards/teacher_assignment_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QPushButton, QLineEdit, QScrollArea, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont

class TeacherAssignmentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)
        main.setSpacing(16)

        # --- Top Metrics Bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        bh = QHBoxLayout(bar)
        bh.setContentsMargins(8, 8, 8, 8)
        bh.setSpacing(12)

        def make_card(title, value, icon=None, circle=False, legend=None):
            frm = QFrame()
            frm.setFixedHeight(80)
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            fl = QVBoxLayout(frm)
            fl.setContentsMargins(8, 4, 8, 4)
            fl.setSpacing(4)

            lbl = QLabel(title)
            lbl.setFont(QFont("Arial", 10))
            fl.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)

            if circle:
                # simple circle placeholder
                circ = QLabel()
                circ.setFixedSize(60, 60)
                circ.setStyleSheet("""
                    QLabel {
                        border: 4px solid lightgray;
                        border-radius: 30px;
                        background: transparent;
                    }
                """)
                fl.addWidget(circ, alignment=Qt.AlignmentFlag.AlignCenter)
                if legend:
                    lg = QLabel(legend)
                    lg.setFont(QFont("Arial", 8))
                    lg.setStyleSheet("color: #ccc;")
                    fl.addWidget(lg, alignment=Qt.AlignmentFlag.AlignCenter)
            else:
                row = QHBoxLayout()
                if icon:
                    ico = QLabel()
                    pix = QPixmap(icon)
                    if not pix.isNull():
                        ico.setPixmap(pix.scaled(20,20,Qt.AspectRatioMode.KeepAspectRatio,
                                                 Qt.TransformationMode.SmoothTransformation))
                    row.addWidget(ico)
                val = QLabel(str(value))
                val.setFont(QFont("Arial", 14, QFont.Weight.Bold))
                row.addWidget(val)
                row.addStretch()
                fl.addLayout(row)

            return frm

        # left pie
        bh.addWidget(make_card("", "", circle=True, legend="Already:40%  Not yet:40%"))
        # four stats
        bh.addWidget(make_card("Student Type", "$0", icon="resources/icons/student.png"))
        bh.addWidget(make_card("Event",        "05", icon="resources/icons/event.png"))
        bh.addWidget(make_card("Attendance",  "100%", icon="resources/icons/attendance.png"))
        bh.addWidget(make_card("Subject",      "04", icon="resources/icons/subject.png"))
        # right pie
        bh.addWidget(make_card("", "", circle=True, legend="Pass:40%  Fail:40%"))

        bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main.addWidget(bar)

        # --- Search + Create Row ---
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(8)

        # search box
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background:white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(8)
        lbl = QLabel("Assignment")
        lbl.setFont(QFont("Arial", 12))
        sfl.addWidget(lbl)
        le = QLineEdit()
        le.setPlaceholderText("Search Assignment")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row.addWidget(sf, 1)

        # Create button
        btn_create = QPushButton("+ Create")
        btn_create.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_create.setFixedHeight(32)
        btn_create.setStyleSheet("""
            QPushButton {
                background: #FD367E; color: white;
                border: none; border-radius: 16px;
                padding: 0 16px; font-size:13px;
            }
            QPushButton:hover { background: #ff5a8f; }
        """)
        row.addWidget(btn_create)

        main.addLayout(row)

        # --- Assignment List ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        cv = QVBoxLayout(container)
        cv.setContentsMargins(0,0,0,0)
        cv.setSpacing(8)

        # sample data
        demo = [
            {"title":"School management System",
             "date":"12/Jan/2025, 12:00PM",
             "subject":"Oracle"}
        ] * 6

        for item in demo:
            itm = QFrame()
            itm.setStyleSheet("""
                QFrame { background: #1B3452; border-radius:6px; }
                QLabel { color: white; }
            """)
            il = QHBoxLayout(itm)
            il.setContentsMargins(12, 8, 12, 8)
            il.setSpacing(12)

            # icon
            ico = QLabel()
            pix = QPixmap("resources/icons/assignment.png")
            if not pix.isNull():
                ico.setPixmap(pix.scaled(32,32,Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation))
            il.addWidget(ico)

            # text
            txt = QLabel(
                f"<b>Title :</b> {item['title']}    "
                f"<b>Dateline :</b> {item['date']}    "
                f"<b>Subject :</b> {item['subject']}"
            )
            txt.setFont(QFont("Arial", 11))
            il.addWidget(txt, 1)

            # buttons
            btns = QFrame()
            bl = QVBoxLayout(btns)
            bl.setContentsMargins(0,0,0,0)
            bl.setSpacing(4)
            for name in ("Edit","View"):
                b = QPushButton(name)
                b.setCursor(Qt.CursorShape.PointingHandCursor)
                b.setFixedSize(60,24)
                b.setStyleSheet("""
                    QPushButton {
                        background: none; color: white;
                        border: 1px solid white; border-radius:4px;
                        font-size:12px;
                    }
                    QPushButton:hover { background: #255083; }
                """)
                bl.addWidget(b)
            il.addWidget(btns)

            cv.addWidget(itm)

        cv.addStretch(1)
        scroll.setWidget(container)
        main.addWidget(scroll, 1)
