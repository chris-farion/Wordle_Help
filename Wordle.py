import random

CMD_EXIT = ["we","exit"]
CMD_RANDOM = ["rand","random"]
CMD_STATUS = ["sts","status"]
CMD_PLAY = "play"
CMD_RESET = "reset"
KEYWORD = "wrd"
CMD_SUGGEST = "?"

NO_RESULT = 'n'
WILDCARD_RESULT = '.'
WRONG_RESULT = 'w'
YES_RESULT = 'y'

class Wordle_Guess:
    def __init__(self, guess, result):
        self.guess = guess
        self.result = result
    def matching_lengths(self):
        return len(self.guess)==len(self.result)

class Wordle_Node:
    def __init__(self, letter=WILDCARD_RESULT, value=WILDCARD_RESULT, position=0, next=None):
        self.letter = letter
        self.val = value
        self.pos = position
        self.next = next
    def has_next(self):
        next_exists = False
        if self.next is not None:
            next_exists = True
        return next_exists
    def __str__(self):
        return f"{self.letter}={self.val}@{self.pos}"
    def disp(self):
        print(f"{self.letter}={self.val}@{self.pos}")

class Duplicate_Node:
    def __init__(self, letter=WILDCARD_RESULT):
        self.letter = letter
        self.count = 1
        self.present = 0
    def disp(self):
        sign = '>='
        if self.count != self.present:
            sign = '='
        print(f"{self.letter} {sign} {self.present}")
    def diff(self):
        difference_between_count_and_presence = False
        if self.count != self.present:
            difference_between_count_and_presence = True
        return difference_between_count_and_presence

class Rank_Node:
    def __init__(self, word="",score=float("-inf")):
        self.word = word
        self.score = score
        self.isBlue = False #Blue=True in a blue/gold tree
        if self.word == "":
            #For nil purposes
            self.isBlue = True
        self.left = None
        self.right = None
        self.parent = None
    def parent_direction(self):
        if self.parent is None:
            direction = "root"
        elif self == self.parent.left:
            direction = "left"
        else:
            direction = "right"
        return direction
    def __str__(self):
        return super().__repr__()[-6:-1]
    def disp(self):
        color = "Gold"
        if self.isBlue:
            color = "Blue"
        if self.parent is None:
            prnt = "None"
        else:
            prnt = self.parent.score
        return f"{self.score}-{color}-{prnt}-{self.left.score}-{self.right.score}"

