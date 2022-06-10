from os import system, name
import random

from art import logo, vs

from game_data import data


def clear():
    """
    clear the console
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def choose_two_items_from_data():
    """
    random pick 2 items from data,
    print info in the console
    and return A or B who has bigger follower

    """

    competitors = random.sample(data, 2)
    a = competitors[0]
    b = competitors[1]

    print(logo)

    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")

    print(vs)

    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def user_guess(correct_answer):
    """
    get user's answer and compare with correct answer and returen true or false
    """

    user_answer = input("Who has more followers? Type'A' or 'B': ")

    while user_answer.lower() not in ["a", "b"]:

        user_answer = input(
            "Opoos, incorrect input format!!!Try again.\nWho has more followers? Type'A' or 'B': "
        )

    return user_answer.lower() == correct_answer


if __name__ == "__main__":

    is_continue = True

    score = 0

    while is_continue:

        right_answer = choose_two_items_from_data()

        is_continue = user_guess(correct_answer=right_answer)

        if is_continue:
            score += 1
            clear()

        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong, Final score: {score}")
