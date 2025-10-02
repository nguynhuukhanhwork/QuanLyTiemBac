# class_display_panel.py
# Layout để hiển thị dữ liệu cần thiết

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton, QMessageBox, QHeaderView
)
from PyQt5.QtCore import Qt
import sqlite3

from gui.style import STYLE_DISPLAY, STYLE_TABLE_PRIMARY, STYLE_LABEL_PRIMARY
from database import db_get_table_products


class GuiDisplayPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(STYLE_DISPLAY)

        # === Layout chính chứa các chế độ ===
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # === View Mode ===
        self.view_widget = QWidget()
        self.view_layout = QVBoxLayout()
        self.view_widget.setLayout(self.view_layout)

        self.label = QLabel("Chưa có dữ liệu để hiển thị")
        self.label.setStyleSheet(STYLE_LABEL_PRIMARY)

        self.view_table = QTableWidget()
        self.view_table.setStyleSheet(STYLE_TABLE_PRIMARY)
        self.view_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view_table.verticalHeader().setVisible(False)

        self.view_layout.addWidget(self.label)
        self.view_layout.addWidget(self.view_table)

        # === Manager Mode ===
        self.manager_widget = QWidget()
        self.manager_layout = QVBoxLayout()
        self.manager_widget.setLayout(self.manager_layout)

        title = QLabel("Quản lý hóa đơn bán hàng")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        self.manager_table = QTableWidget()

        self.manager_layout.addWidget(title)
        self.manager_layout.addWidget(self.manager_table)

        # === Thêm vào layout chính ===
        self.layout.addWidget(self.view_widget)
        self.layout.addWidget(self.manager_widget)
        self.setLayout(self.layout)

        self.set_mode("view_mode")  # Mặc định

    def set_mode(self, mode: str):
        if mode == "view_mode":
            self.view_widget.show()
            self.manager_widget.hide()
        elif mode == "manager_mode":
            self.view_widget.hide()
            self.manager_widget.show()
            self.load_sales()
        else:
            print(f"[GuiDisplayPanel] Mode không hợp lệ: {mode}")

    # === View Mode ===
    def show_content(self, data, headers=None):
        if isinstance(data, str):
            self.label.setText(data)
            self.label.show()
            self.view_table.hide()
            return

        table_data, table_headers = (data, headers)
        if isinstance(data, tuple):
            table_data, table_headers = data
            if not table_headers:
                table_headers = headers

        if table_data and isinstance(table_data, list) and all(isinstance(row, (list, tuple)) for row in table_data):
            self.label.hide()
            self.view_table.show()
            self._adjust_table_height()
            self._populate_view_table(table_data, table_headers)
        else:
            self.label.setText("Dữ liệu không hợp lệ")
            self.label.show()
            self.view_table.hide()

    def _adjust_table_height(self):
        current_title = self.label.text().strip()
        if current_title == "Sản phẩm mua":
            self.setMaximumHeight(300)
        else:
            self.setMaximumHeight(16777215)

    def _populate_view_table(self, data, headers=None):
        table = self.view_table
        table.clear()

        if not data:
            table.setRowCount(0)
            table.setColumnCount(0)
            return

        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))

        if headers and len(headers) == len(data[0]):
            table.setHorizontalHeaderLabels(headers)
        else:
            table.setHorizontalHeaderLabels([f"Cột {i+1}" for i in range(len(data[0]))])

        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell = QTableWidgetItem(str(item))
                cell.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                table.setItem(row_idx, col_idx, cell)

        header = table.horizontalHeader()
        for col in range(len(data[0])):
            if col in [0, 1, 2]:
                header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
            else:
                header.setSectionResizeMode(col, QHeaderView.Stretch)

        table.resizeRowsToContents()

    # === Manager Mode ===
    def load_sales(self):
        data = db_get_table_products()

        self.manager_table.setRowCount(len(data))
        self.manager_table.setColumnCount(6)
        self.manager_table.setHorizontalHeaderLabels(["Mã HĐ", "Mã KH", "Ngày bán", "Tổng tiền", "Ghi chú", "Xóa"])

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.manager_table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            btn_delete = QPushButton("Xóa")
            btn_delete.setStyleSheet("background-color: #d9534f; color: white;")
            btn_delete.clicked.connect(lambda _, sale_id=row_data[0]: self.delete_sale(sale_id))
            self.manager_table.setCellWidget(row_idx, 5, btn_delete)

        self.manager_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def delete_sale(self, sale_id):
        confirm = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa hóa đơn #{sale_id}?\nChi tiết sản phẩm sẽ bị xóa theo.",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            conn = sqlite3.connect("myshop.db")
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Sales WHERE sale_id = ?", (sale_id,))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Đã xóa", f"Hóa đơn #{sale_id} đã bị xóa.")
            self.load_sales()
