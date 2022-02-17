from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver.exe")
Url = "https://app.qca-qa.com/login"
#
email = "ruhama.sardar@quarrio.com"
password = "Ruha@1234"
question = "list of accounts"

class Features:

    def login(self):
        driver.get(Url)
        time.sleep(5)
        driver.find_element_by_name("username").send_keys(email)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("showHidePassword").click()
        driver.find_element_by_xpath("//*[@id='profile_form']/div[3]/div/div/div/input").click()
        time.sleep(10)
        
    def forgotPassword(self):
        driver.get(Url)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@class='loginsubmit row']/div/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@placeholder='user@example.com']").send_keys(email)
        time.sleep(5)
        driver.find_element_by_xpath("//input[@value='Recover Password']").click()
        
    def About_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='side-menu']/li/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[normalize-space()='Privacy Policy']").click()
        time.sleep(5) 
        driver.find_element_by_xpath("//*[@id='side-menu']/li/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[normalize-space()='Terms of services']").click()
        time.sleep(5) 
      
    def ask_page(self):
        driver.find_element_by_class_name("logo").click()
        time.sleep(3)
        driver.find_element_by_id("askanotherquestion").send_keys(question)
        driver.find_element_by_class_name("chatsendbtn").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='scrolltotop']/img").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='scrolltobottom']/img").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/nav/div/ul/li[1]/div/label/span[1]").click()
        time.sleep(5)

        
    def settings_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)

#settings path
        driver.find_element_by_xpath("//*[@id='side-menu']/li[3]/a").click()
        time.sleep(3)
#for selecting dropdown
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[2]/div[1]/a/h3").click()
        drop = Select(driver.find_element_by_id("clearData"))
        drop.select_by_visible_text("Clear conversation questions")
        driver.find_element_by_class_name("cleardashboard").click()
        time.sleep(5)
#data identifier path
        driver.find_element_by_xpath("//*[@id='accordion2']/div/div/a/h3").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='isNullToZero']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[6]/div[1]/a/h3").click()
        drop = Select(driver.find_element_by_id("showSql"))
        drop.select_by_visible_text("Yes")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div/div[8]/div[1]/a/h3").click()
        drop = Select(driver.find_element_by_id("showParaphrase"))
        drop.select_by_visible_text("Yes")
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").click()
        time.sleep(5)
        driver.find_element_by_id("scrolltobottom").click()
        time.sleep(5)
        driver.find_element_by_id("scrolltotop").click()
        time.sleep(5)
        
    def feedback_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)       
        driver.find_element_by_xpath("//*[@id='side-menu']/li[4]/a").click()
        time.sleep(5)
        driver.find_element_by_id("subject").send_keys("test sample")
        time.sleep(5)
        driver.find_element_by_id("message").send_keys(" testing feature")
        time.sleep(5)
        driver.find_element_by_id("filename").send_keys("C:/Users/user/download.png")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div[8]/div/div/input").submit()
        time.sleep(5)
        
    def custadmin_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@class='adminicon']/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='custAdminCollapse']/li/a").click()
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").click()
        time.sleep(5)
        driver.find_element_by_id("firstName").send_keys("test")
        time.sleep(5)
        driver.find_element_by_id("lastName").send_keys("user")
        time.sleep(5)
        driver.find_element_by_id("email").send_keys("TestUser22@gmail.com")
        time.sleep(5)
        driver.find_element_by_id("phone").send_keys("0578545674456782")
        time.sleep(5)
        driver.find_element_by_name("Save").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='Disconnect all sub-users']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@title='Yes']").click()
        time.sleep(5)
        
    def questionlogs_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@class='adminicon']/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='custAdminCollapse']/li[2]/a").click()
        time.sleep(5)
        drop = Select(driver.find_element_by_xpath("//*[@id='page-wrapper']/section[2]/div/div/div/div[1]/div[2]/select"))
        drop.select_by_index(1)
        time.sleep(10)
        driver.find_element_by_xpath("//button[@class='smallbtn1']").click()
        time.sleep(5)        
        driver.find_element_by_class_name("close").click()
        time.sleep(5)
        
    def myprofile_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='My Profile']").click()
        time.sleep(5)
##profile pic upload
#        driver.find_element_by_xpath("//label[normalize-space()='Choose Image']").click()
#        driver.find_element_by_xpath("//label[normalize-space()='Choose Image']").send_keys("C:/Users/user/download.png")
#        time.sleep(5)
#
        driver.find_element_by_class_name("firstname").clear()
        driver.find_element_by_class_name("firstname").send_keys("test")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@name='lastName']").clear()
        driver.find_element_by_xpath("//input[@name='lastName']").send_keys("user")
        time.sleep(5)
#job title path
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div[3]/div[4]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='profile_form']/div/div[3]/div[4]/div/input").send_keys("QA Engineer")
        time.sleep(5)
        driver.find_element_by_class_name("company").clear()        
        driver.find_element_by_class_name("company").send_keys("Quario")
        time.sleep(5)
        driver.find_element_by_class_name("phone").clear()
        driver.find_element_by_class_name("phone").send_keys("4567865434567654")
        time.sleep(5)
        driver.find_element_by_class_name("smallbtn1").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='wrapper']/div[1]/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='side-menu']/li[7]/div/div[2]/a[2]").click()
        time.sleep(10)
        
    def mypassword_page(self):
        driver.find_element_by_class_name("menubars").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='My Password']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@name='currentPassword']").send_keys("Ruha@1234")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@name='password']").send_keys("Ruha@12345")
        driver.find_element_by_xpath("//input[@name='confirmPassword']").send_keys("Ruha@12345")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='profile_form']/div[4]/input").submit()
        time.sleep(5)

    def logout(self):
        driver.find_element_by_class_name("help_icon").click()
        time.sleep(10)
        driver.quit()
        print("Test Completed")


obj = Features()
obj.login()
obj.forgotPassword()
obj.About_page()
obj.ask_page()
obj.settings_page()
obj.feedback_page()
obj.custadmin_page()
obj.questionlogs_page()
obj.myprofile_page()
obj.mypassword_page()
obj.logout()
