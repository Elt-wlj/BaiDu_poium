from poium import Page, Element,Elements


class BaiduPage(Page):
    search_input = Element(id_='kw', describe="搜索输入框")
    search_button = Element(id_='su', describe="搜索按钮")


