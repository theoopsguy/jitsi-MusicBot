import time
from selenium.webdriver.common.by import By

# Turn off video and select virtual device for audio input
def turnMicCamOff(driver):
    driver=driver
    driver.find_element(By.CLASS_NAME, 'video-preview').click()
    print("Cam off")
    driver.implicitly_wait(3000)
    driver.find_element(By.ID, 'audio-settings-button').click()
    driver.implicitly_wait(1000)
    micDevices=driver.find_elements(By.CLASS_NAME, 'audio-preview-entry')
    for micDevice in micDevices:
        if "VB-Audio" in micDevice.text or "BlackHole" in micDevice.text:
            micDevice.click()
            break
    print("Mic input set to virtual device output")
    driver.implicitly_wait(3000)
    driver.find_element(By.ID, 'audio-settings-button').click()
    driver.implicitly_wait(3000)

# Joining meet
def joinNow(driver):
    driver=driver
    driver.find_element(By.CLASS_NAME, 'field').send_keys("MusicBot")
    driver.find_element(By.CLASS_NAME, 'jss19').click()
    driver.implicitly_wait(1000)
    print("Joining meet")
