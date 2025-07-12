# ui/dashboards/teacher_result_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QScrollArea, QTableWidget,
    QTableWidgetItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class TeacherResultWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)
        main.setSpacing(16)

        # --- Top summary bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        bh = QHBoxLayout(bar)
        bh.setContentsMargins(8, 8, 8, 8)
        bh.setSpacing(12)

        # Helper to build each card
        def make_card(widget):
            w = QFrame()
            w.setFixedHeight(80)
            w.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            layout = QVBoxLayout(w)
            layout.setContentsMargins(8, 4, 8, 4)
            layout.setSpacing(4)
            layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)
            return w

        # 1) Major/Batch/Class multiline label
        txt = QLabel(
            "Major : Computer science and Engineering\n"
            "Batch : 08\n"
            "Class : Weekend"
        )
        txt.setFont(QFont("Arial", 11))
        txt.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        bh.addWidget(make_card(txt), 2)

        # 2) Student count
        stud_lbl = QLabel()
        stud_lbl.setText("Student\n\n24")
        stud_lbl.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        stud_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bh.addWidget(make_card(stud_lbl), 1)

        # 3) Result pie placeholder
        pie = QFrame()
        pie.setFixedSize(60, 60)
        pie.setStyleSheet("""
            QFrame {
                border: 4px solid lightgray;
                border-radius: 30px;
                background: transparent;
            }
        """)
        legend = QLabel("Pass: 40%   Fail: 40%")
        legend.setFont(QFont("Arial", 8))
        legend.setStyleSheet("color: #ccc;")
        container = QVBoxLayout()
        container.setContentsMargins(0, 0, 0, 0)
        container.addWidget(pie, alignment=Qt.AlignmentFlag.AlignCenter)
        container.addWidget(legend, alignment=Qt.AlignmentFlag.AlignCenter)
        holder = QFrame()
        holder.setLayout(container)
        bh.addWidget(make_card(holder), 1)

        main.addWidget(bar)

        # --- Search + Submit Row ---
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(8)

        # Search field
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(8)
        lbl = QLabel("Result")
        lbl.setFont(QFont("Arial", 12))
        sfl.addWidget(lbl)
        le = QLineEdit()
        le.setPlaceholderText("Search Result")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row.addWidget(sf, 1)

        # Submit button
        btn = QPushButton("+ Submit")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedHeight(32)
        btn.setStyleSheet("""
            QPushButton {
                background: #FD367E; color: white;
                border: none; border-radius: 16px;
                padding: 0 16px; font-size:13px;
            }
            QPushButton:hover { background: #ff5a8f; }
        """)
        row.addWidget(btn)

        main.addLayout(row)

        # --- Result Table ---
        tbl = QTableWidget()
        headers = [
            "No", "Student_ID", "Student Name", "Gender",
            "Attendance", "Assignment", "Exam",
            "Survey", "Class Activity", "Total"
        ]
        tbl.setColumnCount(len(headers))
        tbl.setHorizontalHeaderLabels(headers)
        tbl.horizontalHeader().setStretchLastSection(True)
        tbl.verticalHeader().setVisible(False)
        tbl.setAlternatingRowColors(True)
        tbl.setStyleSheet("""
            QTableWidget {
                background: white;
                alternate-background-color: #f4f4f4;
            }
        """)

        # demo data: repeat 11 rows
        demo = [("007361", "Moeng Kimheang", "Male",
                 "10", "40", "40", "10", "05", "105")] * 11
        tbl.setRowCount(len(demo))
        for i, rowdata in enumerate(demo):
            tbl.setItem(i, 0, QTableWidgetItem(f"{i+1:02d}"))
            for col, val in enumerate(rowdata, start=1):
                tbl.setItem(i, col, QTableWidgetItem(str(val)))

        # put table into a scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        wrapper = QWidget()
        wl = QVBoxLayout(wrapper)
        wl.setContentsMargins(0, 0, 0, 0)
        wl.addWidget(tbl)
        scroll.setWidget(wrapper)

        main.addWidget(scroll, 1)
