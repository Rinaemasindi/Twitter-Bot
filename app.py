from module.Twitter import Twitter
import os
from dotenv import load_dotenv
load_dotenv()

twt = Twitter()

# Your Twitter username or email
USERNAME = os.getenv("EMAIL")
# Your Twitter password
PASSWORD = os.getenv("PASSWORD")

twt.login(USERNAME, PASSWORD)

twt.search_tweets('UFC', '2024-01-01', '2024-01-28')