from module.Twitter import Twitter
import os
from dotenv import load_dotenv
load_dotenv()

twt = Twitter()

# Your Twitter username or email
USERNAME = os.getenv("EMAIL")
# Your Twitter password
PASSWORD = os.getenv("PASSWORD")

twt.login('devrinae', 'ZZk7ezzJtzytP42')

twt.search_tweets('ANC')