"""make a wordle game for comp110"""

__author__ = "730553768"


def contains_char(search_me: str, character_guess: str) -> bool:
    """search for a character in a string of text"""
    assert len(character_guess) == 1, f"len('{character_guess}') is not 1"
    i: int = 0
    """i indexes so we can search characters individually"""
    while i <= (len(search_me) - 1):
        """length f(x) to account for diff length words"""
        """-1 bc len starts at 1 and index starts at 0"""
        if search_me[i] == character_guess:
            return True
        """runs thru character by character for length of word"""
        i += 1
    return False


"""false if we've gone thru entire length of word and no matches"""


def emojified(guess_emoji: str, secret_emoji: str) -> str:
    """assign different colored boxes to character status like in wordle"""
    assert len(guess_emoji) == len(secret_emoji), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    Box: str = ""
    """blank so that i can add the box colors to the string for output"""
    i: int = 0
    """using i for indexing again to search char by char to assign boxes per char"""

    while i < len(secret_emoji):
        if guess_emoji[i] == secret_emoji[i]:
            Box += GREEN_BOX
            """if at the right spot its green"""
        elif contains_char(search_me=secret_emoji, character_guess=guess_emoji[i]):
            Box += YELLOW_BOX
            """yellow used contains_char bc yellow = the char is in the word"""
        else:
            Box += WHITE_BOX
            """if not in word it's white"""
        i += 1
        """keeps looping till we're thru word"""
    return Box


"""so we can see the string of box colors"""


def input_guess(expected_length: int) -> str:
    """allows us to know how long the secret word will be"""
    guess_attempt: str = input(f"Enter a {expected_length} character word: ")
    """have to use input bc the f(x) depends on what the user guesses"""
    while len(guess_attempt) != expected_length:
        guess_attempt = input(f"That wasn't {expected_length} chars! Try again: ")
        """asks for input again since length was wrong"""
    return guess_attempt


"""will return the word bc that means we know it's the right length"""


def main(secret: str) -> None:
    """the entrypoint of the program and main game loop"""
    turn_number: int = 1
    """turn_number keeps track of what turn it is since turn number matters"""
    secret_length: int = len(secret)
    """need len(secret) for input_guess; secret stays constant so above while"""

    while turn_number <= 6:
        print(f"=== Turn {turn_number}/6 ===")
        user_guess: str = input_guess(expected_length=secret_length)
        """uses input_guess to gather input, checks length"""
        emojis: str = emojified(guess_emoji=user_guess, secret_emoji=secret)
        """runs emojified and compares character by character"""
        print(emojis)
        """actually shows the output of the emojified function"""
        if secret == user_guess:
            print(f"You won in {turn_number}/6 turns!")
            return None
        """complete guess match= win, return none so we exit the function"""
        turn_number += 1

    print("X/6 - Sorry, try again tomorrow!")
    return None


"""ran out of turns, return none so we exit the function"""


if __name__ == "__main__":
    main(secret="codes")
