'''
测试用例1：新建沙盒
1、点击新建沙盒
2、弹窗-填写沙盒名称
3、下拉列表选择vector
4、输入描述
5、点击确定
测试用例2：删除沙盒
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from script.test_login import *

class CreateSandBox():
    def __init__(self,driver):
        self.driver=driver
    def test_createsandbox(self):
        time.sleep(1)
        #2、开始创建沙盒
        self.driver.find_element_by_xpath('//div[@class="mo-hollow-btn-info"]').click()
        #3、输入沙盒名称
        self.driver.find_element_by_id('name').send_keys("autotest")
        #4、数据类型选择-下拉列表
        select=self.driver.find_element_by_class_name("ant-select-selection__rendered")
        ActionChains(self.driver).click(select).send_keys(Keys.ENTER).perform()
        #5、输入描述
        self.driver.find_element_by_id("description").send_keys("自动化测试")
        #6、点击确定
        self.driver.find_element_by_css_selector(".mo-btn-info.create-btn").click()
        #7、判断是否创建成功
        time.sleep(1)
        msg=self.driver.find_element_by_class_name("ant-message").text
        print(msg)
        if msg=="新建沙盒成功！":
            print("沙盒创建成功")
        else:
            print("沙盒创建失败")

    def test_cancelsandbox(self):
        '''下面执行删除沙盒'''
        #8、先找到要删除的沙盒
        boxnames=self.driver.find_elements_by_css_selector(".inner-name-box")
        index=0
        for boxname in boxnames:
            if boxname.text=="autotest":
                break
            index+=1
        print(index)
        #9、点击卡片，进入删除页面
        self.driver.find_elements_by_css_selector(".inner-name-box")[index].click()
        #10、点击删除按钮
        point=self.driver.find_element_by_class_name("inner-more-box")   #三个点
        cancle=self.driver.find_element_by_class_name("inner-pop-item")  #删除按钮
        ActionChains(self.driver).click(point).click(cancle).perform()  #删除动作
        #11、点击确定按钮
        time.sleep(1)
        self.driver.find_element_by_css_selector(".ant-btn.ant-btn-primary").click()
        time.sleep(1)
        message=self.driver.find_element_by_class_name("ant-message").text
        print(message)
        if message=="删除成功":
            print("沙盒删除成功")
        else:
            print("沙盒删除失败")

if __name__ == '__main__':
    #调用的方法来实现
    login=Login()
    chrome=login.test_login()  #登录

    sanbox=CreateSandBox(chrome)  #实例化沙盒类
    sanbox.test_createsandbox()  #新建沙盒
    sanbox.test_cancelsandbox()  #删除沙盒

    login.closedriver()  #关闭浏览器
