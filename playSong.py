import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def playSong(driver, songName):
    originalMeetWindow=driver.current_window_handle
    driver.switch_to.new_window('tab') 
    youtubeMusicWindow=driver.current_window_handle

    driver.get("https://music.youtube.com/search?q="+songName)
    driver.implicitly_wait(3000)
    # driver.find_element(By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a').click()
    driver.find_element(By.ID, 'play-button').click()
    time.sleep(2)

    driver.execute_script('var sink_id = "";navigator.mediaDevices.enumerateDevices().then(inspect_devices).catch(errorCallback);function inspect_devices(deviceInfos) {console.log("Inspecting Devices: " + deviceInfos.length + " device(s) total (audio/video input/output)");for (var deviceIdx = 0; deviceIdx < deviceInfos.length; deviceIdx++) {var deviceInfo = deviceInfos[deviceIdx];if (deviceInfo.label.includes("VB-Audio") && (deviceInfo.kind == "audiooutput")) {sink_id = deviceInfo.deviceId;update_all_sinks();}}}function update_all_sinks() {var allMedia = document.querySelectorAll("audio,video");for (var mediaElement = 0; mediaElement < allMedia.length; mediaElement++) {allMedia[mediaElement].setSinkId(sink_id);}}function errorCallback(error) {console.log("Error: "+ error);}')
    driver.implicitly_wait(3000)
    time.sleep(1)

    # Handle ads, need to skip ad if ad is shown or can also let it play

    driver.switch_to.window(originalMeetWindow)
    time.sleep(1)

    return youtubeMusicWindow