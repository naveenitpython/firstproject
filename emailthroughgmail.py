from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

win = Tk()

uservar = StringVar()
passvar = StringVar()
tovar = StringVar()
subjectvar = StringVar()
emailbodyvar = StringVar()

def sendmail():

	username = uservar.get()
	password = passvar.get()
	tomailid = tovar.get()
	subject = subjectvar.get()
	emailbody = emailbodyvar.get()
		
	driver = webdriver.Chrome()
	url="https://www.gmail.com"

	driver.get(url)
	driver.find_element_by_xpath('//input[@id="Email"]').clear()
	time.sleep(1)

	email = driver.find_element_by_xpath('//input[@id="Email"]')
	email.click()
	email.send_keys(username)
	time.sleep(2)

	nextpage = driver.find_element_by_xpath('//input[@id="next"]')
	nextpage.click()
	time.sleep(2)

	pwd=driver.find_element_by_xpath('//input[@id="Passwd"]')
	pwd.click()
	pwd.send_keys(password)

	submit = driver.find_element_by_xpath('//input[@id="signIn"]')
	submit.click()
	time.sleep(3)
	
	composetab=driver.find_element_by_xpath('//div[@class="T-I J-J5-Ji T-I-KE L3"]')
	composetab.click()
	time.sleep(2)
	
	toemail=driver.find_element_by_xpath('//textarea[@name="to"]')
	toemail.click()
	toemail.send_keys(tomailid)
	time.sleep(2)
	emailclick = driver.find_element_by_xpath('//b[@class="Jd-JU"]')
	emailclick.click()
	
	subjectspace=driver.find_element_by_xpath('//input[@name="subjectbox"]')
	subjectspace.click()
	subjectspace.send_keys(subject)

##	emailbody=driver.find_element_by_xpath('//*[@id=":am"]')                     
##	emailbody.click()
##	time.sleep(1)
##	emailbody.send_keys(emailbody)
##	time.sleep(3)

	send=driver.find_element_by_xpath('//div[@class="T-I J-J5-Ji aoO T-I-atl L3"]')
	send.click()
	time.sleep(5)
	
	driver.close()

# entry label

mainlabel = Label(win, text = "GMAIL")
userlabel = Label(win, text = "User_Name")
passlabel = Label(win, text = "Password")
tolabel = Label(win, text = "To")
subject = Label(win, text = "Subject")
compose = Label(win, text = "Body of the mail")

mainlabel.grid(row=0, column = 0, columnspan = 2)
userlabel.grid(row = 1, column = 0, sticky = W)
passlabel.grid(row = 2, column = 0, sticky = W)
tolabel.grid(row = 3, column = 0, sticky = W)
subject.grid(row = 4, column = 0, sticky = W)
compose.grid(row = 5, column = 0, sticky = W)

# entry widgets

userwidget = Entry(win, textvariable = uservar)
passwidget = Entry(win, textvariable = passvar)
tomailwidget = Entry(win, textvariable = tovar)
subjectwidget = Entry(win, textvariable = subjectvar)
composewidget = Entry(win, textvariable = emailbodyvar)

userwidget.grid(row = 1, column = 1)
passwidget.grid(row = 2, column = 1)
tomailwidget.grid(row = 3, column = 1)
subjectwidget.grid(row = 4, column = 1)
composewidget.grid(row = 5, column = 1)

# entry button

submitbutton = Button(win, text = "SEND")
submitbutton.grid(row = 6, column = 1, columnspan = 2)
submitbutton.configure(command = sendmail)

win.mainloop()
