import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    path=r"D:\UI_test\script"
    #path="./"
    discover=unittest.defaultTestLoader.discover(path,"test_*.py")
    report=path+"\\"+"testreport.html"
    rep=open(report,"wb")
    runner=HTMLTestRunner(stream=rep,verbosity=1,title="自动化测试报告",description="接口自动化",tester="孔维东")
    runner.run(discover)
    rep.close()