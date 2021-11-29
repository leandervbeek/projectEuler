# Leander van Beek
# Problem 2

N = 4E6

sequence = [1, 2]
sumEvenNumbers = 2 # we already have a 2 in the sequence

while sequence[-1] < 4E6:

    newNumber = sequence[-1] + sequence[-2]
    
    sequence.append(newNumber)
    
    if newNumber % 2 == 0:
        sumEvenNumbers += newNumber

print(sumEvenNumbers)