from selenium import webdriver
import time

tag = '?rel=0&amp;autoplay=1'

DRIVER = r'D:\Downloads\Google\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(DRIVER)
driver.get('https://www.youtube.com/embed/OWbI6WtlI-k'+tag)
time.sleep(2)
screenshot = driver.save_screenshot(r'D:\my_screenshot.png')
driver.quit()
