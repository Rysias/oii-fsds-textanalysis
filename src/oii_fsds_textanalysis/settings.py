# config/settings.py
# Remember to replace the placeholder values with your own Reddit API credentials.
import os

from dotenv import load_dotenv

load_dotenv()
USER_AGENT = os.getenv("USER_AGENT")
if USER_AGENT is None:
    raise ValueError("USER_AGENT is not set in .env file")
API_BASE_URL = "https://api.reddit.com"
RATE_LIMIT_DELAY = 2
