from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # for msgs in grp
    # h12
    # //*[@id="chatconversation"]/div[1]/div[1]/div/div/div/div[2] 1
    # //*[@id="chatconversation"]/div[1]/div[2]/div[1]/div/div/div 2
    # h11
    # //*[@id="chatconversation"]/div[2]/div[1]/div/div/div/div[2] 1
    # //*[@id="chatconversation"]/div[2]/div[2]/div[1]/div/div/div 2
    # h12
    # //*[@id="chatconversation"]/div[3]/div/div[1]/div/div/div[2] 3
    # h13
    # //*[@id="chatconversation"]/div[4]/div[1]/div/div/div/div[2] 1
    # //*[@id="chatconversation"]/div[4]/div[2]/div[1]/div/div/div 2

    # To read chat, you need to keep looking if a new group has been created then read it as first line,
    #  or if not then keep an eye on the occurance of new msg in same local group.

    #Read chat commands
    i=2
    run=1
    while(run==1):
        WebDriverWait(driver, 2000000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="chatconversation"]/div['+str(i)+']/div/div[1]/div/div/div[2]')))
        chatText=driver.find_element(By.XPATH, '//*[@id="chatconversation"]/div['+str(i)+']/div/div[1]/div/div/div[2]').text
        # For now not reading messages in group by the same person. Can implement later.

        #Removing author details
        actualChatText=str(chatText).split("\n",1)[1]
        actualChatText=str(actualChatText).lower()

        if "/playsong" in actualChatText:
            print("Play Song")
            i=i+1
        elif "/exit" in actualChatText:
            run=0
            print("Exit bot")
            driver.close()
        else:
            print(actualChatText)
            i=i+1