from Wordle import *

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
            all_words = full_list_of_words
            rando = random.randint(0,len(all_words))
            play(all_words[rando])
        elif cmd_line == CMD_SUGGEST:
            suggestions = suggest_words(w)
            print(suggestions)
        else:
            try:
                schedule,duplicates = scheduler(cmd_line)
                w = exe(w,schedule,duplicates)
            except TypeError as e:
                print("Error code ->", e)

#https://wordlearchive.com/349
# Suggest error below
#vakil nnnwn
#rents wwwwn
#inert yyyyy
