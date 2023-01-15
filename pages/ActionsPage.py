from Exercicio3.locators.locators import *
from Exercicio3.pages.BasePage import PageElement


class ActionsPage(PageElement):

    def click_main_page(self) -> None:
        """
        Click on button located at main page.

        :return: None.
        """
        self.do_click(PageLocators.btn_click_tabbed_windows_page)

    def move_to_new_separate_windows(self) -> None:
        """
        Click on button "Open New Separate Windows".

        :return: None.
        """
        self.do_click(PageLocators.btn_move_to_new_separate_windows)

    def click_new_separate_windows(self) -> None:
        """
        Click on button located on "Open new Separate Windows".

        :return: None.
        """
        self.do_click(PageLocators.btn_click_new_separate_windows)

    def extract_text_from_selenium_page(self) -> str:
        """
        Extract text from banner on selenium page.("
        Selenium automates browsers. That's it!").

        :return: str.
        """
        banner = self.get_text_to_element(PageLocators.selenium_banner_page)

        return banner

    def switch_tab(self, index_page: int) -> None:
        """
        Switch to selenium tab.

        :return: None.
        """
        self.driver.switch_to.window(self.driver.window_handles[index_page])
        return None

    def close_tab(self) -> None:
        """
        Close the current open tab.

        :return: None.
        """
        self.driver.close()
        return None

    def get_title_of_page(self) -> str:
        """
        Get the title of current page.

        :return: str.
        """
        title = self.driver.title
        return title
