import time
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def test_login(self):
        path = r"C:\Users\ibm\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        self.driver=webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()

        self.driver.get("http://192.168.153.170/platform/home/login?from=/studio/asset/data/sandbox")
        self.driver.find_element_by_css_selector('[placeholder="用户名"]').send_keys("test_admin")
        self.driver.find_element_by_css_selector('[placeholder="密码"]').send_keys("123456")
        self.driver.find_element_by_class_name("login-btn").click()
        self.driver.switch_to.frame()
        time.sleep(1)
        name=self.driver.find_element_by_class_name("user-name").text
        print(name)
        if name=="test_admin":
            print("登录成功")
        else:
            print("登录失败")
        return self.driver
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

# if __name__ == '__main__':
#     loginObj=Login()
#     loginObj.test_login()
#     loginObj.closedriver()
