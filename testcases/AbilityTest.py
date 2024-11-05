# !/usr/bin/env python
# coding: utf-8
"""
#!!================================================================
#文 件 名：                 AbilityTest.py
#文件说明：                 应用启动测试。
#作    者：                 li.hao85
#生成日期：                 2024-10-25
#!!================================================================
"""

from devicetest.core.test_case import TestCase, Step
from hypium import *


class AbilityTest(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)

    def setup(self):
        Step("1.回到桌面")
        self.driver.swipe_to_home()

    def process(self):
        Step("2.启动设置应用")
        self.driver.start_app(
            package_name="com.lihao.cookbook",
            page_name="EntryAbility")

    def teardown(self):
        Step("3.关闭设置应用")
        self.driver.stop_app("com.lihao.cookbook")
