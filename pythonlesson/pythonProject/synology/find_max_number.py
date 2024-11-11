from datetime import datetime
import re


def find_min_date_in_filenames(filenames):
    # 初始化一个变量来保存找到的最小日期（使用datetime的最大可能值作为初始值）
    min_date = datetime.max

    # 编译一个正则表达式来匹配日期格式
    date_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})')

    # 遍历文件名列表
    for filename in filenames:
        # 使用正则表达式查找文件名中的日期
        match = date_pattern.search(filename)

        # 如果找到了匹配的日期
        if match:
            # 提取年、月、日
            year, month, day = match.groups()

            # 将它们转换为整数并创建datetime对象
            date_obj = datetime(int(year), int(month), int(day))

            # 如果这个日期比当前已知的最小日期还要小，则更新它
            if date_obj < min_date:
                min_date = date_obj

                # 如果找到了有效的日期，则返回它；否则返回None（或选择一个合适的默认值）
    if min_date != datetime.max:
        return min_date.strftime('%Y%m%d')  # 转换回字符串格式，如果需要的话
    else:
        return None

    # 示例文件名列表


filenames = ['report_20230401.pdf', 'data_20221231.csv', 'archive-20210101.zip']

# 调用函数并打印结果
print(find_min_date_in_filenames(filenames))