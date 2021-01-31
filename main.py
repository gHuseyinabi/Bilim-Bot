import praw
import json
redditprefs = json.load(open("auth.json","r"))
bakilacak = "inşallah"
son = "bilim"
reddit = praw.Reddit(**redditprefs)

def degistir(body):
    return body.lower().replace(bakilacak,son.lower())

def cevapal(eski,yeni):
    return f"""{eski}?more like {yeni} 😎
    ^ben ^bir ^bot"""


for comment in reddit.subreddit('kgbtr').stream.comments(skip_existing=True):
     cbody = comment.body
     if degistir(cbody) != cbody.lower() and not "bot" in cbody :
         comment.reply(cevapal(cbody,degistir(cbody)))
         print("[Bot] cevap verildi")
     print(cbody)
     comment.author.name