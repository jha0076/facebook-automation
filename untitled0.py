from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def logging_editing_deleting(url):
    driver = webdriver.Chrome(executable_path='C:/Users/HI/Desktop/Chrome driver/chromedriver_win32/chromedriver.exe')
   #giving the exceution path to the webdriver
    #url="https://www.facebook.com/pythonmate.botscr.7/posts/104102788197903"
    driver.get(url)
   #automating the login process
#driver.find_element_by_link_text("Log In").click()


#email automation

#explicit wait to find the element
     wait = WebDriverWait(driver, 10)
     email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))


    email.send_keys("pythonmatehelp@gmail.com")
#password automation
    password = driver.find_element_by_id("pass")
    password.send_keys("Pythonmate@1234")
#clicking on the login button by finding it using web elements
    login_button = driver.find_element_by_id("loginbutton")
    login_button.click()
    #finding and clicking the menu option on facebook post
    wait = WebDriverWait(driver, 10)
    menu=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div')))
    menu.click()  
    #finding edit button
    edit=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]')))
    edit.click()
    time.sleep(5)
    editing=driver.find_element_by_class_name("_5bvl mentions-input")
    editing.click()
    time.sleep(5)
   #writing new text in the post section
    editing.send_keys("Testing using Name not ID.Selenium is easy.")
   #saving the edited post
    save=driver.find_element_by_id("u_2j_3")
    save.click()
    time.sleep(5)
   #automating the  clicking of delete buttton
    delete=driver.find_element_by_class_name('_56bz _54k8 _55i1 _58a0 touchable _53n6')
    delete.click()
    time.sleep(5)
   #deleting the post
    final_delete=driver.find_element_by_xpath(("//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[4]"))
    final_delete.click()
   
 #taking input from user about link of the post to edit  
url=input("Enter the post url")
logging_editing_deleting(url)