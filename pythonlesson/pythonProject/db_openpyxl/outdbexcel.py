from openpyxl import Workbook
import requests
import json
import os

# 发送 POST 请求
payload = {
    "FunID": "RS020101",
    "Language": 1,
    "Data": {
        # Incumbency 1表示在职 0表示离职
        "Incumbency": 1
    }
}

# 定义请求头
headers = {'Content-Type': 'application/octet-stream'}

# 发送 POST 请求，并设置请求头为"raw"
response = requests.post("http://172.16.10.42:18010/RESTService/Search", json=payload, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 如果请求成功，解析响应数据并打印w
    data = response.json().get('Data')

    data_json = json.loads(data)
else:
    # 如果请求失败，打印响应状态码
    print("POST 请求失败:", response.status_code)


def export_dict_to_excel(data, excel_file):
    wb = Workbook()
    ws = wb.active

    # 写入表头
    headers = list(data[0].keys())
    ws.append(headers)

    # 写入数据
    for item in data:
        row_data = [item[header] for header in headers]
        ws.append(row_data)

    # 保存工作簿到Excel文件中
    wb.save(excel_file)
    print("数据已成功导出到Excel文件:", excel_file)


# 指定要保存的Excel文件名
excel_file = 'output.xlsx'

# 导出数据到Excel表
export_dict_to_excel(data_json, excel_file)
print("导出成功")
os.startfile('output.xlsx')
