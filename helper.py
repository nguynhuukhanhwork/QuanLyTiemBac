from datetime import datetime

# ==========
# ví dụ: 06/07/2025 00:38:42
# ==========
def get_cur_date_time():
    now = datetime.now()
    return now.strftime("$d/%m/%Y %H:%M:%S")  


# ==========
# Create Log and Write log
# ==========
def error_log(error):
    with open("debug.log", "w") as file:
        file.write(error)
    return error