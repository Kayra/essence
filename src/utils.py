import sys
import random
import linecache


def prepare_word_to_guess() -> str:
    word_to_guess = linecache.getline("words.txt", random.randint(1, 49))
    return word_to_guess.lower().strip()


def win(word_to_guess: str):
    print(f"Congratulations! You win.\nThe word was {word_to_guess}!")
    sys.exit(0)


def update_current_guess_state(current_guess_state: str, guessed_character: str, word_to_guess: str) -> str:

    offset = 0
    characters_in_word_to_guess = word_to_guess.count(guessed_character)

    for _ in range(characters_in_word_to_guess):

        character_index = word_to_guess.find(guessed_character)

        current_guess_state_list = list(current_guess_state)
        current_guess_state_list[character_index + offset] = guessed_character
        current_guess_state = "".join(current_guess_state_list)

        offset = offset + character_index + 1
        word_to_guess = word_to_guess[offset:]

    return current_guess_state


def is_valid_character_guess(string_guess: str, word_to_guess: str, current_guess_state: str) -> bool:
    return len(string_guess) == 1 and \
           string_guess in word_to_guess and \
           word_to_guess.count(string_guess) - current_guess_state.count(string_guess) > 0
