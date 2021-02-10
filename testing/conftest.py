# @Time : 2021/2/10 15:06 
# @Author : qiulingfeng
# @File : conftest.py

import datetime

import pytest


@pytest.fixture(scope='session')
def login():
    print("login")
    token = datetime.datetime.now()
    yield token
    print("logout")