class Blue_Gold_Tree: # This is typically Red/Black pero soy hincha de Boca
    def __init__(self):
        self.nil = Rank_Node()
        self.root = self.nil
        self.nodes = 0
    def __add__(self,node):
        self.nodes += 1
        node.left = node.right = self.nil
        parent = None
        ptr = self.root
        while ptr != self.nil:
            parent = ptr
            if node.score < ptr.score:
                ptr = ptr.left
            else:
                ptr = ptr.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.score < parent.score:
            parent.left = node
        else:
            parent.right = node
        self._add_fix(node)
        return self
    def _add_fix(self,node):
        while self.root != node and node.parent.isBlue == False:
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                #Uncle will be on the right
                uncle = grandparent.right
                if uncle.isBlue == False:
                    grandparent.isBlue = False
                    node.parent.isBlue = True
                    uncle.isBlue = True
                    node = grandparent
                elif node == node.parent.right:
                    node = node.parent
                    self._rotate_left(node)
                elif node == node.parent.left:
                    self._rotate_right(grandparent)
                    node.parent.isBlue = True
                    grandparent.isBlue = False
            else: #Uncle will be on the left
                uncle = grandparent.left
                #Gold Uncle
                if uncle.isBlue == False:
                    grandparent.isBlue = False
                    node.parent.isBlue = True
                    uncle.isBlue = True
                    node = grandparent
                #Blue Uncle Angle
                elif node == node.parent.left:
                    node = node.parent
                    self._rotate_right(node)
                #Blue Uncle Line
                elif node == node.parent.right:
                    self._rotate_left(grandparent)
                    node.parent.isBlue = True
                    grandparent.isBlue = False
        self.root.isBlue = True
        return self
    def _rotate_left(self,node):
        child = node.right
        node.right = self.nil
        if child.left != self.nil:
            node.right = child.left
            child.left.parent = node
        child.left = node
        if node.parent is None:
            self.root = child
            child.parent = None
        else:
            child.parent = node.parent
            direction = node.parent_direction()
            if direction == "left":
                node.parent.left = child
            else:
                node.parent.right = child
        node.parent = child
        return self
    def _rotate_right(self,node):
        child = node.left
        node.left = self.nil
        if child.right != self.nil:
            node.left = child.right
            child.right.parent = node
        child.right = node
        if node.parent is None:
            self.root = child
            child.parent = None
        else:
            child.parent = node.parent
            direction = node.parent_direction()
            if direction == "left":
                node.parent.left = child
            else:
                node.parent.right = child
        node.parent = child
        child.right = node
        return self
    def __sub__(self,node_to_delete):
        node = self._find(node_to_delete,node_to_delete.score)
        if node == self.nil:
            #Node not found
            return self
        replacement_color = node.isBlue
        if node.left == self.nil:
            #leaf or one child regardless
            subtree = node.right
            self._relocate(node,node.right)
        elif node.right == self.nil:
            subtree = node.left
            self._relocate(node,node.left)
        else:
            replacement = self._in_order_successor(node.right)
            replacement_color = replacement.isBlue
            subtree = replacement.right
            if replacement.parent == node:
                subtree.parent = replacement
            else:
                self._relocate(replacement,replacement.right)
                replacement.right = node.right
                replacement.right.parent = replacement
            self._relocate(node,replacement)
            replacement.left = node.left
            replacement.left.parent = replacement
            replacement.isBlue = node.isBlue
        if replacement_color:
            self._sub_fix(subtree)
        del node
        self.nodes -= 1
        return self
    def _sub_fix(self,node):
        while node != self.root and node.isBlue:
            #Sibling on the right
            if node == node.parent.left:
                sibling = node.parent.right
                if not sibling.isBlue:
                    sibling.isBlue = True
                    node.parent.isBlue = False
                    self._rotate_left(node.parent)
                else:
                    if sibling.left == self.nil or sibling.left is None:
                        sibling_left_child_isBlue = True
                    else:
                        sibling_left_child_isBlue = sibling.left.isBlue
                    if sibling.right == self.nil or sibling.right is None:
                        sibling_right_child_isBlue = True
                    else:
                        sibling_right_child_isBlue = sibling.right.isBlue
                    if sibling_left_child_isBlue and sibling_right_child_isBlue:
                        sibling.isBlue = False
                        node = node.parent
                    elif not sibling_left_child_isBlue and sibling_right_child_isBlue:
                        sibling.left.isBlue = True
                        sibling.isBlue = False
                        self._rotate_right(sibling)
                    else:
                        sibling.isBlue = node.parent.isBlue
                        sibling.right.isBlue = True
                        node.parent.isBlue = True
                        self._rotate_left(node.parent)
                        node = self.root
            else: #Sibling on the left
                sibling = node.parent.left
                if not sibling.isBlue:
                    sibling.isBlue = True
                    node.parent.isBlue = False
                    self._rotate_right(node.parent)
                else:
                    if sibling.left == self.nil or sibling.left is None:
                        sibling_left_child_isBlue = True
                    else:
                        sibling_left_child_isBlue = sibling.left.isBlue
                    if sibling.right == self.nil or sibling.right is None:
                        sibling_right_child_isBlue = True
                    else:
                        sibling_right_child_isBlue = sibling.right.isBlue
                    if sibling_left_child_isBlue and sibling_right_child_isBlue:
                        sibling.isBlue = False
                        node = node.parent
                    elif not sibling_right_child_isBlue and sibling_left_child_isBlue:
                        sibling.right.isBlue = True
                        sibling.isBlue = False
                        self._rotate_left(sibling)
                    else:
                        sibling.isBlue = node.parent.isBlue
                        sibling.left.isBlue = True
                        node.parent.isBlue = True
                        self._rotate_right(node.parent)
        node.isBlue = True
        self.root.isBlue = True
        return self
    def _find(self,node,data):
        ptr = self.root
        while ptr.score != data:
            if ptr == self.nil:
                return self.nil
            if ptr.score < data:
                ptr = ptr.right
            else:
                ptr = ptr.left
        if ptr.score == data:
            return node
    def _relocate(self,deleting,subtree):
        if deleting.parent is None:
            self.root = subtree
        elif deleting == deleting.parent.left:
            deleting.parent.left = subtree
        else:
            deleting.parent.right = subtree
        subtree.parent = deleting.parent
        return self
    def _in_order_successor(self,node):
        ptr = node
        while ptr.left != self.nil:
            ptr = ptr.left
        return ptr
    def _in_order_predecessor(self,node):
        ptr = node
        while ptr.right != self.nil:
            ptr = ptr.right
        return ptr


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

