from main import user_guess
from tud_test_base import set_keyboard_input, get_display_output


def test_case_1_user_guess():
    set_keyboard_input(["a"])

    assert user_guess("b") == False


def test_case_2_user_guess():
    set_keyboard_input(["A"])

    assert user_guess("b") == False


def test_case_3_user_guess():
    set_keyboard_input(["b"])

    assert user_guess("b") == True


def test_case_4_user_guess():
    set_keyboard_input(["B"])

    assert user_guess("b") == True
