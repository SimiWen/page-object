""" 百度页面
"""
from base.page import PageObject


class BaiDuPage(PageObject):
    def __init__(self, driver):
        super(BaiDuPage, self).__init__(driver)
        self.url = 'http://www.baidu.com'
        self.locators.update({
            '搜索框': 'name=wd',
            '百度一下': 'id=su',
            '搜索总数': 'class=nums_text'
        })
