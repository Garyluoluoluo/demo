import sys
import unittest 
import LoginPage
from selenium import webdriver
import HTMLTestRunner
import time

class CaseloginGC(unittest.TestCase):
    """
    登录GC账号
     """
  
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        self.url ="https://connect.garmin.cn/modern/activities"
        self.username =""    ###账号
        self.password =""    ###密码

    #用例执行体
    def test_login_mail(self):
        #声明LoginPage类对象
        login_page =LoginPage.LoginPage(self.driver, self.url, u"Garmin Connect: Sign In")

        #调用打开页面组件
        login_page.open()
        #调用用户名输入组件
        login_page.switch_iframe()

        login_page.input_username(self.username)
        #调用密码输入组件
        login_page.input_password(self.password)
        #调用点击登录按钮组件
        login_page.click_submit()

    def tearDown(self):
        #self.driver.quit()
        pass


if __name__ =="__main__":
    # suite_1 = unittest.TestLoader().loadTestsFromTestCase(Caselogin126mail)
    # suite_2 = unittest.TestLoader().loadTestsFromTestCase(Caselogin126mail)
    # suite = unittest.TestSuite([suite_1,suite_2])
    # filename = "test.html"
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = '登陆126测试',description = '测试登陆过程')

    # runner.run(suite)
    unittest.main()
