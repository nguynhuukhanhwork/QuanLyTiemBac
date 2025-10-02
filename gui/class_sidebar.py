# class_sidebar.py
# SideBar Của GUI chứa các nút nhấn để làm việc

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox
from PyQt5.QtCore import pyqtSignal
from gui.style import STYLE_BUTTON_PRIMARY, STYLE_BUTTON_SECOND, STYLE_BUTTON_THIRD
from database import db_get_table_products, db_get_table_customers, db_get_table_suppliers ,db_get_purchase_history, \
    db_get_sale_history


# noinspection PyUnresolvedReferences
class GuiSidebar(QWidget):
    set_mode_display = pyqtSignal(str) # Tín hiệu để nhận diện loại giao diện hiển thị
    set_mode_input = pyqtSignal(str) # Tín hiệu để thay đổi Form nhập cho phù hợp

    change_header = pyqtSignal(str)  # Signal để thay đổi tiêu đề Display
    change_display = pyqtSignal(tuple)  # Signal để gửi (data, headers) đến DisplayPanel
    change_input = pyqtSignal(str)  # Signal để hiển thị form trong InputPanel

    input_mode = ['add_sale', 'add_user', 'add_product']
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # === Group: Xem thông tin hệ thống ===
        # Group này dùng để xem dữ liệu cần thiết trong các bảng
        # Các bảng cần xem là: Products, Customers,
        view_group = QGroupBox("XEM THÔNG TIN")
        view_layout = QVBoxLayout()

        # Xem thông tin sản phẩm trong hệ thống
        view_product = QPushButton("Xem sản phẩm")
        view_product.setFixedHeight(40)
        view_product.setStyleSheet(STYLE_BUTTON_PRIMARY)
        view_product.clicked.connect(self.show_product)

        # Xem thông tin khách hàng
        view_customer = QPushButton("Xem khách hàng")
        view_customer.setFixedHeight(40)
        view_customer.setStyleSheet(STYLE_BUTTON_PRIMARY)
        view_customer.clicked.connect(self.show_customers)

        # Xem kho hàng
        view_supplier = QPushButton("Xem thông tin nhà cung cấp")
        view_supplier.setFixedHeight(40)
        view_supplier.setStyleSheet(STYLE_BUTTON_PRIMARY)
        view_supplier.clicked.connect(self.show_supplier)

        # Xem thông tin nhập hàng
        view_purchase = QPushButton("Xem lịch sử nhập hàng")
        view_purchase.setFixedHeight(40)
        view_purchase.setStyleSheet(STYLE_BUTTON_PRIMARY)
        view_purchase.clicked.connect(self.show_transaction_purchase)

        # Xem tất tả lịch sử giao dịch
        view_transaction = QPushButton("Xem lịch sử bán hàng")
        view_transaction.setFixedHeight(40)
        view_transaction.setStyleSheet(STYLE_BUTTON_PRIMARY)
        view_transaction.clicked.connect(self.show_transaction_sale)

        # Add Button -> Layout
        view_layout.addWidget(view_product)
        view_layout.addWidget(view_customer)
        view_layout.addWidget(view_supplier)
        view_layout.addWidget(view_purchase)
        view_layout.addWidget(view_transaction)

        view_group.setLayout(view_layout) # Set layout


        # ==========
        # --- Group: Quản lý --
        # Dùng để xóa dữ liệu
        # ==========

        manager_group = QGroupBox("Quản lý dữ liệu")
        manger_layout = QVBoxLayout()

        manager_sales_btn = QPushButton("Quản lý sản phẩm bán ra")
        manager_sales_btn.setFixedHeight(40)
        manager_sales_btn.setStyleSheet(STYLE_BUTTON_SECOND)
        manager_sales_btn.clicked.connect(self.show_manager_mode)

        manger_layout.addWidget(manager_sales_btn)

        manager_group.setLayout(manger_layout)

        # ==========
        # === Group: Hóa đơn ===
        # ==========
        invoice_group = QGroupBox("Hóa đơn")
        invoice_layout = QVBoxLayout()

        preview_order_btn = QPushButton("Xem hóa đơn trước khi xuất")
        preview_order_btn.setFixedHeight(40)
        preview_order_btn.setStyleSheet(STYLE_BUTTON_PRIMARY)

        invoice_layout.addWidget(preview_order_btn)
        invoice_group.setLayout(invoice_layout)

        # === Group: Input ===
        input_group= QGroupBox("Nhập liệu")
        input_layout = QVBoxLayout()

        # Nút chuyển sang form để nhập dữ liệu bán hàng
        input_add_sale_btn = QPushButton("Thêm giao dịch bán")
        input_add_sale_btn.setFixedHeight(40)
        input_add_sale_btn.setStyleSheet(STYLE_BUTTON_THIRD)
        input_add_sale_btn.clicked.connect(self.convert_input_mode_add_sale)

        # Nút chuyển sang form để nhập dữ liệu sản phẩm
        input_add_product_btn = QPushButton("Nhập sản phẩm mới")
        input_add_product_btn.setFixedHeight(40)
        input_add_product_btn.setStyleSheet(STYLE_BUTTON_THIRD)
        input_add_product_btn.clicked.connect(self.convert_input_mode_add_product)

        input_layout.addWidget(input_add_sale_btn)
        input_layout.addWidget(input_add_product_btn)
        input_group.setLayout(input_layout)

        # === Add các group vào layout chính ===
        main_layout.addWidget(view_group)
        main_layout.addWidget(manager_group)
        main_layout.addWidget(invoice_group)
        main_layout.addWidget(input_group)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def show_product(self):

        self.set_mode_display.emit("view_mode")

        """Hiển thị danh sách sản phẩm từ database."""
        try:
            data, headers = db_get_table_products()
            self.change_header.emit("Danh sách sản phẩm")
            self.change_display.emit((data, headers))
        except Exception as e:
            self.change_header.emit("Lỗi khi tải sản phẩm")
            self.change_display.emit(("Lỗi: " + str(e), []))

    def show_customers(self):
        self.set_mode_display.emit("view_mode")

        """Hiển thị danh sách khách hàng từ database."""
        try:
            data, headers = db_get_table_customers()
            self.change_header.emit("Danh sách khách hàng")
            self.change_display.emit((data, headers))
        except Exception as e:
            self.change_header.emit("Lỗi khi tải khách hàng")
            self.change_display.emit(("Lỗi: " + str(e), []))

    def show_supplier(self):
        self.set_mode_display.emit("view_mode")

        try:
            data, headers = db_get_table_suppliers() # Get Data & Header
            self.change_header.emit("Danh sách nhà cung cấp")
            self.change_display.emit((data, headers))
        except Exception as e:
            self.change_header.emit("Lỗi khi tải khách hàng")
            self.change_display.emit(("Lỗi: " + str(e), []))

    def show_transaction_purchase(self):
        self.set_mode_display.emit("view_mode")

        "Hiển thị các giao dịch"
        try:
            data, header = db_get_purchase_history()
            self.change_header.emit("Hóa đơn bán")
            self.change_display.emit((data, header))
        except Exception as e:
            self.change_header.emit("Lỗi khi tải hóa đơn bán")
            self.change_display.emit(("Lỗi: " + str(e), []))

    def show_transaction_sale(self):
        self.set_mode_display.emit("view_mode")

        "Hiển thị các Hàng đã bán ra"
        try:
            data, header= db_get_sale_history()
            self.change_header.emit("Hóa đơn bán")
            self.change_display.emit((data, header))
        except Exception as e:
            self.change_header.emit("Lỗi khi tải hóa đơn bán")
            self.change_display.emit(("Lỗi: " + str(e), []))

    def show_no_feature(self):
        self.set_mode_display.emit("view_mode")

        "Thông báo chức năng chưa thực hiện"
        self.change_header.emit("chức năng chưa thực hiện")
        self.change_display.emit(("Chức năng này đang phát triển", []))

    def show_manager_mode(self):
        self.set_mode_display.emit("manager_mode")

    def check_input_mode(self, mode):
        valid_mode = self.input_mode
        if mode not in valid_mode:
            print("[Error] Input Mode không hợp lệ")
            return False

        return mode

    def convert_input_mode_add_sale(self):
        """Check and emit mode -> Chuyển mode ở Input Panel"""
        mode_sale = "add_sale"
        mode = self.check_input_mode(mode_sale)
        self.set_mode_input.emit(mode)

    def convert_input_mode_add_product(self):
        """Check and emit mode -> Chuyển mode ở Input Panel"""
        mode_add_product = "add_product"
        mode = self.check_input_mode(mode_add_product)
        self.set_mode_input.emit(mode)
