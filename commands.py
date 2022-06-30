from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def commands(driver):
    driver=driver
    # Open chat box
    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("c")\
        .key_up(Keys.SHIFT)\
        .perform()

    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="usermsg"]').send_keys("Hi! I'm Music bot. Use '/help' to read all my commands" + Keys.ENTER)
    driver.implicitly_wait(3)
    print("Introduced in chat")
   