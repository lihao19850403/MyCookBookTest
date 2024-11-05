# !/usr/bin/env python
# coding: utf-8
"""
#!!================================================================
#文 件 名：                 NewsTest.py
#文件说明：                 首页 - 头条测试。
#作    者：                 li.hao85
#生成日期：                 2024-10-25
#!!================================================================
"""

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *

from testcases.utils.TitleBarTextUtils import check_title_bar_text_is


class NewsTest(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()

    def setup(self):
        Step("回到桌面")
        self.driver.swipe_to_home()

    def process(self):
        Step("【1】启动应用")
        self.driver.start_app(
            package_name="com.lihao.cookbook",
            page_name="EntryAbility")
        Step("【2】标题栏切换")
        # TabBar是否存在？
        self.driver.wait(1)
        self.driver.check_component_exist(BY.text("头条"))
        # 否能切换至对应标签页？
        tab_bar_item = self.driver.find_component(BY.text("头条"))
        tab_bar_item.click()
        self.driver.wait(1)
        check_title_bar_text_is(self.driver, "头条")
        Step("【3】列表点击测试")
        # 是否加载出了新闻内容？
        self.driver.wait(1)
        self.driver.check_component_exist(BY.type("WaterFlow"))
        CheckPoint("这项测试需要联网获取新闻列表后才能继续")
        # 是否能跳转至新闻详情？
        self.driver.wait(1)
        self.driver.check_component_exist(BY.id("NewsTipsCard0"))
        news_tips_card = self.driver.find_component(BY.id("NewsTipsCard0"))
        news_tips_card.click()
        self.driver.wait(1)
        check_title_bar_text_is(self.driver, "新闻")
        # 是否能跳转至浏览器页？
        self.driver.check_component_exist(BY.id("news_link"))
        news_link = self.driver.find_component(BY.id("news_link"))
        news_link.click()
        self.driver.wait(1)
        check_title_bar_text_is(self.driver, "浏览器")
        # 返回首页。
        self.driver.press_back()
        self.driver.press_back()

    def teardown(self):
        Step("关闭设置应用")
        self.driver.stop_app("com.lihao.cookbook")
