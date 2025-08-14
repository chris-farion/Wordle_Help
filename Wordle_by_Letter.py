import logging
import random
import time
import timeit

CMD_EXIT = "exit"
CMD_RANDOM = ["rand","random"]
CMD_STATUS = ["sts","status"]
CMD_PLAY = "play"
CMD_RESET = "reset"
KEYWORD = "wrd"

DICT_KEY_INDEX = 0
DICT_VALUE_INDEX = 1

YES_RESULT = 'y'
NO_RESULT = 'n'
WRONG_RESULT = 'w'

DUPLICATE_SEARCH_ORDER = [YES_RESULT,WRONG_RESULT,NO_RESULT]
NORMAL_SEARCH_ORDER = [YES_RESULT,NO_RESULT,WRONG_RESULT]

WORD_LENGTH = 5

def load_5_letter_words():
    file_path = 'Total_Wordle_Word_Bank.txt'
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words

def include_range(words,from_index,to_index):
    words = words[from_index:to_index]
    return words

def exclude_range(words,from_index,to_index):
    words = words[:from_index] + words[to_index:]
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

def refactor_merge_sort(words,position=0):
    Sorted_List = is_list_sorted_by_position(words,position)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = refactor_merge_sort(arr0,position)
        arr1 = refactor_merge_sort(arr1,position)
        words = refactor_merge_lists(arr0,arr1,position)
    return words

def is_list_sorted_by_position(words,position):
    #Using logic to 'jump' 2 words so that the same word is not reloaded
    is_Sorted = True
    word_count = len(words)
    if word_count <= 1:
        return is_Sorted
    compare_A_to_B = True
    switch_scenario = True
    letter_A = words[0][position]
    letter_B = words[1][position]
    for word_index in range(((word_count)-2)):
        if compare_A_to_B:
            if letter_A > letter_B:
                is_Sorted = False
                break
            letter_A = words[word_index+2][position]
            compare_A_to_B ^= switch_scenario
        else:
            if letter_B > letter_A:
                is_Sorted = False
                break
            letter_B = words[word_index+2][position]
            compare_A_to_B ^= switch_scenario
    if compare_A_to_B:
        if letter_A > letter_B:
            is_Sorted = False
    else:
        if letter_B > letter_A:
            is_Sorted = False
    return is_Sorted

def merge_lists_by_position(first_half,second_half,position):
    return_array = []
    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0][position] == second_half[0][position]):
            if (first_half[0] > second_half[0]):
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

def refactor_merge_lists(first_half,second_half,position=0):
    return_array = []
    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0][position] == second_half[0][position]):
            if (first_half > second_half):
                return_array.append(second_half[0])
                second_half = second_half[1:]
            else:
                return_array.append(first_half[0])
                first_half = first_half[1:]
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
    if word_count <= 1:
        return is_Sorted
    compare_A_to_B = True
    switch_scenario = True
    word_A = words[0]
    word_B = words[1]
    for word_index in range(((word_count)-1)):
        if compare_A_to_B:
            if word_A > word_B:
                is_Sorted = False
                break
            if word_index+2 < word_count:
                word_A = words[word_index+2]
                compare_A_to_B ^= switch_scenario
        else:
            if word_B > word_A:
                is_Sorted = False
                break
            if word_index+2 < word_count:
                word_B = words[word_index+2]
                compare_A_to_B ^= switch_scenario
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

def find_range(words,letter,position):
    # Assume list already ordered by position
    # There are four pointers, 2 for the lower end of the range and two for the high
    # Each pointer will 'hug' the index that starts and ends with the same letter
    if len(words) < 1:
        print(f"No more words!")
        return_lower = return_upper  = 0
        return return_lower,return_upper
    from_lo = to_lo = 0
    from_hi = to_hi = len(words)-1
    if words[0][position]==letter:
        from_hi = 0
        from_lo = from_hi-1
    if words[len(words)-1][position]==letter:
        to_hi = len(words)
        to_lo = to_hi-1
    while (from_hi - from_lo > 1 or to_hi - to_lo > 1):
        #if from_lo != from_hi-1:
        if from_hi - from_lo > 1:
            ptr  = (from_lo + from_hi) >> 1
            ltr  = words[ptr][position]
            if ltr < letter:
                from_lo = ptr
            else:
                from_hi = ptr
        #if to_lo != to_hi-1:
        if to_hi - to_lo > 1:
            ptr1 = (to_lo + to_hi) >> 1
            ltr1 = words[ptr1][position]
            if ltr1 > letter:
                to_hi = ptr1
            else:
                to_lo = ptr1
    if words[from_hi][position] != letter:
        from_hi = to_hi
    if words[to_lo][position] != letter:
        to_hi = from_hi
    return_lower = from_hi
    return_upper = to_hi
    return return_lower,return_upper

