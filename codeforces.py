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
options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")

try:
    browser = webdriver.Chrome(options=options)
    browser.get("https://codeforces.com/profile/tourist")
    
    # Wait for the elements to be present
    wait = WebDriverWait(browser, 10)

    username_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/div[2]/h1/a')))
    username = username_element.text
    print("Username - " + username)

    contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]')))
    contest_rating = contest_rating_element.text
    print("Contest Rating - " + contest_rating)

    all_time_problem_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[1]/div[1]')))
    all_time_problem_solved = all_time_problem_solved_element.text
    print("All Time Problem Solved - " + all_time_problem_solved)

    problems_solved_last_year_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[2]/div[1]')))
    problems_solved_last_year = problems_solved_last_year_element.text
    print("Problems Solved Last Year - " + problems_solved_last_year)

    problems_solved_last_month_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[3]/div[1]')))
    problems_solved_last_month = problems_solved_last_month_element.text
    print("Problems Solved Last Month - " + problems_solved_last_month)

    max_days_in_a_row_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[2]/div[1]/div[1]')))
    max_days_in_a_row = max_days_in_a_row_element.text
    print("Max Days In A Row - " + max_days_in_a_row)

    # Add a delay of 5 seconds before the program terminates
    sleep(5)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window regardless of any exceptions
    if 'browser' in locals():
        browser.quit()
