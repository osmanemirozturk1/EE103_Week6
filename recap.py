year = int(input("What year is this? "))
year_str = str(year)
total = 0
for digit in year_str:
    total += int(digit)
print("Average of digits:", total / len(year_str))

