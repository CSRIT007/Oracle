from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem

class StudentsTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("All Students"))
        table = QTableWidget(3, 5)
        table.setHorizontalHeaderLabels(["ID", "Name", "Gender", "DOB", "Email"])
        # Example rows
        table.setItem(0, 0, QTableWidgetItem("01000001"))
        table.setItem(0, 1, QTableWidgetItem("Moeng Kimheang"))
        table.setItem(0, 2, QTableWidgetItem("Male"))
        table.setItem(0, 3, QTableWidgetItem("21/10/2006"))
        table.setItem(0, 4, QTableWidgetItem("heang@gmail.com"))
        layout.addWidget(table)
