from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-dev.com/"

email = "naveeeed.ariff@gmail.com"
password = "Nido123##"
currentPassword = "Nido123##"
newPassword = "Test@123"
confirmPassword = "Test@123"


class MyPassword:
    def login(self):
        driver.get(Url)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_id("username").send_keys(email)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("showHidePassword").click()
        driver.find_element_by_xpath("//*[@id='profile_form']/div[3]/div/div/div/input").click()
        time.sleep(10)

    def myPassword_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='side-menu']/li[6]/div/div[2]/a[2]").click()
        time.sleep(10)
        driver.find_element_by_name("currentPassword").send_keys(currentPassword)
        time.sleep(5)
        driver.find_element_by_name("password").send_keys(newPassword)
        time.sleep(5)
        driver.find_element_by_name("reEnterPassword").send_keys(confirmPassword)
        time.sleep(5)
        # driver.find_element_by_name("Save").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = MyPassword()
obj.login()
obj.myPassword_page()
obj.logout()
