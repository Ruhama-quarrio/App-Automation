from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-dev.com/"

email = "naveeeed.ariff@gmail.com"
password = "Nido123##"


class CustomerAdmin:
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

    def question_logs(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='side-menu']/span[3]/li[2]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='custAdminCollapse']/li[2]/a").click()
        time.sleep(10)
        drop = Select(
            driver.find_element_by_xpath("//*[@id='page-wrapper']/section[2]/div/div/div/div[1]/div[2]/select"))
        drop.select_by_visible_text("Muhammad Naveed")
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").click()
        time.sleep(5)
        driver.find_element_by_class_name("close").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = CustomerAdmin()
obj.login()
obj.question_logs()
obj.logout()
