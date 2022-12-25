from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random
from json import loads
from threading import Thread
from owo import owoify
from animeAPI import getAnimeChar

un = ""
pw = ""

balls = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'You are cringe, do not ask again or there will be consequences.']

def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=random.randint(0,100)
    if(com.startswith("!percent")):
        uploadGJComment(un,pw,f"{perc}%",perc,level)
        print("Executed percent")
    elif(com.startswith("!owo")):
        c=com.split("!owo ")
        try:
            cc=owoify(c[1])
            uploadGJComment(un,pw,f"@{u} {cc}",perc,level)
            print("Executed owo")
        except:
            return
    elif(com.startswith("!demon")):
        c=com.split("!demon ")
        d=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?limit=100").text)
        d2=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?after=100").text)
        d3=d+d2
        try:
            cc=int(c[1])-1
            ccc=f"#{d3[cc]['position']}: {d3[cc]['name']} by {d3[cc]['publisher']['name']}, verified by {d3[cc]['verifier']['name']}"
            uploadGJComment(un,pw,f"@{u} {ccc}",perc,level)
            print("Executed demon")
        except:
            return
    elif(com.startswith("!8ball")):
        lol=random.choice(balls)
        try:
            uploadGJComment(un,pw,f"@{u} {lol}",perc,level)
            print("Executed balls")
        except:
            return
    elif(com.startswith("!stats")):
        c=com.split("!stats ")
        try:
            cc=c[1]
            shtats=loads(requests.get(f"http://gdbrowser.com/api/profile/{cc}").text)
            ccc=f"@{u}, {c[1]} has {shtats['stars']} stars, {shtats['diamonds']} diamonds, {shtats['coins']} coins, {shtats['userCoins']} user coins, {shtats['demons']} demons and {shtats['cp']} CP."
            uploadGJComment(un,pw,f"{ccc}",perc,level)
            print("Executed shtats")
        except:
            return
    elif(com.startswith("!anime")):
        c=com.split("!anime ")
        num=0
        try:
            cc=c[1]
            num=int(cc)
        except:
            num=0
        char=getAnimeChar(num)
        try:
            cn=char['Character']['name']['userPreferred']
            ca=char['Character']['age']
            cg=char['Character']['gender']
            if(ca==None):
                ca="Unknown"
            if(cg==None):
                cg="Unknown"
            ccc=f"Name: {cn}, Age: {ca}, Gender: {cg}."
            uploadGJComment(un,pw,f"@{u} {ccc}",perc,level)
            print("Executed anime")
        except:
            return
    elif(com.startswith("!source")):
        uploadGJComment(un,pw,f"@{u} You can find my source code here: https://github.com/HarmOnGitHub/SimpleGDBot",perc,level)
        print("Executed source")
    

lvl=input("Level id: ")

while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(2)
    except:
        print("err")
