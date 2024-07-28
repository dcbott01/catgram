import requests
import json
from urllib.parse import parse_qs, unquote

# Function to perform the login request for each account
def process_account(initdata):
    # Parse the initdata string
    parsed_data = parse_qs(initdata)

    # Extract data from parsed_data
    query_id = parsed_data['query_id'][0]
    user_data = json.loads(unquote(parsed_data['user'][0]))
    auth_date = parsed_data['auth_date'][0]
    hash_value = parsed_data['hash'][0]

    # Define the login payload using extracted data
    login_payload = {
        "auth_date": auth_date,
        "hash": hash_value,
        "query_id": query_id,
        "user": user_data
    }

    # Define the login request URL
    login_url = 'https://api.catgram.io/auth/telegram-login'

    # Define the headers for the login request
    login_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Origin': 'https://play.catgram.io',
        'Pragma': 'no-cache',
        'Referer': 'https://play.catgram.io/',
        'Sec-CH-UA': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    # Send the POST request to login
    login_response = requests.post(login_url, headers=login_headers, data=json.dumps(login_payload))

    # Check if the login request was successful
    if login_response.status_code == 200:
        print('Login request was successful!')
        login_data = login_response.json()
        # Extract the token
        token = login_data['data']['token']
        full_name = login_data['data']['user_info']['full_name']
        print(f'Full Name: {full_name}')
        
        # Save the token to token.txt
        with open('token.txt', 'a') as token_file:
            token_file.write(f'{token}\n')
    else:
        print(f'Login request failed with status code {login_response.status_code}')
        print(login_response.text)

# Read initdata from query.txt and process each line as a separate account
with open('query.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        initdata = line.strip()
        if initdata:  # Process only non-empty lines
            process_account(initdata)
