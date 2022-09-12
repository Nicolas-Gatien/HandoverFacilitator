from rake_nltk import Rake # NLP Library
import json

# replace text inside the triple quotes with your own text and it will find and export the most important parts
text = """ 
Patient states “I fell while playing hockey a few days ago and my fingers haven’t stopped hurting, it gets a lot worse whenever pressure is applied”.
Patient is a 13 year old male. Prior to the visit, the patient says he was taking advil and tylenol for a few days.
Xray shows 2 clear fractures on the ring and middle finger on the right hand.
Patient fractured ring and middle finger on the right hand.
Make a temporary cast.
Follow up at Cheo in 5 days for an appointment to make a more solid one.
"""

# initialize export file
data = {}

# analyze text
nlp = Rake()
nlp.extract_keywords_from_text(text)

# print top [3] results
numOfResults = 3
resultsLeft = numOfResults
for item in nlp.get_ranked_phrases_with_scores():
    if (resultsLeft > 0):
        print(item)
        resultsLeft -= 1

# find results in text and extract them
for x in range(0, numOfResults):
    importantIndex = text.lower().find(nlp.get_ranked_phrases_with_scores()[x][1])
    ind = importantIndex

    # back up until start of sentence
    while(text.lower()[ind] != '.'):
        ind -= 1

    ind += 2
    excerpt = ""
    sentences = 2 # number of sentences per extraction

    # extract sentences
    while (ind < text.__len__() and sentences > 0):
        excerpt = excerpt + text[ind]
        ind += 1
        if (ind < text.__len__()):
            if (text[ind] == '.'):
                sentences -= 1
    
    # add sentences to a dictionary
    data[x] = excerpt.strip()

# write dictionary to JSON file
with open('export_data.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("New json file is created from export_data.json file")