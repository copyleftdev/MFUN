from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://qasf.efax.co.uk/faq")
ele = driver.find_element_by_id('makeFaxSuccess')
ele.click()
