from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\KIIT\\Desktop\\selenium\\chromedata")
driver = webdriver.Chrome('chromedriver', options=options)
driver.get("https://www.1mg.com/drugs-all-medicines")
# a = driver.find_elements(By.CLASS_NAME, "style__product-name___HASYw")
a = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "style__product-name___HASYw")))
link = a[0].get_attribute('href')
# driver.execute_script('''window.open("'''+link+'''", "_blank");''')
# driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL+"w")
driver.switch_to.new_window('tab')
driver.get(link)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/h1")))
print(element.get_attribute('innerHTML'))
driver.quit()
