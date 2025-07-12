# ui/dashboards/teacher_class_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QSizePolicy, QHeaderView, QScrollArea
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt

class TeacherClassWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        # --- root layout ---
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(16)

        # --- summary bar ---
        summary = QFrame()
        summary.setStyleSheet("background: #1B3452; border-radius:6px;")
        sb = QHBoxLayout(summary)
        sb.setContentsMargins(8, 8, 8, 8)
        sb.setSpacing(12)

        def make_card(title, value, icon_path=None, circle=False):
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
                circ = QLabel(value)
                circ.setFixedSize(60, 60)
                circ.setStyleSheet("""
                    QLabel {
                        background: white;
                        color: #1B3452;
                        border-radius: 30px;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)
                fl.addWidget(circ, alignment=Qt.AlignmentFlag.AlignCenter)
            else:
                row = QHBoxLayout()
                if icon_path:
                    ico = QLabel()
                    pix = QPixmap(icon_path)
                    if not pix.isNull():
                        ico.setPixmap(pix.scaled(
                            20, 20,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation
                        ))
                    row.addWidget(ico)
                val = QLabel(str(value))
                val.setFont(QFont("Arial", 14, QFont.Weight.Bold))
                row.addWidget(val)
                row.addStretch()
                fl.addLayout(row)

            return frm

        sb.addWidget(make_card("Classmate", 25, "resources/icons/class.png"))
        sb.addWidget(make_card("Female",   12, "resources/icons/female.png"))
        sb.addWidget(make_card("",         "CSE", circle=True))
        sb.addWidget(make_card("Start",   "12/Jan/2025"))
        sb.addWidget(make_card("End",     "20/Jan/2025"))
        summary.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        root.addWidget(summary)

        # --- search & action row ---
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(8)

        # search box
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(8)

        lbl = QLabel("Student")
        lbl.setFont(QFont("Arial", 12))
        sfl.addWidget(lbl)

        le = QLineEdit()
        le.setPlaceholderText("Search Student")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)

        icon = QLabel("🔍")
        sfl.addWidget(icon)
        row2.addWidget(sf, 1)

        # class info button
        btn = QPushButton("Class Information")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedHeight(32)
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

        # --- student list table ---
        tbl = QTableWidget()
        tbl.setColumnCount(9)
        tbl.setHorizontalHeaderLabels([
            "No", "Student_ID", "Photo", "Student Name",
            "Gender", "Date of birth", "Phone number",
            "E-mail", "From School"
        ])
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tbl.verticalHeader().setVisible(False)
        tbl.setAlternatingRowColors(True)
        tbl.setStyleSheet("""
            QTableWidget {
                background: white;
                alternate-background-color: #f4f4f4;
            }
        """)

        # sample data
        sample = [
            ("0007361", "Sok Sao", "Female", "12/Jan/2006",
             "015647282", "Sao736@gmail.com", "BatDoeng High School")
        ] * 10

        tbl.setRowCount(len(sample))
        for i, (sid, name, gender, dob, phone, email, school) in enumerate(sample):
            tbl.setItem(i, 0, QTableWidgetItem(f"{i+1:02d}"))
            tbl.setItem(i, 1, QTableWidgetItem(sid))

            pic = QLabel()
            pix = QPixmap("resources/icons/person.png")
            if not pix.isNull():
                pic.setPixmap(pix.scaled(
                    24, 24,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
            tbl.setCellWidget(i, 2, pic)

            tbl.setItem(i, 3, QTableWidgetItem(name))
            tbl.setItem(i, 4, QTableWidgetItem(gender))
            tbl.setItem(i, 5, QTableWidgetItem(dob))
            tbl.setItem(i, 6, QTableWidgetItem(phone))
            tbl.setItem(i, 7, QTableWidgetItem(email))
            tbl.setItem(i, 8, QTableWidgetItem(school))

        # wrap table in scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(tbl)
        root.addWidget(scroll, 1)
