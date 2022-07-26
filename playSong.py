import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def playSong(driver, songName):
    originalMeetWindow=driver.current_window_handle
    driver.switch_to.new_window('tab') 
    youtubeMusicWindow=driver.current_window_handle

    driver.get("https://music.youtube.com/search?q="+songName)
    driver.implicitly_wait(3000)
    driver.find_element(By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a').click()
    time.sleep(2)

    # Handle ads, need to skip ad if ad is shown or can also let it play

    driver.switch_to.window(originalMeetWindow)
    time.sleep(1)

    # Sharing audio in meet
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div[3]').click()
