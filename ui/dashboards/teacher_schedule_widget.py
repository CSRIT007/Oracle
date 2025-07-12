# ui/dashboards/teacher_schedule_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class TeacherScheduleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12,12,12,12)
        root.setSpacing(16)

        # --- Top summary bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(8,8,8,8)
        bl.setSpacing(12)

        # Today's Course card
        def make_stat(title, value, icon_path):
            frm = QFrame()
            frm.setFixedHeight(80)
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            fl = QVBoxLayout(frm)
            fl.setContentsMargins(8,4,8,4)
            fl.setSpacing(4)

            lbl = QLabel(title)
            lbl.setFont(QFont("Arial", 10))
            fl.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)

            row = QHBoxLayout()
            ico = QLabel()
            pix = QPixmap(icon_path)
            if not pix.isNull():
                ico.setPixmap(pix.scaled(24,24,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
            row.addWidget(ico)
            val = QLabel(str(value))
            val.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            row.addWidget(val)
            row.addStretch()
            fl.addLayout(row)
            return frm

        bl.addWidget(make_stat("Today's Course", 5, "resources/icons/class.png"))

        # Profile card
        prof = QFrame()
        prof.setStyleSheet("background: #1B3452; border-radius:6px;")
        pl = QHBoxLayout(prof)
        pl.setContentsMargins(12,8,12,8)
        pl.setSpacing(16)

        avatar = QLabel()
        pix = QPixmap("resources/icons/user-white.png")
        if not pix.isNull():
            avatar.setPixmap(pix.scaled(48,48,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
        pl.addWidget(avatar)

        info = QLabel(
            "Name       : Teacher Name\n"
            "Position : Full Time\n"
            "Computer Science and engineering"
        )
        info.setStyleSheet("color: white;")
        info.setFont(QFont("Arial", 12))
        pl.addWidget(info, 1)

        prof.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        prof.setFixedHeight(80)
        bl.addWidget(prof, 1)

        root.addWidget(bar)

        # --- Search + Today toggle ---
        row2 = QHBoxLayout()
        row2.setContentsMargins(0,0,0,0)
        row2.setSpacing(8)

        # Search
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        sfl.setSpacing(8)
        lbl = QLabel("Course")
        lbl.setFont(QFont("Arial", 12))
        sfl.addWidget(lbl)
        le = QLineEdit()
        le.setPlaceholderText("Search Course")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row2.addWidget(sf, 1)

        # Today button
        btn = QPushButton("Today")
        btn.setFixedHeight(32)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: #1B3452; color: white;
                border: none; border-radius:16px;
                padding: 0 16px; font-size:13px;
            }
            QPushButton:hover { background: #255083; }
        """)
        row2.addWidget(btn)
        root.addLayout(row2)

        # --- Time Table grid ---
        grid_frame = QFrame()
        grid_frame.setStyleSheet("background: #1B3452; border-radius:6px;")
        gl = QGridLayout(grid_frame)
        gl.setContentsMargins(8,8,8,8)
        gl.setSpacing(12)

        def make_card(subject, cid="CS412", date="12/Jan/2025",
                      time="8:00 PM - 9:40 PM", cls="Brasat Banteay Kdei", bld="Build B"):
            frm = QFrame()
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            fl = QVBoxLayout(frm)
            fl.setContentsMargins(8,8,8,8)
            fl.setSpacing(6)

            # icon + subject row
            row = QHBoxLayout()
            ico = QLabel()
            pix = QPixmap("resources/icons/class.png")
            if not pix.isNull():
                ico.setPixmap(pix.scaled(20,20,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
            row.addWidget(ico)
            row.addWidget(QLabel(subject))
            row.addStretch()
            fl.addLayout(row)

            # details
            for label, val in (
                ("ID", cid), ("Date", date),
                ("Time", time), ("Class", cls), ("Building", bld)
            ):
                hl = QHBoxLayout()
                hl.addWidget(QLabel(f"{label} :"))
                hl.addWidget(QLabel(val))
                hl.addStretch()
                fl.addLayout(hl)

            return frm

        # populate 2 rows × 5 columns = 10 cards
        rows = 2; cols = 5
        for i in range(rows*cols):
            r = i // cols
            c = i % cols
            card = make_card("Oracle")
            card.setFixedWidth(220)
            gl.addWidget(card, r, c)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(grid_frame)
        root.addWidget(scroll, 1)
