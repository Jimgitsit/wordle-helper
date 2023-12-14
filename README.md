# ChatGPT plugin for Wordle

This is a helper for ChatGPT so that it is better at playing Wordle.

This project started with me trying to get ChatGPT to play wordle (on its own) 
which did not go very well. It had a difficult time with letter positions, 
i.e., determining what letter is in what position and vice versa. It also 
hallucinated words a lot and could not understand the basic strategy of 
the game no matter how I wrote the prompt. I tried many different 
prompting techniques; longer and more detailed, shorter and more concise, 
with strategy tips and without, various ways of describing the game and 
rules, various forms for inputs and outputs, etc. Nothing worked.

(since I finished with this project, there have been some new techniques 
for prompting that I have not tried, such as chain-of-thought and 
step-by-step. I may come back to this sometime in the future and give 
those a try.)

Not wanting to give up, I decided to build a plugin that could help it 
with its deficiencies having function it can call like char_to_pos and 
num_to_word etc. which did help it with figuring out letter positions. 
I also added a database of all five-letter words in the english language 
to keep it from hallucinating. However, it still sucked at strategy. It 
didn't know what words were more common than others, or it just didn't 
understand this concept, so I added frequency of use to each word in the 
database. It would still have a hard time making educated guesses. I 
eventually added the functions getFirstWord and getNextWord, which are 
basically Wordle cheaters. The AI started using them with every guess and 
became pretty good at the game. Not sure if this counts as it's not 
"thinking" about it at all, just cheating.

Then again, isn't this the same thing we humans do as we play? The Only  
difference is our database of words in our heads is probably not as 
thorough, and our sense of 'frequency of use' is going to be hazy at best,  
relying on our experience and intuition.


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
