import requests
import json

# 发送 POST 请求
payload = {
    "FunID": "RS020101",
    "Language": 1,
    "Data": {
        # Incumbency 1表示在职 0表示离职
        "Incumbency": 0
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

    row_need = []
    for row in data_json:
        row_need.append({"员工姓名": row['EmpName'],
                         "部门": row['PerField26'],
                         "岗位": row['QTTypeName'],
                         "手机": row['Mobile'],
                         "在职情况": "离职"})
else:
    # 如果请求失败，打印响应状态码
    print("POST 请求失败:", response.status_code)
