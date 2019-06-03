import quandl
#I have my API key set in a text file and this line configures it by reading an 'api-key.txt' file
quandl.ApiConfig.api_key = open('api-key.txt', 'r').readline()
import datetime

#Sets the variables for the date parameters
now = datetime.datetime.now()
start_date = '2015-12-31'
end_date = now.strftime("%Y-%m-%d")

#Getting the data from the specific columns (ticker, data, and adj_close) of the listed tickers/stocks
#within the given date range. Padinate will extend the limit of rows from 10,000 to 1,000,000.
data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'], 
                        qopts = { 'columns': ['ticker', 'date', 'open', 'high','low', 'close', 'volume', 'adj_close'] }, 
                        date = { 'gte': start_date, 'lte': end_date }, 
                        paginate=True)

#Sets the date as the index
new = data.set_index('date')

print(new.head())
