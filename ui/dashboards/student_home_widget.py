# ui/dashboards/student_home_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame,
    QCalendarWidget, QTableWidget, QTableWidgetItem, QSizePolicy, QSpacerItem
)
from PyQt6.QtGui import QPixmap, QFont, QPainter, QPainterPath
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtCharts import QChart, QChartView, QPieSeries

class StudentHomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()
        self._populate_notifications()
        self._populate_attendance_chart()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        main.setSpacing(12)

        # — Header —
        hdr = QFrame()
        hdr.setStyleSheet("background:#1B3452; color:white;")
        hdr.setFixedHeight(100)
        hdl = QHBoxLayout(hdr)
        hdl.setContentsMargins(16,8,16,8)
        hdl.setSpacing(12)

        # Avatar (circular)
        avatar = QLabel()
        pix = QPixmap("resources/images/person.png").scaled(80,80,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation)
        mask = QPixmap(80,80)
        mask.fill(Qt.GlobalColor.transparent)
        p = QPainter(mask)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0,0,80,80)
        p.setClipPath(path)
        p.drawPixmap(0,0,pix)
        p.end()
        avatar.setPixmap(mask)
        hdl.addWidget(avatar, 0, Qt.AlignmentFlag.AlignVCenter)

        # Name / location / major
        text = QVBoxLayout()
        name = QLabel("Student Name")
        name.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        text.addWidget(name)

        info = QLabel("📍 Location   •   Computer Science and Engineering")
        info.setFont(QFont("Arial", 11))
        text.addWidget(info)

        hdl.addLayout(text, 1)

        # View Profile button
        btn = QPushButton("View Profile")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background:#FD367E; color:white; border:none;
                border-radius:6px; padding:6px 16px; font-size:13px;
            }
            QPushButton:hover { background:#ff5a8f; }
        """)
        hdl.addWidget(btn, 0, Qt.AlignmentFlag.AlignVCenter)

        main.addWidget(hdr)

        # — Metric cards —
        metrics = QHBoxLayout()
        for title, val, unit in (
            ("Today's Class","04","Total"),
            ("Payment","$1,200","Year"),
            ("Assignment","05","Term"),
        ):
            card = QFrame()
            card.setStyleSheet("background:#1B3452; color:white; border-radius:6px;")
            card.setFixedHeight(80)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(12,8,12,8)
            cl.addWidget(QLabel(title), 0, Qt.AlignmentFlag.AlignLeft)
            v = QLabel(val)
            v.setFont(QFont("Arial", 20, QFont.Weight.Bold))
            cl.addWidget(v, 0, Qt.AlignmentFlag.AlignLeft)
            unit_lbl = QLabel(unit)
            unit_lbl.setFont(QFont("Arial", 9))
            unit_lbl.setStyleSheet("color:#ccc;")
            cl.addWidget(unit_lbl, 0, Qt.AlignmentFlag.AlignLeft)
            metrics.addWidget(card)
        main.addLayout(metrics)

        # — Content area: left calendar + right panel —
        content = QHBoxLayout()
        content.setSpacing(12)

        # ← Calendar
        cal_frame = QFrame()
        cal_frame.setStyleSheet("background:white; border-radius:6px;")
        cl = QVBoxLayout(cal_frame)
        cl.setContentsMargins(8,8,8,8)
        title = QLabel("Event Calendar")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        cl.addWidget(title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMaximumWidth(350)
        self.calendar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        cl.addWidget(self.calendar)
        content.addWidget(cal_frame, 2)

        # → Right: attendance chart + notifications
        right_v = QVBoxLayout()
        right_v.setSpacing(12)

        # Attendance
        attend_frame = QFrame()
        attend_frame.setStyleSheet("background:white; border-radius:6px;")
        al = QVBoxLayout(attend_frame)
        al.setContentsMargins(8,8,8,8)
        al.addWidget(QLabel("Attendance"), 0, Qt.AlignmentFlag.AlignHCenter)
        self._chart_view = QChartView()
        self._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self._chart_view.setMinimumHeight(200)
        al.addWidget(self._chart_view)
        right_v.addWidget(attend_frame, 1)

        # Notifications
        notif_frame = QFrame()
        notif_frame.setStyleSheet("background:white; border-radius:6px;")
        nl = QVBoxLayout(notif_frame)
        nl.setContentsMargins(8,8,8,8)
        header = QHBoxLayout()
        header.addWidget(QLabel("Notification"), 1)
        header.addItem(QSpacerItem(20,0))
        nl.addLayout(header)

        self._tbl = QTableWidget(0,3)
        self._tbl.setHorizontalHeaderLabels(["Event","Date",""])
        self._tbl.horizontalHeader().setStretchLastSection(False)
        self._tbl.setColumnWidth(0,120)
        self._tbl.setColumnWidth(1,180)
        self._tbl.setColumnWidth(2,60)
        self._tbl.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._tbl.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        nl.addWidget(self._tbl)
        right_v.addWidget(notif_frame, 2)

        content.addLayout(right_v, 3)

        main.addLayout(content)

    def _populate_attendance_chart(self):
        series = QPieSeries()
        series.append("A",   40)
        series.append("P",   40)
        series.append("AP",  20)
        for s in series.slices():
            s.setLabel(f"{s.label()} {s.percentage()*100:.0f}%")
            s.setLabelVisible(True)
        chart = QChart()
        chart.addSeries(series)
        chart.setBackgroundVisible(False)
        chart.legend().setVisible(False)
        self._chart_view.setChart(chart)

    def _populate_notifications(self):
        data = [
            ("Stop Day", "12/Jan/2025 to 13/Jan/2025"),
            ("Stop Day", "12/Jan/2025 to 13/Jan/2025"),
            ("Stop Day", "12/Jan/2025 to 13/Jan/2025"),
            ("Stop Day", "12/Jan/2025 to 13/Jan/2025"),
            ("Stop Day", "12/Jan/2025 to 13/Jan/2025"),
        ]
        self._tbl.setRowCount(len(data))
        for i,(evt,dt) in enumerate(data):
            self._tbl.setItem(i, 0, QTableWidgetItem(evt))
            self._tbl.setItem(i, 1, QTableWidgetItem(dt))
            btn = QPushButton("View")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background:#1B3452; color:white;
                    border:none; border-radius:4px;
                    padding:2px 6px;
                }
                QPushButton:hover { background:#255083; }
            """)
            self._tbl.setCellWidget(i,2,btn)
