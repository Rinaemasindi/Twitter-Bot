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
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(20)

    def login(self,username:str, password:str):
        self.driver.get("https://twitter.com/i/flow/login")
        btn_classes = "css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"
        self.driver.find_element(By.NAME, 'text').send_keys(username)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        return True
    
    def unfollow(self, limit:int):
        return True
    
    def search_and_follow(self,keyword:str, limit:int):
        sleep(15)
        url = "https://twitter.com/search?q="+keyword+"&src=typed_query&f=top"
        self.driver.get(url)
        return True