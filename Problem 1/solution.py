# Leander van Beek
# Problem 1

N = 1001 # Number up to which to check +1, as the range is exclusive in the line below.

lst = range(1, N)

valid_numbers = []

for number in lst:
    if number % 3 == 0 or number % 5 == 0:
        valid_numbers.append(number)

print(sum(valid_numbers))