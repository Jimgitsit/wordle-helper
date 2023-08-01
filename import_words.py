import pymongo
import json
import urllib.request

def load_words():
    valid_words = []

    # Word source: http://wordlist.aspell.net/12dicts-readme/#classic
    #   and https://github.com/mongodb-developer/mongordle/blob/main/words.json
    with open('2of12inf.txt') as word_file:
        all_words = set(word_file.read().split())

    for word in all_words:
        word = word.upper()
        if len(word) != 5:
            continue

        # if word contains a hyphen, skip
        if "-" in word:
            continue

        valid_words.append(word)

    print(len(all_words))

    ww = open('wordle_words.json')
    wordle_words = json.load(ww)

    for word in wordle_words:
        this_word = word.get("_id").upper()
        if this_word not in valid_words:
            valid_words.append(this_word)

    # remove duplicates in valid_words
    valid_words = list(set(valid_words))

    print(len(valid_words))
    return valid_words

def convert_words(words):
    new_words = []
    for word in words:
        # if length is not 5, skip
        if len(word) != 5:
            continue

        # if word contains a hyphen, skip
        if "-" in word:
            continue

        # get the word frequency
        response = urllib.request.urlopen("https://api.datamuse.com/words?sp=" + word + "&md=f&max=1")
        data = json.loads(response.read())
        score = 0
        if len(data) > 0:
            if 'score' in data[0]:
                score = data[0].get('score')

        # format the word into json
        # from https://www.mongodb.com/developer/products/mongodb/wordle-solving-mongodb-query-api-operators/
        new_words.append({
            "_id": word.upper(),
            "freq": score,
            "letter1": word[0].upper(),
            "letter2": word[1].upper(),
            "letter3": word[2].upper(),
            "letter4": word[3].upper(),
            "letter5": word[4].upper(),
            "letters": list(word.upper())
        })

    return new_words

def save_to_db(words):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["GFG"]
    collection = db["all_words"]
    collection.drop()
    collection.insert_many(words)

def do_import():
    words = load_words()
    words = convert_words(words)
    # print word count
    print("Got " + str(len(words)) + " words")
    save_to_db(words)

if __name__ == "__main__":
    do_import()
