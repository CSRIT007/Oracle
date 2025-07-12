# ui/dashboards/parent_experience_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QScrollArea
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ParentExperienceWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(12)

        # --- 1) Top summary bar ---
        top = QFrame()
        top.setStyleSheet("background: #003366; color: white;")
        t_layout = QHBoxLayout(top)
        t_layout.setContentsMargins(12, 6, 12, 6)
        t_layout.setSpacing(24)

        def make_card(icon, title, value):
            card = QFrame()
            card.setStyleSheet("background: transparent;")
            cl = QVBoxLayout(card)
            cl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if icon:
                lbl = QLabel()
                lbl.setPixmap(
                    QPixmap(icon)
                    .scaled(32, 32,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation)
                )
                cl.addWidget(lbl)
            cl.addWidget(QLabel(f"<b>{title}</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(QLabel(value), alignment=Qt.AlignmentFlag.AlignCenter)
            return card

        # Left cards
        t_layout.addWidget(make_card("resources/icons/experience.png", "Experience", "04"))
        t_layout.addWidget(make_card("resources/icons/event.png",      "Event",      "05"))

        # Center title
        center = QLabel("<b>Social Activity</b>")
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setStyleSheet("font-size: 16pt;")
        t_layout.addWidget(center, 1)

        # Right cards
        t_layout.addWidget(make_card("resources/icons/subject.png", "Subject", "100%"))
        t_layout.addWidget(make_card("resources/icons/type.png",    "Type",    "$0"))

        root.addWidget(top, 0)

        # --- 2) Search bar ---
        search_frame = QFrame()
        sf_layout = QHBoxLayout(search_frame)
        sf_layout.setContentsMargins(0, 0, 0, 0)
        sf_layout.setSpacing(8)

        lbl = QLabel("<b>Experience</b>")
        lbl.setStyleSheet("padding:4px 8px; background:#0055aa; color:white; border-top-left-radius:4px; border-bottom-left-radius:4px;")
        sf_layout.addWidget(lbl)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Experience")
        sf_layout.addWidget(self.search, 1)

        btn = QPushButton("View")
        btn.setFixedWidth(60)
        sf_layout.addWidget(btn)

        root.addWidget(search_frame, 0)

        # --- 3) Experience List header ---
        header = QFrame()
        header.setStyleSheet("background: #003366; color: white; padding: 6px;")
        h_layout = QHBoxLayout(header)
        h_layout.setContentsMargins(12, 0, 12, 0)
        h_layout.addWidget(QLabel("<b>Experience List</b>"))
        root.addWidget(header, 0)

        # --- 4) Scrollable list of experiences ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(8)

        # Sample items (replace in load_data)
        sample = [
            ("School International Exchange Program", "12/May/2025 - 20/May/2025", "AUB Campus"),
            ("Coordinator Football Matching Friendship", "01/May/2025",       "Olympic Stadium"),
            ("Volunteer for Organizing Khmer New Year",    "05/Apr/2025",       "AUB Campus"),
            ("School Exchange Program",                   "03/Mar/2024 - 13/Mar/2024", "AUB Campus"),
        ]
        for title, dates, loc in sample:
            item = QFrame()
            item.setStyleSheet("background: #002244; color: white; border-radius:4px;")
            item_layout = QHBoxLayout(item)
            item_layout.setContentsMargins(12, 8, 12, 8)
            item_layout.setSpacing(16)

            icon = QLabel()
            icon.setPixmap(
                QPixmap("resources/icons/experience.png")
                .scaled(24, 24,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation)
            )
            item_layout.addWidget(icon)

            item_layout.addWidget(QLabel(title),       3)
            item_layout.addWidget(QLabel(f"Date: {dates}"), 2)
            item_layout.addWidget(QLabel(loc),         2)

            view_btn = QPushButton("View")
            view_btn.setStyleSheet("background: #28a745; color: white; padding:4px 8px; border-radius:4px;")
            view_btn.setFixedWidth(60)
            item_layout.addWidget(view_btn)

            container_layout.addWidget(item)

        container_layout.addStretch()
        scroll.setWidget(container)
        root.addWidget(scroll, 1)

    def load_data(self, summary: dict, items: list[tuple]):
        """
        :param summary: {
            'experience_count': str,
            'event_count': str,
            'subject_percent': str,
            'type_amount': str
        }
        :param items: list of (title, dates, location)
        """
        # TODO: update top cards, clear & rebuild list in `container`
        pass
