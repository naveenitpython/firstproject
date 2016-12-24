##import requests
##from lxml import html
####import lxml
##import csv
##import urllib2
##
##url = "http://docs.python-requests.org/en/master/user/quickstart/"
##
####page=requests.get(url)
##tree=html.fromstring(page.text/page.content)
##
##page=urllib2.urlopen(url)
##tree=html.fromstring(page.read())
##
##header=tree.xpath('//div[@id="make-a-request"]/p/text()')
##print " ".join(header)


from selenium import webdriver
import csv
from lxml import html
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()

url="https://register.epo.org/advancedSearch?lng=en"
driver.get(url)
driver.find_element_by_xpath('//textarea[@name="pn"]').clear()
time.sleep(1)

element=driver.find_element_by_xpath('//textarea[@name="pn"]')
element.click()
element.send_keys('EP2248508')
time.sleep(2)

driver.find_element_by_xpath('//input[@type="submit"]').click()

time.sleep(2)

tree=html.fromstring(driver.page_source)

information=tree.xpath('//table[@class="tableType3 printTable"]/text()')
print information



##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##from lxml import html
##import time
##
##driver = webdriver.Chrome()
##url = 'https://gmail.com/'
##driver.get(url)
##driver.find_element_by_xpath('//input[@id="Email"]').clear()
##time.sleep(1)
##
##email=driver.find_element_by_xpath('//input[@id="Email"]')
##email.click()
##email.send_keys('naveenitlearning@gmail.com')
##time.sleep(2)
##
##nxt=driver.find_element_by_xpath('//input[@id="next"]').click()
##time.sleep(2)
##
##pwd=driver.find_element_by_xpath('//input[@id="Passwd"]')
##pwd.click()
##pwd.send_keys('abc@@123')
##
##driver.find_element_by_xpath('//input[@id="signIn"]').click()
##
##time.sleep(1)
##
##
##submitting=driver.find_element_by_xpath('//input[@type="submit"]')
##submitting.click()
##
##time.sleep(3)
##
##
##
##time.sleep(1)



