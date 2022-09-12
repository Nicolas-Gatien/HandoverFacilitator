from urllib import response
from requests_html import HTMLSession
from rake_nltk import Rake
import json
import io

text = """
Patient states “I fell while playing hockey a few days ago and my fingers haven’t stopped hurting, it gets a lot worse whenever pressure is applied”.
Patient is a 13 year old male. Prior to the visit, the patient says he was taking advil and tylonol for a few days.
Xray shows 2 clear fractures on the ring and middle finger on the right hand.
Patient fractured ring and middle finger on the right hand.
Make a temporary cast.
Follow up at Cheo in 5 days for an appointment to make a more solid one.
"""
data = {}

r = Rake()
r.extract_keywords_from_text(text)

y = 3
for item in r.get_ranked_phrases_with_scores():
    if (y > 0):
        print(item)
        y -= 1

with open('data.json', 'w') as f:
    print("data.json is made")

for x in range(0, 3):
    importantIndex = text.lower().find(r.get_ranked_phrases_with_scores()[x][1])
    ind = importantIndex

    while(text.lower()[ind] != '.'):
        ind -= 1

    ind += 2
    excerpt = ""
    sentences = 3
    while (ind < text.__len__() and sentences > 0):
        excerpt = excerpt + text[ind]
        ind += 1
        if (ind < text.__len__()):
            if (text[ind] == '.'):
                sentences -= 1
    data[x] = excerpt

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("New json file is created from data.json file")