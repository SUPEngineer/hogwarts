# @Time : 2021/2/10 15:06 
# @Author : qiulingfeng
# @File : conftest.py

import datetime

import pytest
import yaml

from py_code.calculator import Caculator


@pytest.fixture(scope='session')
def login():
    print("login")
    token = datetime.datetime.now()
    yield token
    print("logout")


def get_datas():
    with open("./datas/calc.yml", encoding='utf-8') as f:
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
    print("start calculate")
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


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
