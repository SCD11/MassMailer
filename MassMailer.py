import praw

reddit = praw.Reddit(client_id="8JXEHzLfCkVJFA",
                     client_secret="azBcht6nHeOOKey61dC4U6JSZI0",
                     user_agent="A massMailer app by u/Hoisted_Variable",
                     username="onebitboi",
                     password="KryptonKnight36")

print(reddit.read_only)  # Output: False

subreddit_name = input("Enter the name of the Subreddit : ")

subreddit = reddit.subreddit("IndiaSpeaks")

list_users = []


for submissions in subreddit.hot(limit = 10):
    print(submissions.author)#to get the author of the submission
    submissions.comments.replace_more(limit=10)
    for comment in submissions.comments.list():
        print(comment.author)#to get to know the author name of the comments

print(list_users)
# reddit.redditor("kryptonKnightXi").message("subject of the mail","Content of the mail from r/HindiLanguage")#to send private message to the users


#Just let me bullet point following things
#So this is what we want
#send this mod mail to the users who are from r/IndiaSpeaks r/Chodi r/IndianDiscussion
#To do this we have to go through the people who are commenting on the top 100 posts and extract their username and send them this mail right
#At the same time we have to maintain a database that these members were already sent this mod mail

#Now, this is what I have accomplished:
#How to fetch the author names of the reddit submissions/comments
#How to send private message to the reddit users

#Now, this is what I need to do:
#First create a file that keeps track of every contacted user
#Now, read through each user and compare with new user that you fetched from the online
#If the users are same ignore
#else, in the "temp.txt" upload the usersname and send him the "modmail"
#at the end upload the users from temp.txt to "ContactedUsers.txt"
#clear the contents of temp.txt