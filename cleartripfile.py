from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.cleartrip.com/flights")

# Close the flex element if it exists
try:
    flex = driver.find_element(By.CSS_SELECTOR, "body > div.p-fixed.l-0.r-0.b-0.t-0.flex.flex-center.flex-middle.z-70 "
                                                "> div > div > div > "
                                                "div.bg-white.o-hidden.d-flex.flex-column.brLoginNew-4 > div > "
                                                "div.pt-6.pb-6.flex.flex-top.flex-between > "
                                                "div.px-1.flex.flex-middle.nmx-1.pb-1 > svg")
    if flex:
        flex.click()
        print("Closed the flex element")
except Exception as e:
    print(f"Error: {e}")

# Set departure city, destination city, and date
dept_ct = "BOM"
dest_ct = "DEL"
date_time = "Sun, Apr 21"

# Wait for some time to ensure the page is loaded
try:
    date_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div["
                                              "2]/div[3]/div/div/div[1]/input"))
    )
except Exception as e:
    print(f"Error: {e}")
# Enter departure city
try:
    dept_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div["
                                                 "1]/div[2]/div[3]/div/div/div[1]/input")
    if dept_element:
        dept_element.send_keys(dept_ct)
        time.sleep(2)  # Adding a small delay to ensure dropdown options load
        driver.find_element(By.CLASS_NAME, "m-1").click()
        print(f"Entered departure city: {dept_ct}")
except Exception as e:
    print(f"Error: {e}")

# Enter destination city
try:
    dest_element = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div["
                                       "3]/div/div/div[3]/input")
    if dest_element:
        dest_element.send_keys(dest_ct)
        time.sleep(2)  # Adding a small delay to ensure dropdown options load
        driver.find_element(By.CLASS_NAME, "m-1").click()
        print(f"Entered destination city: {dest_ct}")
except Exception as e:
    print(f"Error: {e}")

# CLICKING ON DATE SECTION
try:
    date_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/button[1]"))
    )
    date_element.click()
    print(f"CLICK date: {date_time}")
except Exception as e:
    print(f"Error: {e}")

time.sleep(5)
#selecting the date
try:
    date_e = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[4]/div/div[1]/div/div/div/ul/div[3]/div/div[2]/div[1]/div[3]/div[3]/div[7]"))
    )
    date_e.click()
    print(f"selected: {date_time}")
except Exception as e:
    print(f"Error: {e}")

time.sleep(5)
#clicking on the search button
try:
    search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[4]/div/div[2]")
    search.click()
    print("clicked search button")
except Exception as e:
    print(f"Error: {e}")
# Wait for some time to observe the changes
time.sleep(20)

# Close the browser
driver.quit()
