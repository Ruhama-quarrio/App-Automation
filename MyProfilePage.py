from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="G:\\chromedriver\\chromedriver.exe")
Url = "https://app2.qca-dev.com/"

email = "naveeeed.ariff@gmail.com"
password = "Nido123##"
firstname = "Muhammad"
lastname = "Naveed"
jobtitle = "QA Engineer"
organization = "Quarrio"
phone = "03228872222"


class MyProfile:
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

    def myprofile_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='side-menu']/li[6]/div/div[2]/a[1]").click()
        time.sleep(10)
        driver.find_element_by_id("profilePicture").send_keys("G:/Naveed.jpeg")
        time.sleep(5)
        driver.find_element_by_name("firstName").clear()
        time.sleep(3)
        driver.find_element_by_name("firstName").send_keys(firstname)
        time.sleep(3)
        driver.find_element_by_name("lastName").clear()
        time.sleep(3)
        driver.find_element_by_name("lastName").send_keys(lastname)
        time.sleep(3)
        driver.find_element_by_name("jobTitle").clear()
        time.sleep(3)
        driver.find_element_by_name("jobTitle").send_keys(jobtitle)
        time.sleep(3)
        driver.find_element_by_name("organization").clear()
        time.sleep(3)
        driver.find_element_by_name("organization").send_keys(organization)
        time.sleep(3)
        driver.find_element_by_name("phone").clear()
        time.sleep(3)
        driver.find_element_by_name("phone").send_keys(phone)
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").submit()
        time.sleep(10)
        driver.find_element_by_class_name("gototop").click()
        time.sleep(5)
        driver.find_element_by_class_name("gotobottom").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()


obj = MyProfile()
obj.login()
obj.myprofile_page()
obj.logout()
