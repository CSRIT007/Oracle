# ui/dashboards/teacher_salary_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QScrollArea, QSizePolicy
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class TeacherSalaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        main.setSpacing(16)

        # 1) Header strip (profile + donut + salary total)
        top = QFrame()
        top.setStyleSheet("background: #1B3452; border-radius:6px;")
        top.setFixedHeight(100)
        tlay = QHBoxLayout(top)
        tlay.setContentsMargins(16,8,16,8)
        tlay.setSpacing(12)

        # avatar
        av = QLabel()
        pix = QPixmap("resources/images/person.png")
        av.setPixmap(pix.scaled(64,64, Qt.AspectRatioMode.KeepAspectRatio))
        tlay.addWidget(av)

        # info
        info = QVBoxLayout()
        nm = QLabel("Teacher Name")
        nm.setStyleSheet("color:white; font-size:18px; font-weight:600;")
        info.addWidget(nm)
        loc = QLabel("📍 Location")
        loc.setStyleSheet("color:white; font-size:12px;")
        info.addWidget(loc)
        dept = QLabel("Computer Science and engineering")
        dept.setStyleSheet("color:white; font-size:12px;")
        info.addWidget(dept)
        tlay.addLayout(info)

        tlay.addStretch(1)

        # donut placeholder
        donut = QFrame()
        donut.setFixedSize(80,80)
        donut.setStyleSheet("background:white; border-radius:40px;")
        tlay.addWidget(donut)

        # salary total
        sal = QFrame()
        sal.setStyleSheet("background:white; border-radius:6px;")
        sal.setFixedHeight(80)
        slay = QVBoxLayout(sal)
        slay.setContentsMargins(12,4,12,4)
        slay.setSpacing(4)
        lbl = QLabel("Salary Total")
        lbl.setFont(QFont("Arial", 10))
        slay.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)
        amt = QLabel("$1,000 / month")
        amt.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        slay.addWidget(amt, alignment=Qt.AlignmentFlag.AlignCenter)
        tlay.addWidget(sal)

        main.addWidget(top)

        # 2) Search + buttons row
        row2 = QHBoxLayout()
        row2.setSpacing(8)

        # salary search
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background:white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        sfl.setSpacing(8)
        tab = QLabel("Salary")
        tab.setFont(QFont("Arial", 11))
        sfl.addWidget(tab)
        le = QLineEdit()
        le.setPlaceholderText("Search Salary ID")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row2.addWidget(sf, 1)

        # action buttons
        for text in ("+ Request", "Report", "Invoice", "Report Attendance"):
            b = QPushButton(text)
            b.setFixedHeight(28)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius: 14px;
                    padding: 0 12px; font-size: 13px;
                }
                QPushButton:hover { background: #255083; }
            """)
            row2.addWidget(b)

        main.addLayout(row2)

        # 3) Salary table
        header = QFrame()
        header.setStyleSheet("background: #1B3452; border-radius:6px;")
        header.setFixedHeight(28)
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(12,0,0,0)
        hlay.addWidget(QLabel("Salary List", styleSheet="color:white; font-weight:600;"))
        main.addWidget(header)

        tbl = QTableWidget()
        cols = ["No","Teacher_ID","Teacher Name","Gender","Attendance",
                "Date","Time In","Time Out","Total"]
        tbl.setColumnCount(len(cols))
        tbl.setHorizontalHeaderLabels(cols)
        tbl.setAlternatingRowColors(True)
        tbl.setStyleSheet("""
            QTableWidget { background:white; alternate-background-color:#f4f4f4; }
        """)
        tbl.verticalHeader().setVisible(False)
        tbl.horizontalHeader().setStretchLastSection(True)
        tbl.setRowCount(10)
        demo = ("007361","Moeng Kimheang","Male","0","12/Jan/2025",
                "08:00","09:30","1.5")
        for i in range(10):
            tbl.setItem(i, 0, QTableWidgetItem(f"{i+1:02d}"))
            for j, text in enumerate(demo, start=1):
                tbl.setItem(i, j, QTableWidgetItem(text))
        main.addWidget(tbl, 1)
