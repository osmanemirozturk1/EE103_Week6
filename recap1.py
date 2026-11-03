x = 0.1
y = 0.2
result = x + y
print("Exact match:", result == 0.3)
print("Close enough:", 0.3 - 1e-4 <= result <= 0.3 + 1e-4)