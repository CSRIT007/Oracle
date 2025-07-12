from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ParentPaymentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # ----- Outer layout -----
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        # ----- Top: Summary cards & Payment News -----
        top_frame = QWidget()
        top_layout = QHBoxLayout(top_frame)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(12)

        # Summary cards container
        summary_frame = QFrame()
        sum_layout = QHBoxLayout(summary_frame)
        sum_layout.setContentsMargins(0, 0, 0, 0)
        sum_layout.setSpacing(8)

        def make_card(icon, title, value, subtitle=""):
            card = QFrame()
            card.setStyleSheet("background:white; border:1px solid #ccc;")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(12, 8, 12, 8)
            cl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if icon:
                img = QLabel()
                img.setPixmap(
                    QPixmap(icon)
                    .scaled(24, 24,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation)
                )
                cl.addWidget(img)
            cl.addWidget(QLabel(f"<b>{title}</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(QLabel(value),      alignment=Qt.AlignmentFlag.AlignCenter)
            if subtitle:
                cl.addWidget(QLabel(subtitle), alignment=Qt.AlignmentFlag.AlignCenter)
            return card

        # Four cards
        sum_layout.addWidget(make_card("resources/icons/payments.png", "Payment", "09", "Times"), 1)
        sum_layout.addWidget(make_card("resources/icons/discount.png", "Discount", "0%", "Year"),   1)
        sum_layout.addWidget(make_card("resources/icons/payments.png", "Payment", "$1200", "Year"), 1)
        sum_layout.addWidget(make_card("resources/icons/add.png",      "Pay Now", "",       ""),     1)

        top_layout.addWidget(summary_frame, 2)

        # Payment News panel
        news_frame = QFrame()
        news_frame.setStyleSheet("background:white; border:1px solid #ccc;")
        news_layout = QVBoxLayout(news_frame)
        news_layout.setContentsMargins(12, 8, 12, 8)
        news_layout.addWidget(QLabel("<b>Payment News</b>"))

        # Sample news items
        sample_news = [
            ("30/May/2025", "Semester2, Year2"),
            ("15/Jun/2025", "English Course"),
            ("10/Jun/2025", "Admin Fee"),
        ]
        for date, desc in sample_news:
            row = QHBoxLayout()
            row.addWidget(QLabel(f"Date: {date}"), 2)
            row.addWidget(QLabel(desc),  3)
            btn = QPushButton("Pay Now")
            btn.setFixedWidth(80)
            row.addWidget(btn, 1)
            news_layout.addLayout(row)

        top_layout.addWidget(news_frame, 1)
        layout.addWidget(top_frame)

        # ----- Bottom: Search bar + Payment List -----
        table_frame = QFrame()
        table_frame.setStyleSheet("background:white; border:1px solid #ccc;")
        table_layout = QVBoxLayout(table_frame)
        table_layout.setContentsMargins(0, 0, 0, 0)
        table_layout.setSpacing(4)

        # Tab header + Search
        header_h = QHBoxLayout()
        tab_lbl = QLabel("<b>Payment</b>")
        tab_lbl.setStyleSheet(
            "padding: 4px 12px; "
            "background: #0055aa; color: white; "
            "border-top-left-radius: 4px; border-top-right-radius: 4px;"
        )
        header_h.addWidget(tab_lbl)
        header_h.addStretch()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Invoice_ID, Total Price, Payment_Date")
        self.search.setMinimumWidth(200)
        header_h.addWidget(self.search)
        table_layout.addLayout(header_h)

        # Payment table
        self.table = QTableWidget(0, 8)
        self.table.setHorizontalHeaderLabels([
            "No", "Student_ID", "Total Price", "Payment Purpose",
            "Select Payment", "Payment Type", "Invoice_ID", "Payment Date"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        table_layout.addWidget(self.table)

        layout.addWidget(table_frame, 1)

        # Load some demo rows
        self._load_sample_data()

    def _load_sample_data(self):
        sample_rows = [
            ("01","0007361","$170","Chinese",       "Term",     "BANK","016273848011","20/May/2025"),
            ("02","0007361","$180","English Course","Term",     "BANK","016273848011","29/Apr/2025"),
            ("03","0007361","$170","English Course","Term",     "BANK","016273848011","12/Feb/2025"),
            ("04","0007361","$650","Late Payment S1,Y2","One Time","BANK","016273846900","11/Feb/2025"),
            ("05","0007361","$50", "Admin Fee",     "Year",     "BANK","016273846500","02/Jan/2025"),
            ("06","0007361","$150","Advance Excel", "Course",   "BANK","016273846303","15/May/2024"),
            ("07","0007361","$150","English Course","Term",     "BANK","016273846302","15/May/2024"),
            ("08","0007361","$600","BBA, S2,Y1",    "Semester", "Cash","016273846301","15/May/2024"),
            ("09","0007361","$600","BBA, S1,Y1",    "Semester", "Cash","016273846254","11/Jan/2024"),
        ]
        for row_data in sample_rows:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, val in enumerate(row_data):
                item = QTableWidgetItem(val)
                # highlight late payment in red
                if row_data[0] == "04":
                    item.setForeground(Qt.GlobalColor.red)
                self.table.setItem(row, col, item)

    def load_data(self, records, news_items):
        """
        Replace the demo data with real SQLite results.
        :param records: list of tuples for payment rows
        :param news_items: list of (date_str, description_str)
        """
        # Clear and repopulate `self.table` and the news panel here.
        pass
