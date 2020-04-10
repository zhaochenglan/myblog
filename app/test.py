# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/04/07 14:25:57
@Author  :   edgar.zhao 
@Version :   1.0
@Contact :   1101017794@qq.com
@Desc    :   None
'''

# here put the import lib


class test(object):
    def __init__(self):
        self.name = "edgar"

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with test() as e:
    print(1)
