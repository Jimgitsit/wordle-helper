# ChatGPT plugin for Wordle

Wordle helper.

Requires a mongodb "wordle-helper" and a collection "all_words"
```
mongorestore -d backup/wordle-helper/ --drop
```

Run server:

```
python3 main.py
```

Access server at http://localhost:5000/{input}

Where input is in the format of: `[word]:[guess],[word]:[guess],...`

Guesses are in the form of:
~ = letter is in the work but not in the right place  
^ = letter is in word and in the right place  
x = letter is not in word  

Example:
```
curl http://0.0.0.0:5003/getFirstWord
curl http://0.0.0.0:5003/getNextWord/broad:xx~x^ 
curl http://0.0.0.0:5003/getNextWord/broad:xx~x^,cosed:x^xx^
```
