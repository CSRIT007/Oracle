# ui/dashboards/student_schedule_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QFrame, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class CourseCard(QFrame):
    def __init__(self, cid, name, date, time, cls, building, icon_path="resources/icons/class.png"):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background: #1B3452;
                border-radius: 6px;
                color: white;
            }
        """)
        self.setFixedSize(200, 180)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8,8,8,8)
        layout.setSpacing(6)

        # top icon
        ico = QLabel()
        pix = QPixmap(icon_path)
        if not pix.isNull():
            ico.setPixmap(pix.scaled(32,32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        ico.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(ico)

        def make_label(prefix, text):
            lbl = QLabel(f"<b>{prefix}</b> {text}")
            lbl.setFont(QFont("Arial",  nine:=9))
            return lbl

        layout.addWidget(make_label("ID :", cid))
        layout.addWidget(make_label("Name :", name))
        layout.addWidget(make_label("Date :", date))
        layout.addWidget(make_label("Time :", time))
        layout.addWidget(make_label("Class :", cls))
        layout.addWidget(make_label("Building :", building))


class StudentScheduleWidget(QWidget):
    def __init__(self):
        super().__init__()
        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        main.setSpacing(16)

        # --- Top summary + profile row ---
        top = QFrame()
        th = QHBoxLayout(top)
        th.setContentsMargins(0,0,0,0)
        th.setSpacing(12)

        # Today's Course card
        today_card = QFrame()
        today_card.setFixedSize(180, 100)
        today_card.setStyleSheet("""
            QFrame { background: #1B3452; color: white; border-radius: 6px; }
        """)
        tc = QHBoxLayout(today_card)
        tc.setContentsMargins(8,8,8,8)
        ico = QLabel()
        px = QPixmap("resources/icons/class.png")
        if not px.isNull():
            ico.setPixmap(px.scaled(32,32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        tc.addWidget(ico)
        tc.addWidget(QLabel("<b>Today's Course</b>\n\n05"), alignment=Qt.AlignmentFlag.AlignCenter)
        th.addWidget(today_card)

        # Profile card
        prof = QFrame()
        prof.setStyleSheet("background: #1B3452; color: white; border-radius: 6px;")
        prof.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        prof.setFixedHeight(100)
        ph = QHBoxLayout(prof)
        ph.setContentsMargins(12,12,12,12)
        ph.setSpacing(12)
        av = QLabel()
        avpix = QPixmap("resources/images/person.png")
        if not avpix.isNull():
            av.setPixmap(avpix.scaled(64,64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        ph.addWidget(av)
        info = QVBoxLayout()
        lbl_name = QLabel("Name  :  Moeng Kimheang")
        lbl_batch= QLabel("Batch : 08")
        lbl_maj = QLabel("Computer Science and Engineering")
        for w in (lbl_name,lbl_batch,lbl_maj):
            w.setStyleSheet("font-size: 13px;")
            w.setFont(QFont("Arial", 11))
        info.addWidget(lbl_name)
        info.addWidget(lbl_batch)
        info.addWidget(lbl_maj)
        ph.addLayout(info,1)
        th.addWidget(prof,1)

        main.addWidget(top)

        # --- Search + toggles ---
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        sfl.setSpacing(8)
        lbl = QLabel("Course")
        lbl.setFont(QFont("Arial",11))
        sfl.addWidget(lbl)
        inp = QLineEdit()
        inp.setPlaceholderText("Search Course")
        inp.setFrame(False)
        inp.setStyleSheet("font-size:13px;")
        sfl.addWidget(inp,1)
        sfl.addWidget(QLabel("🔍"))
        main.addWidget(sf)

        btns = QHBoxLayout()
        btn_today = QPushButton("Today")
        btn_total = QPushButton("Schedule Total")
        for b in (btn_today, btn_total):
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(28)
            b.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color:white;
                    border:none; border-radius:14px; padding:4px 12px;
                }
                QPushButton:hover {
                    background: #255083;
                }
            """)
            btns.addWidget(b)
        btns.addStretch(1)
        main.addLayout(btns)

        # --- Time Table header ---
        hdr = QLabel("Time Table")
        hdr.setFont(QFont("Arial",14, QFont.Weight.Bold))
        hdr.setStyleSheet("color: #1B3452;")
        main.addWidget(hdr)

        # --- Scrollable grid of CourseCard ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        grid = QGridLayout(container)
        grid.setContentsMargins(0,0,0,0)
        grid.setSpacing(12)

        # demo data
        demo = [("CS412","Oracle","12/Jan/2025","8:00 PM - 9:40 PM","Brasat Banteay Kdei","B")] * 10
        cols = 4
        for i, data in enumerate(demo):
            r,c = divmod(i, cols)
            card = CourseCard(*data)
            grid.addWidget(card, r, c)

        scroll.setWidget(container)
        main.addWidget(scroll,1)
