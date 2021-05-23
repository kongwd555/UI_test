'''定义一个函数'''

def fun(x,y,z):
    if x>1 and y==0:
        z=z+x
    if x==2 or z>1:
        z+=1
    print(z)
    return z

import unittest
class FunTest(unittest.TestCase):
    @classmethod    #装饰器
    def setUpClass(cls):   #类的初始化方法
        print("世纪高通")
    '''
    (1)测试用例一：x=2、y=0、z=3
    '''
    def setUp(self):   #测试用例的初始化方法
        print("开始执行测试")
    def test1_shid(self):
        print("测试用例1")
        val=fun(2,0,3)
        self.assertEqual(6,val,msg="你错了")
    '''
    (2)测试用例二：x=2、y=0、z=1
    '''
    def test2_wehkd(self):
        print("测试用例2")
        val=fun(2, 0, 1)
        self.assertEqual(4,val)
    '''
    (3)测试用例三：x=0、y=1、z=0
    '''
    def test3_fekash(self):
        print("测试用例3")
        fun(0, 1, 0)
    '''
    (4)测试用例四：x=2、y=1、z=3
    '''
    def test4_rewfsd(self):
        print("测试用例4")
        fun(2, 1, 3)

    def tearDown(self):
        print("结束测试")
    @classmethod
    def tearDownClass(cls):
        print("牛转钱坤")
if __name__ == '__main__':
    #执行方法一
    # unittest.main()
    #执行方法二
    suite=unittest.TestSuite()
    suite.addTest(FunTest("test2_wehkd"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
    #执行方法三
    
