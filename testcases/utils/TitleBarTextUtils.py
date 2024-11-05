from hypium import *
from hypium.action.host.host import check_not_equal, check_equal


def find_common_title_bar_text(driver: UiDriver):
    """
    查找标题栏文字组件，先从Nav内容页找，再从主页上找。
    :param driver: 传入的driver参数。
    :return: 标题栏文字组件。
    """
    title_bar = driver.find_component(
        BY.xpath("//Navigation/NavigationContent/NavDestination/NavDestinationContent/Column/Stack/Text"))
    if title_bar is None:
        title_bar = driver.find_component(
            BY.xpath("//Navigation/NavBar/NavBarContent/Tabs/Swiper/TabContent/Column/Stack/Text"))
    return title_bar


def check_title_bar_text_is(driver: UiDriver, text: str):
    """
    检查标题栏文字区是否存在，并检查标题内容是否正确。
    :param driver: 传入的driver参数。
    :param text: 待检查的标题。
    """
    title_bar = find_common_title_bar_text(driver)
    check_not_equal(title_bar, None)
    title = title_bar.getText()
    check_equal(title, text)
