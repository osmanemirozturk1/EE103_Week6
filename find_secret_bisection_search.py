from secret_data import secret_year

low = 0
high = 2026
guess = (low + high) // 2
guesses = 1

while guess != secret_year:
    if guess < secret_year:
        low = guess + 1
    else:
        high = guess - 1
    guess = (low + high) // 2
    guesses += 1

print(f"Found secret year: {guess} in {guesses} guesses.")