import XLutils
import time
from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Downloaded\\chromedriver.exe")
driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
driver.maximize_window()
#locating file and getting the rowcount
path = "D:\\Sample.xlsx"
rows = XLutils.getrowcount(path, "Sheet3")

for r in range(2, rows+1):
    username = XLutils.readdata(path, "Sheet3", r, 1)
    password = XLutils.readdata(path, "Sheet3", r, 2)

    driver.find_element_by_xpath("//input[@id='user_email']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='user_password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='commit']").click()
    time.sleep(10)

    value = driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
    print(value)
    if value == "Invalid email or password.":
        print("Login failed")
        XLutils.writedata(path, "Sheet3", r, 3, "Test failed")
        driver.save_screenshot("D://Doccument//sample.png")
        time.sleep(2)
    driver.find_element_by_xpath("//input[@id='user_email']").clear()
    time.sleep(5)

driver.quit()