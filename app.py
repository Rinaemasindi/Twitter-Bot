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

# Number of poeple you want to unfollow
LIMIT = 10

twt.search_and_follow('test',29)