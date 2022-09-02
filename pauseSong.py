import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def pauseSong(driver, musicWindow):
    originalMeetWindow=driver.current_window_handle
    driver.switch_to.window(musicWindow)
    driver.implicitly_wait(3000)
    driver.find_element(By.ID, 'play-pause-button').click()
    driver.implicitly_wait(3000)
    driver.switch_to.window(originalMeetWindow)
    driver.implicitly_wait(3000)
