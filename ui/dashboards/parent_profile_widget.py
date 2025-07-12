# ui/dashboards/parent_profile_widget.py

from PyQt6.QtWidgets import (
    QWidget, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ParentProfileWidget(QWidget):
    """
    Profile panel with a dark-blue header and white body,
    right-aligned avatar, and a form of label:value rows.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._fields = {}
        self._build_ui()

    def _build_ui(self):
        # --- Root ---
        root = QVBoxLayout(self)
        root.setContentsMargins(0,0,0,0)
        root.setSpacing(0)

        # --- Header Bar ---
        header = QFrame()
        header.setStyleSheet("background: #003366;")
        hdr = QHBoxLayout(header)
        hdr.setContentsMargins(12,4,12,4)
        title = QLabel("My Information")
        title.setStyleSheet("color:white; font-weight:bold;")
        hdr.addWidget(title)
        root.addWidget(header, 0)

        # --- Body Panel ---
        body = QFrame()
        body.setStyleSheet("background: white; border: 1px solid #ccc;")
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(12,8,12,8)
        body_layout.setSpacing(24)

        # 1) Form
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form.setFormAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # placeholder data
        initial = {
            "Name":         "Moeng Sokea",
            "Gender":       "Male",
            "Job":          "Businessman",
            "E_mail":       "moengsoka168@gmail.com",
            "Phone Number": "0962843473",
            "Address":      "Kampong Speu",
        }
        for field, value in initial.items():
            lbl = QLabel(value)
            form.addRow(f"{field} :", lbl)
            self._fields[field] = lbl

        body_layout.addLayout(form, 1)

        # 2) Avatar
        avatar = QLabel()
        pix = QPixmap("resources/avatars/parent.png")
        if not pix.isNull():
            avatar.setPixmap(
                pix.scaled(100,100,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation)
            )
        avatar.setAlignment(Qt.AlignmentFlag.AlignTop)
        body_layout.addWidget(avatar, 0)

        root.addWidget(body, 1)

    def update_profile(self, info: dict):
        """
        :param info: dict mapping field names to new values.
        Updates existing rows; adds new ones if needed.
        """
        layout: QFormLayout = self.findChild(QFormLayout)
        for field, value in info.items():
            if field in self._fields:
                self._fields[field].setText(value)
            else:
                # add a new row
                lbl = QLabel(value)
                layout.addRow(f"{field} :", lbl)
                self._fields[field] = lbl
