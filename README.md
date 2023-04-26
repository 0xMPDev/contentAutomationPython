# contentAutomationPython

## Summary
This package API generates news articles about the Powerball lottery jackpot. It provides information on the latest Powerball jackpot amount, the winning numbers (if applicable), and the state of the winner (if applicable).

## How to setup and run on local machine


## How to use this API
To use the API, simply send a GET request to the following endpoint: http://127.0.0.1:5000/generateArticles

## Response
The response will be a JSON object with the following keys:

    Example:
    {
    "headline": "The Powerball jackpot worth $28 Million has been claimed by a player from NY!",
    "article": "<p>The latest Powerball jackpot was worth $28 Million, and it was won by a lucky player from NY who matched all the winning numbers in the last drawing. The winning numbers were 01, 02, 03, 04, 05, and the Powerball was 06. The next drawing will be on Wednesday, April 27, 2023, with an estimated jackpot of $30 Million.</p>"
    }

## How to improve
1. We might want to handle cases where we'll have more than one jackpot winner. Also, if we have 2 or more winners, they might be in the same state or in different states. So we might add this logic when we store winning_data and also improve content generation with this logic.
2. We could add AI element in conent generation and add OpenAI API or train our own LLM or fine-tune existing open source LLMs
3. We could add rate-limiting in case this would be used on public endpoints
4. Currently we store winning_data in JSON file, we could add a database
5. You could run this on your local machine, but we could also run it as public API service with authentication or run on local network behind firewall
6. We could consider scaling if needed

For more details on the scope, design and requiorements as well as implementation, you can read these articles:
- https://mpdev.hashnode.dev/content-automation
- https://mpdev.hashnode.dev/content-automation-part-2
    
## License
This project is licensed under the MIT License.
