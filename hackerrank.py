from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "D:/Chrome Driver/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument("--incognito")
# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")

try:
    browser = webdriver.Chrome(options=options)
    browser.get("https://leetcode.com/tanishq2505/")
    
    # Wait for the elements to be present
    wait = WebDriverWait(browser, 10)

    

    # Add a delay of 5 seconds before the program terminates
    sleep(5)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window regardless of any exceptions
    if 'browser' in locals():
        browser.quit()
