import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def helpCommand(driver):
    driver.find_element(By.XPATH, '//*[@id="usermsg"]').send_keys("/play <songName> - Plays a song." + Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="usermsg"]').send_keys("/pause - Pauses the song being played." + Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="usermsg"]').send_keys("/resume - Resumes playback of the song."  + Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="usermsg"]').send_keys("/exit - Quits the music bot." + Keys.ENTER)
    driver.implicitly_wait(3)
