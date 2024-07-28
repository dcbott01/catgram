import requests
import json
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to print the welcome message
def print_welcome_message():
    print(r"""
 
  _  _   _    ____  _   ___    _   
 | \| | /_\  |_  / /_\ | _ \  /_\  
 | .` |/ _ \  / / / _ \|   / / _ \ 
 |_|\_/_/ \_\/___/_/ \_\_|_\/_/ \_\
                                   

    """)
    print(Fore.GREEN + Style.BRIGHT + "CATGRAM BOT")
    print(Fore.CYAN + Style.BRIGHT + "Jajanin dong orang baik :)")
    print(Fore.YELLOW + Style.BRIGHT + "0x5bc0d1f74f371bee6dc18d52ff912b79703dbb54")
    print(Fore.RED + Style.BRIGHT + "Update Link: https://github.com/dcbott01/catgram")
    print(Fore.BLUE + Style.BRIGHT + "Tukang Rename MATI AJA")

# Function to join the guild
def join_guild(headers):
    join_guild_url = 'https://api.catgram.io/guild/join?guild_id=634&referral_code=v4lv1BXuIT'
    join_guild_payload = {
        'guild_id': '634',
        'referral_code': 'v4lv1BXuIT'
    }

    # Send the POST request to join the guild
    join_guild_response = requests.post(join_guild_url, headers=headers, data=join_guild_payload)

