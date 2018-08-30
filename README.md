# Hangman

**Please use Python 3.7**

## How to run

No third party libraries are required to run a game:

```bash
python src/hangman.py
```

However testing requires the installation of `pytest`, which can be done as follows:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
```

## Alternate rules

It may be preferable to have the player guess each letter individually. In this case, the `update_current_guess_state` function would be as follows:

```python
def update_current_guess_state(current_guess_state: str, guessed_letter: str, word_to_guess: str, offset=0) -> str:

    guessed_letter_index = word_to_guess[offset:].find(guessed_letter)

    if list(current_guess_state[offset:])[guessed_letter_index] == "_":

        guessed_letter_index += offset
        current_guess_state_list = list(current_guess_state)
        current_guess_state_list[guessed_letter_index] = guessed_letter
        current_guess_state = "".join(current_guess_state_list)

        return current_guess_state

    else:
        offset = offset + guessed_letter_index + 1
        return update_current_guess_state(current_guess_state, guessed_letter, word_to_guess, offset)

```

# Original Spec

Create a guess a word game - also known as Hangman game.
* Please write in Python and specify which version of Python you are using.
* Please include instructions on how to run.
* Please don't spend more than 30 minutes on this even if it is incomplete.

Rules:
1) When the game starts the player can see how many characters the word has.
2) The player can guess up to 9 times if a letter appears in the secret word.
   If the letter is in the word then the place of the character is shown to the player.
   Over the span of the game the incomplete word will appear to the player.
3) At any stage the player can propose a word. Each proposal reduces the number of attempts by one.
4) The player wins if he can find the secret word within the guess limit. Otherwise the game is lost.


The method of interaction is up to you, you can do it via the Puthon shell, as a command line game, or as Django app
or anything else (but Python!).

Where the initial word comes from is up to you.

* General game info: https://en.wikipedia.org/wiki/Hangman_(game)