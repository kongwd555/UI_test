from script.test_login import *
from script.wwtest_SandBox import *
from script.edtest_adddata import *


if __name__ == '__main__':
    login=Login()
    chrome=login.test_login()   #登录

    sanbox=CreateSandBox(chrome)  #实例化沙盒类
    sanbox.test_createsandbox()  #新建沙盒

    data=SandData(chrome)#实例化数据源
    data.test_adddata() #添加数据源