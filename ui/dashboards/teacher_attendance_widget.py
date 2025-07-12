# ui/dashboards/teacher_attendance_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QSizePolicy, QHeaderView, QScrollArea
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class TeacherAttendanceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        # --- root layout ---
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(16)

        # --- top summary bar ---
        top_bar = QFrame()
        top_bar.setStyleSheet("background: #1B3452; border-radius:6px;")
        tb = QHBoxLayout(top_bar)
        tb.setContentsMargins(8, 8, 8, 8)
        tb.setSpacing(12)

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

        tb.addWidget(make_card("Classmate", 25,      "resources/icons/class.png"))
        tb.addWidget(make_card("Female",   12,      "resources/icons/female.png"))
        tb.addWidget(make_card("Absent",   2,       "resources/icons/absent.png"))
        tb.addWidget(make_card("Request",  3,       "resources/icons/request.png"))
        tb.addWidget(make_card("",         "CSE",   circle=True))

        top_bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        root.addWidget(top_bar)

        # --- search + action buttons ---
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(8)

        # search frame
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

        # Submit button
        btn_submit = QPushButton("Submit")
        for b in (btn_submit,):
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(28)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius:14px;
                    padding: 0 16px; font-size:13px;
                }
                QPushButton:hover { background: #255083; }
            """)
        row2.addWidget(btn_submit)

        # Report Attendance button
        btn_report = QPushButton("Report Attendance")
        for b in (btn_report,):
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(28)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius:14px;
                    padding: 0 16px; font-size:13px;
                }
                QPushButton:hover { background: #255083; }
            """)
        row2.addWidget(btn_report)

        # Notification button
        btn_notif = QPushButton("Notification")
        for b in (btn_notif,):
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(28)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color: white;
                    border: none; border-radius:14px;
                    padding: 0 16px; font-size:13px;
                }
                QPushButton:hover { background: #255083; }
            """)
        row2.addWidget(btn_notif)

        root.addLayout(row2)

        # --- attendance table ---
        tbl = QTableWidget()
        tbl.setColumnCount(8)
        tbl.setHorizontalHeaderLabels([
            "No", "Student_ID", "Photo", "Student Name",
            "Gender", "Statue", "Reason", "Remark"
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

        # demo data
        demo = [
            ("0007361", "Sok Sao", "Female", "A", "", "")
        ] * 10

        tbl.setRowCount(len(demo))
        for i, (sid, name, gender, status, reason, remark) in enumerate(demo):
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
            tbl.setItem(i, 5, QTableWidgetItem(status))
            tbl.setItem(i, 6, QTableWidgetItem(reason))
            tbl.setItem(i, 7, QTableWidgetItem(remark))

        # wrap in scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(tbl)
        root.addWidget(scroll, 1)
