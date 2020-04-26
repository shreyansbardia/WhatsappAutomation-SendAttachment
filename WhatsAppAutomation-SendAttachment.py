# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:15:47 2020

@author: ADMIN
"""

from selenium import webdriver
from time import sleep
#Connect with the ChromeDriver
driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')

#Go to the Website
driver.get('https://web.whatsapp.com/')


name = "demo" #Name of the person to send
filepath = "F:\images.jpg" #Location of the file to be send
count = 4 #Number of times message to be sent
mssg="This is a scenary" 
input('Enter anything after scanning QR code')

#Finding the name of the person via XPATH - To get the Xpath Inspect the element and click copy -copy Xpath
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click() #Click on the user

#Finding the attachment using the Xpath module
attachment = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
attachment.click()


#Finding the imagebutton and sending the filepath in it.
imagebttn = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
imagebttn.send_keys(filepath)
sleep(3) #Sleep until new window arrives
#Writing text for the Textinit path
Textinit = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
Textinit.send_keys(mssg)

#Finally sending the button.
Finalbttn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div')
Finalbttn.click()









