import allure

TEST_LINK = 'http://www.baidu.com'
@allure.testcase(TEST_LINK, 'testLink链接1')
@allure.feature("登陆模块")
class TestLogin:
    @allure.story("登陆成功")
    @allure.title("登陆成功测试用例")
    def test_login_succ(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")

        with allure.step("步骤1：打开应用"):
            print("输入账号密码，点击登陆")
        print("这是 登陆成功 测试用例")
        pass

    @allure.story("登陆失败")
    def test_login_faile(self):
        print("这是 登陆失败 测试用例")
        assert 1 == 2
        pass

@allure.testcase(TEST_LINK, 'testLink链接2')
@allure.feature("搜索模块")
class TestSearch:
    @allure.story("搜索成功")
    def test_search_succ(self):
        print("这是 搜索成功 测试用例")
        pass

    @allure.story("搜索失败")
    def test_search_faile(self):
        assert 1 == 2
        print("这是 搜索失败 测试用例")
        pass

    @allure.story("插入纯文本")
    def test_attach_text(self):
        allure.attach("纯文本", attachment_type=allure.attachment_type.TEXT)


    @allure.story("插入HTML")
    def test_attach_html(self):
        allure.attach("<body>一段HTML</body>", "HTML段", attachment_type=allure.attachment_type.HTML)

    @allure.story("插入图片")
    def test_attach_picture(self):
        allure.attach('C:/Users/qiulingfeng01/Desktop/测试上传文档/测试图片/e0074c086e061d950f0dca4a70f40ad162d9ca7b.jpg',
                      "图片", attachment_type=allure.attachment_type.JPG)

    @allure.story("插入视频")
    def test_attach_video(self):
        allure.attach("D:/BaiduNetdiskDownload/02 Linux与Bash课程 √/1 Linux系统与Shell环境准备.ts", "视频", attachment_type=allure.attachment_type.TSV)