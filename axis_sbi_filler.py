from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass



print "\t\t Bank details for 1.SBI and 2. Axis "
print "\n"



bankname=raw_input('Select a bank name: \t');

if bankname=="SBI":
	UName=raw_input('\nEnter the username: \t')
	passwd=getpass.getpass()
	accno=raw_input('\nEnter the account_no: \t')
	driver = webdriver.Firefox()
	driver.get("https://retail.onlinesbi.com/retail/login.htm")
	driver.find_element_by_class_name('continue_btn').click()
	driver.find_element_by_id('username').send_keys(UName)
	driver.find_element_by_id('label2').send_keys(passwd)
	driver.find_element_by_id('Button2').click()

	driver.find_element_by_id('accBal000000'+accno).click()
	#driver.find_element_by_class_name('nowrap').click()

elif bankname=="Axis":

	UNameAxis=raw_input('\nEnter the username for Axis bank: \t')
	passwd_axis=getpass.getpass()
	driver = webdriver.Firefox()
	driver.get("https://retail.axisbank.co.in/wps/portal/rBanking/axisebanking/AxisRetailLogin/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOKNAzxMjIwNjLwsQp0MDBw9PUOd3HwdDQwMjIEKIoEKDHAARwNC-sP1o_ArMYIqwGNFQW6EQaajoiIAVNL82A!!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/")
	driver.find_element_by_id('loginId').send_keys(UNameAxis)
	driver.find_element_by_class_name('password-lbl').send_keys(passwd_axis)
	driver.find_element_by_name('ABCustomLoginPortletFormSubmit').click()

else:
	print "Cant open for other banks"


