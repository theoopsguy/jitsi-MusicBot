import time
from selenium.webdriver.common.by import By

# Turn off audio and video
def turnMicCamOff(driver):
    driver=driver
    driver.find_element(By.XPATH, '//*[@id="new-toolbox"]/div/div/div/div[2]/div/div[1]/div/div/div').click()
    print("Cam off")
    driver.implicitly_wait(3000)

    #Instead of muting audio need to change audio input device to cable input
    
    # driver.find_element(By.XPATH, '//*[@id="new-toolbox"]/div/div/div/div[1]/div/div[1]/div/div/div').click()
    # print("Mic off")
    # driver.implicitly_wait(3000)
    time.sleep(1)


# Joining meet
def joinNow(driver):
    driver=driver
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="videoconference_page"]/div[3]/div[1]/div/div/div[1]/input').send_keys("MusicBot")
    driver.find_element(By.XPATH, '//*[@id="videoconference_page"]/div[3]/div[1]/div/div/div[1]/div/div').click()
    # driver.implicitly_wait(10)
    print("Joining meet")
