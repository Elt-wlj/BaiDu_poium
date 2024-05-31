import pytest, time
from page.baidupage import BaiduPage


class TestSearch():
    def test_baidupage(self, browser, base_url):
        page = BaiduPage(browser)
        page.open(base_url)
        # page.get(base_url)
        page.search_input.send_keys("python")

        page.search_button.click()
        time.sleep(3)
        assert browser.title == 'python_百度搜索'
