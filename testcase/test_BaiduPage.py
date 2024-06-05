import pytest, time, allure
from page.baidupage import BaiduPage


class TestSearch():
    @allure.feature("搜索功能")
    def test_baidupage(self, browser, base_url):
        page = BaiduPage(browser)
        page.open(base_url)
        # page.get(base_url)
        page.search_input.send_keys("python")

        page.search_button.click()
        time.sleep(3)
        assert browser.title == 'python_百度搜索'
