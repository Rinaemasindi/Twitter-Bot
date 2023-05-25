from module.Twitter import Twitter
twt = Twitter()

# Your Twitter username or email
USERNAME = "naquwoso@ai1.lol"
# Your Twitter password
PASSWORD = 'mQnqD"D]Wc%GRa7'

# Number of poeple you want to unfollow
LIMIT = 10

twt.login(USERNAME, PASSWORD)
# twt.unfollow(LIMIT)