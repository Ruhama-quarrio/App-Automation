from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-dev.com/"

email = "naveeeed.ariff@gmail.com"
password = "Nido123##"
question = "List of Opps"


class Ask_Page():
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

    def ask_page(self):
        driver.find_element_by_class_name("logo").click()
        time.sleep(10)
        driver.find_element_by_class_name("downloadqtool").click()
        time.sleep(5)
        driver.find_element_by_xpath().click()
        time.sleep(5)
        driver.find_element_by_id("askanotherquestion").send_keys(question)
        driver.find_element_by_class_name("chatsendbtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='scrolltotop']/img").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='scrolltobottom']/img").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_class_name("menubars").click()
        time.sleep(10)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = Ask_Page()
obj.login()
obj.ask_page()
obj.logout()