def contains_duplicates(word):
    ret_val = False
    letters = {}
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
            ret_val = True
            break
        else:
            letters[letter] = [i]
    return ret_val

def order_letters_by_duplicates(word):
    letters = {}
    contains_duplicates = False
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
            contains_duplicates = True
        else:
            letters[letter] = [i]
    sorted_dict = dict(sorted(letters.items(), key=lambda item: len(item[DICT_VALUE_INDEX]), reverse=True))
    print(sorted_dict)
    return sorted_dict

def yes(word_bank, schedule, position, remaining_positions, duplicate_dict):
    if position not in remaining_positions:
        return word_bank
    letter = schedule['letter']
    word_count = len(word_bank)
    duplicate_dict[letter].remove(position)
    schedule['char_count'] = schedule['char_count'] - 1 
    remaining_positions.remove(position)
    word_bank = refactor_merge_sort(word_bank,position)
    first,last = find_range(word_bank,letter, position)
    ##print(f"{letter.upper()} - [{first}:{last}) @ {position}")
    word_bank = include_range(word_bank,first,last)
    return word_bank

def no(word_bank, schedule, position, remaining_positions, duplicate_dict):
    letter = schedule['letter']
    compare_sign = "="
    if len(duplicate_dict[letter]) >= 2:
        compare_sign = duplicate_handling(schedule,duplicate_dict)
    #Condition below should never occur. Here as a safety valve.
    if compare_sign == ">=":
        return word_bank
    word_count = len(word_bank)
    if schedule['char_count'] == 0:
        for position in remaining_positions:
            word_bank = refactor_merge_sort(word_bank,position)
            #word_bank = merge_sort_by_position(word_bank,position)
            first,last = find_range(word_bank,letter, position)
            ##print(f"{letter.upper()} - [:{first})[{last}:) @ {position}")
            word_bank = exclude_range(word_bank,first,last)
    else:
        word_bank = refactor_merge_sort(word_bank,position)
        #word_bank = merge_sort_by_position(word_bank,position)
        first,last = find_range(word_bank,letter, position)
        ##print(f"{letter.upper()} - [:{first})[{last}:) @ {position}")
        word_bank = exclude_range(word_bank,first,last)
    return word_bank

def wrong(word_bank, schedule, position, remaining_positions, duplicate_dict):
    letter = schedule['letter']
    compare_sign = "="
    if len(duplicate_dict[letter]) >= 2:
        compare_sign = duplicate_handling(schedule,duplicate_dict)
    compare_sign = duplicate_handling(schedule,duplicate_dict)
    word_count = len(word_bank)
    word_bank = refactor_merge_sort(word_bank,position)
    #word_bank = merge_sort_by_position(word_bank,position)
    first,last = find_range(word_bank,letter, position)
    ##print(f"{letter.upper()} - [:{first})[{last}:) @ {position}")
    word_bank = exclude_range(word_bank,first,last)
    temp = []
    #print(f"Before entering...\nLetter: {letter}: {schedule['char_count']}")
    if compare_sign == "=":
        for word in word_bank:
            if word.count(letter) == schedule['char_count']:
                #print(f"{word}: {word.count(letter)}")
                temp.append(word)
    elif compare_sign == ">=":
        for word in word_bank:
            if word.count(letter) >= schedule['char_count']:
                #print(f"{word}: {word.count(letter)}")
                temp.append(word)
    else:
        pass
    ##print(f"{letter.upper()} - Wrong @ {position} {compare_sign} {schedule['char_count']}")
    word_bank = temp
    #print(f"{letter.upper()} - Wrong @ {position}")
    return word_bank


