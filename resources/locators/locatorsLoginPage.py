from selenium.webdriver.common.by import By


class Locators:
    # --- login to morelePage locators ---
    LOGIN_USERNAME_INPUT = (By.XPATH, '//div/input[contains(@id,"username")]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//div/input[contains(@id,"password")]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(),"Zaloguj się")]')
    LOGIN_PAGE_ASSERTION = (By.XPATH, '//span[contains(text(),"Witaj")]')
    LOGIN_ERROR_MESSAGE_ITEM_PUSH = (By.XPATH, '//div[contains(@class,"mn-item mn-type-danger mn-item-push")]')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[contains(text(), "Dane logowania nie są poprawne. Zalogowanie nie powiodło się.")]')



