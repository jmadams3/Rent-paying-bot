from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def order():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://unionchapelhillnew.residentportal.com/auth")
    driver.maximize_window()  # For maximizing window
    time.sleep(5)
    username = driver.find_element(By.XPATH, '//*[@label="Email"]')
    username.send_keys(input('Enter email: '))
    password = driver.find_element(By.XPATH, '//*[@label="Password"]')
    password.send_keys(input('Enter password: '))
    logInButton = driver.find_element(By.TAG_NAME, 'button')
    logInButton.send_keys(Keys.ENTER)
    time.sleep(2)
    continueBtn = driver.find_element(By.XPATH, '//*[@type="submit"]')
    continueBtn.send_keys(Keys.ENTER)
    time.sleep(3)

    payments = driver.find_element(By.XPATH, '//*[@title="Payments"]')
    payments.send_keys(Keys.ENTER)
    time.sleep(5)

    due = driver.find_element(
        By.XPATH, '//*[@class="css-jwwls e1uqkhov4"]').text
    print("The amount currently due is " + due + ".")

    makePayment = driver.find_element(By.XPATH, '//*[@appearance="action"]')
    makePayment.send_keys(Keys.ENTER)
    time.sleep(2)

    customAmt = driver.find_element(
        By.XPATH, '//*[@name="custom_amount"]')
    customAmt.send_keys(input('Enter payment amount: '))
    customAmt.send_keys(Keys.TAB)
    time.sleep(2)

    chooseMethod = driver.find_element(
        By.XPATH, '//*[@name="1082174"]')
    chooseMethod.click()
    chooseMethod.send_keys(Keys.RETURN)
    time.sleep(2)

    payment_memo = driver.find_element(By.XPATH, '//*[@name="payment_memo"]')
    payment_memo.send_keys(input('Enter a payment note: '))
    payment_memo.send_keys(Keys.TAB)
    time.sleep(2)

    nextBtn = driver.find_element(
        By.XPATH, '//*[@type="submit"]')
    nextBtn.click()
    time.sleep(3)

    agree = driver.find_element(By.XPATH, '//*[@type="checkbox"]')
    agree.click()
    time.sleep(2)

    finalize = driver.find_element(By.XPATH, '//*[@type="submit"]')
    # finalize.click()
    time.sleep(5)


order()
