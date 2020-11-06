import json
from difflib import get_close_matches 
import time 

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        ya = input("Did you mean %s instead? " % get_close_matches(w,data.keys())[0]+ "Y or N?: ")
        if ya == "Y" or "y":
           return data[get_close_matches(w,data.keys())[0]]
        elif ya == "N" or "n":
            return "That word does not exist!"          

word = input("What word would you like to define " )

print(translate(word))