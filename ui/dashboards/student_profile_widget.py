# ui/dashboards/student_profile_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QGridLayout, QComboBox, QListWidget, QTableWidget,
    QTableWidgetItem, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class StudentProfileWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(12, 12, 12, 12)

        # --- Top header cards ---
        header_frame = QFrame()
        header_layout = QHBoxLayout(header_frame)
        header_layout.setSpacing(6)
        header_layout.setContentsMargins(0, 0, 0, 0)

        def make_card(title, subtitle=None, icon=None, width=150):
            card = QFrame()
            card.setStyleSheet("background:white; border-radius:8px;")
            card.setFixedHeight(80)
            card.setFixedWidth(width)
            layout = QVBoxLayout(card)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if icon:
                ico = QLabel()
                px = QPixmap(icon)
                if not px.isNull():
                    ico.setPixmap(px.scaled(24,24,Qt.AspectRatioMode.KeepAspectRatio,
                                            Qt.TransformationMode.SmoothTransformation))
                layout.addWidget(ico)
            lbl = QLabel(title)
            lbl.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(lbl)
            if subtitle:
                sub = QLabel(subtitle)
                sub.setFont(QFont("Arial", 10))
                sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(sub)
            return card

        header_layout.addWidget(make_card("Student Type", icon="resources/icons/class.png"))
        header_layout.addWidget(make_card("Scholarship", subtitle="100%"))
        header_layout.addWidget(make_card("Subject", icon="resources/icons/subject.png"))
        header_layout.addWidget(make_card("Computer Science\nand Engineering", width=240))
        header_layout.addWidget(make_card("Event",    icon="resources/icons/event.png"))
        header_layout.addWidget(make_card("05", subtitle="Total"))
        main_layout.addWidget(header_frame)

        # --- Middle panels: Info / Notices / Chart placeholder ---
        content_frame = QFrame()
        content_layout = QHBoxLayout(content_frame)
        content_layout.setSpacing(12)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # -- My Information panel --
        info_frame = QFrame()
        info_frame.setStyleSheet("background:white; border-radius:8px;")
        info_layout = QVBoxLayout(info_frame)
        info_layout.setContentsMargins(8, 8, 8, 8)

        # Title bar
        ti = QLabel("My Information")
        ti.setStyleSheet("background:#1B3452; color:white; padding:4px;")
        ti.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        ti.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_layout.addWidget(ti)

        # Details + photo
        body = QHBoxLayout()
        grid = QGridLayout()
        grid.setVerticalSpacing(6)
        data = [
            ("StudentID", "0007361"),
            ("Name", "Moeng Kimheang"),
            ("Gender", "Male"),
            ("Father Name", "Moeng Sokea"),
            ("Mother Name", "Sao Savat"),
            ("Date Of Birth", "21/Oct/2006"),
            ("E_mail", "heang015873174@gmail.com"),
            ("Phone Number", "0962843472"),
            ("Address", "Compong speu"),
            ("Admission Date", "01/Jan/2024"),
            ("Major", "Computer Science and Engineering"),
            ("Batch", "08"),
            ("High School", "BatDoeng High School"),
            ("Bac II", "A"),
            ("Student", "Scholarship (100%)"),
        ]
        for r, (label, val) in enumerate(data):
            lbl = QLabel(f"{label}:")
            lbl.setFont(QFont("Arial",10))
            grd = QLabel(val)
            grd.setFont(QFont("Arial",10))
            grid.addWidget(lbl, r, 0, Qt.AlignmentFlag.AlignLeft)
            grid.addWidget(grd, r, 1, Qt.AlignmentFlag.AlignLeft)
        body.addLayout(grid, 3)

        # Photo
        pic = QLabel()
        px = QPixmap("resources/images/avatar.png")
        if not px.isNull():
            pic.setPixmap(px.scaled(100,100,Qt.AspectRatioMode.KeepAspectRatio,
                                    Qt.TransformationMode.SmoothTransformation))
        pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        body.addWidget(pic, 1)

        info_layout.addLayout(body)
        content_layout.addWidget(info_frame, 2)

        # -- Notice Board panel --
        notice = QFrame()
        notice.setStyleSheet("background:white; border-radius:8px;")
        nlay = QVBoxLayout(notice)
        nlay.setContentsMargins(8,8,8,8)
        h = QLabel("Notice Board")
        h.setStyleSheet("background:#1B3452; color:white; padding:4px;")
        h.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nlay.addWidget(h)
        lst = QListWidget()
        for it in ["Payment","Log in","Log out","Get Experience","Get Result","New Class","Payment"]:
            lst.addItem(f"• {it}    Date: 12/Jan/2025 05:30PM")
        nlay.addWidget(lst)
        content_layout.addWidget(notice, 1)

        # -- Total Study placeholder panel --
        study = QFrame()
        study.setStyleSheet("background:white; border-radius:8px;")
        slay = QVBoxLayout(study)
        slay.setContentsMargins(8,8,8,8)
        tt = QLabel("Total Study")
        tt.setStyleSheet("background:#1B3452; color:white; padding:4px;")
        tt.setFont(QFont("Arial",12, QFont.Weight.Bold))
        tt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        slay.addWidget(tt)
        placeholder = QLabel("📊 Chart goes here")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("color: #888888;")
        slay.addWidget(placeholder, 1)
        content_layout.addWidget(study, 1)

        main_layout.addWidget(content_frame)

        # --- Bottom: All Exam Result ---
        result = QFrame()
        rlay = QVBoxLayout(result)
        rlay.setContentsMargins(0,0,0,0)

        rt = QLabel("All Exam Result")
        rt.setStyleSheet("background:#1B3452; color:white; padding:6px;")
        rt.setFont(QFont("Arial",12,QFont.Weight.Bold))
        rt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rlay.addWidget(rt)

        sel = QHBoxLayout()
        sel.addWidget(QLabel("Select Term:"))
        cb = QComboBox()
        cb.addItems(["Y1 S1","Y1 S2","Y2 S1","Y2 S2"])
        sel.addWidget(cb, 1)
        rlay.addLayout(sel)

        tbl = QTableWidget(4, 7)
        tbl.setHorizontalHeaderLabels([
            "Code","Course Title","Alpha Grade",
            "Credits Attempted","Credits Earned","Grade","Remarks"
        ])
        rows = [
            ("CS 212","Web Development I","A+","3","3","4.00","Superior"),
            ("CS 214","Java Programming","A","6","6","4.00","Excellent"),
            ("CS 211","UX/UI Design","A","3","3","4.00","Excellent"),
            ("CS213","Data Structure & Alg","A+","3","3","4.00","Superior"),
        ]
        for r, row in enumerate(rows):
            for c, v in enumerate(row):
                tbl.setItem(r,c, QTableWidgetItem(v))
        tbl.resizeColumnsToContents()
        rlay.addWidget(tbl)

        summary = QLabel(
            "Total Credits Transferred: 0    "
            "Total Credits Attained: 15    "
            "Cumulative GPA: 4.00"
        )
        summary.setFont(QFont("Arial",10,QFont.Weight.Bold))
        summary.setAlignment(Qt.AlignmentFlag.AlignRight)
        summary.setContentsMargins(8,4,8,4)
        rlay.addWidget(summary)

        main_layout.addWidget(result)
