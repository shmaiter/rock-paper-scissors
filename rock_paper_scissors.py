import random


def play():
    user = input(
        "Choose 'r' for ROCK, 'p' for PAPER or 's' for SCISSORS\n").lower()
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It\'s a tie"

    if user_win(user, computer):
        return "You won!!"

    return "You lost!!"


def user_win(player, opponent):
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or \
            (player == "p" and opponent == "r"):
        return True


# Runs the program
print(play())
