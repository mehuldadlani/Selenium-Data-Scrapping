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
    browser.get("https://www.codingninjas.com/studio/profile/Anish5665")
    
    # Wait for the elements to be present
    wait = WebDriverWait(browser, 10)

    username_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[1]/codingninjas-profile-user-basic-info/div/div[1]/div[1]/div[1]/div[2]')))
    username = username_element.text
    print("Username - " + username)

    # level_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@_ngcontent-serverapp-c209=""]')))
    # level = level_element.text
    # print("Level - " + level)

    total_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[1]/div[1]')))
    total_problems_solved = total_problems_solved_element.text
    print("Total Problems Solved - " + total_problems_solved)

    easy_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[1]/div[1]')))
    easy_problems_solved = easy_problems_solved_element.text
    print("Easy Problems Solved - " + easy_problems_solved)

    moderate_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[2]/div[1]')))
    moderate_problems_solved = moderate_problems_solved_element.text
    print("Moderate Problems Solved - " + moderate_problems_solved)

    hard_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[3]/div[1]')))
    hard_problems_solved = hard_problems_solved_element.text
    print("Hard Problems Solved - " + hard_problems_solved)

    current_streak_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div[1]/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/p')))
    current_streak = current_streak_element.text
    print("Current Streak - " + current_streak)

    longest_streak_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div[1]/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p')))
    longest_streak = longest_streak_element.text
    print("Longest Streak - " + longest_streak)




    # Add a delay of 5 seconds before the program terminates
    sleep(5)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window regardless of any exceptions
    if 'browser' in locals():
        browser.quit()
