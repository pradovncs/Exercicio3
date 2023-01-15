from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.ActionsPage import ActionsPage
from selenium import webdriver
from time import sleep


service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_chrome)
driver.maximize_window()

action_page = ActionsPage(driver, url="https://demo.automationtesting.in/Windows.html")
action_page.open()
action_page.click_main_page()
action_page.switch_tab(1)
print(action_page.extract_text_from_selenium_page())
action_page.close_tab()
action_page.switch_tab(0)
action_page.move_to_new_separate_windows()
action_page.click_new_separate_windows()
action_page.switch_tab(1)
print(action_page.extract_text_from_selenium_page())
action_page.close_tab()

sleep(5)
