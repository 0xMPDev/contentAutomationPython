import datetime
import json
import os
import requests
from bs4 import BeautifulSoup

def getPowerballResults(date):
    url = f'https://www.powerball.com/draw-result?gc=powerball&date={date}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Winning numbers
    winning_numbers = []

    numbers_div = soup.find('div', class_='d-flex col-auto flex-nowrap game-ball-group mx-auto')

    for div in numbers_div.find_all('div'):
        number = div.text.strip()
        if number:
            winning_numbers.append(int(number))

    # Jackpot
    jackpot_element = soup.find("div", class_="estimated-jackpot").find_all("span")[1]
    jackpot = jackpot_element.text.strip()

    # Jackpot Winners
    powerball_winners = soup.find('div', {'class': 'winners-group'})
    if powerball_winners is None:
        jackpot_winners = None
        winning_state = None
    else:
        jackpot_winners = powerball_winners.find('span', {'class': 'winner-type'}, text='JACKPOT WINNERS')
        if jackpot_winners is None:
            jackpot_winners = 0
            winning_state = None
        else:
            jackpot_winners = jackpot_winners.find_previous_sibling().text.strip()
            # Find the <span> tag with class 'winner-location' and get its text
            winning_state = soup.find('span', {'class': 'winner-location'}).get_text().strip()
            print(winning_state)

    # Create a dictionary of data and store to our JSON file
    powerball_data = {
        'winning_numbers': winning_numbers,
        'jackpot': jackpot,
        'jackpot_winners': jackpot_winners,
        'winning_state': winning_state
    }

    # Get the current date
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # Open the JSON file
    if os.path.isfile('powerball_data.json'):
        with open('powerball_data.json', 'r') as f:
            # Load the existing data from the file
            existing_data = json.load(f)
    else:
        # Create an empty dictionary if the file does not exist
        existing_data = {}

    # Check if the data for today already exists in the file
    if today in existing_data:
        print(f"Data for {today} already exists in the file.")
    else:
        # Add the new data to the dictionary
        existing_data[today] = powerball_data

        # Open the JSON file in write mode
        with open('powerball_data.json', 'w') as f:
            # Write the updated data to the file
            json.dump(existing_data, f, indent=4)
