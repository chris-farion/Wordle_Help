from Wordle import *

class Wordle:
    def __init__(self):
        self.all_words = load_5_letter_words()
        self.active_words = load_5_letter_words()
        self.avail_letters = Available_Letters()
        self.current_tree = Blue_Gold_Tree()
        letter_counts = collect_data(self.all_words)
        mean,stdev = stats(letter_counts)
        self.stats = [mean,stdev]
        self.scores = normalize(letter_counts,mean,stdev)
        COMMANDS = [
                Command(["we","exit"],0,0,0,"Exit the current screen",self.quit),
                Command(["<word> <result>"],0,0,0,"Eliminate words using (Y)es, (N)o, and (W)rong",self.eliminate),
                Command(["reset"],0,0,0,"Reset the current word list",self.reset),
                Command(["rand","random"],0,0,0,"Display a random word from the current list",self.random),
                Command(["sts","status"],0,0,0,"Display the current word list",self.status),
                Command(["play"],0,0,["p"],"Play Wordle with a random word",self.play),
                Command(["?"],0,0,["#","str"],"Suggest words from a full and current list",self.suggest),
                Command(["help"],0,0,0,"Help menu",self.help),
        ]
        self.cmd = COMMANDS
        self.screen_num = 1
        self.loop()
    def quit(self):
        self.screen_num -= 1
    def help(self):
        for command in self.cmd:
            print(f"{command.description:<46}\t\t{command.keywords}")
    def reset(self):
        self.active_words = self.all_words
        self.avail_letters = Available_Letters()
        letter_counts = collect_data(self.all_words)
        mean,stdev = stats(letter_counts)
        self.stats = [mean,stdev]
        self.scores = normalize(letter_counts,mean,stdev)
    def status(self):
        self.active_words = merge_sort(self.active_words)
        print(self.active_words)
    def random(self):
        random_index = random.randint(0,len(self.active_words)-1)
        print(f"Random word: {self.active_words[random_index]}")
    def suggest(self,*options):
        top = 12 #Default value for suggestions
        if options and options[0].isnumeric():
            top = int(options[0])
        letter_counts = collect_data(self.active_words)
        mean,stdev = stats(letter_counts)
        self.stats = [mean,stdev]
        self.scores = normalize(letter_counts,mean,stdev)
        if options and not options[0].isnumeric():
            score = get_score(options[0],self.scores)
            print(f"{options[0]} = {score}")
            return
        print(f"Mean:    {mean:0.4f}\nStdev.P: {stdev:0.4f}")
        print(f"{self.scores}")
        suggestions = formulate_tree(self.all_words,self.scores,top)
        suggestions_from_current = formulate_tree(self.active_words,self.scores,top)
        print_top_answers(suggestions.root)
        print("------------")
        print_top_answers(suggestions_from_current.root)
    def play(self,selection=""):
        self.screen_num += 1
        if selection != "":
            word = selection
        else:
            random_index = random.randint(0,len(self.all_words)-1)
            word = self.all_words[random_index]
        guess = ""
        while guess != CMD_EXIT:
            #guess = input(f"{self.screen_num}> ")
            guess = input(f"play> ")
            guess = guess.strip()
            if guess in CMD_EXIT:
                self.screen_num -= 1
                return
            result = result_string(word,guess)
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
        self.screen_num -= 1
    def eliminate(self):
        pass
    def loop(self):
        while (self.screen_num): #Exit when the screen number is 0
            #user_input = input(f"{self.screen_num}> ")
            user_input = input(f"wrd > ")
            user_input_stripped = user_input.strip()
            components = user_input_stripped.split(' ')
            if components != ['']:
                self.exe_command(*components)
    def exe_command(self,*inp):
        number_of_words = len(inp)
        for command in self.cmd:
            if inp[0] in command.keywords:
                if number_of_words > 1:
                    opt = inp[1:]
                    command.function(*opt)
                    return
                else:
                    command.function()
                    return
        for word in inp:
            # TODO input checker
            if len(word) != WORDLE_LENGTH:
                print(f"Not a word with a length of {WORDLE_LENGTH}")
                return
        try:
            schedule,duplicates = scheduler(*inp)
            self.active_words = exe(self.active_words,schedule,duplicates)
        except TypeError as e:
            print("Error code ->", e)
