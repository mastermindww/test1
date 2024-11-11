from smb.SMBConnection import SMBConnection
from datetime import datetime
import re
import os


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


def delete_directory_files(conn, share_name, file_path, timeout):
    # 列出目录中的所有内容
    try:
        for item in conn.listPath(share_name, file_path):
            item_path = os.path.join(file_path, item.filename)
            if item.filename in ('.', '..'):
                continue
            elif item.isDirectory:
                # 如果是目录，递归删除
                delete_directory_files(conn, share_name, item_path, timeout)
                # 删除目录
                conn.deleteDirectory(share_name, item_path, timeout)
            else:
                # 如果是文件，删除文件
                conn.deleteFiles(share_name, item_path)
    except Exception as e:
        print(f"Error while deleting {file_path}: {e}")


def delete_smb_Directory(username, password, client_name, server_name, server_ip, share_name, file_path):
    # 创建一个SMBConnection对象
    conn = SMBConnection(username, password, client_name, server_name, domain='', use_ntlm_v2=True)

    try:
        # 连接到SMB服务器
        conn.connect(server_ip, 445)
        print("连接成功")

        # 删除文件
        # 注意：file_path 应该是共享文件夹内的相对路径，例如 'folder/subfolder/file.txt'
        # 注意路径分隔符，有时需要是 '\\' 而不是 '/'
        conn.deleteDirectory(share_name, file_path, 30)

    except Exception as e:
        print(f"连接或删除文件时出错: {e}")

    finally:
        # 关闭连接
        conn.close()


def delete_smb_file(username, password, client_name, server_name, server_ip, share_name, file_path):
    # 创建一个SMBConnection对象
    conn = SMBConnection(username, password, client_name, server_name, domain='', use_ntlm_v2=True)

    try:
        # 连接到SMB服务器
        conn.connect(server_ip, 445)
        print("连接成功")

        # 删除文件
        # 注意：file_path 应该是共享文件夹内的相对路径，例如 'folder/subfolder/file.txt'
        # 注意路径分隔符，有时需要是 '\\' 而不是 '/'
        conn.deleteFiles(share_name, file_path, False)

    except Exception as e:
        print(f"连接或删除文件时出错: {e}")

    finally:
        # 关闭连接
        conn.close()


def delete_smb(username, password, client_name, server_name, server_ip, share_name, file_path):
    # 创建一个SMBConnection对象
    conn = SMBConnection(username, password, client_name, server_name, domain='', use_ntlm_v2=True)

    try:
        # 连接到SMB服务器
        conn.connect(server_ip, 445)
        print("连接成功")

        # 删除文件
        # 注意：file_path 应该是共享文件夹内的相对路径，例如 'folder/subfolder/file.txt'
        # 注意路径分隔符，有时需要是 '\\' 而不是 '/'
        delete_directory_files(conn, share_name, file_path, 30)
    finally:
        # 关闭连接
        conn.close()


def clean_up(username, password, client_name, server_name, server_ip, share_name, file_path, clean_up_num):
    # 创建一个SMBConnection对象
    conn = SMBConnection(username, password, client_name, server_name, domain='', use_ntlm_v2=True)
    # 连接到SMB服务器
    try:
        conn.connect(server_ip, 445)
        list_filename = []
        # 列出共享文件夹中的文件和目录
        files_and_dirs = conn.listPath(share_name, file_path)  # 注意：路径分隔符可能因SMB服务器而异，有时是'\'，有时是'/'
        for file_info in files_and_dirs:
            list_filename.append(file_info.filename)
        while True:
            if len(list_filename) > clean_up_num + 2:
                min_result = 'EIS' + find_min_date_in_filenames(list_filename) + '000000'
                temp_min_result = file_path + '\\' + min_result
                delete_smb(username, password, client_name, server_name, server_ip, share_name, temp_min_result)
                delete_smb_Directory(username, password, client_name, server_name, server_ip, share_name,
                                     temp_min_result)
                list_filename.remove(min_result)
            else:
                break
    except Exception as e:
        print(f"clean_up()报错--连接或删除文件时出错: {e}")
    finally:
        conn.close()


# clean_up()传递的参数：登录用户名、密码、计算机名、服务器名、服务器地址、共享文件夹、路径、保留文件夹版本数量
clean_up('administrator', 'info@admin8813', 'CJ-IT1416', 'doc', '172.16.10.12',
         'Databackup', '\EIS8\D\DataBackup', 150)
