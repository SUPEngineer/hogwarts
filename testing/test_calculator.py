import sys
import pytest
import yaml
from py_code.calculator import Caculator

sys.path.append('../')


# 测试计算器
# 测试用例

def get_datas():
    with open("./datas/calc.yml")as f:
        ya = yaml.safe_load(f)
        return (ya['add']['datas'], ya['add']['ids'],
                ya['div']['normal']['datas'], ya['div']['normal']['ids'],
                ya['div']['error']['datas'], ya['div']['error']['ids'])


class TestCal:
    test_datas: tuple = get_datas()

    def setup_class(self):
        self.calc = Caculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, result", test_datas[0], ids=test_datas[1])
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a, b, result", test_datas[2], ids=test_datas[3])
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result

    @pytest.mark.parametrize("a, b, result", test_datas[4], ids=test_datas[5])
    def test_erro_div(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            return a/b

