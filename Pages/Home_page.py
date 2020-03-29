class Home_page():

    def __init__(self,driver):
        self.driver=driver

        self.number_xpath="//span[text()='<5']"

    def verification(self):
        x = self.driver.find_element_by_xpath(self.number_xpath).text
        assert x == "<5"




