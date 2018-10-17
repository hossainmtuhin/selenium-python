from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("D://Tuhin_Backup//software_//automation_//selenium webdriver tools//chromedriver_win32//chromedriver.exe")

driver.get("https://google.com")

assert "Google" in driver.title

element = driver.find_element_by_name('q')

element.clear()

element.send_keys('test')

element.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source 

driver.close()