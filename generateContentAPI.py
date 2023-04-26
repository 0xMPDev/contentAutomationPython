from flask import Flask, jsonify
from datetime import datetime, timedelta
from generatingContent.getNextDraw import getNextDrawDate
from generatingContent.generateArticle import generateArticle
import json

app = Flask(__name__)

# Load the data from the JSON file
with open('powerballData/powerball_data.json', 'r') as f:
    existing_data = json.load(f)

@app.route('/generateArticles', methods=['GET'])
def get_winning_data():
    today = datetime.today()

    # Get stored winning data
    winning_data = existing_data.get(str(today.date()), {})

    # Call the function to get the next draw date
    nextDrawDate = getNextDrawDate()

    # Generate Content
    article = generateArticle(winning_data, nextDrawDate)

    # Return the data in JSON format
    return jsonify({'article': article})

if __name__ == '__main__':
    app.run()
