# ui/dashboards/base_dashboard.py
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class BaseDashboard(QWidget):
    def __init__(self, user_name="User", left_menus=None, main_widget=None):
        super().__init__()
        self.setWindowTitle(f"Dashboard")
        self.setMinimumSize(1200, 700)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # --- Left Menu ---
        left_menu = QFrame()
        left_menu.setFixedWidth(260)
        left_menu.setStyleSheet("background: #1a1e37; color: white;")
        left_layout = QVBoxLayout(left_menu)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # Logo
        logo = QLabel("ACLEDA\nUNIVERSITY")
        logo.setStyleSheet("font-size: 24px; font-weight: bold;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(logo)
        # Avatar + User
        avatar = QLabel()
        avatar.setPixmap(QPixmap("resources/images/avatar.png").scaled(90, 90, Qt.AspectRatioMode.KeepAspectRatio))
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(avatar)
        name = QLabel(user_name)
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(name)
        # Menus
        if left_menus is None:
            left_menus = []
        for menu in left_menus:
            btn = QPushButton(menu)
            btn.setStyleSheet("text-align: left; padding: 10px; background: none; border: none; color: white; font-size: 16px;")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            left_layout.addWidget(btn)
        left_layout.addStretch(1)
        copyright_label = QLabel("copyright © 2025 ACLEDA University of Business")
        copyright_label.setStyleSheet("font-size: 10px; color: #ccc;")
        left_layout.addWidget(copyright_label)
        
        # --- Right: Header Bar + Main ScrollArea ---
        right = QFrame()
        right.setStyleSheet("background: #f4f6fa;")
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        # Header bar
        header = QFrame()
        header.setFixedHeight(60)
        header.setStyleSheet("background: #2c3250; color: white;")
        header_layout = QHBoxLayout(header)
        search = QLineEdit()
        search.setPlaceholderText("Search")
        search.setFixedWidth(300)
        header_layout.addWidget(search)
        header_layout.addStretch(1)
        for item in ["Notifications", "English ▼"]:
            btn = QPushButton(item)
            btn.setStyleSheet("background: none; border: none; color: white; font-size: 15px;")
            header_layout.addWidget(btn)
        right_layout.addWidget(header)
        # Main area (scrollable)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll.setWidget(self.scroll_content)
        right_layout.addWidget(self.scroll)
        if main_widget:
            self.set_main_widget(main_widget)
        main_layout.addWidget(left_menu)
        main_layout.addWidget(right)
        self.setLayout(main_layout)

    def set_main_widget(self, widget):
        # Remove old
        for i in reversed(range(self.scroll_layout.count())):
            item = self.scroll_layout.takeAt(i)
            if item.widget():
                item.widget().deleteLater()
        self.scroll_layout.addWidget(widget)
