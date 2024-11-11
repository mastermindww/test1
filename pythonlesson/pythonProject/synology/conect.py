from smb.SMBConnection import SMBConnection
from openpyxl import Workbook
import os

# SMB连接信息
server_name = 'doc'  # 可以是服务器名或IP地址
server_ip = '172.16.10.12'  # 服务器的IP地址
server_port = 139  # SMB服务的端口，通常是139或445
username = 'test'  # 登录用户名
password = '123456'  # 登录密码
client_name = 'CJ-IT1416'  # 客户端机器名
share_name = 'Databackup'  # 要访问的共享文件夹名

# 创建SMB连接对象
conn = SMBConnection(username, password, client_name, server_name, use_ntlm_v2=True)

# 连接到SMB服务器
conn.connect(server_ip, server_port)

# ... 进行文件操作 ...
files_and_dirs_ERP = conn.listPath(share_name, '\ERP\D\ERPbackup\ZT006')
files_and_dirs_ERP2 = conn.listPath(share_name, '\ERP2\D\ERPbackup\ZT002')
files_and_dirs_ERP3 = conn.listPath(share_name, '\ERP3\D\ERPDATABUCKUP\ZT801')
files_and_dirs_EIS8 = conn.listPath(share_name, '\EIS8\D\DataBackup')
files_and_dirs_SHARKSQL = conn.listPath(share_name, '\SHARKSQL\D\shark_backup\shark')

list_ERP = []
list_ERP.append("ERP服务器备份记录")
list_ERP2 = []
list_ERP2.append("ERP2服务器备份记录")
list_ERP3 = []
list_ERP3.append("ERP3服务器备份记录")
list_EIS8 = []
list_EIS8.append("EIS8服务器备份记录")
list_SHARKSQL = []
list_SHARKSQL.append("SHARKSQL服务器备份记录")

for entry in files_and_dirs_ERP:
    list_ERP.insert(1, entry.filename)

for entry in files_and_dirs_ERP2:
    list_ERP2.insert(1, entry.filename)

for entry in files_and_dirs_ERP3:
    list_ERP3.insert(1, entry.filename)

for entry in files_and_dirs_EIS8:
    list_EIS8.insert(1, entry.filename)

for entry in files_and_dirs_SHARKSQL:
    list_SHARKSQL.insert(1, entry.filename)

# 关闭连接
conn.close()

# 创建一个Workbook（工作簿）对象
wb = Workbook()
# 激活当前工作表
ws = wb.active

# 遍历列表，并将它们作为行添加到工作表中
# 注意：我们假设所有列表的长度相同，或者我们只想取最短的那个列表的长度
# 如果列表长度不同，你可能需要调整循环逻辑
for col_index, data in enumerate([list_ERP, list_ERP2, list_ERP3, list_EIS8, list_SHARKSQL], start=1):  # 从第1行开始
    for row_index, value in enumerate(data, start=1):  # 从第1列开始
        ws.cell(row=row_index, column=col_index, value=value)
# 设置列A到列E的宽度为30
for col in ['A', 'B', 'C', 'D', 'E']:
    ws.column_dimensions[col].width = 30
# 保存工作簿到文件
wb.save('synology_backup.xlsx')
print("保存成功")
os.startfile('synology_backup.xlsx')
