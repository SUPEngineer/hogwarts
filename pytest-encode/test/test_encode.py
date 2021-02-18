# @Time : 2021/2/18 10:41 
# @Author : qiulingfeng
# @File : test_encode.py
import pytest


@pytest.mark.parametrize('name', ['小明', '小李'])
def test_encode(name):
    print(name)
