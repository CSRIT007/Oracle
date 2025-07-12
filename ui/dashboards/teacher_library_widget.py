# ui/dashboards/teacher_library_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QScrollArea,
    QLineEdit, QPushButton, QComboBox, QListWidget, QSizePolicy,
    QGridLayout, QGroupBox
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class TeacherLibraryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12,12,12,12)
        root.setSpacing(16)

        # --- Top Banner ---
        banner = QFrame()
        banner.setFixedHeight(100)
        banner.setStyleSheet("background: #1B3452; border-radius:6px;")
        bl = QHBoxLayout(banner)
        bl.setContentsMargins(8,8,8,8)
        bl.setSpacing(12)

        # Left: Campus image
        img = QLabel()
        pix = QPixmap("resources/images/campus.png")
        if not pix.isNull():
            img.setPixmap(pix.scaledToHeight(84, Qt.TransformationMode.SmoothTransformation))
        img.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        bl.addWidget(img)

        # Center: University name
        title = QLabel("អេស៊ីល​ដា\nACLEDA UNIVERSITY")
        title.setStyleSheet("color:white;")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bl.addWidget(title, 1)

        # Right: stats cards
        def make_stat(icon_path, number, label):
            card = QFrame()
            card.setFixedHeight(80)
            card.setStyleSheet("""
                QFrame { background: #1B3452; color: white; border-radius:6px; }
                QLabel { color: white; }
            """)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(8,4,8,4)
            cl.setSpacing(4)
            top = QHBoxLayout()
            ico = QLabel()
            px = QPixmap(icon_path)
            if not px.isNull():
                ico.setPixmap(px.scaled(24,24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            top.addWidget(ico)
            top.addSpacing(4)
            top.addWidget(QLabel(label))
            cl.addLayout(top)
            num = QLabel(str(number))
            num.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            num.setAlignment(Qt.AlignmentFlag.AlignRight)
            cl.addWidget(num)
            return card

        stats = [
            ("resources/icons/book.png",       1000, "All Book"),
            ("resources/icons/book.png",        200, "Book"),
            ("resources/icons/book-stack.png",  400, "Book Khmer"),
            ("resources/icons/book-stack.png",  600, "English Book"),
        ]
        for icon, num, lbl in stats:
            bl.addWidget(make_stat(icon, num, lbl))

        root.addWidget(banner)

        # --- Book List Header ---
        header = QLabel("Book List")
        header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        header.setStyleSheet("background: #1B3452; color: white; padding:8px; border-radius:6px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(header)

        # --- Main Content: filters + grid ---
        content = QHBoxLayout()
        content.setSpacing(12)

        # Left: filter panel
        filt = QFrame()
        filt.setStyleSheet("background: white; border-radius:6px;")
        fl = QVBoxLayout(filt)
        fl.setContentsMargins(8,8,8,8)
        fl.setSpacing(12)

        # Department
        fl.addWidget(QLabel("Department", font=QFont("Arial", 12, QFont.Weight.Bold)))
        for dept in ("Computer","Law","Science","Chinese","English","Khmer"):
            rb = QLabel(f"  ◉ {dept}")
            rb.setFont(QFont("Arial", 11))
            fl.addWidget(rb)

        # Language
        fl.addSpacing(8)
        fl.addWidget(QLabel("Language", font=QFont("Arial", 12, QFont.Weight.Bold)))
        for lang in ("English","Khmer"):
            rb = QLabel(f"  ◉ {lang}")
            rb.setFont(QFont("Arial", 11))
            fl.addWidget(rb)

        fl.addStretch(1)
        filt.setFixedWidth(150)
        content.addWidget(filt)

        # Right: scrollable grid of books
        grid_container = QFrame()
        gl = QVBoxLayout(grid_container)
        gl.setContentsMargins(0,0,0,0)
        gl.setSpacing(8)

        # Search bar
        search_frame = QFrame()
        search_frame.setFixedHeight(32)
        search_frame.setStyleSheet("background: white; border-radius: 16px;")
        sfl = QHBoxLayout(search_frame)
        sfl.setContentsMargins(12,0,12,0)
        sfl.addWidget(QLabel("Book"))
        le = QLineEdit()
        le.setPlaceholderText("Search All Book")
        le.setFrame(False)
        sfl.addWidget(le, 1)
        sfl.addWidget(QLabel("🔍"))
        gl.addWidget(search_frame)

        # Scroll area
        sc = QScrollArea()
        sc.setWidgetResizable(True)
        inner = QWidget()
        grid = QGridLayout(inner)
        grid.setContentsMargins(0,0,0,0)
        grid.setHorizontalSpacing(16)
        grid.setVerticalSpacing(16)

        # Dummy items
        for idx in range(12):
            col = idx % 3
            row = idx // 3

            card = QFrame()
            card.setStyleSheet("background: white; border-radius:6px;")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(4,4,4,4)
            cl.setSpacing(4)

            cover = QLabel()
            cp = QPixmap("resources/images/book-cover.png")
            if not cp.isNull():
                cover.setPixmap(cp.scaled(100,140, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            cover.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(cover)

            title = QLabel("The Let Them Theory\nA Life-Changing Tool…")
            title.setWordWrap(True)
            title.setFont(QFont("Arial", 10))
            cl.addWidget(title)

            stars = QLabel("★ ★ ★ ★ ☆   52,268")
            stars.setFont(QFont("Arial", 9))
            cl.addWidget(stars)

            grid.addWidget(card, row, col)

        sc.setWidget(inner)
        gl.addWidget(sc)

        content.addWidget(grid_container, 1)
        root.addLayout(content)
