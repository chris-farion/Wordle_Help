import random

N = 0       #Letter does not exist in word
Y = 1       #Letter in correct location
W = 2       #Letter in wrong location
X = 3       #Error

WORD_LENGTH = 5

def load_5_letter_words():
    file_path = 'Total_Wordle_Word_Bank.txt'
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words

def split_list(words):
    word_count = len(words)
    mid_point = word_count >> 1 # Essentially divide by 2
    first_half = words[:mid_point]
    second_half = words[mid_point:]
    return first_half,second_half

def merge_sort_by_position(words,position):
    Sorted_List = is_list_sorted_by_position(words,position)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = merge_sort_by_position(arr0,position)
        arr1 = merge_sort_by_position(arr1,position)
        words = merge_lists_by_position(arr0,arr1,position)
    return words

def is_list_sorted_by_position(list_of_words,position):
    is_Sorted = True
    word_count = len(list_of_words)
    for word_index in range((word_count)-1):
        current_letter = list_of_words[word_index][position]
        compare_letter = list_of_words[word_index+1][position]
        if current_letter > compare_letter:
            is_Sorted = False
            break
    return is_Sorted

def merge_lists_by_position(first_half,second_half,position):
    return_array = []

    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0][position] == second_half[0][position]):
            if (first_half[0][0] > second_half[0][0]):
                return_array.append(second_half[0])
                return_array.append(first_half[0])
                first_half = first_half[1:]
                second_half = second_half[1:]
            else:
                return_array.append(first_half[0])
                return_array.append(second_half[0])
                first_half = first_half[1:]
                second_half = second_half[1:]
        elif (first_half[0][position] < second_half[0][position]):
            return_array.append(first_half[0])
            first_half = first_half[1:]
        else:
            return_array.append(second_half[0])
            second_half = second_half[1:]
    if first_half:
        #If the first array is still left over, add it to the end
        return_array.extend(first_half)
    if second_half:
        #If the second array is still left over, add it to the end
        return_array.extend(second_half)
    return return_array

#_________________________________
def merge_sort(words):
    Sorted_List = is_list_sorted(words)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = merge_sort(arr0)
        arr1 = merge_sort(arr1)
        words = merge_lists(arr0,arr1)
    return words

def is_list_sorted(words):
    is_Sorted = True
    word_count = len(words)
    for word_index in range((word_count)-1):
        current_word = words[word_index]
        compare_word = words[word_index+1]
        if current_word > compare_word:
            is_Sorted = False
            break
    return is_Sorted

def merge_lists(first_half,second_half):
    return_array = []
    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0] == second_half[0]):
            return_array.append(first_half[0])
            return_array.append(second_half[0])
            first_half = first_half[1:]
            second_half = second_half[1:]
        elif (first_half[0] < second_half[0]):
            return_array.append(first_half[0])
            first_half = first_half[1:]
        else:
            return_array.append(second_half[0])
            second_half = second_half[1:]
    if first_half:
        #If the first array is still left over, add it to the end
        return_array.extend(first_half)
    if second_half:
        #If the second array is still left over, add it to the end
        return_array.extend(second_half)
    return return_array

#_________________
def find_range(words,letter,position):
    # Assume list already ordered
    if len(words) == 1:
        return_lower = 0
        return_upper = 1
        return return_lower,return_upper
    lo = lo1 = 0
    hi = hi1 = len(words)-1

    if words[0][position]==letter:
        hi = 0
        lo = hi-1
        
    if words[len(words)-1][position]==letter:
        hi1 = len(words)
        lo1 = hi1-1
        
    while (lo != hi-1 or lo1 != hi1-1):
        if lo != hi-1:
            ptr  = (lo + hi) >> 1
            ltr  = words[ptr][position]
            if ltr < letter:
                lo = ptr
            elif ltr > letter:
                hi = ptr
            else:
                hi = ptr
        if lo1 != hi1-1:
            ptr1 = (lo1 + hi1) >> 1
            ltr1 = words[ptr1][position]
            if ltr1 < letter:
                lo1 = ptr1
            elif ltr1 > letter:
                hi1 = ptr1
            else:
                lo1 = ptr1

    return_lower = hi
    return_upper = hi1
    return return_lower,return_upper

