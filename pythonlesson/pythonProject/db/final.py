import db_attendance_management_unemployed
import oa_attendance_management_employed
import db_attendance_management_employed

# 东宝人事系统离职人员
db_unemployed_list = db_attendance_management_unemployed.row_need

# 东宝人事系统在职人员
db_employed_list = db_attendance_management_employed.row_need

# oa系统在职人员
oa_employed_list = oa_attendance_management_employed.row_need

# 东宝人事系统重新雇佣的人员
reemployed_list = []

for unemployed_list in db_unemployed_list:
    for employed_list in db_employed_list:
        if unemployed_list["手机"] == employed_list["手机"] and unemployed_list["员工姓名"] == \
                employed_list["员工姓名"]:
            reemployed_list.append({"员工姓名": employed_list["员工姓名"],
                                    "部门": employed_list["部门"],
                                    "岗位": employed_list["岗位"],
                                    "手机": employed_list["手机"],
                                    "在职情况": employed_list["在职情况"]})
# print("这是东宝系统重复入职的人")
# for i in reemployed_list:
#     print(i)

# OA在职人员and东宝离职人员
same_list = []

for db_list_entry in db_unemployed_list:
    for oa_list_entry in oa_employed_list:
        if db_list_entry["手机"] == oa_list_entry["手机"] and db_list_entry["员工姓名"] == oa_list_entry[
            "员工姓名"]:
            same_list.append({"员工姓名": oa_list_entry["员工姓名"],
                              "部门": oa_list_entry["部门"],
                              "岗位": oa_list_entry["岗位"],
                              "手机": oa_list_entry["手机"],
                              "在职情况": oa_list_entry["在职情况"]})
print("这是东宝系统离职但是在OA系统内在职的人")
for i in same_list:
    print(i)

padding = []
for unoa in same_list:
    for undb in reemployed_list:
        if unoa["员工姓名"] == undb["员工姓名"]:
            padding.append({
                "员工姓名": unoa["员工姓名"],
                "部门": unoa["部门"],
                "岗位": unoa["岗位"],
                "手机": unoa["手机"],
                "在职情况": unoa["在职情况"]
            })
print("这是匹配人员")
for i in padding:
    print(i)



# 1.东宝重复入职人员（有了）
# 2.东宝离职人员（有了）
# 3.OA在职人员（有了）
# 4.OA在职人员and东宝离职人员（有了）
# 判断4是否在1内，不在的话导出4的相同名称
