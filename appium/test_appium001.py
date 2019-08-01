from appium import webdriver
import time,os,traceback
import pytest

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "b9913849"
caps["app"] = r"C:\Temp\toutiao.apk"
caps["appPackage"] = "io.manong.developerdaily"
caps["appActivity"] = "io.toutiao.android.ui.activity.LaunchActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
caps["noReset"] = True

print("SetUp ongoing!")
try:
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("driver created succeed")
except Exception as e:
    print("driver created failed: Exception", format(e))

print("test_start function begin!")
time.sleep(1)
try:
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    print("find the start button")
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='密码登录']").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/edt_phone").send_keys("15210663614")
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/edt_password").send_keys("897577")
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_login").click()
except Exception as e:
    print("Exception:", format(e))

time.sleep(1)
try:
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus")
    print("login succeed!")
except Exception as e:
    print('login failed: ', format(e))
