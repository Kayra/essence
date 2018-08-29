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
pip install -r requirements
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