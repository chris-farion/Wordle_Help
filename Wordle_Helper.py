LENGTH = 5
GUESSES = 6

N = 0       #Letter does not exist in word
Y = 1       #Letter in correct location
W = 2       #Letter in wrong location
X = 3       #Error

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
available_chars = [CHARS]*LENGTH
    
def order_letters_by_duplicates(word):
    print(word)
    letters = {}
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
        else:
            letters[letter] = [i]

    sorted_dict = dict(sorted(letters.items(), key=lambda item: len(item[1]), reverse=True))
    print(sorted_dict)
    return sorted_dict

test = order_letters_by_duplicates("STSST")

