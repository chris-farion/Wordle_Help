## Wordle_Help

### Commands

 You are given one word bank to work from. Each guess you enter eliminates options from this bank to reveal the available answers.

 * Enter Wordle Guess  
  Place the characters of your guess after a '-'. Then use another '-' and place the following characters signifying the result of your guess.
   * y = Correct position in the word
   * n = Does not exist in the word
   * w = Exists in the word but in the wrong position

  Example:
  > agony ywyyn

 * Status  
  Use **sts** or **status** to see the words available in your word bank
  > sts _or_ status

 * Reset  
  Use **reset** to go back to a full word bank
  > reset

 * Random word  
  Use **rand** to select a random word out of the available words left in the word bank
   > rand

  * Suggest  
  When left with only one or two unknown letters, this will search the available letters in a full dictionary to cover these.
  > (e.g. 'champ', 'clamp', 'cramp', 'stamp', 'swamp', 'tramp', etc.)
  Use the following command
  > ?

  * Play  
  Use **play** to play Wordle on a random 5 letter word. To exit play mode, use **exit** or **we**.
 > play

  * Exit  
  Enter **exit** or **we** to exit the script
 > we _or_ exit
