import unittest
from base import browser
from pages.baidu import BaiDuPage


class TestBaiDu(unittest.TestCase):

    def setUp(self):
        self.driver = browser.Chrome()
        self.page = BaiDuPage(self.driver).open()

    def tearDown(self):
        self.page.close()

    def test_search(self):
        self.page.element('搜索框').text = '测试'
        self.page.element('百度一下').click()
        self.page.element('搜索总数').wait_for_displayed()
        self.assertEqual('测试_百度搜索', self.page.title)


if __name__ == '__main__':
    unittest.main()