# netguru-task-2
# Python selenium Framework for Automated Tests

#### Recommended python:
    3.7
    
#### Required pip packages:

    behave - gherkin
    selenium - browser automation
    pyhamcrest - more detailed assertions
    requests - api request automation
    python-dotenv - parsing .env file
    pylint - static code analyser

#### Running tests

Application is fully dockerized, there are 2 containers, first with python and behave service and second selenium/standalone-chrome.
The second one could be replaced with any other webdrivers.

First make a docker-compose build:
  
   docker-compose -f docker-compose.dev.yml build

Then set it up:
   
   docker-compose -f docker-compose.dev.yml up

and connect to localhost to watch the tests (on Mac ScreenSharing e.g. )

Docker starts by default with ports
- 4444:4444
- 5900:5900

It can be simply changed in docker-compose.dev.yml and docker-compose.yml files

The project can be run in the local environment. See Environment variables line 127.

###IMPORTANT###
If this is the first time you want to run the tests make sure you create a .env file next to .env.dist and copy its content.
.env.dist and .env files are included in the project. If for some reason they are not please add them under the project with following lines:

.env.dist

E2E_URL='https://'

SCREEN_WIDTH=1350

SCREEN_HEIGHT=950

.env

E2E_URL=''

TARGET = docker

SCREEN_WIDTH=1350

SCREEN_HEIGHT=950

To run tests with docker use this command

    docker-compose run --rm app behave --no-capture --no-skip --tags @successful features 
    
#### Code quality

You should run pylint on your code you can do this with the following command (in the main project directory)

    pylint --errors-only */*.py

# Documentation:

## 1. Structure

### Elements
This is where you create page elements and define their specific actions.
BaseElement is already created and contains actions available for all elements i.e. click, setValue, isElementVisible
It also makes sure that all the basic actions are properly handled in terms of stability

It also contains wait_for_page_load private method that can wait for various technologies to load for page (angular,jquery etc)

In order to define new element add new file with the element class and make sure you inherit the BaseClass (either
directly or indirectly through other element)

In example if we have Datepicker element we should create a new class inheriting from BaseElement and add method like:
setDate(date) which will accept date and handle all selectors and logic which enables a clean interface
Same for dropdown and i.e. method setOption()

Then you create elements in page objects as i.e. password = new TextField(...)

You can also specify locators(i.e. xpaths) with parameters like .//div[contains(@class,'this') and text()='{}']
and then easily set the element parameter with set_locator_parameters method
i.e. table_row_with_text = '//table/tr[text()='{}]'', later table_row_with_text.set_parameters(offer_name).click()

### Page Objects
[Quick introduction to Page Object Pattern](https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests)

Basically each page in the application should have a corresponding page object i.e. LoginPage, HomePage.

Obviously if we have 10.000 products and each has its own page we will create just 1 page object to represent it

loginPage.py is a good example of how a simple page could look like

Each page object should contain elements and actions connected with the page it represents so they can be used in Steps.

If there are some elements/actions shared among all pages / some pages it is recommended to use them i.e.

                      Base Page (i.e. app-wide notifications, popups etc)

    LoginPage RegisterPage HomePage             ProductPage

                                 ProductType1Page ProductType2Page ...

New Page Objects should be added to pages.py file and can be acessed through context.pages.PAGE_NAME

### Steps
Those files contain definitions of Gherkin steps.

They should be split according to some criterium(i.e. bussiness) in order to avoid big files with many steps

IMPORTANT:[Context](https://pythonhosted.org/behave/context_attributes.html) behave-specific object that contains info
through the whole test run (if we want to reuse variables in next steps we should define them in Context)

### Features
Contain scenarios written in Gherkin language - [behave gherkin documentation](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language)

### Environment.py file
This file contains behave hooks like before_all, after_scenario etc where we can define various behaviour that we want
to occurr for example after each scenario or before the whole suite.

[Environmental controls](http://pythonhosted.org/behave/tutorial.html#environmental-controls)

Some environment variables can be exported to the docker container (or your PyCharm Run Config) so that all tests can 
run however most have sensible defaults

Environment variables:
- TARGET target browser for testing, see utilities/browserCapabilites.py for available browsers and OS. 
Use the default value 'local' to run against a locally available Chromedriver (in localhost, Docker, Openshift, etc)

Default: docker
