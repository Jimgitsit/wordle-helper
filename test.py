def get_vowel_combos():
    vowels = ['A', 'E', 'I', 'O', 'U']
    combos = []
    for x in range(0, 5):
        for y in range(0, 5):
            if x < y:
                combo = [vowels[x], vowels[y]]
                combos.append(combo)

    print(combos)
    print(len(combos))
    return combos

def get_first_word_alt():
    query = {"$or": []}
    combos = get_vowel_combos()
    for combo in combos:
        query["$or"].append({"letters": {"$all": combo}})
        # { "letters": { "$all": ["A", "E"] } }

    print(query)

get_first_word_alt()

# {"letters": {"$or": {"$all": ["A", "E"]}}}

# { $or: [ { "letters": { "$all": ["A", "E"] } }, { "letters": { "$all": ["A", "I"] } } ] }
