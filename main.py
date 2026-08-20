from initialize import *

wrd = Wordle()
cmd_line = ""
while cmd_line != CMD_EXIT:
    cmd_line = enter()
    if cmd_line != CMD_EXIT:
        if cmd_line == CMD_RESET:
            wrd.reset()
        elif cmd_line == CMD_STATUS:
            wrd.status()
        elif cmd_line is None:
            pass
        elif cmd_line == CMD_RANDOM:
            wrd.random()
        elif cmd_line == CMD_PLAY:
            all_words = wrd.all_words
            rando = random.randint(0,len(all_words))
            play(all_words[rando])
        elif cmd_line == CMD_SUGGEST:
            wrd.suggest()
        else:
            try:
                schedule,duplicates = scheduler(cmd_line)
                wrd.active_words = exe(wrd.active_words,schedule,duplicates)
                #a = exe_letters(a,schedule,duplicates)
            except TypeError as e:
                print("Error code ->", e)

#https://wordlearchive.com/373
#Suggest error below
#vakil nnnwn
#rents wwwwn
#inert yyyyy
