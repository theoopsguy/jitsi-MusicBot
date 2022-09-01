from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from joinMeet import turnMicCamOff, joinNow
from commands import commands

# Handling permission popups and browser window props
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("enable-usermedia-screen-capturing")
opt.add_argument("enable-usermedia-screen-capturing")
opt.add_argument("auto-select-desktop-capture-source=YouTube Music")    #Auto select which screen to share, for now YTM
opt.add_experimental_option('excludeSwitches', ['test-type'])
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
})

# Starting browser
driver= webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe",options=opt)
print("browser start")

# Meeting link goes here
driver.get('https://meet.jit.si/EmptyControlsMapAccidentally')
driver.implicitly_wait(1000)
time.sleep(1)

# Joining meet
turnMicCamOff(driver)
driver.implicitly_wait(100)
joinNow(driver)
driver.implicitly_wait(100)
time.sleep(1)
# Accessing chat and following commands
commands(driver)