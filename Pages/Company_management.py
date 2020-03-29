class Company():
    def __init__(self, driver):
        self.driver=driver

        self.section_company="//a[@data-for='Company']"
        self.select_operating_site_xpath="//div/span[text()='Operating Sites']"
        self.choosing_holiday_xpath="//div[text()='holiday']/parent::div/parent::div/following-sibling::div"
        self.click_delete_button_xpath="//button/span[text()='Delete']"
        self.title_xpath="//div/h2[text()='Löschen nicht möglich']"

    def company(self):
        self.driver.find_element_by_xpath(self.section_company).click()

    def selection_operating_sites(self):
        self.driver.find_element_by_xpath(self.select_operating_site_xpath).click()

    def choose_holiday_op(self):
        self.driver.find_element_by_xpath(self.choosing_holiday_xpath).click()

    def click_del_button(self):
        self.driver.find_element_by_xpath(self.click_delete_button_xpath)

    def title_verification(self,value):
        x = self.driver.find_element_by_xpath(self.title_xpath).text
        assert x==value