# Function to process account information and perform actions
def process_account(token, process_cards):
    # Define the headers, including the authorization header with the token
    headers = {
        'Authorization': f'Bearer {token}',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    # Join the guild
    join_guild(headers)

    # Define the user information request URL
    user_info_url = 'https://api.catgram.io/user/get/'

    # Send the GET request to /user/get/
    user_info_response = requests.get(user_info_url, headers=headers)

    # Check if the user information request was successful
    if user_info_response.status_code == 200:
        user_info = user_info_response.json().get('data', {})
        
        full_name = user_info.get('full_name', 'Unknown')
        print(f"{Fore.CYAN}[Name] : {Fore.MAGENTA}{full_name}{Style.RESET_ALL}")
    else:
        print(Fore.RED + f'User information request failed with status code {user_info_response.status_code}')
        print(Fore.RED + user_info_response.text)

    # Define the info request URL
    info_url = 'https://api.catgram.io/tap/info'

    # Send the GET request to /tap/info
    info_response = requests.get(info_url, headers=headers)

    # Check if the info request was successful
    if info_response.status_code == 200:
        info_data = info_response.json().get('data', {})
        
        available_taps = info_data.get('available_taps', 0)
        max_taps = info_data.get('max_taps', None)
        balance_coins = info_data.get('balance_coins', None)
        exchange_name = info_data.get('exchange_name', None)
        base_earn_per_hour = info_data.get('base_earn_per_hour', None)
        
        print(f"{Fore.CYAN}[Balance] : {Fore.MAGENTA}{balance_coins}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[Exchange] : {Fore.MAGENTA}{exchange_name}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[Earn Per Hour] : {Fore.MAGENTA}{base_earn_per_hour}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[Available Taps] : {Fore.MAGENTA}{available_taps}{Style.RESET_ALL}")
    else:
        print(Fore.RED + f'Info request failed with status code {info_response.status_code}')
        print(Fore.RED + info_response.text)

    # Use available taps for the tap action
    if available_taps > 0:
        # Define the tap request URL
        tap_url = 'https://api.catgram.io/tap/tap'
        
        # Define the payload for the tap request
        tap_payload = {'count': available_taps}

        # Send the POST request to /tap/tap
        tap_response = requests.post(tap_url, headers=headers, json=tap_payload)

        # Check if the tap request was successful
        if tap_response.status_code == 200:
            print(Fore.GREEN + f'Successfully tapped {available_taps} times!')
        else:
            print(Fore.RED + f'Tap request failed with status code {tap_response.status_code}')
            print(Fore.RED + tap_response.text)

    # Define the daily reward request URL
    daily_reward_url = 'https://api.catgram.io/mission/get-daily-reward'

    # Send the GET request to /mission/get-daily-reward
    daily_reward_response = requests.get(daily_reward_url, headers=headers)

    # Check if the daily reward request was successful
    if daily_reward_response.status_code == 200:
        daily_reward_data = daily_reward_response.json().get('data', {})
        can_claim = daily_reward_data.get('can_claim', False)
        
        if can_claim:
            claim_status = Fore.GREEN + 'Ready to Claim'
        else:
            claim_status = Fore.RED + 'Claimed'
        
        print(Fore.CYAN + f'Daily Claim: {claim_status}')
        
        # If can_claim is True, make the request to claim the daily reward
        if can_claim:
            claim_reward_url = 'https://api.catgram.io/mission/daily-reward'
            
            # Send the POST request to /mission/daily-reward
            claim_reward_response = requests.post(claim_reward_url, headers=headers)
            
            # Check if the reward claim request was successful
            if claim_reward_response.status_code == 200:
                print(Fore.GREEN + 'Daily reward claimed successfully!')
            else:
                print(Fore.RED + f'Reward claim request failed with status code {claim_reward_response.status_code}')
                print(Fore.RED + claim_reward_response.text)
    else:
        print(Fore.RED + f'Daily reward request failed with status code {daily_reward_response.status_code}')
        print(Fore.RED + daily_reward_response.text)

    # Process the card list only if process_cards is True
    if process_cards:
        # Define the card list request URL
        card_list_url = 'https://api.catgram.io/card/list'

        # Send the GET request to /card/list
        card_list_response = requests.get(card_list_url, headers=headers)

        # Check if the card list request was successful
        if card_list_response.status_code == 200:
            print(Fore.GREEN + 'Card list request was successful!')
            print(Fore.YELLOW + '-' * 40)
            cards = card_list_response.json().get('data', [])
            
            # Print details for each card if available
            for card in cards:
                if card.get('is_available') == True:  # Only process available cards
                    print(Fore.YELLOW + f"ID: {card.get('id', 'N/A')}")
                    print(Fore.YELLOW + f"Name: {card.get('name', 'N/A')}")
                    print(Fore.YELLOW + f"Price: {card.get('price', 'N/A')}")
                    print(Fore.YELLOW + f"Profit per Hour: {card.get('profit_per_hour', 'N/A')}")
                    print(Fore.YELLOW + f"Level: {card.get('level', 'N/A')}")
                    
                    # Check conditions for unlocking the card
                    if card.get('check_status', 0) == 1:
                        unlock_card(card['id'], headers)
                        # Add a delay of 2 seconds after unlocking each card
                        time.sleep(2)
                        
                    # Upgrade the available card
                    upgrade_card(card['id'], headers)
                    # Add a delay of 2 seconds after upgrading each card
                    time.sleep(1)
                    print(Fore.YELLOW + '-' * 40)
        else:
            print(Fore.RED + f'Card list request failed with status code {card_list_response.status_code}')
            print(Fore.RED + card_list_response.text)

# Function to unlock a card
def unlock_card(card_id, headers):
    unlock_url = 'https://api.catgram.io/card/unlock'
    unlock_payload = {'card_id': card_id}

    # Send the POST request to /card/unlock
    unlock_response = requests.post(unlock_url, headers=headers, json=unlock_payload)

    # Check if the unlock request was successful
    if unlock_response.status_code == 200:
        unlock_data = unlock_response.json()
        print(Fore.GREEN + f'Card {card_id} unlocked successfully!')
    else:
        print(Fore.RED + f'Failed to unlock card {card_id} with status code {unlock_response.status_code}')
        print(Fore.RED + unlock_response.text)

# Function to upgrade a card
def upgrade_card(card_id, headers):
    upgrade_url = 'https://api.catgram.io/card/upgrade'
    upgrade_payload = {'card_id': card_id}

    # Send the POST request to /card/upgrade
    upgrade_response = requests.post(upgrade_url, headers=headers, json=upgrade_payload)

    # Check if the upgrade request was successful
    if upgrade_response.status_code == 200:
        print(f"{Fore.YELLOW}Upgrade Status : {Fore.GREEN}Card upgraded successfully{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Upgrade Status : {Fore.RED}Failed. Not Enough Balance{Style.RESET_ALL}")

# Main script loop
def main():
    # Print the welcome message
    print_welcome_message()
    
    # Ask user if they want to process the card list
    process_cards_input = input(Fore.YELLOW + "Do you want to process the card list? This for Unlock and Upgrade Features (yes/no): ").strip().lower()
    process_cards = process_cards_input == 'yes'

    while True:
        with open('token.txt', 'r') as file:
            initData_lines = file.readlines()

        # Process each account
        for index, initData in enumerate(initData_lines):
            initData = initData.strip()
            if initData:
                print(f"{Fore.YELLOW}====== Processing account {index + 1}/{len(initData_lines)} ======")
                remaining_seconds = process_account(initData, process_cards)
                time.sleep(2)  # Adding a delay of 2 seconds between processing accounts

        print(f"{Fore.GREEN}====== Semua Akun Telah Di Proses ======")

        # Calculate and print remaining time
        hours = 0
        minutes = 30
        seconds = 0
        print(f"{Fore.CYAN}Waiting {hours} hours, {minutes} minutes, and {seconds} seconds before re-processing...{Style.RESET_ALL}")

        # Wait for 60 minutes before the next loop
        time.sleep(30 * 60)  # Sleep for 30 minutes

# Run the main script
if __name__ == "__main__":
    main()
