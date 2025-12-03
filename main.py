from Wordle import *

def play(word):
    word_dict = {}
    for index,letter in enumerate(word):
        if letter not in word_dict:
            word_dict[letter] = [index]
        else:
            word_dict[letter].append(index)
    guess = ""
    while guess != CMD_EXIT:
        guess = input(">> ")
        guess = guess.strip()
        components = guess.split(' ')
        num_of_components = len(components)
        if guess in CMD_EXIT:
            return
        guess_dict = {}
        result = []
        for index,letter in enumerate(guess):
            temp = Wordle_Node(letter,NO_RESULT,index,None)
            result.append(temp)
            if letter not in guess_dict:
                guess_dict[letter] = [index]
            else:
                guess_dict[letter].append(index)
        #Start processing
        for guess_key in guess_dict.keys():
            if guess_key in word_dict:
                #Pass 1
                num_of_letter_correct = 0
                for guess_key_val in guess_dict[guess_key]:
                    if guess_key_val in word_dict[guess_key]:
                        num_of_letter_correct += 1
                        result[guess_key_val].val = YES_RESULT
                #Pass 2
                word_iters = len(word_dict[guess_key])-num_of_letter_correct
                guess_iters = len(guess_dict[guess_key])-num_of_letter_correct
                iters = min(word_iters,guess_iters)
                current_index = 0
                while iters !=0:
                    guess_index = guess_dict[guess_key][current_index]
                    index_result = result[guess_index].val
                    if index_result is not YES_RESULT:
                        result[guess_index].val = WRONG_RESULT
                        iters -= 1
                        current_index += 1
        #Display result
        response_str = ""
        for current_letter in range(len(result)):
            if result[current_letter].val is YES_RESULT:
                response_str += f"\033[30;42m{result[current_letter].letter}\033[0m"
            elif result[current_letter].val is WRONG_RESULT:
                response_str += f"\033[37;44m{result[current_letter].letter}\033[0m"
            else:
                response_str += f"{result[current_letter].letter}"
        print(f"{response_str}")

full_list_of_words = load_5_letter_words()
w = full_list_of_words
cmd_line = ""
while cmd_line != CMD_EXIT:
    cmd_line = enter()
    if cmd_line != CMD_EXIT:
        if cmd_line == CMD_RESET:
            w = full_list_of_words
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
            rando = random.randint(0,len(w))
            play(w[rando])
        elif cmd_line == CMD_SUGGEST:
            suggestions = collect_remaining_letters(w)
            print(suggestions)
        else:
            try:
                schedule,duplicates = scheduler(cmd_line)
                w = exe(w,schedule,duplicates)
            except TypeError as e:
                print("Error code ->", e)

