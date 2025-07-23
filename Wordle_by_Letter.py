import random
import time
import timeit

CMD_EXIT = "exit"
CMD_RANDOM = ["rand","random"]
CMD_STATUS = ["sts","status"]
CMD_PLAY = "play"
CMD_RESET = "reset"
KEYWORD = "wrd"

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

def is_list_sorted_by_position(words,position):
    #print(f"Using this logic to 'jump' 2 words so that the same work is not reloaded")
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
    # Assume list already ordered
    if len(words) <= 1:
        return_lower = 0
        return_upper = 1
        return return_lower,return_upper
    from_lo = to_lo = 0
    from_hi = to_hi = len(words)-1
    if words[0][position]==letter:
        from_hi = 0
        from_lo = from_hi-1
    if words[len(words)-1][position]==letter:
        to_hi = len(words)
        to_lo = to_hi-1
    while (from_lo != from_hi-1 or to_lo != to_hi-1):
        if from_lo != from_hi-1:
            ptr  = (from_lo + from_hi) >> 1
            ltr  = words[ptr][position]
            if ltr < letter:
                from_lo = ptr
            else:
                from_hi = ptr
        if to_lo != to_hi-1:
            ptr1 = (to_lo + to_hi) >> 1
            ltr1 = words[ptr1][position]
            if ltr1 > letter:
                to_hi = ptr1
            else:
                to_lo = ptr1
    return_lower = from_hi
    return_upper = to_hi
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

def wrong(word_bank, schedule, position, remaining_positions, duplicate_dict):  
    letter = schedule['letter']
    print(f"{letter.upper()} - Wrong @ {position}")
    word_count = len(word_bank)
    word_bank = merge_sort_by_position(word_bank,position)
    temp = []
    singular = False
    count = schedule['char_count']
    ct = len(duplicate_dict[letter])
    #TODO: fix befrom_low so that the duplicates are handled correctly(-adder -wwnww)
    if count != ct:
        singular = True
    for word in word_bank:
        if word.count(letter) == count and singular and word[position] != letter:
            temp.append(word)
        elif word.count(letter) >= count and not singular and word[position] != letter:
            temp.append(word)
        else:
            pass
    word_bank = temp
    return word_bank

def yes(word_bank, schedule, position, remaining_positions, duplicate_dict):
    if position not in remaining_positions:
        return word_bank
    letter = schedule['letter']
    print(f"{letter.upper()} - Yes @ {position}")
    word_count = len(word_bank)
    duplicate_dict[letter].remove(position)
    schedule['char_count'] = schedule['char_count'] - 1 
    remaining_positions.remove(position)
    word_bank = merge_sort_by_position(word_bank,position)
    first,last = find_range(word_bank,letter, position)
    word_bank = word_bank[first:last]
    return word_bank

def no(word_bank, schedule, position, remaining_positions, duplicate_dict):
    letter = schedule['letter']
    word_count = len(word_bank)
    if word_count == 1:
        #TODO Somewhat cheating if there are 2-3 options
        return word_bank
    if len(duplicate_dict[letter]) > 1:
        print(f"{letter.upper()} - No @ {position}")
        word_bank = merge_sort_by_position(word_bank,position)
        first,last = find_range(word_bank,letter, position)
        if last == word_count:
            word_bank = word_bank[:first]
        else:
            word_bank = word_bank[:first] + word_bank[last:]
    else:
        print(f"{letter.upper()} - No @ {remaining_positions}")
        for position in remaining_positions:
            word_bank = merge_sort_by_position(word_bank,position)
            first,last = find_range(word_bank,letter, position)
            if last == word_count:
                word_bank = word_bank[:first]
            else:
                word_bank = word_bank[:first] + word_bank[last:]
    return word_bank

def enter():
    cmd = input(">> ")
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
    elif num_of_components > 3:
        return
    else:
        return components

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
    ref = {}
    for ltr in duplicates:
        ref[ltr] = 0
        for ind in duplicates[ltr]:
            if wordle_result[ind] != 'n':
                ref[ltr] = ref[ltr] + 1
    guess = {}
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
            w = merge_sort(w)
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
                schedule,duplicate_info = scheduler(cmd_line)
                w = exe(w,schedule,p,duplicate_info)
            except TypeError as e:
                print("Error code ->", e)
                print("Incorrect input! Please remember to use '-'.")



def bug_reports():
    '''
    world
    wrd -eorls -nyyyn

    briar
    wrd -ferns -nnwnn
    wrd -roily -wnynn
    wrd -chirp -nnywn
    wrd -triad -nyyyn

    blurt
    wrd -rangs -wnnnn
    wrd -tuyer -wwnnw
    wrd -court -nnyyy

    merge
    wrd -stale -nnnny
    wrd -fence -nynny
    wrd -pewee -nynny
    wrd -herye -nyyny
    wrd -eerie -nyyny #eerie should not be here after pewee

    exult
    wrd -meant -nwnny
    wrd -eruct -ynyny #No words left after this guess

    https://wordlearchive.com/192
    '''
    print("Comments contain bugs")
