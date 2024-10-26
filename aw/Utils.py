from hypium import *

def get_app_version_code(driver: UiDriver, bundle: str) -> int:
    info = driver.shell('bm dump -n {} |grep versionCode'.format(bundle))
    if 'versionCode' not in info:
        return 0
    token = info.splitlines()[-1]
    code_str = token.replace('"versionCode":', '').replace(',', '').strip()
    return int(code_str)

def check_if_title_bar_exist(driver: UiDriver):
    driver.check_component_exist(BY.id("LHCommonTitleBar_title"))

def get_title_bar_text(driver: UiDriver) -> str:
    title_bar = driver.find_component(BY.id("LHCommonTitleBar_title"))
    title = title_bar.getText()
    return title