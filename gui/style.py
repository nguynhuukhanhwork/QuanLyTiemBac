# styles.py
# Style cho các thành phần GUI

STYLE_BUTTON_PRIMARY = """
QPushButton {
    background-color: #2980b9;
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    text-align: left;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #666666;
}
QPushButton:pressed {
    background-color: #666666;
}
"""

STYLE_BUTTON_SECOND = """
QPushButton {
    background-color: #830000;
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    text-align: left;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #666666;
}
QPushButton:pressed {
    background-color: #666666;
}
"""

STYLE_BUTTON_THIRD= """
QPushButton {
    background-color: #1e7e34;
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    text-align: left;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #666666;
}
QPushButton:pressed {
    background-color: #666666;
}
"""

STYLE_BUTTON_WARNING = """
QPushButton {
    background-color: #e74c3c;
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    text-align: left;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #ff6050;
}
QPushButton:pressed {
    background-color: #c0392b;
}
"""

STYLE_BUTTON_SUBMIT = """
QPushButton {
    background-color: #e74c3c;
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 6px;
    text-align: center;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 0.5px;
}
QPushButton:hover {
    background-color: #ff6050;
}
QPushButton:pressed {
    background-color: #c0392b;
}
"""


STYLE_LABEL_PRIMARY = """
QLabel {
    font-size: 14px;
    color: red;
    qproperty-alignment: 'AlignCenter';}
"""

STYLE_INPUT_PRIMARY = """
QLineEdit {
    padding: 6px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}
QLineEdit:focus {
    border: 1px solid #2980b9;
    background-color: #ecf0f1;
}
"""

STYLE_COMBOBOX_PRIMARY = """
QComboBox {
    padding: 6px;
    border: 1px solid #ccc;
    font-size: 14px;
    background-color: white;
}
"""

STYLE_GROUPBOX_PRIMARY = """
QGroupBox {
    border: 1px solid #ccc;
    border-radius: 8px;
    margin-top: 20px;
    font-weight: bold;
    font-size: 14px;
    padding: 10px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
}
"""

STYLE_TABLE_PRIMARY = """
QTableWidget {
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    background-color: white;
}
QTableWidget::item {
    padding: 5px;
}
QTableWidget::item:selected {
    background-color: #3498db;
    color: white;
}
QHeaderView::section {
    background-color: #2980b9;
    color: white;
    padding: 5px;
    border: none;
}
"""

STYLE_SIDEBAR = """
QWidget {
    background-color: #2c3e50;
    border-right: 1px solid #34495e;
}
"""

STYLE_DISPLAY = """
QWidget {
    background-color: #ecf0f1;
}
"""

