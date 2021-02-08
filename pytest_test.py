import pytest
import allure

def func(a):
    return a + 1

class Test_demo:

    def test_1(self):
        assert func(1) == 2

    def test_2(self):
        assert func(2) == 4


