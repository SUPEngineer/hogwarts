import unittest

from util.HTMLTestRunner_PY3 import HTMLTestRunner


class TestStringMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown\n")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_a(self):
        self.assertEqual(1, 2, "1==1?")

if __name__ == '__main__':
    # unittest.main()
    #创建测试套件
    suite = unittest.TestSuite()
    #添加测试用例到套件
    suite.addTest(TestStringMethod("test_a"))
    #执行套件
    # unittest.TextTestRunner.run(suite)

    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)


