#! python3
import sys
import praw
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText as text

#Why Did I Do This?
#To Measure The Limits of My Abilities"
class ImplementInfo:
    counter= " "
    personal_use_script= " "
    secret_key= " "
    reddit_app= " "
    reddit_user= " "
    reddit_password= " "
    sub_reddit= " "
    Email_address= " "
    Email_password = " "
    Blessings22 = " "
    Blessings23 = " "
    rcptlist = []
    def __init__(self, data):
        self.counter = data[1]
        self.personal_use_script = data[3]
        self.secret_key = data[5]
        self.reddit_app = data[7]
        self.reddit_user = data[9]
        self.reddit_password = data[11]
        self.sub_reddit = data[13]
        self.Email_address = data[15]
        self.Email_password = data[17]

    def scrapeReddit(self):
        reddit = praw.Reddit(client_id=self.personal_use_script,
                             client_secret=self.secret_key,
                             user_agent=self.reddit_app,
                             username=self.reddit_user,
                             password=self.reddit_password)

        subreddit = reddit.subreddit(self.sub_reddit)

        for submission in subreddit.top('day', limit=1):
            print(submission.title)
            print(submission.url)
            self.Blessings22 = submission.title
            self.Blessings23 = submission.url

    def getSubsList(self):
        with open(sys.argv[2], 'r') as file:
            sublist = file.read().splitlines()
        return sublist

    def sendEmail(self):
        port = 465

        self.rcptlist = self.getSubsList()
        receivers = ','.join(self.rcptlist)

        msg = MIMEMultipart('mixed')
        #msg['Subject'] = 'Surely He will save you from the fowlers snare and from these deadly memes. Test #' + self.counter
        msg['Subject'] = 'In the beginning was the Meme, and the Meme was with God: Day ' + self.counter
        msg['From'] = self.Email_address
        msg['To'] = receivers

        memeDescription = """
            <html>
                <head>
                    <style type="text/css" media="screen">
                        p.text{ 
                            font-size: 200%; 
                            font-family: 'Garamond';
                            text-align: center;
                        } 
                    </style>
                </head>
                <body>
                    <p class = 'text'>""" + self.Blessings22 + """</p>
                </body>
            </html>
            """

        msg.attach(text(memeDescription, 'html', 'utf-8'))
        msg.attach(text('<html><body><p><img src = "' + self.Blessings23 + '"></p></body></html>', 'html', 'utf-8'))
        msg.attach(text('This meme was found and emailed to you automatically, courtesy of the Python programming language\n Warning: Memes are not curated.\n\n', 'plain', 'utf-8'))
        msg.attach(text('Why Did I Do This? To Measure The Limits of My Abilities', 'plain', 'utf-8'))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.Email_address, self.Email_password)
            server.sendmail(self.Email_address, self.rcptlist, msg.as_string())

    def updatecounter(self, data):
        counterInc = int(self.counter)
        counterInc +=1
        self.counter = str(counterInc)
        data[1] = self.counter

        with open(sys.argv[1], 'w') as file:
            file.write('\n'.join(data) + '\n')

with open(sys.argv[1], 'r') as file:
    data = file.read().splitlines()

appInfo = ImplementInfo(data)
appInfo.scrapeReddit()
appInfo.sendEmail()
appInfo.updatecounter(data)

print(" \n We Did it \n")