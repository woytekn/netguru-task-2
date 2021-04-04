class ExpectedConditionJavascript(object):
    """An expectation for checking that a javascript hah been usn

    locator - used to find the element to run the script against
    returns the WebElement once the script has run
    """

    def __init__(self, locator, script):
        # TODO not sure if element locator could be optional here
        self.locator = locator
        self.script = script

    def __call__(self, driver):
        element = driver.find_element(*self.locator)  # Finding the referenced element
        if driver.execute_script(self.script, element):
            return element
        else:
            return False
