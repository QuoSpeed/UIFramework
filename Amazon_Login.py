from selenium import webdriver #from selenium package
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]").click()
driver.find_element_by_name("email").send_keys("8217386760")
driver.find_element_by_id("continue").click()
driver.implicitly_wait(1)
driver.find_element_by_name("password").send_keys("Hari&sadu11")
driver.find_element_by_id("signInSubmit").click()
driver.implicitly_wait(2)
driver.find_element_by_id("twotabsearchtextbox").send_keys("mi note7")
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
driver.implicitly_wait(2)
