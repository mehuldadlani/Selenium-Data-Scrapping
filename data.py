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

    name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-label-1.dark\\:text-dark-label-1.break-all.text-base.font-semibold")))
    name = name_element.text
    print("Name - " + name)

    usename_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-label-3.dark\\:text-dark-label-3.text-xs")))
    username = usename_element.text
    print("Username - " + username)

    github_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[1]/a/div/span[2]/div/span')))
    github = github_element.text
    print("Github - " + github)

    # Fetch the contest rating element using XPath from the parent element
    contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]')))
    contest_rating = contest_rating_element.text
    print("Contest Rating - " + contest_rating)

    problem_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[1]')))
    problem_solved = problem_solved_element.text
    print("Problem Solved - " + problem_solved)

    global_ranking_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]')))
    global_ranking = global_ranking_element.text
    print("Global Ranking - " + global_ranking)

    top_percentage_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]')))
    top_percentage = top_percentage_element.text
    print("Top Percentage - " + top_percentage)

    python_solutions_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[6]/div[1]')))
    python_solutions = python_solutions_element.text
    print("Python Solutions - " + python_solutions)

    cpp_solution_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[6]/div[2]')))
    cpp_solution = cpp_solution_element.text
    print("C++ Solutions - " + cpp_solution)

    # Add a delay of 5 seconds before the program terminates
    sleep(5)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window regardless of any exceptions
    if 'browser' in locals():
        browser.quit()
