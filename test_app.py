from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:30001/register")

# Fill form
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "event").send_keys("DevOps Workshop")

# Submit
submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
submit_btn.click()

# Verify result
if "Registration Successful" in driver.page_source:
    print("✅ Selenium Test Passed: Registration successful")
else:
    print("❌ Selenium Test Failed: Registration message not found")

driver.quit()
