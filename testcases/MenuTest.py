# !/usr/bin/env python
# coding: utf-8
"""
#!!================================================================
#文 件 名：                 MenuTest.py
#文件说明：                 首页 - 菜谱测试。
#作    者：                 li.hao85
#生成日期：                 2024-10-25
#!!================================================================
"""

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import *
from hypium.action.host.host import check_equal, check_greater, check_not_equal
from hypium.model import UiParam

from testcases.utils.TitleBarTextUtils import check_title_bar_text_is, get_title_bar_text


class MenuTest(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()
        # 今日推荐消息标题横幅。
        self.recommend_menu_header_path: str = "//Navigation/NavBar/NavBarContent/Tabs/Swiper/TabContent/Column/List/ListItemGroup[1]/Row"
        # 推荐菜谱列表第一个五星。
        self.first_star_path: str = "//Navigation/NavigationContent/NavDestination/NavDestinationContent/Column/List/ListItem[1]/Stack/Row/Stack/Image"

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
        self.driver.check_component_exist(BY.text("菜谱"))
        # 是否能切换至对应标签页？
        tab_bar_item = self.driver.find_component(BY.text("菜谱"))
        tab_bar_item.click()
        self.driver.wait(1)
        check_title_bar_text_is(self.driver, "菜谱")
        Step("【3】推荐菜谱列表点击测试")
        # 推荐菜谱列表点击测试。
        self.driver.wait(1)
        grid = self.driver.find_all_components(BY.type("Grid"), 0)
        check_not_equal(grid, None)
        CheckPoint("这项测试需要联网获取推荐菜谱列表后才能继续")
        # 是否能跳转至推荐菜谱列表？
        self.driver.check_component_exist(BY.xpath(self.recommend_menu_header_path))
        self.test_add_favorite_menu(self.recommend_menu_header_path)
        page_list = self.driver.find_all_components(BY.type("List"), 0)
        check_not_equal(page_list, None)
        self.driver.swipe(UiParam.UP, 90, page_list)  # 列表向上滚动。
        grid = self.driver.find_all_components(BY.type("Grid"), 1)
        if grid is None:
            self.test_add_favorite_menu(self.recommend_menu_header_path)  # 如果取消收藏，则再加入一次。
        grid = self.driver.find_all_components(BY.type("Grid"), 1)
        check_not_equal(grid, None)
        Step("【4】菜谱收藏夹列表点击测试")
        self.driver.wait(1)
        # 是否加载出了菜谱内容？
        grid = self.driver.find_all_components(BY.type("Grid"), 1)
        check_not_equal(grid, None)
        # 是否能跳转至菜谱详情？
        menu_tips = self.driver.find_all_components(BY.type("GridItem"))
        if isinstance(menu_tips, list):
            menu_tips_length = len(menu_tips)
            check_greater(menu_tips_length, 0)
            last_favorite_menu_tips_card = menu_tips[menu_tips_length - 1]
        else:
            check_not_equal(menu_tips, None)
            last_favorite_menu_tips_card = menu_tips
        page_list = self.driver.find_all_components(BY.type("List"), 0)
        check_not_equal(page_list, None)
        self.driver.swipe(UiParam.UP, 90, page_list)  # 列表向上滚动。
        last_favorite_menu_tips_card.click()  # 单击最后一个列表组件。
        self.driver.wait(1)
        title = get_title_bar_text(self.driver)
        pure_title = title[0: 2]
        check_equal(pure_title, "家常")
        # 是否能跳转至图片阅览页？
        image = self.find_menu_detail_card_image()
        check_not_equal(image, None)
        image.click()
        self.driver.wait(1)
        self.driver.check_component_exist(BY.type("Image"))
        # 返回首页。
        self.driver.press_back()
        self.driver.press_back()

    def teardown(self):
        Step("关闭设置应用")
        self.driver.stop_app("com.lihao.cookbook")

    # 测试将菜谱加入收藏。
    def test_add_favorite_menu(self, header_type_str: str):
        recommend_menu_tips = self.driver.find_component(BY.xpath(header_type_str))
        recommend_menu_tips.click()
        self.driver.wait(1)
        title = get_title_bar_text(self.driver)
        pure_title = title[0: 4]
        check_equal(pure_title, "今日推荐")
        title_length = len(title)
        num_str = title[5: title_length - 1]
        recommend_menu_count = int(num_str)
        check_greater(recommend_menu_count, 0)
        # 是否能将菜谱加入收藏？
        star = self.driver.find_component(BY.xpath(self.first_star_path))
        check_not_equal(star, None)
        star.click()
        self.driver.wait(1)
        self.driver.press_back()  # 返回首页检查菜谱收藏结果。
        self.driver.wait(1)

    def find_menu_detail_card_image(self):
        # 菜谱详情页小图片(竖屏模式)。
        menu_detail_card_image_path = "//Navigation/NavigationContent/NavDestination/NavDestinationContent/Column/Scroll/Column/Image"
        image = self.driver.find_component(BY.xpath(menu_detail_card_image_path))
        if image is None:
            menu_detail_card_image_path = "//Navigation/NavigationContent/NavDestination/NavDestinationContent/Column/Scroll/Row/Image"
            image = self.driver.find_component(BY.xpath(menu_detail_card_image_path))
        return image