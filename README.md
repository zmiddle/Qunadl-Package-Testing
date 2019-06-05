# Qunadl-Package-Testing
Testing the Quandl package in Python to pull stock data from the WIKI/PRICES table.

![Screen shot](https://github.com/zmiddle/Qunadl-Package-Testing/blob/master/APPL%20Output.JPG)

### What I learned
* Reading text from other files and using the output as somewhat automated process; For example I can have multiple API keys in my 'api-key.txt' file and just change which line the open method uses.
* Configuring the API key specificly for the Quandl package, other packages or API usually just have the key inserted in the request.
* Setting parameters for the requested tables and pulling the data from a set date range.

### Going forward
* I will have to play around with the package some more, but it seems well documented will plenty of resources.
* Some tweeks in the code could be to allow the user to set a starting date or have preset ranges (past 24 hours, 3 days, 3 months, etc.) for the user to select.
* Also an input for what stock ticker that the user would want is an improvemnt, but I would have to also add in an exception check for the request because the API does not have a complete list of stocks (for example UBER was not listed).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
