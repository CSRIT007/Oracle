# ui/dashboards/base_dashboard.py

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame,
    QScrollArea, QLineEdit, QComboBox, QListWidget, QStackedWidget,
    QSizePolicy, QToolButton, QMenu, QButtonGroup
)
from PyQt6.QtCore import Qt, QPoint, QSize
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QPainterPath, QAction


class SidebarButton(QPushButton):
    def __init__(self, text, icon_path=None, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setText("  " + text)
        if icon_path:
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(20, 20))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 10px 18px;
                background: none;
                border: none;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background: #255083;
            }
            QPushButton:checked {
                background: #255083;
            }
        """)


class Sidebar(QFrame):
    def __init__(self, user_name, switch_callback):
        super().__init__()
        self.setObjectName("Sidebar")
        self.setFixedWidth(220)
        self.setStyleSheet("#Sidebar { background: #1B3452; }")

        # button‐group for exclusive selection:
        self._btn_group = QButtonGroup(self)
        self._btn_group.setExclusive(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # — Logo —
        logo = QLabel()
        pix = QPixmap("resources/images/logo.png")
        if not pix.isNull():
            logo.setPixmap(pix)
            logo.setScaledContents(True)
        logo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        logo.setMaximumHeight(60)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)

        # — Circular Avatar —
        avatar = QLabel()
        av = QPixmap("resources/images/person.png")
        if not av.isNull():
            size = 80
            av = av.scaled(size, size,
                           Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                           Qt.TransformationMode.SmoothTransformation)
            mask = QPixmap(size, size)
            mask.fill(Qt.GlobalColor.transparent)
            painter = QPainter(mask)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, av)
            painter.end()
            avatar.setPixmap(mask)
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar.setStyleSheet("margin-top:10px; margin-bottom:2px;")
        layout.addWidget(avatar)

        # — Username + edit icon —
        name_row = QHBoxLayout()
        name_row.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_lbl = QLabel(user_name)
        name_lbl.setStyleSheet("color:white; font-size:14px; font-weight:600;")
        name_row.addWidget(name_lbl)
        edit = QLabel()
        edit_pix = QPixmap("resources/icons/compose.png")
        if not edit_pix.isNull():
            edit.setPixmap(edit_pix.scaled(16,16, Qt.AspectRatioMode.KeepAspectRatio))
        name_row.addWidget(edit)
        container = QFrame()
        container.setLayout(name_row)
        layout.addWidget(container)

        # — Navigation buttons —
        menu_items = getattr(switch_callback.__self__, 'left_menus', []) or []
        self.buttons = {}
        for label, icon in menu_items:
            btn = SidebarButton(label, icon)
            self._btn_group.addButton(btn)
            btn.clicked.connect(lambda _, txt=label: switch_callback(txt))
            layout.addWidget(btn)
            self.buttons[label] = btn

        # Check the first button by default (if any)
        all_buttons = self._btn_group.buttons()
        if all_buttons:
            all_buttons[0].setChecked(True)

        layout.addStretch()
        footer = QLabel("© 2025 ACLEDA University of Business")
        footer.setStyleSheet("color:#777; font-size:10px; padding:8px;")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(footer)

from PyQt6.QtWidgets import QToolButton, QLabel, QMenu
from PyQt6.QtCore    import Qt
from PyQt6.QtGui     import QAction

class NotificationButton(QToolButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        # — Text only (no icon) —
        self.setText("Notifications")
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        # — Fixed height & pointer —
        self.setFixedHeight(32)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    

        # — Styling: outline, hover, and hide the menu arrow —
        self.setStyleSheet("""
            QToolButton {
                background: none;
                border: 1px solid white;
                border-radius: 4px;
                padding: 0 10px;
                color: white;
                font-size: 14px;
            }
            QToolButton:hover {
                background: #B3B5BB;
                color: black;
            }
        """)

class BaseDashboard(QWidget):
    def __init__(self, user_name="User", left_menus=None, main_widget: QWidget=None):
        super().__init__()
        self.setWindowTitle("ACLEDA University Portal")
        self.setMinimumSize(1200, 700)
        self.showFullScreen()

        self.left_menus = left_menus or []

        root = QHBoxLayout(self)
        root.setContentsMargins(0,0,0,0)
        root.setSpacing(0)

        # — Sidebar —
        self.sidebar = Sidebar(user_name, self.switch_form)
        root.addWidget(self.sidebar)

        # — Right side: header + content —
        right = QFrame()
        right.setStyleSheet("background:#f4f6fa;")
        rlay = QVBoxLayout(right)
        rlay.setContentsMargins(0,0,0,0)
        rlay.setSpacing(0)

        # --- Header bar (60px tall) ---
        header = QFrame()
        header.setFixedHeight(60)
        header.setStyleSheet("background: #1B3452;")
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(20, 8, 20, 8)   # a little extra vertical padding
        hlay.setSpacing(12)

        # — Search field (36px tall) —
        sf = QFrame()
        sf.setFixedHeight(36)
        sf.setStyleSheet("""
            background: #ffffff;
            width: 400px;
            border-radius: 18px;
        """)
        sfl = QHBoxLayout(sf)
        sfl.setContentsMargins(15, 0, 12, 0)
        sfl.setSpacing(8)

        search_icon = QLabel()
        search_icon.setPixmap(
            QPixmap("resources/icons/search.png")
            .scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        sfl.addWidget(search_icon)

        search_input = QLineEdit()
        search_input.setPlaceholderText("Search...")
        search_input.setFrame(False)
        search_input.setStyleSheet("""
            border: none;
            color: #444444;
            font-size: 14px;
        """)
        sfl.addWidget(search_input, 1)  # stretch

        hlay.addWidget(sf, 0)

        hlay.addStretch(1)

        notif_btn = NotificationButton()
        hlay.addWidget(notif_btn)

        # — Language dropdown —
        lang = QComboBox()
        lang.addItems(["English", "ខ្មែរ", "中文"])
        lang.setStyleSheet("""
            QComboBox {
                color: white;
                background: transparent;
                border: 1px solid white;
                border-radius: 4px;
                padding: 4px 10px;
                font-size: 14px;
                min-width: 60px;
            }
            QComboBox:hover {
                color: black;
                background: #B3B5BB;
            }
            QComboBox::drop-down { border: none; }
            QComboBox::down-arrow {
                image: url(resources/icons/row.png);
                width: 40px; 
                height: 40px;
                margin-right: 10px;
            }
            QComboBox QAbstractItemView {
                background: #1B3452;
                color: white;
                selection-background-color: #D52462;
            }
        """)
        hlay.addWidget(lang)

        # — Logout button —
        lbtn = QPushButton("Logout")
        lbtn.setFixedHeight(32)
        lbtn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                border: 1px solid white;
                border-radius: 4px;
                padding: 4px 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background: #B3B5BB;
                color: black;
            }
        """)
        lbtn.clicked.connect(self.do_logout)
        hlay.addWidget(lbtn)

        # finally add header into your main layout
        rlay.addWidget(header)

        # — Main content area —
        self.content = QStackedWidget()
        if main_widget:
            if not isinstance(main_widget, QStackedWidget):
                sw = QScrollArea()
                sw.setWidgetResizable(True)
                sw.setWidget(main_widget)
                self.content.addWidget(sw)
            else:
                self.content = main_widget
        rlay.addWidget(self.content)

        root.addWidget(right)
        self.setLayout(root)

        # default to first page
        if isinstance(self.content, QStackedWidget) and len(self.left_menus) == self.content.count():
            self.content.setCurrentIndex(0)

    def switch_form(self, name: str):
        for idx, (label, _) in enumerate(self.left_menus):
            if label == name:
                self.content.setCurrentIndex(idx)
                return

    def do_logout(self):
        from ui.login import LoginWindow
        self.close()
        self.login = LoginWindow()
        self.login.showFullScreen()
