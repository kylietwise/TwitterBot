# TwitterBot

I built a twitter bot that replies to four commands: "help", "info", "inspiration", and "quote" with the bots username @kyliewise20 tagged. 

For tweets that mention the bot with keywords help or info my bot replies with information about how to use the bot.

For tweets that mention the bot with keywords inspiration or quote my bot replies with a quote from a quote API. The quote API is "https://api.quotable.io/random" which is a link that randomly pulls a quote and all of it's information in a JSON. I then extracted just the quote and author and put it in my desired format to tweet back as a reply. 

This bot was built on my local computer, however I also hosted it on an API, Python Anywhere. The reason it lives here is so that it can be sent/accessed by other computers easily and if I want to have it tweet or turn on at certain times throughout the day, I would be able to enable this through the Python Anywhere API.


Limitations:

Unfortunately, the bot only functions when you have the API Python Anywhere code or FinalBotCode running on your local device. Thus, when both off these are off, the bot is not functioning. If you need the bot to run, email @ktw5nb@virginia.edu to turn on Python Anywhere. 
