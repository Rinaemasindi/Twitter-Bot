from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

class Twitter:
    def __init__(self):
        fireFoxOptions = Options()
        # fireFoxOptions.add_argument("--headless")

        self.driver = webdriver.Firefox(options=fireFoxOptions)

    def login(self,username:str, password:str):
        self.driver.get("https://twitter.com")
        sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span").click()
        wait =  WebDriverWait(self.driver, 20)
        sleep(5)
        next_button_selector = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
        username_input_selector = 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]'
        
        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_input_selector)))
        # password_input = self.driver.find_element(By.NAME, 'text')
        username_input.send_keys(username)
        sleep(2)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, next_button_selector)))
        self.driver.execute_script("arguments[0].click();", next_button)
        return True
    
    def unfollow(self, limit:int):

        return True