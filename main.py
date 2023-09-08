import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(ChromeDriverManager().install())

driver_path = "C:\chromedriver.exe"

URL = "https://www.dice.com/"

element = driver.find_element("id","submitSearch-button") #will be used to get the Search jobs button and to perform an automatic click

jobTitle = input("Enter the job title: ")

jobLocation = input("Enter the job location:") 

def replace_white_space(string):
    return string.replace(" ","%20")

parameters = {jobTitle:replace_white_space(jobTitle),jobLocation:replace_white_space(jobLocation)}

altered_url = URL + "q=" + parameters[jobTitle] + "&location=" + parameters[jobLocation]

time.sleep(2)

# element.click()

driver.get(URL)

# driver.find_element(By.XPATH, "//h1[text()='ITC Speedtest']//following-sibling::div[@id='startStopBtn' and starts-with(@onclick, 'startStop')]").click()