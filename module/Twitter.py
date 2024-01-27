# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from seleniumwire.utils import decode
import json
from time import sleep

class Twitter:
    
    def __init__(self):
        # fireFoxOptions = Options()
        # # fireFoxOptions.add_argument("--headless")
        # self.driver = webdriver.Firefox(options=fireFoxOptions)
        # self.wait = WebDriverWait(self.driver, 10)
        # self.driver.implicitly_wait(20)
        service = Service(executable_path=r'./chromedriver.exe')
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self,username:str, password:str):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        btn_classes = "css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"
        self.driver.find_element(By.NAME, 'text').send_keys(username)
        sleep(3)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        sleep(3)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(3)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        return True
    
    def unfollow(self, limit:int):
        return True
    
    def search_tweets(self,keyword:str):
        sleep(5)
        url = "https://twitter.com/search?q="+keyword+"&src=typed_query&f=top"
        self.driver.get(url)
        print('here')
        sleep(5)
        for request in self.driver.requests:
            if('https://twitter.com/i/api/graphql/' in request.url and 'SearchTimeline' in request.url):
                body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                print(body)
            
        return True

