# ui/dashboards/student_payment_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt

class StudentPaymentWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(16)

        # --- Top summary cards ---
        top_frame = QFrame()
        top_layout = QHBoxLayout(top_frame)
        top_layout.setSpacing(10)
        def make_card(title, subtitle=None, icon=None, button=None, width=180):
            frm = QFrame()
            frm.setStyleSheet("background:#1B3452; color:white; border-radius:8px;")
            frm.setFixedSize(width, 80)
            ly = QHBoxLayout(frm)
            ly.setContentsMargins(12, 8, 12, 8)
            if icon:
                ico = QLabel()
                pix = QPixmap(icon)
                if not pix.isNull():
                    ico.setPixmap(pix.scaled(24,24,Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation))
                ly.addWidget(ico)
            txt = QVBoxLayout()
            t = QLabel(title)
            t.setFont(QFont("Arial", 10))
            t.setStyleSheet("color:#ccc;")
            txt.addWidget(t)
            if subtitle is not None:
                s = QLabel(subtitle)
                s.setFont(QFont("Arial", 16, QFont.Weight.Bold))
                txt.addWidget(s)
            ly.addLayout(txt)
            if button:
                ly.addStretch()
                ly.addWidget(button, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            return frm

        pay_now_btn = QPushButton()
        pay_now_btn.setIcon(QIcon("resources/icons/plus-white.png"))
        pay_now_btn.setFixedSize(28,28)
        pay_now_btn.setStyleSheet("""
            QPushButton {
                background: #FD367E; border:none; border-radius:14px;
            }
            QPushButton:hover {
                background: #ff5a8f;
            }
        """)

        top_layout.addWidget(make_card("Payment", "13 Times", icon="resources/icons/payment.png"))
        top_layout.addWidget(make_card("Discount", "0%", icon="resources/icons/discount.png"))
        top_layout.addWidget(make_card("Yearly Paid", "$1200", icon="resources/icons/money.png"))
        top_layout.addWidget(make_card("Pay Now", None, button=pay_now_btn, width=120))
        layout.addWidget(top_frame)

        # --- Payment notifications ---
        notif_frame = QFrame()
        notif_frame.setStyleSheet("background:white; border-radius:8px;")
        notif_layout = QVBoxLayout(notif_frame)
        notif_layout.setContentsMargins(8, 8, 8, 8)
        title = QLabel("Payment Notification")
        title.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        title.setStyleSheet("background:#1B3452; color:white; padding:6px; border-top-left-radius:8px; border-top-right-radius:8px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        notif_layout.addWidget(title)

        for _ in range(3):
            row = QHBoxLayout()
            lbl_date = QLabel("Date : 12/Jan/2025")
            lbl_info = QLabel("Payment Information")
            pay_btn = QPushButton("+ Pay Now")
            pay_btn.setFixedHeight(24)
            pay_btn.setStyleSheet("""
                QPushButton {
                    background: #1B3452; color:white; border:none; border-radius:4px;
                    padding:0 8px; font-size:12px;
                }
                QPushButton:hover { background:#255083; }
            """)
            row.addWidget(lbl_date)
            row.addSpacing(12)
            row.addWidget(lbl_info, 1)
            row.addWidget(pay_btn, 0, Qt.AlignmentFlag.AlignRight)
            notif_layout.addLayout(row)
            notif_layout.addSpacing(6)
        layout.addWidget(notif_frame)

        # --- Search bar ---
        search_frame = QFrame()
        search_frame.setFixedHeight(32)
        search_frame.setStyleSheet("""
            background:white; border-radius:16px;
        """)
        sf_l = QHBoxLayout(search_frame)
        sf_l.setContentsMargins(12,0,12,0)
        sf_l.setSpacing(8)
        inp = QLineEdit()
        inp.setPlaceholderText("Search Payment ID")
        inp.setFrame(False)
        sf_l.addWidget(QLabel("Payment"))
        sf_l.addWidget(inp, 1)
        sf_l.addWidget(QLabel("🔍"), 0)
        layout.addWidget(search_frame)

        # --- Payment list table ---
        tbl_frame = QFrame()
        tbl_layout = QVBoxLayout(tbl_frame)
        tbl_layout.setContentsMargins(0,0,0,0)

        hdr = QLabel("Payment List")
        hdr.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        hdr.setStyleSheet("background:#1B3452; color:white; padding:6px; border-top-left-radius:8px; border-top-right-radius:8px;")
        hdr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tbl_layout.addWidget(hdr)

        table = QTableWidget(9, 7)
        table.setHorizontalHeaderLabels([
            "No", "Student_ID", "Total Price", "Payment",
            "Select Payment", "Invoice_ID", "Payment_Date"
        ])
        # fill example rows
        for row in range(9):
            data = [
                f"{row+1:02}",
                "0007361",
                "$1200",
                "Bachelor",
                "Year",
                "016273846254",
                "11/Jan/2025"
            ]
            for col, txt in enumerate(data):
                table.setItem(row, col, QTableWidgetItem(txt))
        table.resizeColumnsToContents()
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        tbl_layout.addWidget(table)

        layout.addWidget(tbl_frame)
