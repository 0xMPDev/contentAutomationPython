from getPowerballResults import getPowerballResults
from getNextDraw import getNextDrawDate
from datetime import datetime, timedelta
from generateArticle import generateArticle

today = datetime.today()

winning_data = getPowerballResults(today)
