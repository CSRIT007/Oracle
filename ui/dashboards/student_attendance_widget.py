# ui/dashboards/student_attendance_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QSizePolicy, QHeaderView
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class StudentAttendanceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)
        main.setSpacing(16)

        # --- Header Title ---
        title_bar = QFrame()
        title_bar.setStyleSheet("background: #1B3452;")
        tb_layout = QHBoxLayout(title_bar)
        tb_layout.setContentsMargins(8, 8, 8, 8)
        lbl = QLabel("Attendance")
        lbl.setStyleSheet("color: white;")
        lbl.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        tb_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
        main.addWidget(title_bar)

        # --- Summary Cards ---
        summary = QFrame()
        sh = QHBoxLayout(summary)
        sh.setContentsMargins(0, 0, 0, 0)
        sh.setSpacing(12)

        def make_card(label, value, icon_path=None):
            card = QFrame()
            card.setFixedHeight(80)
            card.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius: 6px; }
                QLabel { color: white; }
            """)
            v = QVBoxLayout(card)
            v.setContentsMargins(8, 4, 8, 4)
            v.setSpacing(4)

            top = QHBoxLayout()
            if icon_path:
                ico = QLabel()
                pix = QPixmap(icon_path)
                if not pix.isNull():
                    ico.setPixmap(pix.scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, 
                                             Qt.TransformationMode.SmoothTransformation))
                top.addWidget(ico)
            top.addWidget(QLabel(label))
            top.addStretch(1)
            v.addLayout(top)

            bottom = QHBoxLayout()
            val = QLabel(str(value))
            val.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            bottom.addStretch(1)
            bottom.addWidget(val)
            v.addLayout(bottom)

            return card

        sh.addWidget(make_card("Attendance", "04", "resources/icons/attendance.png"))
        sh.addWidget(make_card("Rate", "02.01%", "resources/icons/percentage.png"))
        sh.addWidget(make_card("Score", "04", "resources/icons/score.png"))
        sh.addWidget(make_card("Subject", "04", "resources/icons/exam.png"))
        summary.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main.addWidget(summary)

        # --- Search + Request Row ---
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(8)

        # Search box
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(4)
        sfl.addWidget(QLabel("Attendance"))
        le = QLineEdit()
        le.setPlaceholderText("Search Attendance")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row2.addWidget(sf, 1)

        # Request button
        req = QPushButton("+ Request")
        req.setFixedHeight(32)
        req.setCursor(Qt.CursorShape.PointingHandCursor)
        req.setStyleSheet("""
            QPushButton {
                background: #1B3452; color: white;
                border: none; border-radius: 16px;
                padding: 0 16px; font-size: 13px;
            }
            QPushButton:hover { background: #255083; }
        """)
        row2.addWidget(req, 0)
        main.addLayout(row2)

        # --- Attendance Table ---
        tbl = QTableWidget()
        headers = [
            "No", "Student_ID", "Photo", "Student Name", "Gender",
            "Date", "Start Time", "End Time", "Subject", "Reason"
        ]
        tbl.setColumnCount(len(headers))
        tbl.setHorizontalHeaderLabels(headers)
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tbl.verticalHeader().setVisible(False)
        tbl.setAlternatingRowColors(True)
        tbl.setStyleSheet("""
            QTableWidget {
                background: white;
                alternate-background-color: #f4f4f4;
            }
        """)

        # dummy data
        demo = [
            ("0007361", "Sok Sao", "Female", "12/Jan/2006", "08:00 PM", "09:30 PM", "Oracle", "")
        ] * 10

        tbl.setRowCount(len(demo))
        for i, (sid, name, gender, date, st, et, subj, reason) in enumerate(demo):
            tbl.setItem(i, 0, QTableWidgetItem(f"{i+1:02d}"))
            tbl.setItem(i, 1, QTableWidgetItem(sid))

            # Photo icon
            pic = QLabel()
            pix = QPixmap("resources/icons/person.png")
            if not pix.isNull():
                pic.setPixmap(pix.scaled(24,24,Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation))
            tbl.setCellWidget(i, 2, pic)

            tbl.setItem(i, 3, QTableWidgetItem(name))
            tbl.setItem(i, 4, QTableWidgetItem(gender))
            tbl.setItem(i, 5, QTableWidgetItem(date))
            tbl.setItem(i, 6, QTableWidgetItem(st))
            tbl.setItem(i, 7, QTableWidgetItem(et))
            tbl.setItem(i, 8, QTableWidgetItem(subj))
            tbl.setItem(i, 9, QTableWidgetItem(reason or "..."))

        main.addWidget(tbl, 1)
