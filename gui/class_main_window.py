from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame
from gui.class_input_panel import GuiInputPanel
from gui.class_sidebar import GuiSidebar
from gui.class_display_panel import GuiDisplayPanel  # Đã gộp

class GuiRoot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Bán Hàng Tiệm Bạc")
        self.resize(1280, 800)

        self.mode_list = ['view_mode', 'manager_mode']
        self.mode_name = ''

        # === Sidebar, Input và Display Panel
        self.sidebar_frame = GuiSidebar()
        self.input_panel = GuiInputPanel()
        self.display_panel = GuiDisplayPanel()

        # === Main Layout chứa Display + Input
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.display_panel)
        self.main_layout.addWidget(self.input_panel)

        self.main_frame = QFrame()
        self.main_frame.setLayout(self.main_layout)

        app_layout = QHBoxLayout()
        app_layout.addWidget(self.sidebar_frame)
        app_layout.addWidget(self.main_frame)
        self.setLayout(app_layout)

        # === Kết nối signal từ sidebar
        self.sidebar_frame.change_display.connect(self.display_panel.show_content)
        self.sidebar_frame.set_mode_display.connect(self.display_panel.set_mode)
        self.sidebar_frame.set_mode_input.connect(self.input_panel.switch_input_mode)

    def set_mode(self, mode: str):
        """Hàm này không còn cần thiết nữa nếu chuyển mode qua display_panel.set_mode"""
        print("Mode nhận được:", mode)
