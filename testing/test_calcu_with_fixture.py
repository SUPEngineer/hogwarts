# @Time : 2021/2/10 16:01 
# @Author : qiulingfeng
# @File : test_calcu_with_fixture.py
import pytest


class TestCal:

    def test_add(self, get_instance, get_addDatas_with_fixture):
        f = get_addDatas_with_fixture
        assert get_instance.add(f[0], f[1]) == f[2]

    def test_div(self, get_instance, get_divDatas_with_fixture):
        f = get_divDatas_with_fixture
        assert get_instance.div(f[0], f[1]) == f[2]

    def test_div_erro(self, get_instance, get_div_erro_Datas_with_fixture):
        f = get_div_erro_Datas_with_fixture
        with pytest.raises(ZeroDivisionError):
            return get_instance.div(f[0], f[1])
