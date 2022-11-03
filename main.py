from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random
from json import loads

un = ""
pw = ""

def randomFact():
    r=requests.get("https://uselessfacts.jsph.pl/random.json?language=en").text
    r=loads(r)
    if(len(r['text'])>(150-len(un))):
        return randomFact()
    else: return r['text']


while 1:
    try:
        print(uploadGJComment(un,pw,"Random Fact: "+randomFact(),85133487))
        time.sleep(random.randint(30,46))
    except:
        print("err")
