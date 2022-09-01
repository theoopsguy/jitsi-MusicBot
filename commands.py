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
    # Open chat box
    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("c")\
        .key_up(Keys.SHIFT)\
        .perform()

    driver.implicitly_wait(3)
    driver.find_element(By.CLASS_NAME, 'jss73').send_keys("Hi! I'm Music bot." + Keys.ENTER)
    driver.implicitly_wait(3)
    print("Introduced in chat")

    # To read chat, you need to keep looking if a new group has been created then read it as first line,
    #  or if not then keep an eye on the occurance of new msg in same local group.

    # In a remote grp: 1st:
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[1]
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div/div[2]     text div
    #2nd:
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[3]
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[3]/div[1]/div/div/div/div[2]     2.1
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[3]/div[2]/div/div/div/div        2.2
    #/html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[3]/div[3]/div/div/div/div        2.3
    #3rd:
    # /html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[5]
    # /html/body/div[1]/div[1]/div/div[1]/div[3]/div[1]/div[5]/div/div[1]/div/div/div[2]

    #Read chat commands
    i=1
    run=1
    while(run==1):
        WebDriverWait(driver, 2000000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="chatconversation"]/div['+str(i)+']/div/div[1]/div/div/div[2]')))
        chatText=driver.find_element(By.CLASS_NAME, 'usermessage').text
        print(chatText)
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