def merge_sort_position(words,position=0):
    Sorted_List = is_list_sorted_by_position(words,position)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = merge_sort_position(arr0,position)
        arr1 = merge_sort_position(arr1,position)
        words = merge_lists_by_position(arr0,arr1,position)
    return words

def merge_sort(words):
    Sorted_List = is_list_sorted(words)
    if not Sorted_List:
        arr0,arr1 = split_list(words)
        arr0 = merge_sort(arr0)
        arr1 = merge_sort(arr1)
        words = merge_lists(arr0,arr1)
    return words

def is_list_sorted_by_position(words,position=0):
    #THIS WILL NOT PROPERLY SORT THE LIST. This simply provides bounds to eliminate words.
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
            compare_A_to_B = False
        else:
            if letter_B > letter_A:
                is_Sorted = False
                break
            letter_B = words[word_index+2][position]
            compare_A_to_B = True
    #Last comparison at the list. Avoids out of range errors.
    if compare_A_to_B:
        if letter_A > letter_B:
            is_Sorted = False
    else:
        if letter_B > letter_A:
            is_Sorted = False
    return is_Sorted

def is_list_sorted(words):
    is_Sorted = True
    word_count = len(words)
    if word_count <= 1:
        return is_Sorted
    compare_A_to_B = True
    switch_scenario = True
    letter_A = words[0]
    letter_B = words[1]
    for word_index in range(((word_count)-2)):
        if compare_A_to_B:
            if letter_A > letter_B:
                is_Sorted = False
                break
            letter_A = words[word_index+2]
            compare_A_to_B = False
        else:
            if letter_B > letter_A:
                is_Sorted = False
                break
            letter_B = words[word_index+2]
            compare_A_to_B = True
    #Last comparison at the list. Avoids out of range errors.
    if compare_A_to_B:
        if letter_A > letter_B:
            is_Sorted = False
    else:
        if letter_B > letter_A:
            is_Sorted = False
    return is_Sorted

def merge_lists(first_half,second_half):
    return_array = []
    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0] < second_half[0]):
            return_array.append(first_half[0])
            first_half = first_half[1:]
        elif (first_half[0] > second_half[0]):
            return_array.append(second_half[0])
            second_half = second_half[1:]
        else:
            return_array.append(first_half[0])
            return_array.append(second_half[0])
            first_half = first_half[1:]
            second_half = second_half[1:]
    if first_half:
        #If the first array is still left over, add it to the end
        return_array.extend(first_half)
    if second_half:
        #If the second array is still left over, add it to the end
        return_array.extend(second_half)
    return return_array

def merge_lists_by_position(first_half,second_half,position=0):
    return_array = []
    # While at least one element is in each array...
    while(first_half and second_half):
        if (first_half[0][position] < second_half[0][position]):
            return_array.append(first_half[0])
            first_half = first_half[1:]
        elif (first_half[0][position] > second_half[0][position]):
            return_array.append(second_half[0])
            second_half = second_half[1:]
        else:
            return_array.append(first_half[0])
            return_array.append(second_half[0])
            first_half = first_half[1:]
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
        if from_hi - from_lo > 1:
            ptr  = (from_lo + from_hi) >> 1
            ltr  = words[ptr][position]
            if ltr < letter:
                from_lo = ptr
            else:
                from_hi = ptr
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

