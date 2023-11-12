from module.Twitter import Twitter
import os
from dotenv import load_dotenv
load_dotenv()

twt = Twitter()

# Your Twitter username or email
USERNAME = os.getenv("EMAIL")
# Your Twitter password
PASSWORD = os.getenv("PASSWORD")

# # Number of poeple you want to unfollow
# LIMIT = 10

# twt.login(USERNAME, PASSWORD)
# # twt.unfollow(LIMIT)