# ui/dashboards/student_library_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QLineEdit,
    QRadioButton, QButtonGroup, QScrollArea, QGridLayout, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class BookItem(QWidget):
    def __init__(self, cover_path, title, department, rating, count):
        super().__init__()
        self.setFixedWidth(140)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(4,4,4,4)
        layout.setSpacing(6)

        # cover
        cover = QLabel()
        pix = QPixmap(cover_path)
        if not pix.isNull():
            cover.setPixmap(pix.scaled(128, 180, Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
        cover.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(cover)

        # title
        lbl = QLabel(title)
        lbl.setWordWrap(True)
        lbl.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(lbl)

        # department
        dept = QLabel(department)
        dept.setFont(QFont("Arial", 8))
        dept.setStyleSheet("color: #555;")
        dept.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(dept)

        # rating + count
        rc = QLabel(f"⭐ {rating}   {count:,}")
        rc.setFont(QFont("Arial", 8))
        rc.setStyleSheet("color: #888;")
        rc.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(rc)


class StudentLibraryWidget(QWidget):
    def __init__(self):
        super().__init__()
        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        main.setSpacing(16)

        # --- Top banner: image + logo + summary cards ---
        top = QFrame()
        top.setStyleSheet("background: transparent;")
        th = QHBoxLayout(top)
        th.setSpacing(10)
        th.setContentsMargins(0,0,0,0)

        # left building image
        img = QLabel()
        pix = QPixmap("resources/images/library_building.png")
        if not pix.isNull():
            img.setPixmap(pix.scaledToHeight(100, Qt.TransformationMode.SmoothTransformation))
        img.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        th.addWidget(img, 1)

        # right summary cards
        def card(title, number, width=100):
            f = QFrame()
            f.setFixedHeight(100)
            f.setFixedWidth(width)
            f.setStyleSheet("""
                background: #1B3452;
                color: white;
                border-radius: 8px;
            """)
            ly = QVBoxLayout(f)
            ly.setContentsMargins(8,8,8,8)
            ly.addWidget(QLabel(f"<b>{title}</b>"), 0, Qt.AlignmentFlag.AlignTop)
            num = QLabel(f"<h2>{number}</h2>")
            num.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            ly.addWidget(num, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            return f

        th.addWidget(card("All Books",    "1 000", width=120))
        th.addWidget(card("Books",        "200",   width=120))
        th.addWidget(card("Khmer Books",  "400",   width=120))
        th.addWidget(card("English Books","600",   width=120))
        main.addWidget(top)

        # --- Header "Book List" ---
        header = QLabel("Book List")
        header.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        header.setStyleSheet("background: #1B3452; color: white; padding: 6px; border-radius: 4px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main.addWidget(header)

        # --- Filters + grid ---
        body = QFrame()
        bd = QHBoxLayout(body)
        bd.setContentsMargins(0,0,0,0)
        bd.setSpacing(12)

        # left: filters
        filt = QFrame()
        fl = QVBoxLayout(filt)
        fl.setContentsMargins(0,0,0,0)
        fl.setSpacing(12)

        # Department group
        fl.addWidget(QLabel("<b>Department</b>"))
        dept_grp = QButtonGroup(self)
        for d in ["Computer", "Law", "Science", "Chinese", "English", "Khmer"]:
            rb = QRadioButton(d)
            fl.addWidget(rb)
            dept_grp.addButton(rb)
        fl.addSpacing(16)

        # Language group
        fl.addWidget(QLabel("<b>Language</b>"))
        lang_grp = QButtonGroup(self)
        for l in ["English", "Khmer"]:
            rb = QRadioButton(l)
            fl.addWidget(rb)
            lang_grp.addButton(rb)

        fl.addStretch(1)
        filt.setFixedWidth(120)
        bd.addWidget(filt)

        # right: search + grid scroll
        right = QVBoxLayout()
        # search
        sf = QFrame()
        sf.setFixedHeight(32)
        sf.setStyleSheet("background:white; border-radius:16px;")
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(12,0,12,0)
        inp = QLineEdit()
        inp.setPlaceholderText("Search All Books")
        inp.setFrame(False)
        sfl.addWidget(inp)
        sfl.addWidget(QLabel("🔍"))
        right.addWidget(sf)

        # grid
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        grid_w = QWidget()
        grid = QGridLayout(grid_w)
        grid.setSpacing(12)
        grid.setContentsMargins(0,0,0,0)

        # example: populate with 12 identical items—you’ll hook this up to your DB
        for i in range(12):
            row = i // 4
            col = i % 4
            item = BookItem(
                cover_path  = "resources/images/book_cover.png",
                title       = "The Let Them Theory: A Life-Changing Tool…",
                department  = "Computer",
                rating      = 5,
                count       = 52268
            )
            grid.addWidget(item, row, col)

        scroll.setWidget(grid_w)
        right.addWidget(scroll, 1)

        bd.addLayout(right, 1)
        main.addWidget(body, 1)
