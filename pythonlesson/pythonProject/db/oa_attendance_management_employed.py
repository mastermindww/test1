import pyodbc

# 连接到你的SQL Server数据库
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.10.15;DATABASE=EIS;UID=sa;PWD=info@admin8813')

# 创建游标对象来执行SQL查询
cursor = connection.cursor()

# 定义你的SQL查询
sql_query = (
    "SELECT FI_ORG_EMP.name,FI_ORG_EMP.dept_name,FI_ORG_EMP.position_name,FI_ORG_EMP.mobile,FI_ORG_EMP.isactive,FI_ORG_EMP_FLEX.hometel FROM FI_ORG_EMP INNER JOIN FI_ORG_EMP_FLEX ON FI_ORG_EMP.id = FI_ORG_EMP_FLEX.p_id")

# 执行查询
cursor.execute(sql_query)

# 获取所有结果
results = cursor.fetchall()

# 打印或处理结果
row_emp = []
for row in results:
    row_emp.append(row)

row_need = []
for row in row_emp:
    if row[4] == 1 and row[5] == '1':
        row_need.append({"员工姓名": row[0],
                         "部门": row[1],
                         "岗位": row[2],
                         "手机": row[3],
                         "在职情况": "在职"})

# 关闭游标和连接
cursor.close()
connection.close()
