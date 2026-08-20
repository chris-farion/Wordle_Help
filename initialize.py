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
    def suggest(self):
        letter_counts = collect_data(self.active_words)
        mean,stdev = stats(letter_counts)
        self.stats = [mean,stdev]
        self.scores = normalize(letter_counts,mean,stdev)
        print(f"Mean:    {mean:0.4f}\nStdev.P: {stdev:0.4f}")
        print(f"{self.scores}")
        suggestions = formulate_tree(self.all_words,self.scores)
        suggestions_from_current = formulate_tree(self.active_words,self.scores)
        print_top_answers(suggestions.root)
        print("------------")
        print_top_answers(suggestions_from_current.root)