def yes(word_bank, schedule, duplicate_dict):
    letter = schedule.letter
    position = schedule.pos
    word_bank = merge_sort_position(word_bank,position) 
    first,last = find_range(word_bank, letter, position)
    word_bank = include_range(word_bank,first,last)
    print(f"{letter.upper()} - [{first}:{last}) @ {position+1}")
    return word_bank

def no(word_bank, schedule, duplicate_dict, positions):
    letter = schedule.letter
    remaining_positions = positions
    num_in_answer = duplicate_dict[letter].present
    if num_in_answer != 0:
        duplicate_with_wrong = wrong_exception(schedule)
        if duplicate_with_wrong:
            remaining_positions = [schedule.pos]
    for position in remaining_positions:
        word_bank = merge_sort_position(word_bank,position)
        first,last = find_range(word_bank,letter, position)
        word_bank = exclude_range(word_bank,first,last)
        print(f"{letter.upper()} - [:{first})[{last}:) @ {position+1}")
    return word_bank

def wrong_exception(node):
    guess_contains_wrong = False
    while node.has_next() and not guess_contains_wrong:
        node = node.next
        if node.val == WRONG_RESULT:
            guess_contains_wrong = True
    return guess_contains_wrong

def wrong(word_bank, schedule, duplicate_dict):
    letter = schedule.letter
    position = schedule.pos
    word_count = len(word_bank)
    word_bank = merge_sort_position(word_bank,position)
    first,last = find_range(word_bank,letter, position)
    print(f"{letter.upper()} - [:{first})[{last}:) @ {position+1}")
    word_bank = exclude_range(word_bank,first,last)
    temp = []
    duplicate_catch = duplicate_dict[letter].diff()
    if duplicate_catch:
        for word in word_bank:
            if word.count(letter) == duplicate_dict[letter].present:
                temp.append(word)
        word_bank = temp
    else:
        for word in word_bank:
            if word.count(letter) >= duplicate_dict[letter].present:
                temp.append(word)
        word_bank = temp
    return word_bank

def enter():
    cmd = input(">> ")
    cmd = cmd.strip()
    components = cmd.split(' ')
    num_of_components = len(components)
    if num_of_components == 1:
        if components[0] in CMD_EXIT:
            return CMD_EXIT
        else:
            return
    if num_of_components == 2:
        if components[0] != KEYWORD:
            return "Command not recognized. Please use 'wrd'."
        if components[1] in "help":
            #Create help menu
            pass
        elif components[1] in CMD_RESET:
            return CMD_RESET
        elif components[1] in CMD_SUGGEST:
            return CMD_SUGGEST
        elif components[1] in CMD_STATUS:
            return CMD_STATUS
        elif components[1] in CMD_RANDOM:
            return CMD_RANDOM
        elif components[1] in CMD_PLAY:
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
    guess = Wordle_Guess(wordle_word, wordle_result)
    if not guess.matching_lengths():
        return
    schedule, duplicates = create_schedule_and_duplicates(guess)
    return schedule, duplicates

def create_schedule_and_duplicates(node):
    yes_dummy = Wordle_Node()
    no_dummy = Wordle_Node()
    wrong_dummy = Wordle_Node()
    yCurrent = yes_dummy
    nCurrent = no_dummy
    wCurrent = wrong_dummy
    duplicates = {}
    for index,letter in enumerate(node.guess):
        if letter not in duplicates:
            duplicates[letter] = Duplicate_Node(letter)
            if node.result[index] != NO_RESULT:
                duplicates[letter].present += 1
        else:
            duplicates[letter].count = duplicates[letter].count + 1
            if node.result[index] != NO_RESULT:
                duplicates[letter].present = duplicates[letter].present + 1
        #Start creating the schedule...
        if node.result[index] == YES_RESULT:
            yCurrent.next = Wordle_Node()
            yCurrent = yCurrent.next
            yCurrent.letter = letter
            yCurrent.val = YES_RESULT
            yCurrent.pos = index
        elif node.result[index] == NO_RESULT:
            nCurrent.next = Wordle_Node()
            nCurrent = nCurrent.next
            nCurrent.letter = letter
            nCurrent.val = NO_RESULT
            nCurrent.pos = index
        elif node.result[index] == WRONG_RESULT:
            wCurrent.next = Wordle_Node()
            wCurrent = wCurrent.next
            wCurrent.letter = letter
            wCurrent.val = WRONG_RESULT
            wCurrent.pos = index
        else:
            pass
    start_node = link_nodes_for_schedule(yes_dummy,no_dummy,wrong_dummy,yCurrent,nCurrent,wCurrent)
    return start_node, duplicates

