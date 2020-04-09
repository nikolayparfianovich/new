from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://development.vyble.io")
driver.maximize_window()
driver.find_element_by_id("login-form-email").send_keys("1234@gmail.com")
driver.find_element_by_id("login-form-password").send_keys("asdfghj")
driver.find_element_by_xpath("//button/span[text()='Login']").click()
driver.implicitly_wait(3)
x = driver.find_element_by_xpath("//strong[contains(text(),'The given E-Mail Address was not found.')]")
if x != 'gjgjgjgjg':
    driver.quit()





















