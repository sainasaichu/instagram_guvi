from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

# Open the Instagram page
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
time.sleep(5)  # You may want to use WebDriverWait for a more robust solution

try:
    # Find the first post using a relative XPath
    first_post = driver.find_element(By.XPATH, "//article//div[1]//a")
    first_post.click()

    # Wait for the post to open
    time.sleep(5)

    # Close the post
    close_button = driver.find_element(By.XPATH, "//button[contains(@class, 'wpO6b')]")
    close_button.click()
except Exception as e:
    print("An error occurred:", e)

# Close the browser
driver.quit()
