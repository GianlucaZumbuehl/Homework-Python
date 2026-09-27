# Bulls and Cows
# Bull: correct digit in the correct position.
# Cow: correct digit in a different position.
# For the basic version, assume each guess has four different digits.

secret = "4271"

print("Guess the four-digit code.")

while True:
    guess = input("Your guess: ")
    if guess == "q":
        a = input(
            "ohhhhh, you really want to give up? Are you sure, press q again ")
        if a == "q":
            break
        else:
            continue
    if guess.isdigit() == False:
        print("it should just digits (0-9)")
        continue

    if len(guess) != 4:
        print("Jojojooooo, it should be four digits, try again")
        continue
    if len(set(guess)) != 4:
        print("no repeated digits, its to complex for my Python skills")
        continue

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    print(bulls, cows)
    if bulls == 4:
        print("""WOoooowoOOOOWOOWooow, You are the best!!!!!
          YOu should join the Panzerknacker or the Daltons
          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          """)
        break


# Try 1234: 1 bull, 2 cows. Try 4271: 4 bulls, 0 cows; game ends.

# Optional extensions:
# - Reject guesses whose length is not four. yes
# - Accept only digits 0-9.
# - Reject repeated digits.
#   Check these before the for loop; use continue to ask again if invalid.
# - Let the player enter q to quit.
# - Count guesses or set an attempt limit.
# - Generate a random secret with four different digits.
