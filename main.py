import praw
import json
redditprefs = json.load(open("auth.json","r"))
bakilacak = "inşallah"
son = "bilim"
reddit = praw.Reddit(**redditprefs)
test = False
def degistir(body):
    return body.lower().replace(bakilacak,son.lower())

def cevapal(eski,yeni):
    return f"""{eski}?more like {yeni} 😎\n
    ^ben ^bir ^bot\n
    ^[github](https://github.com/gHuseyinabi/Bilim-Bot/)"""

if test:
    stream = reddit.subreddit('testyapiyorum').stream
else:
    stream = reddit.subreddit('kgbtr').stream
for comment in stream.comments(skip_existing=True):
     cbody = comment.body
     if degistir(cbody) != cbody.lower() and not "bot" in cbody :
         comment.reply(cevapal(cbody,degistir(cbody)))
         print("[Bot] cevap verildi")
     print(cbody)
     comment.author.name