def order_letters_by_duplicates(word):
    letters = {}
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
        else:
            letters[letter] = [i]

    sorted_dict = dict(sorted(letters.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_dict

def wrong(words,letter,position,count,ct):  
    print(f"{letter.upper()} - Wrong @ {position}")
    word_count = len(words)
    if word_count == 1:
        return words
    words = merge_sort_by_position(words,position)
    first,last = find_range(words,letter, position)
    if last == word_count:
        words = words[:first]
    else:
        words = words[:first] + words[last:]
    temp = []

    singular = False
    
    if count != ct:
        singular = True
    
    for word in words:
        if word.count(letter) == count and singular:
            temp.append(word)
        elif word.count(letter) >= count and not singular:
            temp.append(word)
        else:
            pass
    words = temp
    #print(f"{first}:{last} with {len(words)} words remaining")
    return words
    

def yes(words,letter,position,indices):
    print(f"{letter.upper()} - Yes @ {position}")
    word_count = len(words)
    if word_count == 1:
        return words
    if position not in indices:
        return words
    indices.remove(position)
    words = merge_sort_by_position(words,position)
    first,last = find_range(words,letter, position)
    words = words[first:last]
    #print(f"{first}:{last} with {len(words)} words remaining")
    return words

def no(words,letter,positions, count):
    print(f"{letter.upper()} - No @ {positions}")
    if count > 0:
        return words
    for position in positions:
        word_count = len(words)
        if word_count == 1:
            return words
        words = merge_sort_by_position(words,position)
        first,last = find_range(words,letter, position)
        if last == word_count:
            words = words[:first]
        else:
            words = words[:first] + words[last:]
    #print(f"{first}:{last} with {len(words)} words remaining")
    return words

def enter():
    cmd = input(">> ")
    components = cmd.split(' ')
    num_of_components = len(components)

    if num_of_components == 1:
        if components[0] == "exit":
            return "exit"
        else:
            return
    if num_of_components == 2:
        if components[0] != "wrd":
            return "Command not recognized. Please use 'wrd'."
        if components[1] == "help":
            #Create help menu
            pass
        elif components[1] == "reset":
            return "reset"
        elif components[1] == "sts":
            return "status"
        elif components[1] == "rand":
            return "random"
        elif components[1] == "play":
            return "play"
        else:
            return
    elif num_of_components > 3:
        return
    else:
        pass
        
    wordle_keyword = components[0]
    wordle_word = components[1][1:].lower()
    wordle_result = components[2][1:].upper()
    if wordle_keyword != "wrd":
        print("Error. No wrd command")
        return word, indices
    if WORD_LENGTH != len(wordle_word) and len(wordle_word) != len(wordle_result):
        print("Error. Word and result do not match lengths.")
        return word, indices

    duplicates = order_letters_by_duplicates(wordle_word)
    #print(f"duplicates dict:\n{duplicates}")

    ref = {}

    for ltr in duplicates:
        ref[ltr] = 0
        for ind in duplicates[ltr]:
            if wordle_result[ind] != 'N':
                ref[ltr] = ref[ltr] + 1
                
    
    guess = {}
    for i,letter in enumerate(wordle_word):
        guess[i] = {
            'letter': letter,
            'result': wordle_result[i],
            'score': 0,
            'cc': ref[letter],
            'ct': len(duplicates[letter])
            }

        if guess[i]['result'] == 'Y':
            guess[i]['score'] = i + 100
        elif guess[i]['result'] == 'N':
            guess[i]['score'] = i + 50
        elif guess[i]['result'] == 'W':
            guess[i]['score'] = i
        else:
            guess[i]['score'] = -1


    sorted_guess = dict(sorted(guess.items(), key=lambda item: item[1]['score'],reverse=True))

    schedule = dict(sorted_guess)
    
    return schedule

def exe(words,guess,pos):    
    for key,value in guess.items():
        #print(f"Index: {key}, Letter: {value['letter']}, Score: {value['score']}")
        if value['result'] == 'Y':
            words = yes(words,value['letter'],key,pos)
        elif value['result'] == 'N':
            words = no(words,value['letter'],pos,value['cc'])
        elif value['result'] == 'W':
            words = wrong(words,value['letter'],key,value['cc'],value['ct'])
        else:
            pass
    return words
    
#__________________

full_list_of_words = load_5_letter_words()

w = full_list_of_words
p = list(range(WORD_LENGTH))

cmd_line = ""

while cmd_line != "exit":
    cmd_line = enter()
    if cmd_line != "exit":
        if cmd_line == "reset":
            w = full_list_of_words
            p = list(range(WORD_LENGTH))
        elif cmd_line == "status":
            w = merge_sort(w)
            print(w)
        elif cmd_line is None:
            pass
        elif cmd_line == "random":
            rando = random.randint(0,len(w))
            print(f"Random word: {w[rando]}")
        elif cmd_line == "play":
            w = full_list_of_words
            p = list(range(WORD_LENGTH))
            rando = random.randint(0,len(w))
        else:
            w = exe(w,cmd_line,p)



def bug_reports():
    '''
    '''
    print("Comments contain bugs")
