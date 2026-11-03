from secret_data import secret_year

guesses = 0
for guess in range(0,2027):
    guesses += 1
    if guess == secret_year:
        print(f"Found secret year {guess} in {guesses} guesses. ")
        break

