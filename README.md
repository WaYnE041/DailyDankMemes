# DailyDankMemes
**--Scrapes Reddit and Emails Memes from reddit--**


# What You'll Need
> sys library-
- To send in command line arguments
> The PRAW API-
- To scrape Reddit
> smtplib & ssl library-
- To send emails through python
> MIMEMultipart & MIMEText-
- To format the text and html of the emails


# Filling Client_info
**Follow these directions  each Blank space with the appropriate data**

> Email Counter-
- Just used to keep a running counter of how many times function is run(default should be 1). 
- After each run this number increments
- This number will be displayed at end of email's subject line.

> client id, client secret, user_agent-
- To obtain these go to this webpage https://www.reddit.com/prefs/apps
- Create an application
- Give it a name. This name will be what you place under user_agent
- Make your app a script
- Give a description as you see fit
- Leave about url blank
- Place "http://localhost:8080" in the redirect uri section.
- After Creating the application you will get a personal use script and secret key
- Place the personal use script in client_id and the secret key in client_secret

> reddit subreddit: 
- This is the specific subreddit you will be scraping memes from
- Just place the names, do not include "r/"
- Ex. For "r/dankchristianmemes" just put "dankchristianmemes"

> The rest should be self explanatory
   
   
# Extra Information on Email
**For smtp to work with your email you need to turn on "Less secure app access"**
- If you don't your gmail will likely block the emails you send through this program
- Due to this its recommended you use a throwaway email account.


# Filling Subscription_list
**Just populate this file with all the emails you wish to send your memes to.**
- Should be formatted with one email per line.


# Running the Code
**When you run this you will need to run it with 2 command line arguments.** 
- Those being the both the Client_info and subscription_list text files
