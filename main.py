import math
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element_by_css_selector('#book').click()
    # # browser.execute_script("window.scrollBy(0, 100);")
    # time.sleep(10)
    # x_element = browser.find_element_by_css_selector("#input_value")
    # x = x_element.text
    # y = calc(x)
    # browser.find_element_by_css_selector("#answer").send_keys(y)
    # button1 = browser.find_element_by_css_selector("#solve")
    # button1.click()

finally:
    time.sleep(20)
    browser.quit()