import random

def generateArticle(winning_data, next_drawing_date):

    if winning_data['jackpot_winners'] > 0:
    # Set of templates for articles with winning headlines
        headlines = ["Powerball jackpot won by lucky ticket holder in [STATE]!", 
                     "[STATE] player wins Powerball jackpot worth [AMOUNT]!",
                     "Jackpot alert: [AMOUNT] Powerball prize won by player in [STATE]!",
                     "Powerball drawing results in big win for [STATE] player!",
                    "[STATE] resident hits jackpot with winning Powerball numbers!"]
        articles = ["A lucky Powerball player from [STATE] has won the jackpot worth [AMOUNT]!",
                    "The Powerball jackpot worth [AMOUNT] has been won by a player from [STATE]!",
                    "[STATE] is celebrating after a player won the Powerball jackpot worth [AMOUNT]!",
                    "Congratulations to the Powerball winner from [STATE] who has won [AMOUNT]!",
                    "The Powerball jackpot worth [AMOUNT] has been claimed by a player from [STATE]!"]
    else:
        # Set of templates for articles with no winning headlines
        headlines = ["Powerball jackpot rolls over to [AMOUNT] for next drawing!",
                     "No winner in latest Powerball drawing; jackpot grows to [AMOUNT].",
                     "Powerball numbers drawn, but no jackpot winner this time.",
                     "Next Powerball drawing offers [AMOUNT] prize after no jackpot winner.",
                    "Powerball jackpot continues to climb; next drawing worth [AMOUNT]."]
        articles = ["The Powerball jackpot has rolled over to [AMOUNT] for the next drawing!",
                    "No one won the Powerball jackpot in the latest drawing, which has grown to [AMOUNT].",
                    "Although no one won the Powerball jackpot this time, players can try their luck again in the next drawing for a chance to win [AMOUNT]!",
                    "The next Powerball drawing will offer a jackpot worth [AMOUNT] after there was no winner in the previous drawing.",
                    "The Powerball jackpot continues to climb and is now worth [AMOUNT]. Don't miss your chance to win big!"]

    # Replace placeholders in the templates with actual data
    if winning_data['jackpot_winners'] > 0:
        headline = random.choice(headlines).replace("[STATE]", winning_data['winning_state'])
        article = random.choice(articles).replace("[STATE]", winning_data['winning_state']).replace("[AMOUNT]", winning_data['jackpot'])
    else:
        #amount = winning_data['jackpot'].replace("$", "").replace(" Million", "000000")
        #amount = amount.replace(" Million", "")
        #amount_formatted = "${:,.0f}".format(float(amount))

        amount = winning_data['jackpot']
        headline = random.choice(headlines).replace("[AMOUNT]", amount)
        article = random.choice(articles).replace("[AMOUNT]", amount)

    # Generate HTML version of the article
    html_article = "<h1>" + headline + "</h1></ br></ br>"
    html_article += "<p>" + article + "</p></ br>"
    html_article += "<p><strong>Next Drawing would be on:</strong> " + next_drawing_date + "</p>\n"
    html_article += "<p><strong>Estimated Jackpot is:</strong> " + amount + "</p>"

    # Return the generated article and HTML
    return {"headline": headline, "article": html_article}