def link_nodes_for_schedule(yes_dummy,no_dummy,wrong_dummy,yCurrent,nCurrent,wCurrent):
    yes_exists = yes_dummy.has_next()
    no_exists = no_dummy.has_next()
    wrong_exists = wrong_dummy.has_next()
    start_node = Wordle_Node()
    if yes_exists:
        if no_exists:
            yCurrent.next = no_dummy.next
            if wrong_exists:
                nCurrent.next = wrong_dummy.next
        elif wrong_exists:
            yCurrent.next = wrong_dummy.next
        else:
            pass
        start_node = yes_dummy
    elif no_exists:
        if wrong_exists:
            nCurrent.next = wrong_dummy.next
        else:
            pass
        start_node = no_dummy
    elif wrong_exists:
        start_node = wrong_dummy
    else:
        pass
    return start_node

def exe(words,schedule,duplicates):
    positions = remaining_indices(schedule)
    while schedule.has_next():
        schedule = schedule.next
        if schedule.val == YES_RESULT:
            words = yes(words,schedule, duplicates)
        elif schedule.val == NO_RESULT:
            words = no(words,schedule, duplicates, positions)
        elif schedule.val == WRONG_RESULT:
            words = wrong(words,schedule, duplicates)
        else:
            pass
    return words

def remaining_indices(schedule):
    non_yes_indices = []
    while schedule.has_next():
        schedule = schedule.next
        if schedule.val != YES_RESULT:
            non_yes_indices.append(schedule.pos)
    return non_yes_indices

def stats(letter_counts):
    num_of_chars_in_counts = len(letter_counts)
    if num_of_chars_in_counts == 0:
        num_of_chars_in_counts = 1
    summation = 0
    for letter in letter_counts:
        summation += letter_counts[letter]
    mean = summation / num_of_chars_in_counts
    squared_summation = 0
    for letter in letter_counts:
        temp = (letter_counts[letter] - mean)**2
        squared_summation += temp
    sigma_squared = squared_summation / num_of_chars_in_counts
    stdev = sigma_squared**(1/2)
    return mean,stdev

def suggest_words(words,top=12):
    if len(words) <= 1:
        return words
    num_of_words = len(words)
    dictionary = load_5_letter_words()
    letter_count = {}
    # Count number of letters in remaining words
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    # Delete letters that are already Yes or Wrong position
    for letter in list(letter_count.keys()):
        if letter_count[letter] >= num_of_words:
            letter_count[letter] = letter_count[letter] % num_of_words 
        if letter_count[letter] == 0:
            del letter_count[letter]
    mean,stdev = stats(letter_count)
    print(f"Mean: {mean}\nStdev.P: {stdev}")
    if stdev == 0:
        stdev = 1
        scores = {"0":(-mean/stdev)}
        for letter in letter_count:
            scores[letter] = 1
    else:
        scores = {"0":(-mean/stdev)}
        for letter in letter_count:
            scores[letter] = (letter_count[letter]-mean)/stdev
    #Start the Binary Tree
    print(f"Letter scores\n\n {scores}")
    tree = Blue_Gold_Tree()
    for word in dictionary:
        score = 0
        partial_dict = {}
        for letter in word:
            if letter in letter_count and letter not in partial_dict:
                partial_dict[letter] = [letter]
                score += scores[letter]
            elif letter in letter_count and letter in partial_dict:
                score += scores["0"]
            else:
                score += scores["0"]
        if tree.nodes < top:
            node = Rank_Node(word,score)
            tree += node
        else:
            lowest_score = tree._in_order_successor(tree.root)
            if score > lowest_score.score:
                tree -= lowest_score
                tree += Rank_Node(word,score)
    return tree

def print_top_answers(node):
    if node.right.score != float("-inf"):
        print_top_answers(node.right)
    print(f"{node.word}\t{node.score}")
    if node.left.score != float("-inf"):
        print_top_answers(node.left)


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
