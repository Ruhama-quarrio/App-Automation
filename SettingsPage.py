from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-dev.com/"

email = "naveeeed.ariff@gmail.com"
password = "Nido123##"
datalimit = "190"
proposedquestionnumber = "2"


class Settings_Page:
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

    def settings_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='side-menu']/li[4]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[2]/div[1]/a/h3").click()
        drop = Select(driver.find_element_by_id("clearData"))
        drop.select_by_index(2)
        driver.find_element_by_class_name("cleardashboard").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='accordion2']/div/div[1]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='isNullToZero']").click()
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[6]/div/div[1]/a").click()
        time.sleep(5)
        driver.find_element_by_id("dataLimit").clear()
        driver.find_element_by_id("dataLimit").send_keys(datalimit)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[8]/div[1]/a").click()
        drop = Select(driver.find_element_by_xpath("//*[@id='scheduleTypeId']"))
        drop.select_by_index(1)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[10]/div[1]/a").click()
        drop = Select(driver.find_element_by_xpath("//*[@id='language']"))
        drop.select_by_visible_text("English US")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[12]/div/div[1]/a").click()
        driver.find_element_by_id("proposedQuestions").clear()
        time.sleep(5)
        driver.find_element_by_id("proposedQuestions").send_keys(proposedquestionnumber)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[14]/div[1]/a").click()
        drop = Select(driver.find_element_by_id("showSql"))
        drop.select_by_visible_text("Yes")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[16]/div[1]/a").click()
        drop = Select(driver.find_element_by_id("showParaphrase"))
        drop.select_by_visible_text("Yes")
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").click()
        time.sleep(5)
        driver.find_element_by_id("scrolltobottom").click()
        time.sleep(5)
        driver.find_element_by_id("scrolltotop").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/div[1]/div").click()
        driver.find_element_by_xpath("//*[@id='side-menu']/li[5]/a").click()
        time.sleep(10)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = Settings_Page()
obj.login()
obj.settings_page()
obj.logout()
