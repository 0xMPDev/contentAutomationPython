from datetime import date, datetime, timedelta

# Define a function to get the date of the next Powerball draw.
def getNextDrawDate():
    # Get today's date.
    today = date.today()
    # Calculate the number of days until the next Powerball draw.
    # The next draw is on the first of the next three days (Monday, Wednesday, or Saturday).
    days_ahead = (2 - today.weekday()) % 3
    # Calculate the date of the next Powerball draw.
    next_draw_date = today + timedelta(days=days_ahead)
    # Format the date as a string in the YYYY-MM-DD format and return it.
    return next_draw_date.strftime('%Y-%m-%d')
