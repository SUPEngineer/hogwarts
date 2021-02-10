# @Time : 2021/2/10 16:01 
# @Author : qiulingfeng
# @File : test_calcu_with_fixture.py
import pytest
import yaml

from py_code.calculator import Caculator


def get_datas():
    with open("./datas/calc.yml") as f:
        ya = yaml.safe_load(f)
        return (ya['add']['datas'], ya['add']['ids'],
                ya['div']['normal']['datas'], ya['div']['normal']['ids'],
                ya['div']['error']['datas'], ya['div']['error']['ids'])


def get_test_param():
    test_datas = get_datas()
    return test_datas


# 初始化计算器对象等准备工作
@pytest.fixture()
def get_instance():
    print("star calculate")
    calc = Caculator()
    yield calc
    print("end calculate")


# 使用fixture传入数据
@pytest.fixture(params=get_test_param()[0], ids=get_test_param()[1])
def get_addDatas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_test_param()[2], ids=get_test_param()[3])
def get_divDatas_with_fixture(request):
    return request.param

@pytest.fixture(params=get_test_param()[4], ids=get_test_param()[5])
def get_div_erro_Datas_with_fixture(request):
    return request.param


# def test_fixture_param(get_addDatas_with_fixture):
#     print(get_addDatas_with_fixture)


class TestCal:
    # def setup_class(self):
    #     self.calc = Caculator()

    # def setup(self):
    #     print("开始计算")

    # def teardown(self):
    #     print("计算结束")

    def test_add(self, get_instance, get_addDatas_with_fixture):
        f = get_addDatas_with_fixture
        assert get_instance.add(f[0], f[1]) == f[2]

    def test_div(self, get_instance, get_divDatas_with_fixture):
        f = get_divDatas_with_fixture
        assert get_instance.div(f[0], f[1]) == f[2]

    def test_div(self, get_instance, get_div_erro_Datas_with_fixture):
        f = get_div_erro_Datas_with_fixture
        with pytest.raises(ZeroDivisionError):
            return get_instance.div(f[0], f[1])