def duplicate_handling(schedule,duplicate_dict):
    #>> wrd -adder -wwnww
    #        {'d': [1, 2], 'a': [0], 'e': [3], 'r': [4]}
    #Schedule: {'letter': 'd', 'result': 'n', 'score': 52, 'char_count': 1}
    #Duplicates: {'d': [1, 2], 'a': [0], 'e': [3], 'r': [4]}
    letter = schedule['letter']
    duplicates_in_guess = len(duplicate_dict[letter])
    limit_from_response = schedule['char_count']
    #print(f"duplicates_in_guess: {duplicates_in_guess}\nlimit_from_response: {limit_from_response}")
    if duplicates_in_guess != limit_from_response:
        comparator= "="
    else:
        comparator = ">="
    return comparator

def enter():
    cmd = input(">> ")
    cmd = cmd.strip()
    components = cmd.split(' ')
    num_of_components = len(components)
    if num_of_components == 1:
        if components[0] == CMD_EXIT:
            return CMD_EXIT
        else:
            return
    if num_of_components == 2:
        if components[0] != KEYWORD:
            return "Command not recognized. Please use 'wrd'."
        if components[1] == "help":
            #Create help menu
            pass
        elif components[1] == CMD_RESET:
            return CMD_RESET
        elif components[1] in CMD_STATUS:
            return CMD_STATUS
        elif components[1] in CMD_RANDOM:
            return CMD_RANDOM
        elif components[1] == CMD_PLAY:
            return CMD_PLAY
        else:
            return
    elif num_of_components == 3:
        return components
    else:
        return 

def scheduler(components):
    wordle_keyword = components[0]
    wordle_word = components[1][1:].lower()
    wordle_result = components[2][1:].lower()
    if wordle_keyword != KEYWORD:
        print("Error. No wrd command")
        return
    if WORD_LENGTH != len(wordle_word) and (len(wordle_word) != len(wordle_result)):
        return
    duplicates = order_letters_by_duplicates(wordle_word)
    #{'d': [1, 2], 'a': [0], 'e': [3], 'r': [4]}
    print(f"keys: {duplicates.keys()}\nvalues: {duplicates.values()}")
    ref = {}
    for ltr in duplicates:
        ref[ltr] = 0
        for index in duplicates[ltr]:
            if wordle_result[index] != 'n':
                ref[ltr] = ref[ltr] + 1
    guess = {}
    #for i,letter in enumerate(wordle_word):
    for i,letter in enumerate(wordle_word):
        guess[i] = {
            'letter': letter,
            'result': wordle_result[i],
            'score': 0,
            'char_count': ref[letter]
            }
        if guess[i]['result'] == 'y':
            guess[i]['score'] = i + 100
        elif guess[i]['result'] == 'n':
            guess[i]['score'] = i + 50
        elif guess[i]['result'] == 'w':
            guess[i]['score'] = i
        else:
            guess[i]['score'] = -1
    sorted_guess = dict(sorted(guess.items(), key=lambda item: item[1]['score'],reverse=True))
    schedule = dict(sorted_guess)
    return schedule, duplicates

