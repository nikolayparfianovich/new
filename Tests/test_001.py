from selenium import webdriver
import pytest
from Pages.Home_page import Home_page
from Pages.Login import login
from Pages.Company_management import Company

class Test():
    @pytest.fixture()
    def setup(self):
        driver=self.driver
        driver = webdriver.Chrome()
        driver.get("https://development.vyble.io")
        driver.maximize_window()
        login = login(driver)
        login.enter_email("nikolay.parfianovich@innowise-group.com")
        login.enter_password("Sasanchez1+")
        login.click_login()
        yield
        driver.close()
        driver.quit()

    def test_01(self,setup):
        self.driver.implicitly_wait(6)
        x = self.driver.find_element_by_xpath("//span[text()='<5']").text
        assert x=="<5"

    def test_02(self,setup):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//a[@data-for='Company']").click()
        self.driver.find_element_by_xpath("//div/span[text()='Operating Sites']").click()
        self.driver.find_element_by_xpath("//div[text()='holiday']/parent::div/parent::div/following-sibling::div").click()
        self.driver.find_element_by_xpath("//button/span[text()='Delete']").click()
        x=self.driver.find_element_by_xpath("//div/h2[text()='Löschen nicht möglich']").text
        assert x == "Löschen nicht möglich"
        print("Говнарь")










