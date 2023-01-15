from selenium.webdriver.common.by import By


class PageLocators(object):
    btn_click_tabbed_windows_page = (By.XPATH, '//*[@id="Tabbed"]/a/button')
    btn_move_to_new_separate_windows = (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
    btn_click_new_separate_windows = (By.XPATH, '//*[@id="Seperate"]/button')
    selenium_banner_page = (By.XPATH, '//*[@id="td-cover-block-0"]/div/div/div/div/h1')
