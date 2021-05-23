'''
测试用例：
1、添加数据源
2、查看数据源
3、删除数据源
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from script.test_login import *

#继承类来实现
class SandData():
    def __init__(self,driver):
        self.driver=driver
    def test_adddata(self):
        #2、点击添加数据源
        # driver.find_element_by_class_name("mo-btn-info").click()
        # driver.find_element_by_xpath('//div[@class="mo-btn-info"]').click()
        self.driver.find_element_by_css_selector('div.mo-btn-info').click()
        #3、选择数据源
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@name="radiogroup" and @value="shapefile"]').click()
        #4、下一步
        self.driver.find_element_by_css_selector('div.datasource-step1-footer>div.mo-btn-info').click()
        #5、选择沙盒
        select=self.driver.find_element_by_css_selector('div.ant-select-selection__placeholder')
        ActionChains(self.driver).click(select).send_keys(Keys.ENTER).perform()
        #6、填写数据源名称
        self.driver.find_element_by_id("datasourcename").send_keys("hello")
        #7、上传方式
        self.driver.find_element_by_css_selector('.ant-radio-wrapper.ant-radio-wrapper-checked').click()
        #8、上传文件
        file="D:\测试任务\\01MineData@Earth\地理信息系统\\annotation_beijing.zip"
        self.driver.find_element_by_id('upload-file').send_keys(file)
        #9、点确定
        self.driver.find_element_by_css_selector('div.datasource-step2-footer>div.mo-btn-info').click()
        time.sleep(1)
        #显示等待
        WebDriverWait(self.driver,30,0.5).until(lambda x:x.find_element_by_css_selector('.ant-message'))
        message=self.driver.find_element_by_css_selector('.ant-message').text
        print(message)
        #断言
        #assert message=="新建数据源成功！"

if __name__ == '__main__':
    data=SandData()
    data.test_login()
    data.test_adddata()
