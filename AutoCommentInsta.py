# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:52:17 2020

@author: user
"""


from selenium import webdriver
import time
import pyautogui

#put the location where chromedriver is locally situated.
driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\Learning\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.implicitly_wait(5)

def start():
        driver.find_element_by_name("username").send_keys("Your_username") #enter your instagram username at Your_username
        driver.find_element_by_name("password").send_keys("Your_password") #enter your instagram password at Your_password
        pyautogui.press('enter')
        time.sleep(4)
        
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        time.sleep(4)
        pyautogui.typewrite("#search_hastag") #put the hastag you want to search at search_hastag
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        
        #driver.get("https://www.instagram.com/explore/tags/search_hastag/") #put the hastag you want to search at search_hastag
        time.sleep(4)
        comment()
        
        
def comment():
     
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys("hi I am a bot. Put your comment here!!!")
        pyautogui.press('enter')
        time.sleep(6)
        for x in range(1,10): #1 to 10, that is it'll post on 10 top posts.
            pyautogui.press("right")
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form").click()
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys("Hhi I am a bot. Put your comment here!!!")
            pyautogui.press('enter')
            time.sleep(10)

start()
