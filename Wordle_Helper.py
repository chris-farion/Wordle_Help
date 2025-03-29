LENGTH = 5
GUESSES = 6

N = 0       #Letter does not exist in word
Y = 1       #Letter in correct location
W = 2       #Letter in wrong location
X = 3       #Error

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
available_chars = [CHARS]*LENGTH
    
def order_letters_by_duplicates(word):
    letters = {}
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
        else:
            letters[letter] = [i]

    sorted_dict = dict(sorted(letters.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_dict

test0 = order_letters_by_duplicates("STSST")

def binary_search(key,list):
    ret = -1
    lo = 0
    hi = len(list)-1
    while lo != hi-1:
        ptr = (hi+lo)//2
        if key == list[ptr]:
            ret = ptr
            lo = hi-1
        elif key < list[ptr]:
            hi = ptr
        else:
            lo = ptr
    if key == list[lo]:
        ret = lo
    elif key == list[hi]:
        ret = hi
    else:
        pass
    return ret
        


counting = [i for i in range(100)]
test1 = binary_search(12,counting)
