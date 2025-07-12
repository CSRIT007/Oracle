# ui/dashboards/teacher_experience_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class TeacherExperienceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12,12,12,12)
        root.setSpacing(16)

        # --- Top stats bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(8,8,8,8)
        bl.setSpacing(12)

        def make_stat(title, value, icon_path=None):
            frm = QFrame()
            frm.setFixedHeight(80)
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            fl = QVBoxLayout(frm)
            fl.setContentsMargins(8,4,8,4)
            fl.setSpacing(4)

            # title + icon row
            row = QHBoxLayout()
            if icon_path:
                ico = QLabel()
                pix = QPixmap(icon_path)
                if not pix.isNull():
                    ico.setPixmap(pix.scaled(20,20,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation))
                row.addWidget(ico)
            row.addWidget(QLabel(title))
            row.addStretch()
            fl.addLayout(row)

            # value
            val = QLabel(str(value))
            val.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            fl.addWidget(val, alignment=Qt.AlignmentFlag.AlignRight)
            return frm

        # left stats
        bl.addWidget(make_stat("Experience",   "04", "resources/icons/experience.png"))
        bl.addWidget(make_stat("Event",        "05", "resources/icons/event.png"))

        # center big label
        center = QLabel("Experience")
        center.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        center.setStyleSheet("color: white;")
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_frame = QFrame()
        center_frame.setStyleSheet("background: #1B3452; border-radius:6px;")
        cf_layout = QVBoxLayout(center_frame)
        cf_layout.setContentsMargins(0,0,0,0)
        cf_layout.addWidget(center)
        center_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        center_frame.setFixedHeight(80)
        bl.addWidget(center_frame, 1)

        # right stats
        bl.addWidget(make_stat("Subject", "100%", "resources/icons/subject.png"))
        bl.addWidget(make_stat("Type",     "$0",   "resources/icons/type.png"))

        root.addWidget(bar)

        # --- Search bar ---
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        sfl.setSpacing(8)

        lbl = QLabel("Experience")
        lbl.setFont(QFont("Arial", 12))
        sfl.addWidget(lbl)

        le = QLineEdit()
        le.setPlaceholderText("Search Experience")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)

        search_icon = QLabel("🔍")
        search_icon.setFont(QFont("Arial", 14))
        sfl.addWidget(search_icon)

        root.addWidget(sf)

        # --- Experience list ---
        list_header = QLabel("Experience List")
        list_header.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        list_header.setStyleSheet("background: #1B3452; color: white; padding:8px; border-radius:6px;")
        list_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(list_header)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        cl = QVBoxLayout(container)
        cl.setContentsMargins(0,0,0,0)
        cl.setSpacing(8)

        # dummy entries
        for i in range(6):
            item = QFrame()
            item.setStyleSheet("background: #1B3452; border-radius:6px;")
            il = QHBoxLayout(item)
            il.setContentsMargins(12,8,12,8)
            il.setSpacing(16)

            # icon
            ico = QLabel()
            pix = QPixmap("resources/icons/certificate.png")
            if not pix.isNull():
                ico.setPixmap(pix.scaled(32,32,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation))
            il.addWidget(ico)

            # text
            text = QLabel(
                "Title : School management System    "
                "Dateline: 12/Jan/2025, 12:00PM    "
                "Subject: Oracle"
            )
            text.setStyleSheet("color: white;")
            text.setFont(QFont("Arial", 11))
            il.addWidget(text, 1)

            # View button
            btn = QPushButton("View")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background: none;
                    border: 1px solid white;
                    border-radius:4px;
                    color: white;
                    padding: 4px 12px;
                }
                QPushButton:hover {
                    background: #255083;
                }
            """)
            il.addWidget(btn)

            cl.addWidget(item)

        scroll.setWidget(container)
        root.addWidget(scroll, 1)
