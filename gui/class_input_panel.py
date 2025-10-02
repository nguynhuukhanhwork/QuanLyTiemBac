# class_input_panel.py
# Một phần trong GUI dùng để quản nhập liệu

from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLineEdit,
    QPushButton, QGroupBox, QComboBox, QLabel
)
from gui.style import STYLE_GROUPBOX_PRIMARY, STYLE_INPUT_PRIMARY, STYLE_COMBOBOX_PRIMARY, STYLE_LABEL_PRIMARY, STYLE_BUTTON_SUBMIT
from database import db_get_product_compo_box

class GuiInputPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Load Data từ CSDL
        self.product_list, _ = db_get_product_compo_box()
        self.product_lookup = {row[0]: row[1:] for row in self.product_list}  # tên → (chất liệu, size, giá)

        self.current_mode = None
        self.layout_container = QVBoxLayout()
        self.setLayout(self.layout_container)

    def form_add_sale_transaction(self):
        layout = QVBoxLayout()

        # === GroupBox: Thông tin khách hàng ===
        customer_infor_groupbox = QGroupBox("THÔNG TIN KHÁCH HÀNG")
        customer_infor_groupbox.setStyleSheet(STYLE_GROUPBOX_PRIMARY)
        customer_layout = QHBoxLayout()

        customer_name_input = QLineEdit()
        customer_name_input.setStyleSheet(STYLE_INPUT_PRIMARY)
        customer_name_input.setPlaceholderText("Tên khách")

        customer_contact_input = QLineEdit()
        customer_contact_input.setStyleSheet(STYLE_INPUT_PRIMARY)
        customer_contact_input.setPlaceholderText("Liên hệ")

        customer_layout.addWidget(customer_name_input)
        customer_layout.addWidget(customer_contact_input)
        customer_infor_groupbox.setLayout(customer_layout)

        # === GroupBox: Nhập hóa đơn ===
        order_groupbox = QGroupBox("NHẬP HÓA ĐƠN")
        order_groupbox.setStyleSheet(STYLE_GROUPBOX_PRIMARY)
        order_input_row = QHBoxLayout()
        order_label_row = QHBoxLayout()

        # Label Customize
        order_name_label = QLabel("Tên sản phẩm")
        order_name_label.setStyleSheet(STYLE_LABEL_PRIMARY)
        order_size_label = QLabel("Size")
        order_size_label.setStyleSheet(STYLE_LABEL_PRIMARY)
        order_material_label = QLabel("Vật liệu")
        order_material_label.setStyleSheet(STYLE_LABEL_PRIMARY)
        order_cost_label = QLabel("Giá")
        order_cost_label.setStyleSheet(STYLE_LABEL_PRIMARY)

        order_label_row.addWidget(order_name_label)
        order_label_row.addWidget(order_size_label)
        order_label_row.addWidget(order_material_label)
        order_label_row.addWidget(order_cost_label)

        names, types, sizes, prices = self.extract_combo_data()

        order_item = QComboBox()
        order_item.setEditable(True)
        order_item.addItems(names)
        order_item.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        order_size = QComboBox()
        order_size.setEditable(True)
        order_size.addItems(sizes)
        order_size.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        order_type = QComboBox()
        order_type.setEditable(True)
        order_type.addItems(types)
        order_type.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        order_cost = QComboBox()
        order_cost.setEditable(True)
        order_cost.addItems(prices)
        order_cost.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        order_layout = QVBoxLayout()
        order_layout.addLayout(order_label_row)
        order_layout.addLayout(order_input_row)

        # Tự động cập nhật khi chọn sản phẩm
        order_item.currentTextChanged.connect(
            lambda name: self.update_product_fields(name, order_size, order_type, order_cost)
        )

        order_input_row.addWidget(order_item)
        order_input_row.addWidget(order_size)
        order_input_row.addWidget(order_type)
        order_input_row.addWidget(order_cost)
        order_groupbox.setLayout(order_layout)

        # === Note Groupbox ===
        note_groupbox = QGroupBox("THÔNG TIN KHÁCH HÀNG")
        note_groupbox.setStyleSheet(STYLE_GROUPBOX_PRIMARY)
        note_layout = QHBoxLayout()

        note_all_input = QLineEdit()
        note_all_input.setPlaceholderText("Ghi chú thêm")
        note_all_input.setStyleSheet(STYLE_INPUT_PRIMARY)
        note_layout.addWidget(note_all_input)
        note_groupbox.setLayout(note_layout)

        # === Submit Button ===
        submit_btn = QPushButton("Hoàn tất - Xuất hóa đơn")
        submit_btn.setStyleSheet("background-color: green; color: white; padding: 8px;")

        # === Add vào layout chính
        layout.addWidget(customer_infor_groupbox)
        layout.addWidget(order_groupbox)
        layout.addWidget(note_groupbox)
        layout.addWidget(submit_btn)

        return layout

    def form_add_purchase_transaction(self):
        """Layout form dùng để nhập dữ liệu hàng hóa, khi tiệm nhập hàng mới"""

        layout = QVBoxLayout()

        # === Label Layout ===
        purchase_transaction_label_layout = QHBoxLayout()
        label_style = STYLE_LABEL_PRIMARY

        purchase_transaction_label_layout.addWidget(QLabel("Tên sản phẩm"), 2)
        purchase_transaction_label_layout.addWidget(QLabel("Size"), 1)
        purchase_transaction_label_layout.addWidget(QLabel("Loại sản phẩm"), 1)
        purchase_transaction_label_layout.addWidget(QLabel("Số lượng"), 1)
        purchase_transaction_label_layout.addWidget(QLabel("Tổng tiền"), 1)

        purchase_transaction_layout = QVBoxLayout()
        purchase_transaction_layout.addLayout(purchase_transaction_label_layout)

        # === Layout chứa các dòng nhập sản phẩm (ban đầu 1 dòng) ===
        self.purchase_item_rows_layout = QVBoxLayout()
        purchase_transaction_layout.addLayout(self.purchase_item_rows_layout)

        # Tạo dòng đầu tiên
        self.add_item_purchase_transaction()

        # === GroupBox bao layout ===
        purchase_transaction_groupbox = QGroupBox("GHI THÔNG TIN NHẬP HÀNG")
        purchase_transaction_groupbox.setStyleSheet(STYLE_GROUPBOX_PRIMARY)
        purchase_transaction_groupbox.setLayout(purchase_transaction_layout)

        # === Button ===
        add_item_btn = QPushButton("+ Thêm sản phẩm")
        add_item_btn.clicked.connect(self.add_item_purchase_transaction)

        submit_btn = QPushButton("Thêm dữ liệu vào kho")
        submit_btn.setStyleSheet(STYLE_BUTTON_SUBMIT)

        layout.addWidget(purchase_transaction_groupbox)
        layout.addWidget(add_item_btn)
        layout.addWidget(submit_btn)

        return layout

    def add_item_purchase_transaction(self):
        names, types, sizes, prices = self.extract_combo_data()

        input_layout = QHBoxLayout()

        item_name = QComboBox()
        item_name.setEditable(True)
        item_name.addItems(names)
        item_name.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        item_size = QComboBox()
        item_size.setEditable(True)
        item_size.addItems(sizes)
        item_size.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        item_type = QComboBox()
        item_type.setEditable(True)
        item_type.addItems(types)
        item_type.setStyleSheet(STYLE_COMBOBOX_PRIMARY)

        item_quantity = QLineEdit()
        item_quantity.setStyleSheet(STYLE_INPUT_PRIMARY)

        item_cost = QLineEdit()
        item_cost.setStyleSheet(STYLE_INPUT_PRIMARY)

        item_name.currentTextChanged.connect(
            lambda name: self.update_product_fields(name, item_size, item_type, item_cost)
        )

        input_layout.addWidget(item_name, 2)
        input_layout.addWidget(item_size, 1)
        input_layout.addWidget(item_type, 1)
        input_layout.addWidget(item_quantity, 1)
        input_layout.addWidget(item_cost, 1)

        # Thêm dòng mới vào layout chính
        self.purchase_item_rows_layout.addLayout(input_layout)

    def handle_submit_form_sale_transaction(self):
        print("chưa thực hiện")
        return []

    def handle_submit_form_purchase_transaction(self):
        print("chưa thực hiện")
        return []

    def switch_input_mode(self, mode: str):
        print(f"[InputPanel] Đang chuyển sang input mode: {mode}")
        self.current_mode = mode
        while self.layout_container.count():
            item = self.layout_container.takeAt(0)
            if item.layout():
                self.clear_layout(item.layout())
            elif item.widget():
                item.widget().deleteLater()

        if mode == "add_sale":
            self.layout_container.addLayout(self.form_add_sale_transaction())
        elif mode == "add_product":
            self.layout_container.addLayout(self.form_add_purchase_transaction())
        else:
            print(f"[InputPanel] Mode không hợp lệ: {mode}")

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

    def extract_combo_data(self):
        """
        Trích dữ liệu từ product_list thành các list cho ComboBox
        """
        names = sorted(set([row[0] for row in self.product_list]))
        types = sorted(set([row[1] for row in self.product_list]))
        sizes = sorted(set([row[2] for row in self.product_list]))
        prices = sorted(set([row[3] for row in self.product_list]))
        return names, types, sizes, prices

    def update_product_fields(self, product_name, size_box, type_box, price_box):
        """
        Cập nhật các combo box còn lại khi chọn tên sản phẩm
        """
        if product_name in self.product_lookup:
            material, size, price = self.product_lookup[product_name]
            type_box.setCurrentText(material)
            size_box.setCurrentText(size)
            price_box.setCurrentText(price)

