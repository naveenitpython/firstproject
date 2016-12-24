from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

win = Tk()

uservar = StringVar()
passvar = StringVar()

def gmaillogin():
        username = uservar.get()
        password = passvar.get()
        print username, " ", password
        driver = webdriver.Chrome()
        url="https://www.gmail.com"
        driver.get(url)
        driver.find_element_by_xpath('//input[@id="Email"]').clear()
        time.sleep(1)
        email = driver.find_element_by_xpath('//input[@id="Email"]')
        email.click()
        email.send_keys(username)
        time.sleep(2)
        nextpage=driver.find_element_by_xpath('//input[@id="next"]')
        nextpage.click()
        time.sleep(2)
        pwd=driver.find_element_by_xpath('//input[@id="Passwd"]')
        pwd.click()
        pwd.send_keys(password)
        driver.find_element_by_xpath('//input[@id="signIn"]').click()
        time.sleep(3)
	
# entry label

mainlabel = Label(win, text = "GMAIL")
userlabel = Label(win, text = "User_Name")
passlabel = Label(win, text = "Password")

mainlabel.grid(row=0, column=0, columnspan=2)
userlabel.grid(row=1, column=0,sticky=W)
passlabel.grid(row=2, column=0,sticky=W)

# entry widgets

userwidget = Entry(win, textvariable = uservar)
passwidget = Entry(win, textvariable = passvar)
userwidget.grid(row=1, column=1)
passwidget.grid(row=2, column=1)

# entry button

submitbutton = Button(win, text = "SUBMIT")
submitbutton.grid(row=3, column=0, columnspan=2)
submitbutton.configure(command = gmaillogin)

win.mainloop()
