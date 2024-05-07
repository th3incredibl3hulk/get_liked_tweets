import os 
import requests
import subprocess
from subprocess import PIPE, run

print("Downloading new likes")

# Pulls environment variables, must be set in advance 
twitter_bearer_token = os.environ.get('twitter_bearer_token')
cookie_id = os.environ.get('twitter_cookie_id')
personalization_id = os.environ.get('personalization_id')
twitter_user_id= os.environ.get('twitter_user_id')

# Creates the initial request to fetch liked tweets

url = f"https://api.twitter.com/2/users/{twitter_user_id}/liked_tweets"

payload={}
headers = {
  'Authorization': f'Bearer {twitter_bearer_token}',
  'Cookie': f'guest_id={cookie_id}; guest_id_ads={cookie_id}; guest_id_marketing={cookie_id}; personalization_id="{personalization_id}"'
}
response = requests.request("GET", url, headers=headers, data=payload)

# Writes the response to a file
with open("list_tweets.json", "w") as f:
  f.write(response.text)

# Prints response (commented out because it's a large amount of unformatted text)
#print(response.text)

print("Formatting")

# Uses jq to extract tweet IDs from the response and writes them to tweet_ids.json
os.system("jq '.data | map({ id })' list_tweets.json > tweet_ids.json")

# Function to execute a shell command and capture its output
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Extracts pagination token from the response for subsequent requests
pagination_key_temp = out("jq '.meta | .next_token' list_tweets.json")

print("Outputting")

# Removes quotes and leading/trailing whitespace from pagination key
pagination_key_temp2 = pagination_key_temp.replace('"','')
pagination_key_temp2 = pagination_key_temp2.strip()
print(pagination_key_temp2)

# Creates subsequent loop for additional requests (currently set to run only once)
for i in range(1):

  # Constructs URL for the next request using pagination token
  url = f'https://api.twitter.com/2/users/{twitter_user_id}/liked_tweets?max_results=100&pagination_token={pagination_key_temp2}'

  payload={}
  headers = {
    'Authorization': f'Bearer {twitter_bearer_token}',
    'Cookie': f'guest_id={cookie_id}; guest_id_ads={cookie_id}; guest_id_marketing={cookie_id}; personalization_id="{personalization_id}"'
  }

  # Sends request to Twitter API
  response = requests.request("GET", url, headers=headers, data=payload)
  
  # Writes the response to a file
  with open("list_tweets.json", "w") as f:
    f.write(response.text)

  # Uses jq to extract tweet IDs from the response and appends them to tweet_ids.json
  os.system("jq '.data | map({ id })' list_tweets.json >> tweet_ids.json")

  # Extracts pagination token from the response for the next iteration
  pagination_key_temp2 = out("jq '.meta | .next_token' list_tweets.json")
  pagination_key_temp2 = pagination_key_temp2.replace('"','')
  pagination_key_temp2 = pagination_key_temp2.strip()
  print(pagination_key_temp2)
