from secret_data import secret_number

epsilon = 0.01
step = epsilon ** 2
guess = 0.0
guesses = 0

while abs(guess**2 - secret_number) >= epsilon and guess <= secret_number:
    guess += step
    guesses += 1

print(f"Guesses: {guesses}, Approx Square Root: {guess}")