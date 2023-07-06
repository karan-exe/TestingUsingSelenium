import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
parent_element = driver.find_element(By.CSS_SELECTOR, ".container")  # Replace with the appropriate CSS selector of the parent element

# Find all the forms with class name "well" inside the parent element
forms = parent_element.find_elements(By.CSS_SELECTOR, ".well")

# print(len(forms))
#change the color of the forms selected
driver.execute_script("arguments[0].style.backgroundColor = 'red';", forms[0])
driver.execute_script("arguments[0].style.backgroundColor = 'green';", forms[1])
driver.execute_script("arguments[0].style.backgroundColor = 'blue';", forms[2])
driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", forms[3])

#changing properties and sending values
input_field = forms[0].find_elements(By.CSS_SELECTOR, "input[name='First Name']")
input_field[0].send_keys("karan")
submit_button = forms[0].find_elements(By.CSS_SELECTOR, "button[type='submit']")
submit_button[0].click()

input_field1 = forms[1].find_element(By.CSS_SELECTOR, "form textarea[name='About']")
input_field1.send_keys("For About")
#select cancel button and click it
cancel_button = forms[1].find_elements(By.CSS_SELECTOR, "form a.btn.btn-primary")
cancel_button[0].click()

#select checkbox and make it checked
checkbox = forms[2].find_element(By.XPATH, "//input[@id='Agree']")
checkbox.click()
time.sleep(15)
driver.close()
driver.quit()