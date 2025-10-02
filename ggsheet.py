import requests
import csv
from io import StringIO

"""
    Description: Read Data From Google Sheet
    Return: List of Data Rows
""" 
def read_data_from_sheet(sheet_id, sheet_name):
    result = []
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    response = requests.get(url)
    response.encoding = 'utf-8'

    result = list(csv.reader(StringIO(response.text)))

    return result


sheet_products = {"id": "1CXs3mX3eF0R2A2d4bLKGoq-4yqVa3GiZLNSMrVr-CfE", "name": "SanPham" }

data = read_data_from_sheet(sheet_products["id"], sheet_products["name"])
print(data)