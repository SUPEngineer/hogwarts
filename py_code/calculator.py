# 计算器
class Caculator:
    def add(self, a, b):
        # 保留三为小数
        return round(a + b, 3)

    def div(self, a, b):
        if b == 0:
            return "除数为0"
        return a / b
