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
        # for firefox
        # fireFoxOptions = Options()
        # fireFoxOptions.add_argument("--headless")
        # self.driver = webdriver.Firefox(options=fireFoxOptions)
        # self.driver.implicitly_wait(20)
        
        #for chrome
        service = Service(executable_path=r'./chromedriver.exe')
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(20)

    def login(self, username: str, password: str):
        """
        Log in to Twitter using the provided username and password.
        
        Args:
        - username: str, the username to log in with
        - password: str, the password to log in with
        
        Returns:
        - bool, True if the login was successful, False otherwise
        """
        btn_classes = "css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"
        login_url = "https://twitter.com/login"
                
        self.driver.get(login_url)
        self.driver.find_element(By.NAME, 'text').send_keys(username)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_elements(By.XPATH, "//div[@class='"+btn_classes+"']")[2].click()
        sleep(5)
        print('logged in successfully')
        return True
    
    def search_tweets(self, keyword: str, from_date=None, to_date=None) -> bool:
        """
        Searches for tweets based on a keyword within a specified date range.

        Args:
            keyword (str): The keyword to search for in tweets.
            from_date (str): The start date for the search eg 2024-01-01.
            to_date (str): The end date for the search eg 2024-01-28.

        Returns:
            bool: True if the search was successful, False otherwise.
        """
        # Construct the URL based on the provided keyword and date range
        if from_date and to_date:
            url = f"https://twitter.com/search?q={keyword}%20(%40%23{keyword})%20until%3A{to_date}%20since%3A{from_date}&src=typed_query"
        else:
            url = f"https://twitter.com/search?q={keyword}&src=typed_query&f=top"
        
        # Open the URL in the driver and wait for 5 seconds
        self.driver.get(url)
        sleep(2)
        print('searched successfully')

        max_number_of_requests = 10
        requests_count = 0
        tweets = []
        consecutive_same_requests = 0  # Counter for consecutive same requests
        
        # Perform scrolling and count API requests
        while requests_count <= 25:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_requests_count = sum(1 for request in self.driver.requests if 'https://twitter.com/i/api/graphql/' in request.url and 'SearchTimeline' in request.url)
            print(f"Number of requests: {new_requests_count}")
            
            # Check for consecutive same requests
            if new_requests_count == requests_count:
                consecutive_same_requests += 1
            else:
                consecutive_same_requests = 0  # Reset the counter if requests_count changes
            
            requests_count = new_requests_count
            
            if consecutive_same_requests >= max_number_of_requests:
                print("Exiting the loop due to consecutive same requests.")
                break
        
        # Extract tweets from API responses and save to a JSON file
        for request in self.driver.requests:
            if ('https://twitter.com/i/api/graphql/' in request.url and 'SearchTimeline' in request.url):
                body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                body_dict = json.loads(body.decode('utf-8'))
                twitter_data = body_dict['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]
                if 'entries' in twitter_data:
                    tweets_entries = body_dict['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries']
                    tweets.append(tweets_entries)

        print(len(tweets))
        json_data = json.dumps(tweets, indent=2)
        with open('data.json', "w") as json_file:
            json_file.write(json_data)

        return True


