from selenium import webdriver

driver = webdriver.Chrome("D://Tuhin_Backup//software_//automation_//selenium webdriver tools//chromedriver_win32//chromedriver.exe")

driver.get("https://www.seleniumhq.org")

element = driver.find_element_by_xpath('//table[@id="choice"]/tbody/tr/td[1]//a[1]/img')

element.click()

driver.back()

search_element = driver.find_element_by_id("q")

search_element.send_keys("webdriver")

go_button = driver.find_element_by_id("submit")

go_button.click()

import time
time.sleep(1)

driver.switch_to.frame("master-1")

link_elements = driver.find_elements_by_tag_name("a")

print(link_elements[0].get_attribute("href"))