from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def lauchbrowser():
    driver_path = Service("C:\\example\\example\\example\\chromedriver.exe") #Enter your own driver location
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=driver_path,options=options)
    driver.get('https://example.com.mx')
    

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('smartwatch')
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/div/div[2]/aside/section/div[12]/ul/li[1]/a')))
    url = driver.find_element_by_xpath('/html/body/main/div/div[2]/aside/section/div[12]/ul/li[1]/a').get_attribute('href')
    driver.get(url)
    
    
if __name__ == '__main__':
    lauchbrowser()