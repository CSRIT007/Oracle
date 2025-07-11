# ui/dashboards/student_class_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QSizePolicy, QHeaderView
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class StudentClassWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)
        main.setSpacing(16)

        # --- Top summary bar ---
        bar = QFrame()
        bar.setStyleSheet("background: #1B3452;")
        bh = QHBoxLayout(bar)
        bh.setContentsMargins(8, 8, 8, 8)
        bh.setSpacing(12)

        def make_card(title, value, icon_path=None, circle=False):
            frm = QFrame()
            frm.setFixedHeight(80)
            frm.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius: 6px; }
                QLabel { color: white; }
            """)
            layout = QVBoxLayout(frm)
            layout.setContentsMargins(8, 4, 8, 4)
            layout.setSpacing(4)

            lbl_title = QLabel(title)
            lbl_title.setFont(QFont("Arial", 10))
            layout.addWidget(lbl_title, alignment=Qt.AlignmentFlag.AlignLeft)

            if circle:
                circle_lbl = QLabel(value)
                circle_lbl.setFixedSize(60, 60)
                circle_lbl.setStyleSheet("""
                    QLabel {
                        background: white;
                        color: #1B3452;
                        border-radius: 30px;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)
                layout.addWidget(circle_lbl, alignment=Qt.AlignmentFlag.AlignCenter)
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
                val_lbl = QLabel(str(value))
                val_lbl.setFont(QFont("Arial", 14, QFont.Weight.Bold))
                row.addWidget(val_lbl)
                row.addStretch(1)
                layout.addLayout(row)

            return frm

        # Add cards into the layout, not frame
        bh.addWidget(make_card("Classmate", 25, "resources/icons/class.png"))
        bh.addWidget(make_card("Female", 12, "resources/icons/female.png"))
        bh.addWidget(make_card("", "CSE", circle=True))
        bh.addWidget(make_card("Start", "12/Jan/2025"))
        bh.addWidget(make_card("End", "20/Jan/2025"))

        bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main.addWidget(bar)

        # --- Search + action buttons row ---
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(8)

        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12, 0, 12, 0)
        sfl.setSpacing(4)
        sfl.addWidget(QLabel("Student"))
        le = QLineEdit()
        le.setPlaceholderText("Search Student")
        le.setFrame(False)
        le.setStyleSheet("font-size:13px;")
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        row2.addWidget(sf, 1)

        for text in ("Lesson file", "Class Information"):
            b = QPushButton(text)
            b.setFixedHeight(28)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius: 14px; padding: 0 12px;
                    font-size: 13px;
                }
                QPushButton:hover { background: #255083; }
            """)
            row2.addWidget(b)

        main.addLayout(row2)

        # --- Student table ---
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

        demo = [
            ("0007361", "Sok Sao", "Female", "12/Jan/2006",
             "015647282", "sao736@gmail.com", "BatDoeng High School")
        ] * 10

        tbl.setRowCount(len(demo))
        for i, (sid, name, gender, dob, phone, email, school) in enumerate(demo):
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

        main.addWidget(tbl, 1)
        main.addStretch()
