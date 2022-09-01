from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from playSong import playSong
from pauseSong import pauseSong
from resumeSong import resumeSong
from helpCommand import helpCommand

def commands(driver):
    driver=driver
    # To wait until bot joins the meet.
    WebDriverWait(driver, 10000000).until(EC.visibility_of_element_located((By.ID,'new-toolbox')))
    # Open chat box
    chatIcon=driver.find_element(By.CLASS_NAME, 'toolbar-button-with-badge')
    ActionChains(driver).move_to_element(chatIcon).click().perform()
    driver.implicitly_wait(3)
    # To wait until text message box is visible
    WebDriverWait(driver, 10000000).until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-input')))
    driver.find_element(By.CLASS_NAME, 'icon-input').send_keys("Hi! I'm Music bot." + Keys.ENTER)
    driver.implicitly_wait(3)
    print("Introduced in chat")

    #Read chat commands
    i=1
    run=1
    while(run==1):
        WebDriverWait(driver, 2000000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="chatconversation"]/div['+str(i)+']/div/div[1]/div/div/div[2]')))
        # WebDriverWait(driver, 2000000000).until(EC.visibility_of_element_located((By.CLASS_NAME, 'usermessage')))
        chatText=driver.find_element(By.CLASS_NAME, 'usermessage').text
        print("Here's the chat msg: "+chatText)
        # For now not reading messages in group by the same person. Can implement later.

        #Removing author details
        actualChatText=str(chatText).split("\n",1)[1]
        actualChatText=str(actualChatText).lower()

        if "/play" in actualChatText:
            print("Play Song")
            songNameStartIdx=actualChatText.find("/play")+6
            songName=actualChatText[songNameStartIdx:]
            musicWindow=playSong(driver, songName)
            i=i+1
        elif "/pause" in actualChatText:
            print("Pause Song")
            pauseSong(driver, musicWindow)
            i=i+1
        elif "/resume" in actualChatText:
            print("Resume song")
            resumeSong(driver, musicWindow)
            i=i+1
        elif "/help" in actualChatText:
            print("Bot help")
            helpCommand(driver)
            i=i+1
        elif "/exit" in actualChatText:
            run=0
            print("Exit bot")
            driver.quit()
        else:
            print(actualChatText)
            i=i+1