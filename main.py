import re
from dotenv import load_dotenv
import requests
from pprint import pprint
import os
load_dotenv()

WEBSITE_URL = f"{os.getenv('API_URL')}"
print(WEBSITE_URL)

data = requests.get(url=WEBSITE_URL).json()

# for states in data: this gives us the number of statistics for each state
#     pprint(data[states]['total'])

name_list = [state_name for state_name in data]
print(len(name_list),name_list)