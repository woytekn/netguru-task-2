import datetime
import logging
import os

from dotenv import load_dotenv
from selenium import webdriver

from resources.pageObjects import pages
from resources.utilities import browserCapabilities
from resources.utilities.logger import Logger

logging.basicConfig(
    filename='logs/logs-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + '.txt',
    level=logging.INFO,
    format="[%(levelname)-8s %(asctime)s] %(message)s"
)


def before_all(context):
    context.logger = Logger(context)
    context.logger.logger = logging.getLogger(__name__)
    load_dotenv('.env')

    context.selenium_hub_url = os.getenv('SELENIUM_HUB_URL', 'http://localhost:4444/wd/hub')
    # Grabs the selenium hub URL from environment variable
    # defaults to localhost if not set

    context.email_password = os.getenv('EMAIL_PASSWORD')

    context.build_name = os.getenv('BUILD_TAG')
    # String of "jenkins-${JOB_NAME}-${BUILD_NUMBER}". All forward slashes ("/") in the JOB_NAME are replaced with
    # dashes ("-"). Convenient to put into a resource file, a jar file, etc for easier identification.

    if not context.build_name:
        # Then this is not a Jenkins build
        user = os.getenv('USER')  # Gets your username from the OS
        target_name = os.getenv('TARGET')
        timestamp = datetime.datetime.now().strftime("%y-%m-%d %H_%M_%S")
        context.build_name = f'{target_name}: {user} {timestamp}'


def before_feature(context, feature):
    context.feature_tags = feature.tags


def before_scenario(context, scenario):
    context.logger.current_scenario = scenario.name
    context.scenario_tags = scenario.tags

    if 'api' not in scenario.tags + context.feature_tags:
        # Think about moving WebDriver setup to before_all() and reusing the session
        target_name = os.getenv('TARGET')

        if not target_name or target_name == 'default':
            target_name = 'chrome_latest'  # let Chrome be the default

        if target_name == 'docker':
            opt = webdriver.ChromeOptions()
            desired_capabilities = opt.to_capabilities()
            opt.add_argument("--window-size=1300,1065")

            context.browser = webdriver.Remote(command_executor=context.selenium_hub_url,
                                               desired_capabilities=desired_capabilities)
        elif not target_name == 'local':
            try:
                desired_capabilities = browserCapabilities.browsers[target_name]
            except KeyError:
                print(f'The target browser {target_name} is not configured. '
                    f'You could add it to browserCapabilities.py')
                exit(1)

            desired_capabilities['bstack:options']['projectName'] = 'python_testing_framework'
            desired_capabilities['bstack:options']['buildName'] = context.build_name
            desired_capabilities['bstack:options']['sessionName'] = context.feature.name + ': ' + context.scenario.name

            context.browser = webdriver.Remote(command_executor=context.selenium_hub_url,
                                               desired_capabilities=desired_capabilities)

            # local Chrome
            opt = webdriver.ChromeOptions()
            # opt.add_experimental_option('w3c', False)
            opt.add_argument("--window-size=1920,1080")
            desired_capabilities = opt.to_capabilities()
            if os.name == 'posix':
                # chromedriver executable can be found here on OSX if you installed it using Homebrew
                context.browser = webdriver.Chrome(chrome_options=opt,
                                                   executable_path='/usr/local/bin/chromedriver')
            else:
                # chromedriver executable can be found here on RDP 22 and 23, YMMV
                context.browser = webdriver.Chrome(chrome_options=opt,
                                                   executable_path="D:/webdrivers/chromedriver.exe")

        context.pages = pages.Pages(context)


def before_step(context, step):
    context.logger.current_step = step.name


def after_scenario(context, scenario):
    if 'api' not in scenario.tags + context.feature_tags:
        context.logger.info('Closing browser')
        context.browser.quit()


def after_step(context, step):
    if step.status == 'failed' and 'api' not in context.scenario_tags + context.feature_tags:
        context.logger.debug('Taking screenshot of failed step')
        now = datetime.datetime.now()
        context.browser.save_screenshot(
            os.getcwd() + "/screenshots/" + now.strftime("%Y-%m-%d-%H-%M-") + context.scenario.name.replace(" ",
                                                                                                            "-") + ':' + step.name.replace(
                " ", "-") + ".png"
            # TODO refactor this ^^  - IAT-104
        )


def after_all(context):
    pass
