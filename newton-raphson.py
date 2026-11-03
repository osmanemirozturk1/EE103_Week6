from secret_data import secret_number

epsilon = 0.01
guess = secret_number / 2.0
guesses = 0

while abs(guess * guess - secret_number) >= epsilon:
    guess = guess - ((guess**2 - secret_number) / (2 * guess))
    guesses += 1

print(f"Number of guesses: {guesses}")
print(f"Calculated square root: {guess}")