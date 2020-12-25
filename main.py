#imports
from selenium import webdriver
from instapy import InstaPy
from time import sleep 
from selenium.webdriver.common.action_chains import ActionChains
import json
from secrets import pw


#Login into instagram
def login(driver): 
    driver.get("https://www.instagram.com/")
    sleep(1)
    usr =   #enter username or email
    pwd = pw         #enter password in secrets.py file
    username_box = driver.find_element_by_class_name("_2hvTZ.pexuQ.zyHYP")
    username_box.send_keys(usr)
    sleep(1)
    #Logging In
    password_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password_box.send_keys(pwd)
    login_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    login_box.click()
    sleep(5)
    #Skipping Pop-Ups
    save_login_info = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    save_login_info.click()
    sleep(2)
    notif_notnow = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click() 
    sleep(2)


#Initializing driver
driver = webdriver.Chrome()
login(driver)


with open('''Enter directory to json file of followers''') as f:
    followers = json.load(f)




def send_msgs():
    for follower in followers:
        dm_box= driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        sleep(3)
        compose_new_msg = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button").click()
        sleep(3)
        username = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
        username.send_keys(follower)
        sleep(3)
        name_click = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div").click()
        sleep(3)
        click_next = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div").click()
        sleep(3)
        text_msg = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        sleep(3)
        msg = #Enter the message that you want to send
        sleep(3)
        text_msg.send_keys(msg)
        sleep(3)
        send_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        sleep(3)
        click_home_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div").click()

send_msgs()
