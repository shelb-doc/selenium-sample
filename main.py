

from selenium import webdriver
from selenium.webdriver.common.by import By

# Test for Request a Demo
driver = webdriver.Chrome()
driver.get('https://boatrentalmanagement.com/')
driver.implicitly_wait(3)

my_element = driver.find_element(By.CLASS_NAME, 'mkdf-btn-text')
my_element.click()

my_element = driver.find_element(By.NAME, 'your-name')
my_element.send_keys('Shelby')

my_element = driver.find_element(By.NAME, 'your-email')
my_element.send_keys('shelbycignetti@gmail.com')

my_element = driver.find_element(By.NAME, 'your-phone')
my_element.send_keys('7706686431')

my_element = driver.find_element(By.NAME, 'your-message')
my_element.send_keys('Hi, this was made with Automation using Selenium!')

