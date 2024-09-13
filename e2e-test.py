from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("https://saucedemo.com")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    time.sleep(2)

    product = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    product.click()

    time.sleep(2)

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    time.sleep(2)

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    time.sleep(2)

    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    time.sleep(2)

    first_name.send_keys("Ivan")
    last_name.send_keys("Ivanov")
    postal_code.send_keys("12345")

    time.sleep(2)

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    time.sleep(2)

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    confirmation_element = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in confirmation_element.text
    print("Покупка успешно завершена!")

except Exception:
    print("Тест завершился с ошибкой")

time.sleep(2)
driver.quit()

