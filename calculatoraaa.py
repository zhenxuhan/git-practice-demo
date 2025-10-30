def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# calculator.py 新增错误代码
def divide(a, b):
    return a / b  # 错误：未处理 b=0 的情况

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b