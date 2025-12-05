##Wordle_Help

This is a simple project to eliminate 5 letter words from Wordle guesses.

You can also play with a random word selected from a list.

###Commands
 Outside of exiting, start each command with **wrd**
 You are given one word bank to work from. Each guess you enter eliminates options from this bank to reveal the available answers.

 * Enter Wordle Guess
  Place the characters of your guess after a '-'. Then use another '-' and place the following characters signifying the result of your guess.
  * y = Correct position in the word
  * n = Does not exist in the word
  * w = Exists in the word but in the wrong position

  Example:
> wrd -agony -ywyyn

 * Status
  Use **sts** or **status** to see the words available in your word bank

 * Reset
  Use **reset** to go back to a full word bank

 * Random word
  Use **rand** to select a random word out of the available words left in the word bank

 * Suggest
  When left with only one or two unknown letters, this will search the available letters in a full dictionary to cover these.
  > (e.g. 'champ', 'clamp', 'cramp', 'stamp', 'swamp', 'tramp', etc.)

 * Play
  Use **play** to play Wordle on a random 5 letter word. To exit play mode, use **exit** or **we**.

 * Exit
  Enter **exit** or **we** to exit the script
