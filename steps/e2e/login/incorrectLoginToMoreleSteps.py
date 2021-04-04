import logging

from behave import step
from hamcrest import assert_that

from resources.pageObjects.pages import PagesType
from resources.testData.credentials import incorrect_login

logger = logging.getLogger('incorrectLoginSteps')


@step('I am on morele.net login page')
def step_impl(context: PagesType):
    context.pages.login_page.open()


@step('I enter wrong credentials')
def step_impl(context: PagesType):
    context.pages.login_page.login_as(**incorrect_login)


@step('I am not logged in')
def step_impl(context: PagesType):
    assert_that(context.pages.login_page.is_login_failed())
