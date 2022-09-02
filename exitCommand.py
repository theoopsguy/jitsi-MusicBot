import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def exitCommand(driver):
    driver.find_element(By.CLASS_NAME, 'hangup-button').click()
    driver.implicitly_wait(10)
    driver.quit()