import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)
from selenium.webdriver.common.by import By
chrome_service=Service("D:/Download/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
"""driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.maximize_window()
driver.get("https://demoqa.com/elements")
driver.back()
time.sleep(5)
print(driver.current_url)
driver.forward()
time.sleep(5)
driver.refresh()
print(driver.current_url)
driver.close()
"""
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
cart=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
if cart.is_displayed():
    print("User Logged in Successfully")
else:
    print("Something went wrong")

time.sleep(5)
#driver.close()
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(5)
driver.find_element(By.ID,"checkout").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Debdip")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Bhaduri")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("741121")
time.sleep(10)
driver.find_element(By.ID,"continue").click()
time.sleep(5)
driver.find_element(By.ID,"finish").click()
time.sleep(10)

thank_you_text=driver.find_element(By.XPATH,"//h2[contains(text(),'Thank you for your order!')]").text
print('Thank you for your order!')