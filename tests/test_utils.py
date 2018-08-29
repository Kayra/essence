import pytest

from src.utils import prepare_word_to_guess, win, update_current_guess_state, is_valid_character_guess


class TestUtils:

    def test_prepare_word_to_guess(self):
        word = prepare_word_to_guess()
        assert isinstance(word, str)

    def test_win(self, capfd):

        word = "test_word"

        with pytest.raises(SystemExit) as exception:
            win(word)
        print_statement, error = capfd.readouterr()

        assert print_statement == f"Congratulations! You win.\nThe word was {word}!\n"
        assert exception.type == SystemExit
        assert exception.value.code == 0

    def test_update_current_guess_state(self):

        current_guess_state = "_____"
        guessed_character = "k"
        word_to_guess = "kayra"
        expected_guess_state = "k____"

        actual_guess_state = update_current_guess_state(current_guess_state, guessed_character, word_to_guess)

        assert expected_guess_state == actual_guess_state

    def test_update_current_guess_state_multiple_identical_characters(self):

        current_guess_state = "_____"
        guessed_character = "a"
        word_to_guess = "kayra"
        expected_guess_state = "_a__a"

        actual_guess_state = update_current_guess_state(current_guess_state, guessed_character, word_to_guess)

        assert expected_guess_state == actual_guess_state

    def test_is_valid_character_guess(self):

        string_guess = "k"
        word_to_guess = "kayra"
        current_guess_state = "_____"

        assert is_valid_character_guess(string_guess, word_to_guess, current_guess_state) is True

    def test_invalid_is_valid_character_guess(self):

        string_guess = "z"
        word_to_guess = "kayra"
        current_guess_state = "_____"

        assert is_valid_character_guess(string_guess, word_to_guess, current_guess_state) is False

    def test_already_guessed_is_valid_character_guess(self):

        string_guess = "k"
        word_to_guess = "kayra"
        current_guess_state = "k____"

        assert is_valid_character_guess(string_guess, word_to_guess, current_guess_state) is False
