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


def choose_two_items_from_data(item_a):
    """
    random pick 2 items from data,
    print info in the console
    and return A or B who has bigger follower

    """
    item_b = random.choice(data)

    while item_a == item_b:
        item_b = random.choice(data)

    print(logo)

    print(
        f"Compare A: { item_a['name']}, { item_a['description']}, from { item_a['country']}."
    )

    print(vs)

    print(
        f"Against B: { item_b['name']}, { item_b['description']}, from { item_b['country']}."
    )

    if item_a["follower_count"] > item_b["follower_count"]:
        return ("a", item_b)
    else:
        return ("b", item_b)


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

    a = random.choice(data)

    while is_continue:

        right_answer, a = choose_two_items_from_data(item_a=a)

        is_continue = user_guess(correct_answer=right_answer)

        if is_continue:
            score += 1
            clear()

        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong, Final score: {score}")
