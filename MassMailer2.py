import praw
from datetime import date

class MassMailer():
    def __init__(self):
        self.reddit = praw.Reddit(client_id="ZoBzriJtuUg1xg",
                     client_secret="95irMKVAlfnxiY7OZqWnQXeKhYY",
                     user_agent="A massMailer app by u/Hoisted_Variable",
                     username="hoisted_variable",
                     password="KryptonKnight36")

        self.subs = ["Chodi","Indianews","indiadiscussion","politicalhinduism","Hindi"]#subs that need the handling
        self.contactedUsers = open("./ContactedUsers/ContactedUsers.txt","r")#opening the file containing the list of the users already contacted
        self.tempUsers = open("./TemporaryFiles/"+str(date.today())+".txt","w")#temporary list of new users who are accessed
        self.tempUsersList = []

    def checkContact(self, username):

        for line in self.contactedUsers:
            if (line.strip()) == str(username):
                return False

        self.contactedUsers.seek(0)
        return True


    def sendPrivateMessage(self, username):
        message = """Dear sir/madam,
        My name is Umesh Rathore and I am a Hindi educator. For years, Hindi has experienced distortion and taken on words from Urdu 
        -so much so that it is losing its identity. It is with great sadness I say that Shudh Hindi has been pushed out to a few select 
        spaces while a strange mix of Hindi/Urdu has been made mainstream.
        To promote and preserve the original Hindi, I invite you to r/HindiLanguage. 
        It is right now a small but friendly place for Hindi learners and educators.
        Regards,
        U.M. Rathore
        """
        self.reddit.redditor(username).message("Join us at r/HindiLanguage",message)


    def getUsers(self, subreddit):
       
        for submissions in subreddit.hot(limit=50):
            print(submissions.author)
            try:
                if self.checkContact(str(submissions.author)) and (str(submissions.author) not in self.tempUsersList):
                    self.tempUsers.write(str(submissions.author)+"\n")
                    # self.sendPrivateMessage(str(submissions.author))
                    self.tempUsersList.append(str(submissions.author))
                submissions.comments.replace_more(limit=None)
                for comment in submissions.comments.list():
                    try:
                        print(comment.author)
                        if self.checkContact(str(comment.author)) and (str(comment.author) not in self.tempUsersList):
                            # self.sendPrivateMessage(str(comment.author))
                            self.tempUsers.write(str(comment.author)+"\n")
                            self.tempUsersList.append(str(comment.author))
                    except:
                        continue
            except:
                continue
        

    def getSubredditInstance(self):
        for sub in self.subs:
            subreddit = self.reddit.subreddit(sub)
            print("="*10 + sub)
            self.getUsers(subreddit)


    def updateContactedDatabase(self):
        self.contactedUsers.close()
        self.tempUsers.close()
        contacts = open("./ContactedUsers/ContactedUsers.txt","a")
        tempUsers = open("./TemporaryFiles/"+str(date.today())+".txt")
        
        for line in tempUsers:
            contacts.write(line)
        
        tempUsers.close()
        contacts.close()


    def checkCode(self):
        print("Yeah It's Working!")


if __name__ == "__main__":
    obj = MassMailer()
    obj.checkCode()
    # obj.sendPrivateMessage("onebitboi")
    obj.getSubredditInstance()
    obj.updateContactedDatabase()    