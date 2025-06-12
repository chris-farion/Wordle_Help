N = 0       #Letter does not exist in word
Y = 1       #Letter in correct location
W = 2       #Letter in wrong location
X = 3       #Error

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
    while(first_half and second_half):
        if (first_half[0][position] == second_half[0][position]):
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
        return_array.extend(first_half)
    if second_half:
        return_array.extend(second_half)
    return return_array

def find_range(words,letter,position):
    # Assume list already ordered
    if letter == 'a' or words[0][position]==letter:
        return_lower = hi = 0
        return_upper = lo = -1
        lo1 = 0
        hi1 = len(words)-1
    elif letter == 'z' or words[len(words)-1][position]==letter:
        return_lower = -1
        return_upper = lo1 = len(words)-1
        hi1 = len(words)
        lo = 0
        hi = len(words)-1
    else:
        return_lower = return_upper = -1
        lo = lo1 = 0
        hi = hi1 = len(words)-1

    
    while (lo != hi-1 or lo1 != hi1-1):
        if return_lower < 0 and lo != hi-1:
            ptr  = (lo + hi) >> 1
            ltr  = words[ptr][position]
            if ltr < letter:
                lo = ptr
            elif ltr > letter:
                hi = ptr
            else:
                hi = ptr
                
        if return_upper < 0 and lo1 != hi1-1:
            ptr1 = (lo1 + hi1) >> 1
            ltr1 = words[ptr1][position]
            if ltr1 < letter:
                lo1 = ptr1
            elif ltr1 > letter:
                hi1 = ptr1
            else:
                lo1 = ptr1

    return_lower = hi
    return_upper = lo1+1
    return return_lower,return_upper

def load_5_letter_words():
    file_path = 'Total_Wordle_Word_Bank.txt'
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words
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

def split_list(words):
    word_count = len(words)
    mid_point = word_count >> 1 # Essentially divide by 2
    first_half = words[:mid_point]
    second_half = words[mid_point:]
    return first_half,second_half

def merge_lists(first_half,second_half):
    return_array = []
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
        return_array.extend(first_half)
    if second_half:
        return_array.extend(second_half)
    return return_array

#_________________
#CLOCK
#YNNNN

def wrong(words,letter,position,indices):
    print(f"{letter.upper()} - Wrong")
    word_count = len(words)
    words = merge_sort_by_position(words,position)
    first,last = find_range(words,letter, position)
    if last == word_count:
        print(words[first])
        print(words)
        words = words[:first]
        print(words)
    else:
        words = words[:first] + words[last:]
    temp = []
    for word in words:
        if letter in word:
            temp.append(word)
    words = temp
    print(f"{first}:{last} with {len(words)} words remaining")
    return words,indices
    

def yes(words,letter,position,indices):
    print(f"{letter.upper()} - Yes")
    word_count = len(words)
    indices = indices[:position]+indices[position+1:]
    words = merge_sort_by_position(words,position)
    first,last = find_range(words,letter, position)
    words = words[first:last]
    print(f"{first}:{last} with {len(words)} words remaining")
    return words,indices

def no(words,letter,positions):
    print(f"{letter.upper()} - No")
    for position in positions:
        word_count = len(words)
        words = merge_sort_by_position(words,position)
        first,last = find_range(words,letter, position)
        if last == word_count:
            print(words[first])
            print(words)
            words = words[:first]
            print(words)
        else:
            words = words[:first] + words[last:]
        print(f"{first}:{last} with {len(words)} words remaining")
    return words

#__________________

full_list_of_words = load_5_letter_words()
words = full_list_of_words

pos = list(range(5))

#Guesses here for now#

words = merge_sort(words)
