import logging

from behave import step
from hamcrest import assert_that

from resources.pageObjects.pages import PagesType
from resources.testData.credentials import correct_login

logger = logging.getLogger('loginToMoreleSteps')


@step('I enter login and password')
def step_impl(context: PagesType):
    context.pages.login_page.login_as(**correct_login)


@step('I can see login confirmation element on the page present')
def step_impl(context: PagesType):
    assert_that(context.pages.login_page.is_login_successful())