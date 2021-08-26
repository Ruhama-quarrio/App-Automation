from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-qa.com/"

email = "ruhama.sardar@quarrio.com"
password = "Ruha@123"
firstname = "Ruhama"
lastname = "Sardar"
phone = "03221234567"


class AddUser:
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

    def subUser(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_class_name("adminicon").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='custAdminCollapse']/li[1]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='page-wrapper']/section[2]/div/div/div/div[1]/div[2]/button[1]").click()
        time.sleep(10)
        driver.find_element_by_name("firstName").send_keys(firstname)
        time.sleep(3)
        driver.find_element_by_name("lastName").send_keys(lastname)
        time.sleep(3)
        drop = Select(driver.find_element_by_class_name("myemail"))
        drop.select_by_visible_text("ruhamaubinahum@gmail.com")
        time.sleep(5)
        driver.find_element_by_name("phone").send_keys(phone)
        time.sleep(5)
        driver.find_element_by_name("Save").submit()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='page-wrapper']/section[2]/div/div/div/div[1]/div[2]/button[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='share-modal2']/div/div/div[3]/div/button[1]").click()
        time.sleep(10)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = AddUser()
obj.login()
obj.subUser()
obj.logout()
