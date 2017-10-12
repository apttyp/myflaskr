# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
# from test_case import test_baidu
# from test_case import test_youdao
import test_baidu
import test_youdao

#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)