import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

# Proxy Configuration
PROXY = "proxy.soax.com:10002"
PATH = "./chromedriver.exe"

# Set up ChromeOptions with proxy.
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))

# Create a WebDriver instance
driver = webdriver.Chrome() # It automatically download the chrome service on the server

# Open Instagram login page.
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)

#Target the username and password...

# Wait for the username input field to be clickable and locate it by CSS selector
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username.clear()
username.send_keys("tony.9329stark")

# Wait for the password input field to be clickable and locate it by CSS selector
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys("Tajwws@175")

# Locate and click the submit button
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
button.click()
time.sleep(5)

# This is used to find the image and click , (tired when elements is not located)
pyautogui.click('images/notnow1.png')
time.sleep(5)
pyautogui.click('images/notnow2.png')
time.sleep(5)

# Target the input for search.
#Although it can be done with webdriver wait also but it is not working instead axcept pyautogui
# search_box = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder = 'Search']"))).click()
# search_box.clear()
input_search = pyautogui.click('images/search.png')
time.sleep(2)
pyautogui.typewrite("kundan_jwellers_manufacture")
for _ in range(2):
    time.sleep(3)
    pyautogui.press("enter")
time.sleep(5)

#Scroll the window to get all the images
#driver.execute_script("window.scrollTo(1000, 4000)") # the horizontal arg. is almost the 4 time a screen.


# Find the section element using the CSS selector
section_element = driver.find_element(By.CSS_SELECTOR, "#mount_0_0_6c > div > div > ... > div.x1nhvcw1")
time.sleep(5)
# Find all img elements within the section
images_elements = section_element.find_elements(By.TAG_NAME, "img")
# images_elements = driver.find_elements(By.TAG_NAME, "img")
images = [image.get_attribute('src') for image in images_elements]
images = images[ : -2]

print("NO. OF IMGAES", len(images))
driver.get(images[23])
time.sleep(5)
