# ui/dashboards/parent_academic_progress_widget.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QComboBox, QTableWidget, QTableWidgetItem, QScrollArea,
    QPushButton, QSizePolicy, QSpacerItem
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class ParentAcademicProgressWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(8)

        # --- 1) Top summary bar ---
        summary = QFrame()
        summary.setStyleSheet("background: #003366; color: white;")
        s_layout = QHBoxLayout(summary)
        s_layout.setContentsMargins(12, 6, 12, 6)
        s_layout.setSpacing(24)

        def make_card(icon, title, value):
            card = QFrame()
            card.setStyleSheet("background: transparent;")
            cl = QVBoxLayout(card)
            cl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if icon:
                ico = QLabel()
                ico.setPixmap(
                    QPixmap(icon)
                    .scaled(32, 32,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation)
                )
                cl.addWidget(ico)
            cl.addWidget(QLabel(f"<b>{title}</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(QLabel(value), alignment=Qt.AlignmentFlag.AlignCenter)
            return card

        s_layout.addWidget(make_card("resources/icons/users.png", "Classmate", "25"))
        sep = QFrame(); sep.setFrameShape(QFrame.Shape.VLine); sep.setStyleSheet("color: white;")
        s_layout.addWidget(sep)
        s_layout.addWidget(make_card("resources/icons/female.png", "Female", "12"))
        sep2 = QFrame(); sep2.setFrameShape(QFrame.Shape.VLine); sep2.setStyleSheet("color: white;")
        s_layout.addWidget(sep2)

        donut_frame = QFrame()
        df = QVBoxLayout(donut_frame)
        df.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fig = Figure(figsize=(1.5, 1.5))
        ax = fig.add_subplot(111)
        ax.pie([1], radius=1.0, colors=["#0055aa"], wedgeprops=dict(width=0.3))
        ax.text(0, 0, "S2\nY2", ha="center", va="center", color="white", fontsize=14, fontweight='bold')
        ax.axis('equal')
        df.addWidget(FigureCanvas(fig))
        s_layout.addWidget(donut_frame)

        sep3 = QFrame(); sep3.setFrameShape(QFrame.Shape.VLine); sep3.setStyleSheet("color: white;")
        s_layout.addWidget(sep3)
        s_layout.addWidget(make_card(None, "Start", "26/Apr/2025"))
        sep4 = QFrame(); sep4.setFrameShape(QFrame.Shape.VLine); sep4.setStyleSheet("color: white;")
        s_layout.addWidget(sep4)
        s_layout.addWidget(make_card(None, "End", "04/Aug/2025"))

        root.addWidget(summary, 0)

        # --- 2) Divider line ---
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        root.addWidget(line)

        # --- 3) Middle section: grade donut, GPA chart, notes ---
        middle = QHBoxLayout()
        middle.setSpacing(12)

        # 3a) Total Grade donut + legend
        grade_frame = QFrame()
        grade_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        gf = QVBoxLayout(grade_frame)
        gf.setContentsMargins(12, 8, 12, 8)
        gf.addWidget(QLabel("<b>Total Grade</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
        fig2 = Figure(figsize=(2, 2))
        ax2 = fig2.add_subplot(111)
        data = [7, 4, 1]  # A+, A, B+
        ax2.pie(data, labels=None, autopct='%d', startangle=90, colors=['#e41a1c','#377eb8','#4daf4a'])
        ax2.axis('equal')
        gf.addWidget(FigureCanvas(fig2))
        # Legend
        lg = QHBoxLayout()
        lg.setSpacing(16)
        lg.addWidget(QLabel("<span style='color:#e41a1c;'>■</span> A+ : 7"))
        lg.addWidget(QLabel("<span style='color:#377eb8;'>■</span> A  : 4"))
        lg.addWidget(QLabel("<span style='color:#4daf4a;'>■</span> B+ : 1"))
        gf.addLayout(lg)
        middle.addWidget(grade_frame, 1)

        # 3b) All GPA bar chart
        gpa_frame = QFrame()
        gpa_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        gp = QVBoxLayout(gpa_frame)
        gp.setContentsMargins(12, 8, 12, 8)
        gp.addWidget(QLabel("<b>All GPA</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
        fig3 = Figure(figsize=(4, 2))
        ax3 = fig3.add_subplot(111)
        terms = ['S1,Y1','S1,Y2','S2,Y1','S2,Y2']
        values = [4.0, 4.0, 4.0, 4.0]
        ax3.set_xticks(range(len(terms)))
        ax3.set_xticklabels(terms, rotation=45, ha='right')
        ax3.bar(range(len(terms)), values)
        ax3.set_ylim(0, 4.5)
        ax3.set_ylabel("GPA")
        fig3.tight_layout()
        gp.addWidget(FigureCanvas(fig3))
        middle.addWidget(gpa_frame, 2)

        # 3c) School Note list
        note_frame = QFrame()
        note_frame.setStyleSheet("background: white; border: 1px solid #ccc;")
        nf = QVBoxLayout(note_frame)
        nf.setContentsMargins(12, 8, 12, 8)
        nf.addWidget(QLabel("<b>School Note</b>"))
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        il = QVBoxLayout(inner)
        # sample notes
        sample_notes = [
            ("Mr. Chea Banthan, Web II Teacher", "Your Child Permission…", "01/Jun/2025 08:30 AM"),
            ("Mr. Rin Rotha, Oracle Teacher",    "Your Child Absent…",     "31/May/2025 02:00 PM"),
            ("AUB, Academic Affairs Office",     "Your Child Result…",     "30/May/2025 09:15 AM"),
        ]
        for sender, desc, dt in sample_notes:
            row = QHBoxLayout()
            row.addWidget(QLabel(sender), 2)
            row.addWidget(QLabel(desc),   2)
            row.addWidget(QLabel(dt),     2)
            btn = QPushButton("View")
            btn.setFixedWidth(48)
            row.addWidget(btn, 1)
            il.addLayout(row)
        il.addStretch()
        inner.setLayout(il)
        scroll.setWidget(inner)
        nf.addWidget(scroll)
        middle.addWidget(note_frame, 1)

        root.addLayout(middle)

        # --- 4) Bottom: Exam results table ---
        bottom = QFrame()
        bf = QVBoxLayout(bottom)
        bf.setContentsMargins(0, 0, 0, 0)
        bf.setSpacing(8)

        # Term selector
        term_h = QHBoxLayout()
        term_h.addWidget(QLabel("Select Term:"), 0)
        self.term_combo = QComboBox()
        self.term_combo.addItems(["S2,Y2", "S1,Y2", "S2,Y1", "S1,Y1"])
        term_h.addWidget(self.term_combo, 0)
        term_h.addStretch()
        bf.addLayout(term_h)

        # Results table
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels([
            "Code", "Course Title", "Alpha Grade",
            "Credits Attempted", "Credits Earned",
            "Grade Point", "Remarks"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        bf.addWidget(self.table)

        # Summary line
        summary_h = QHBoxLayout()
        summary_h.addWidget(QLabel("Total Credits Transferred:  0"))
        summary_h.addSpacerItem(QSpacerItem(20,0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        summary_h.addWidget(QLabel("Total Credits Attained: 15"))
        summary_h.addSpacerItem(QSpacerItem(20,0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        summary_h.addWidget(QLabel("Cumulative GPA: 4.00"))
        bf.addLayout(summary_h)

        root.addWidget(bottom, 1)

        # Load demo data
        self._load_demo_results()

    def _load_demo_results(self):
        demo = [
            ("CS212", "Web Development I", "A+", "3", "3", "4.00", "Superior"),
            ("CS214", "Java Programming",    "A",  "3", "3", "4.00", "Excellent"),
            ("CS211", "UX/UI Design",        "A",  "3", "3", "4.00", "Excellent"),
            ("CS213", "Data Structures",    "A+", "3", "3", "4.00", "Superior"),
        ]
        for row in demo:
            r = self.table.rowCount()
            self.table.insertRow(r)
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(val))

    def load_data(self, summary_info, grade_dist, gpa_history, notes, exam_records):
        """
        Replace placeholders with real data:
          - summary_info: dict with keys 'classmate','female','term','start','end'
          - grade_dist: list of (label, count)
          - gpa_history: list of (term, value)
          - notes: list of (sender, desc, datetime)
          - exam_records: list of tuples matching table columns
        """
        # TODO: implement actual DB-driven updates here
        pass
