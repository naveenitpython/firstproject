from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver.get('https://www.google.co.in/')

def gmail():
    driver = webdriver.Chrome()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get('https://www.gmail.com/')
    print "gmail opened"

def facebook():
    driver = webdriver.Chrome()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get('https://www.facebook.com/')
    print "facebook opened"

def linkedin():
    driver = webdriver.Chrome()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get('https://www.linkedin.com/')
    print "linkedin opened"

def twitter():
    driver = webdriver.Chrome()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get('https://www.twitter.com/')
    print "twitter opened"

def allsocialnetworks():
    gmail()
    facebook()
    linkedin()
    twitter()
    print "All networks opened"

win = Tk()
l = Label(win, text = 'Famous Social Networks')

g = Button(win, text = 'Gmail')
f = Button(win, text = 'Facebook')
li = Button(win, text = 'LinkedIn')
t = Button(win, text = 'Twitter')
a = Button(win, text = 'All_Networks')

l.pack()

g.pack(side = LEFT)
f.pack(side = LEFT)
li.pack(side = LEFT)
t.pack(side = LEFT)
a.pack(side = LEFT)

g.configure(command = gmail)
f.configure(command = facebook)
li.configure(command = linkedin)
t.configure(command = twitter)
a.configure(command = allsocialnetworks)
win.mainloop()
