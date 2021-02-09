# 测试计算器
# 测试用例
import sys
sys.path.append('../')
from py_code.calculator import Caculator


class TestCal:
    def test_add(self):
        calc = Caculator()
        assert calc.add(1, 1) == 2
