def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("错误：不能被零除！")
        return None
    except TypeError:
        print("错误：输入必须是数字！")
        return None
    else:
        print(f"结果是: {result}")
        return result
    finally:
        print("执行完成。")

# 测试函数
divide_numbers(10, 2)  # 正常情况
divide_numbers(10, 0)  # 被零除的情况
divide_numbers(10, 'a')  # 输入类型错误
