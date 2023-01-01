from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument(
    "no-sandbox")  # code crashes if this line is commented out
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",
                      value="id_password").send_keys("automatedautomated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys(Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2)
  print(driver.current_url)

  return None


print(main())
