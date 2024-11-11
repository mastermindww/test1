from distutils.core import setup

setup(
    name='Release module',  # 包的名称
    version='1.0',  # 版本号
    author='mastermindww',  # 作者
    author_email='mastermindww@163.com',  # 作者邮箱
    description='完整的发送和接收消息模块',  # 简短描述
    long_description_content_type='完整的发送和接收消息模块',  # 描述的内容类型
    url='https://github.com/mastermindww/python',  # 项目主页
    py_modules=['send_receive_20241015.send_message',
                'send_receive_20241015.receive_message']
)
