# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#!!================================================================
#文 件 名：                 MineTest.py
#文件说明：                 首页 - 我的测试。
#作    者：                 li.hao85
#生成日期：                 2024-10-29
#!!================================================================
"""

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium.action.host.host import check_equal, check_not_equal, check_greater

from aw.Utils import check_if_title_bar_exist, get_title_bar_text


class MineTest(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()

    def setup(self):
        Step("回到桌面")
        self.driver.swipe_to_home()

    def process(self):
        CheckPoint("这项测试仅在初始状态下才能测一次")
        Step("【1】启动应用")
        self.driver.start_app(
            package_name="com.lihao.cookbook",
            page_name="EntryAbility")
        Step("【2】标题栏切换")
        # TabBar是否存在？
        self.driver.wait(1)
        self.driver.check_component_exist(BY.text("我的"))
        # 是否能切换至对应标签页？
        tab_bar_item = self.driver.find_component(BY.text("我的"))
        tab_bar_item.click()
        self.driver.wait(1)
        check_if_title_bar_exist(self.driver)
        title = get_title_bar_text(self.driver)
        check_equal(title, "我的")
        Step("【3】每日养生测试")
        self.driver.wait(1)
        self.driver.check_component_exist(BY.text("每日养生"))
        self.driver.check_component_exist(BY.id("todayTips"))
        today_tips = self.driver.find_component(BY.id("todayTips"))
        title = today_tips.getText()
        check_not_equal(title, None)
        title_length = len(title)
        check_greater(title_length, 0)
        CheckPoint("这项测试需要联网获取每日养生信息才能通过")
        Step("【4】应用首页点击测试")
        self.driver.wait(1)
        first_page_grid_item = self.driver.find_all_components(BY.type("GridItem"), 0)
        check_not_equal(first_page_grid_item, None)
        old_config = self.driver.find_all_components(BY.text("头条"))
        check_not_equal(old_config, None)
        old_config_length = len(old_config)
        check_equal(old_config_length, 2)
        first_page_grid_item.click()
        self.driver.wait(1)
        new_config = self.driver.find_all_components(BY.text("头条"))
        new_config_length = len(new_config)
        check_not_equal(new_config_length, None)
        check_equal(new_config_length, 1)
        Step("【5】字号设置功能点击测试")
        self.driver.wait(1)
        second_page_grid_item = self.driver.find_all_components(BY.type("GridItem"), 1)
        check_not_equal(second_page_grid_item, None)
        old_config = self.driver.find_all_components(BY.text("小"))
        check_not_equal(old_config, None)
        old_config_length = len(old_config)
        check_equal(old_config_length, 2)
        second_page_grid_item.click()
        self.driver.wait(1)
        new_config = self.driver.find_all_components(BY.text("小"))
        check_equal(new_config, None)
        Step("【6】分屏设置功能点击测试")
        self.driver.wait(1)
        third_page_grid_item = self.driver.find_all_components(BY.type("GridItem"), 2)
        check_not_equal(third_page_grid_item, None)
        old_config = self.driver.find_all_components(BY.text("关闭"))
        check_not_equal(old_config, None)
        old_config_length = len(old_config)
        check_greater(old_config_length, 0)
        third_page_grid_item.click()
        self.driver.wait(1)
        new_config = self.driver.find_all_components(BY.text("打开"))
        new_config_length = len(new_config)
        check_not_equal(new_config_length, None)
        check_greater(new_config_length, 0)
        Step("【7】跳转至菜谱收藏夹功能点击测试")
        self.driver.wait(1)
        last_page_grid_item = self.driver.find_all_components(BY.type("GridItem"), 3)
        check_not_equal(last_page_grid_item, None)
        last_page_grid_item.click()
        self.driver.wait(1)
        check_if_title_bar_exist(self.driver)
        title = get_title_bar_text(self.driver)
        check_equal(title, "菜谱")

    def teardown(self):
        Step("关闭设置应用")
        self.driver.stop_app("com.lihao.cookbook")