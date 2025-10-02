# database.py
import sqlite3
import os

# ===========
# Các hàm sử dụng chung
# Dùng để kết nối Database, xác định folder chứa các lệnh truy vấn
# ===========
def db_connect():
    """Kết nối đến database."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'data', 'data.sqlite')
    return sqlite3.connect(db_path)


def db_get_sql_folder():
    """Trả về đường dẫn đến thư mục chứa file SQL."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'sql')

def db_execute_script(script):
    """
    Thực thi script SQL hoặc file SQL.

    Args:
        script (str): Chuỗi SQL hoặc đường dẫn file .sql.
    """
    try:
        with db_connect() as conn:
            cursor = conn.cursor()
            if script.endswith(".sql"):
                if not os.path.exists(script):
                    print(f"Lỗi: File {script} không tồn tại")
                    return
                with open(script, "r", encoding="utf-8") as f:
                    sql = f.read()
            else:
                sql = script
            cursor.executescript(sql)
            conn.commit()
            print("Thực thi script thành công.")
    except sqlite3.Error as e:
        print(f"Lỗi khi thực thi script: {e}")

def db_query_select_data_from_file(file_name=''):
    """
    Truy vấn dữ liệu trả về data và headers của truy vấn SQL, với tham số truyền vào là file

    Args:
        file_name (str): Tên file SQL chứa truy vấn

    Returns:
        tuple: (data, headers)
            - data: Danh sách các hàng kết quả
            - headers: Danh sách tên cột
    """
    if file_name == '':
        return "Chưa điền tên file vào Parameter"

    sql_dir = db_get_sql_folder()
    file_path = os.path.join(sql_dir, file_name)

    if not os.path.exists(file_path):
        print(f"[Lỗi] File {file_path} không tồn tại.")
        return [], []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            query = f.read()

        with db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            header = [description[0] for description in cursor.description] if cursor.description else []
            return rows, header

    except sqlite3.Error as e:
        print(f"[Lỗi] khi thực thi truy vấn từ file {file_name}: {e}")
        return [], []


# ==========
# Lấy dữ liệu từ các bảng cụ thể
# ==========

# Lấy dữ liệu từ bảng
def db_get_table_products():
    """Lấy dữ liệu từ bảng Products."""
    rows, header = db_query_select_data_from_file('query/get_products.sql')
    return rows, header


def db_get_table_customers():
    """Lấy dữ liệu từ bảng Customers."""
    rows, header = db_query_select_data_from_file('query/get_customers.sql')
    return rows, header

def db_get_table_suppliers():
    """Lấy dữ liệu từ bảng Suppliers."""
    rows, header = db_query_select_data_from_file('query/get_suppliers.sql')
    return rows, header

# Lấy dữ liệu từ các giao dịch
def db_get_purchase_history():
    """Lấy dữ liệu lịch sử nhập hàng"""
    rows, header = db_query_select_data_from_file('query/get_purchase_history.sql')
    return rows, header

def db_get_sale_history():
    """Lấy dữ liệu lịch sử mua hàng"""
    rows, header = db_query_select_data_from_file('query/get_sale_history.sql')
    return rows, header


# Các hàm để thêm bảng và test dữ liệu
def db_create_database():
    """Tạo CSDL"""
    # Tạo database và chèn dữ liệu mẫu
    sql_path = db_get_sql_folder()

    # Tạo bảng
    sql_create_table_file_name = "create_tables.sql"
    database_script_file_path = os.path.join(sql_path, sql_create_table_file_name)
    if os.path.exists(database_script_file_path):
        db_execute_script(database_script_file_path)
    else:
        print(f"Lỗi: File {database_script_file_path} không tồn tại")

def db_add_demo_data():
    """Thêm dữ liệu mẫu vào các bảng"""
    sql_path = db_get_sql_folder()

    # Chèn dữ liệu mẫu
    sql_insert_demo_data = "insert_demo_data.sql"
    demo_data_table_file_path = os.path.join(sql_path, sql_insert_demo_data)
    if os.path.exists(demo_data_table_file_path):
        db_execute_script(demo_data_table_file_path)
    else:
        print(f"Lỗi: File {demo_data_table_file_path} không tồn tại")

def db_get_product_compo_box():
    """Lấy dữ liệu để nạp vào compo box"""
    rows, header = db_query_select_data_from_file('compo_data/get_product_name.sql')
    return rows, header

if __name__ == '__main__':
    # db_create_database()
    # db_add_demo_data()
    data, headers = db_get_product_compo_box()
    print(data)
    print(headers)