
import random

#Substitutions
substitution = {"r":"w",
"l":"w",
"R":"W",
"L":"W",
"no":"nu",
"has":"haz",
"have":"haz",
"you":"uu",
"the":"da",
"R":"W",
"The":"Da" }
#Prefixes
prefix = ["<3 ",
"H-hewwo?? ",
"HIIII! ",
"Haiiii! ",
"Huohhhh. ",
"OWO ",
"OwO ",
"UwU ",
"88w88 ",
"H-h-hi, ",]
#Suffixes
suffix = [" :3",
" UwU",
" >_>",
" ^_^",
"..",
" Huoh.",
" ^-^",
" ;_;",
" xD",
" x3",
" :D",
" :P",
" ;3",
" XDDD",
", fwendo",
" Sigh.",
" ._.",
" >_<"
"xD xD xD",
":D :D :D",]
def owoify(owo):
    for word, initial in substitution.items():
        owo = owo.replace(word.lower(), initial)
    output = random.choice(prefix) + owo + random.choice(suffix)
    return output