# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:52:17 2020

@author: user
"""


from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\Learning\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.implicitly_wait(5)

def start():
        driver.find_element_by_name("username").send_keys("Your_username")
        driver.find_element_by_name("password").send_keys("Your_password")
        pyautogui.press('enter')
        time.sleep(4)
        
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        time.sleep(4)
        pyautogui.typewrite("#search_hastag")
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        
        #driver.get("https://www.instagram.com/explore/tags/valorant/")
        time.sleep(4)
        comment()
        
        
def comment():
     
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys("Hey! let's play together in VALORANT esports. Link : bit.ly/valorantesports")
        pyautogui.press('enter')
        time.sleep(6)
        for x in range(1,50):
            pyautogui.press("right")
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form").click()
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys("Hey! let's play together in VALORANT esports. Link : bit.ly/valorantesports")
            pyautogui.press('enter')
            time.sleep(10)

start()