def refactor_scheduler(components):
    wordle_keyword = components[0]
    wordle_word = components[1][1:].lower()
    wordle_result = components[2][1:].lower()
    sch = {}
    search_range = range(len(wordle_word))
    duplicates = order_letters_by_duplicates(wordle_word)
    result_dict = order_letters_by_duplicates(wordle_result)
    #print(f"{duplicates}\n{result_dict}\n")
    #{'d': [1, 2], 'a': [0], 'e': [3], 'r': [4]}
    #{'w': [0, 1, 2, 3, 4]}
    #{'e': [1, 3, 4], 'p': [0], 'w': [2]}
    #{'n': [0, 2, 3], 'w': [1], 'y': [4]}
    #print(f"keys: {duplicates.keys()}\nvalues: {duplicates.values()}")
    temp = []
    #duplicates['d'].append(['c','h'])
    for duplicates_key, duplicates_value in duplicates.items():
        compare_sign = '>='
        num_in_ans = 0
        print(f"-{duplicates_key}: {duplicates_value}")
        if len(duplicates_value) != 1:
            print(f"DUPLICATE FOR {duplicates_key}!")
            for i in duplicates_value:
                print(f"i:{i} > {wordle_result[i]}")
                if wordle_result[i] == NO_RESULT:
                    compare_sign = '='
                else:
                    num_in_ans = num_in_ans + 1
                print(f"{compare_sign}" - {num_in_ans})

        for result_key,result_value in result_dict.items():
            print(f"↳{result_key}: {result_value}")
            for i in duplicates_value:
                pass
                #if i in result_value:
                    #print(f"{duplicates_key}:{i} > {result_key}\n")
                if i in result_key[YES_RESULT]:
                    print(f"added a yes")
            for i in duplicates_value:
                if i in result_value:
                    print(f"{duplicates_key}:{i} > {result_key}\n")
    print(f"temp: {temp}")
    temp = []
    for duplicates_key, duplicates_value in duplicates.items():
        #print(f"L0{duplicates_key}:{duplicates_value}")
        for result_key,result_value in result_dict.items():
            #print(f"L1{result_key}:{result_value}")
            if len(duplicates_value) != 1:
                pass
                #print(f"dupl key: {duplicates_key}")
            if YES_RESULT in result_key:
                if duplicates_value == result_key:
                    #print(f"{duplicates_key} Yes @ {duplicates_value}")
                    pass
    #print(f"temp: {temp}")
    ref = {}
    for ltr in duplicates:
        ref[ltr] = 0
        for index in duplicates[ltr]:
            if wordle_result[index] != 'n':
                ref[ltr] = ref[ltr] + 1
    guess = {}
    #for i,letter in enumerate(wordle_word):
    for i,letter in enumerate(wordle_word):
        guess[i] = {
            'letter': letter,
            'result': wordle_result[i],
            'score': 0,
            'char_count': ref[letter]
            }
        if guess[i]['result'] == 'y':
            guess[i]['score'] = i + 100
        elif guess[i]['result'] == 'n':
            guess[i]['score'] = i + 50
        elif guess[i]['result'] == 'w':
            guess[i]['score'] = i
        else:
            guess[i]['score'] = -1
    sorted_guess = dict(sorted(guess.items(), key=lambda item: item[1]['score'],reverse=True))
    schedule = dict(sorted_guess)
    return schedule, duplicates

def exe(words,guess,pos,duplicate_info):
    for key,value in guess.items():
        if value['result'] == 'y':
            words = yes(words,guess[key],key,pos,duplicate_info)
        elif value['result'] == 'n':
            words = no(words,guess[key],key,pos,duplicate_info)
        elif value['result'] == 'w':
            words = wrong(words,guess[key],key,pos,duplicate_info)
        else:
            pass
    return words

full_list_of_words = load_5_letter_words()
w = full_list_of_words
p = list(range(WORD_LENGTH))
cmd_line = ""

#func1 = timeit.timeit(lambda: is_list_sorted_by_position(w,0), number=10000)

#print(f"func0: {func0:.5f}")
#print(f"func1: {func1:.5f}")

while cmd_line != CMD_EXIT:
    cmd_line = enter()
    if cmd_line != CMD_EXIT:
        if cmd_line == CMD_RESET:
            w = full_list_of_words
            p = list(range(WORD_LENGTH))
        elif cmd_line == CMD_STATUS:
            w = refactor_merge_sort(w)
            print(w)
        elif cmd_line is None:
            pass
        elif cmd_line == CMD_RANDOM:
            rando = random.randint(0,len(w)-1)
            print(f"Random word: {w[rando]}")
        elif cmd_line == CMD_PLAY:
            w = full_list_of_words
            p = list(range(WORD_LENGTH))
            rando = random.randint(0,len(w))
        else:
            try:
                schedule,duplicate_info = refactor_scheduler(cmd_line)
                w = exe(w,schedule,p,duplicate_info)
            except TypeError as e:
                print("Error code ->", e)
                print("Incorrect input! Please remember to use '-'.")

def bug_reports():
    '''

    merge
    wrd -stale -nnnny
    wrd -fence -nynny
    wrd -pewee -nynny
    wrd -herye -nyyny
    wrd -eerie -nyyny #eerie should not be here after pewee

    skill
    wrd -depth -nnnnn
    wrd -fujis -nnnww
    wrd -slink -ywynw # Incorrectly eliminates skill 
    wrd -skirl -yyyny 
    
    mamma
    wrd -stale -nnwnn
    wrd -kaugh -nynnn
    #No mamma in sts

    https://wordlearchive.com/240
    '''
    print("Comments contain bugs")
