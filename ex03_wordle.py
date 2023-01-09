"""Exercise 3 Wordle!""" 
# Docstring for documentation




def contains_char(the_word: str, single_word: str) -> bool:
    """This function is seeing if the single_word is in the the_word variable."""
    # We start this function off with a boolean in order to get the True and False return
    assert len(single_word) == 1
    first_index: int = 0
    while first_index < len(the_word):
        if the_word[first_index] == single_word:
            return True
            # This checks if the guess word/letter is in the word that they put and if so it is true
        first_index = first_index + 1
    return False
    # If the guess word/letter is not in the word then it comes out as false


def emojified(single_word: str, the_word: str) -> str:
    """This fuction uses the previous function to codify an inputted word with emojis."""
    assert len(single_word) == len(the_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # These are the 3 emojis being used from the last exercise
    i: int = 0
    resulting_emoji: str = ""
    # This resulting_emoji is where the emojis are being put into
    while i < len(the_word):
        if the_word[i] == single_word[i]:
            resulting_emoji = f"{resulting_emoji}{GREEN_BOX}"  
        # If the guess word is in the actual word then the green box will print out       
        if the_word[i] != single_word[i] and contains_char(the_word, single_word[i]):
            resulting_emoji = f"{resulting_emoji}{YELLOW_BOX}"
            # If the guess word is in the actual word but in the wrong spot then it comes out as yellow
        if not contains_char(the_word, single_word[i]):
            resulting_emoji = f"{resulting_emoji}{WHITE_BOX}"
            # If the guess word is not in the actual word at all then a white box comes
        i = i + 1
    return resulting_emoji
    # Used a return because it is a def function and it will just spit out the 


def input_guess(lenght: int) -> str:
    """This function checks to see if the user puts in the right amount of characters."""
    the_question: str = input(f"Enter a {lenght} character word: ")
    # Simply asks the user for a certain letter word 
    while len(the_question) != lenght:
        the_question = input(f"That wasn't {lenght} chars! Try again: ")
    # This is if the word they put in does not follow the lenght it is supposed to be 
    return the_question


def main() -> None:
    """The entrypoint of the program and main game loop."""
    the_turn: int = 1
    secret_word: str = "codes"
    while the_turn <= 6:
        the_turn_tostr: str = str(the_turn)
        # I did this in order to add the_turn into the f string below
        print(f"=== Turn {the_turn_tostr}/6 ===")
        # Shows what turn the user is on
        their_guess = input_guess(len(secret_word))
        # Calls the input_guess to first ask for the words
        print(emojified(secret_word, their_guess))
        # Calls the emojis to match with the input 
        if their_guess == secret_word:
            print(f"You won in {the_turn_tostr}/6 turns!")
            the_turn = 6
        # If they guess the word then the turns are done and the user has won!
        the_turn = the_turn + 1
        if the_turn > 6 and their_guess != secret_word:
            print("X/6 - Sorry, try again tomorrow!")
        # After the 6 tries the game is over 


if __name__ == "__main__":
    main()
