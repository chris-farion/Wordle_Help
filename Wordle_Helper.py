LENGTH = 5
GUESSES = 6

N = 0       #Letter does not exist in word
Y = 1       #Letter in correct location
W = 2       #Letter in wrong location
X = 3       #Error

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
available_chars = [CHARS]*LENGTH

def merge_sort(words):
    Sorted_List = is_list_sorted(words)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = merge_sort(arr0)
        arr1 = merge_sort(arr1)
        words = merge_lists(arr0,arr1)
    return words
    
def order_letters_by_duplicates(word):
    letters = {}
    for i,letter in enumerate(word):
        if letter in letters:
            letters[letter].append(i)
        else:
            letters[letter] = [i]

    sorted_dict = dict(sorted(letters.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_dict

print(order_letters_by_duplicates("STSST"))

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
print(binary_search(12,counting))

def is_list_sorted(list_of_words):
    is_Sorted = True
    word_count = len(list_of_words)
    for word_index in range((word_count)-1):
        current_word = list_of_words[word_index]
        compare_word = list_of_words[word_index+1]
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
        return_array.extend(first_half[:])
    if second_half:
        return_array.extend(second_half[:])
    return return_array

sample_word_list = ["cigar","rebut","sissy","heath","humph","awake","blush","focal","evade","later","alert","rates","stare","adder","dread","steel","sleet"]

print(f"Before: {sample_word_list}")
final = merge_sort(sample_word_list)
print(f"After:  {final}")
