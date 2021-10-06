#!/usr/bin/env python
# coding: utf-8

# In[90]:


import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[100]:


# advanced cryptography
username = ''
password = [0]
#password = ''.join([chr(x) for x in password[::-1]])
sleep_time = 0


# In[105]:


driver = webdriver.Chrome()
driver.get('https://patientconnect.bu.edu/')
time.sleep(sleep_time)

# login
inputElement = driver.find_element_by_id('j_username')
inputElement.send_keys(username)
inputElement = driver.find_element_by_id('j_password')
inputElement.send_keys(password)
inputElement.send_keys(Keys.ENTER)
time.sleep(sleep_time)

# screen size
appointments = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[4]/a')
if not appointments.is_displayed():
    sidebar = driver.find_element_by_xpath('/html/body/nav/div/div[1]/button[1]')
    sidebar.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Appointments'))).click()
else:
    appointments.click()

time.sleep(sleep_time)

# click schedule appointment
book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/p[1]/input')
book.click()
time.sleep(sleep_time)

# blegh fill out forms
non_threatening = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/span/fieldset/table/tbody/tr[1]/td/span/input')
non_threatening.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/span/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

covid_testing = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[13]/td/span/input')
covid_testing.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

agree = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[1]/td/span/input')
agree.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

agree2 = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/span/li[4]/fieldset/table/tbody/tr[1]/td/span/input')
agree2.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/span/li[4]/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

no_symptoms = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[3]/td/span/input')
no_symptoms.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

no_pos = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[3]/td/span/input')
no_pos.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

cfm_address = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table[2]/tbody/tr/td[2]/input')
cfm_address.click()
time.sleep(sleep_time)

# choose appointment date
date = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/form/div/div[1]/input')
appt_date = driver.execute_script('return document.getElementById("StartDate").getAttribute("value")')

# choose appointment location (med)
select_loc = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/form/div/select')
select_loc.click()
select_loc.send_keys(Keys.DOWN)
select_loc.send_keys(Keys.DOWN)
select_loc.send_keys(Keys.RETURN)
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/form/div/button')
continue_book.click()
time.sleep(sleep_time)

choose_appt = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[2]/fieldset/table/tbody/tr[1]/td[1]/span/input')
choose_appt.click()
continue_book = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[2]/table/tbody/tr/td[2]/input')
continue_book.click()
time.sleep(sleep_time)

cfm_appt = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[2]/table/tbody/tr[1]/td[1]/input')
cfm_appt.click()
time.sleep(sleep_time + 3)

driver.quit()
print('Appointment scheduled for ' + appt_date)


# In[ ]:




