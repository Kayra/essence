from utils import prepare_word_to_guess, win, update_current_guess_state, is_valid_character_guess


def run_hangman(word_to_guess=None):

    if word_to_guess is None:
        word_to_guess = prepare_word_to_guess()
    guesses_remaining = 9
    current_guess_state = "_" * len(word_to_guess)

    while guesses_remaining > 0:

        string_guess = input(f"\n{current_guess_state}\n").lower()

        if string_guess == word_to_guess:
            win(word_to_guess)

        elif is_valid_character_guess(string_guess, word_to_guess, current_guess_state):
            current_guess_state = update_current_guess_state(current_guess_state, string_guess, word_to_guess)
            if current_guess_state == word_to_guess:
                win(word_to_guess)

        else:
            guesses_remaining -= 1
            print(f"Incorrect. {guesses_remaining} guesses remaining.")

    print(f"\nYou were unable to guess correctly. The word was {word_to_guess}.\nBetter luck next time!\n")


if __name__ == "__main__":
    run_hangman()
