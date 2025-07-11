# ui/dashboards/student_result_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QFrame
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class StudentResultWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(16)

        # — Title —
        title = QLabel("Result List")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        root.addWidget(title)

        # — Term selectors —
        term_row = QHBoxLayout()
        term_row.setSpacing(8)
        term_row.addWidget(QLabel("Select Term:"))
        combo1 = QComboBox()
        combo1.addItems(["Term 1", "Term 2", "Term 3"])
        term_row.addWidget(combo1)
        term_row.addWidget(QLabel("Select Your Term:"))
        combo2 = QComboBox()
        combo2.addItems(["Term 1", "Term 2", "Term 3"])
        term_row.addWidget(combo2)
        term_row.addStretch(1)
        root.addLayout(term_row)

        # — Results table —
        tbl = QTableWidget()
        headers = [
            "Code", "Course Title", "Alpha Grade",
            "Credits Attempted", "Credits Earned",
            "Grade", "Total", "Remarks"
        ]
        tbl.setColumnCount(len(headers))
        tbl.setHorizontalHeaderLabels(headers)
        tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tbl.verticalHeader().setVisible(False)
        tbl.setAlternatingRowColors(True)

        # Sample data
        demo = [
            ("CS 212", "Web Development I", "A+", "3", "3", "4.00", "12", "Superior"),
            ("CS 214", "Java Programming",    "A",  "6", "6", "4.00", "24", "Excellent"),
            ("CS 211", "UX/UI Design",        "A",  "3", "3", "4.00", "12", "Excellent"),
            ("CS213", "Data Structures & Algos", "A+", "3", "3", "4.00", "12", "Superior"),
        ]
        tbl.setRowCount(len(demo))
        for i, row in enumerate(demo):
            for j, val in enumerate(row):
                tbl.setItem(i, j, QTableWidgetItem(val))

        # Totals rows
        def add_totals(label, columns):
            row = tbl.rowCount()
            tbl.insertRow(row)
            tbl.setItem(row, 1, QTableWidgetItem(label))
            for col, text in columns.items():
                tbl.setItem(row, col, QTableWidgetItem(text))

        add_totals("Total Credits Transferred", {2: "15", 5: "0", 6: "0", 7: "0.00"})
        add_totals("Total Credits Attained",   {2: "15", 3: "3", 6: "60.00"})

        root.addWidget(tbl, 1)

        # — Cumulative GPA display —
        gpa_frame = QFrame()
        gpa_layout = QHBoxLayout(gpa_frame)
        gpa_layout.addStretch(1)
        gpa_label = QLabel("Cumulative GPA: 4.00")
        gpa_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        gpa_layout.addWidget(gpa_label)
        root.addWidget(gpa_frame)
