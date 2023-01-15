from abc import ABC
from Exercicio3.locators.locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageElement(ABC):
    
    def __init__(self, driver, url: str = ""):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.url = url

    def find_element(self, locator: tuple, timeout: int = 15):
        """
        Find element present in the page.

        :param locator: tuple of locator the element.
        :param timeout: maximum element wait time.
        :return: element.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element

    def do_click(self, locator: tuple, timeout: int = 15) -> None:
        """
        Click on the element from the past locator.

        :param locator: tuple of locator the element.
        :param timeout: maximum element wait time.
        :return: None.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))
        return element.click()

    def get_text_to_element(self, locator: tuple, timeout: int = 15):
        """
        Get text of an element.

        :param locator: tuple of locator the element.
        :param timeout: maximum element wait time.
        :return: element.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = str(wait.until(ec.visibility_of_element_located(locator)).text)
        return element

    def open(self) -> None:
        """
        Open the page.
        :return: None.
        """
        self.driver.get(self.url)
        return None
