from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
import pandas as pd

# Import machine learning functions from machine.py
from machine import predict_elements

# Initialize Selenium WebDriver
driver = WebDriver()
driver.get("https://accounts.lambdatest.com/login")
driver.implicitly_wait(10)
driver.maximize_window()
driver.implicitly_wait(10)



# Self-healing function using ML model
def heal_and_find_element(driver, strategy, locator):
    try:
        element = driver.find_element(strategy, locator)
        return element
    except Exception as e:
        print(f"Element not found using {strategy}='{locator}', trying self-healing...")
        # Call the machine learning model to predict the correct locator
        _, element_name = predict_elements()
        # Example healing: switch strategy based on prediction (you can add more logic here)
        if strategy == 'xpath':
            return driver.find_element('id', element_name)  # Try a different strategy or locator

def enter_user_name(driver):
    try:
        user_element = heal_and_find_element(driver, "xpath", '//input[@name="email"]')
        user_element.send_keys("alamsahdab786@gmail.com")
        print("Username entered.")
    except Exception as e:
        print(e)

def enter_password(driver):
    try:
        pass_element = heal_and_find_element(driver, "id", "password")
        pass_element.send_keys("Nagma@123")
        print("Password entered.")
    except Exception as e:
        print(e)

def click_on_login(driver):
    try:
        login_button = heal_and_find_element(driver, "xpath", '//button[contains(text(),"Login")]')
        login_button.click()
        print("Login clicked.")
    except Exception as e:
        print(e)

# Use the functions
enter_user_name(driver)
enter_password(driver)
click_on_login(driver)
sleep(5)

print("Test completed.")
driver.quit()

print(" ")