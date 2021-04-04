from resources.pageObjects import basePage
from resources.pageObjects.morele import loginToMorelePage


class Pages:
    base_page = None  # type: basePage.BasePage
    login_page = None  # type: loginToMorelePage.LoginPage


    def __init__(self, context):
        self.base_page = basePage.BasePage(context)
        self.login_page = loginToMorelePage.LoginPage(context)


class PagesType:
    pages: Pages