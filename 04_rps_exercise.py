# Rock, Paper, Scissors
# Rock beats scissors; scissors beats paper; paper beats rock.
# For the basic version, assume the player enters a valid lowercase move.

import random

moves = ["rock", "paper", "scissors"]
count = 0


# Complete the rules. Return "win", "draw", or "loss" for the player.
def compare_moves(player, opponent):
    if player == opponent:
        return "draw"
    elif player == "rock":
        if opponent == "scissors":
            return "win"
        else:
            return "loss"

    elif player == "paper":
        if opponent == "rock":
            return "win"
        else:
            return "loss"

    else:
        if opponent == "paper":
            return "win"
        else:
            return "loss"


# Uncomment these examples after completing the function:
# print(compare_moves("paper", "rock"))       # Expected: win
# print(compare_moves("rock", "paper"))       # Expected: loss
# print(compare_moves("scissors", "scissors")) # Expected: draw
# Play five rounds.
for round_number in range(1, 6):
    print("Round:", round_number)
    player = input("rock, paper, or scissors: ").strip().lower()
    while player not in moves and player != "q":
        print(
            "ehiiiiiiii, can you read its rock, paper, scisscors not ROCK POAOEE SCHSCIOCS")
        player = input("rock, paper, or scissors: ").strip().lower()
    if player == "q":
        print("Goodbye!")
        break
    opponent = random.choice(moves)
    print("Computer:", opponent)
    result = compare_moves(player, opponent)
    print(result)
    if result == "win":
        count += 1

print(f"Okay not bad you had {count} wins")


# Simulation: 100000 rounds
wins = 0
draws = 0
losses = 0

for i in range(100000):
    player = random.choice(moves)
    opponent = random.choice(moves)
    result = compare_moves(player, opponent)
    if result == "win":
        wins += 1
    elif result == "draw":
        draws += 1
    else:
        losses += 1

print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)
print(f"Win percentage: {wins / 100000 * 100}%")

# Optional extensions:
# - Simulate 600 rounds using random choices for both players.
#   Print the totals and calculate wins / 600 * 100 as the win percentage.
