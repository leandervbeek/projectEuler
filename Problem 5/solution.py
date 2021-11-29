# Leander van Beek
# Problem 5

def smallestMultiple(N):
    # N being the largers number up to which we divide all numbers.

    evenlyDiv = False

    divisors = list(range(1,N+1))
    divisors.reverse()
    n = N + 1

    while evenlyDiv == False:
        print("Checking {0}".format(n))
        for divisor in divisors:
            if n % divisor != 0:
                # If the division is not exactly 0 (i.e. mod N != 0)
                # Continue to the next number.

                n += 1
                break;

            elif n % divisor == 0 and divisor == 2:
                # If we arrived at 2 and the divisor is zero still,
                # We reached the end of the list and found a result!
               
                evenlyDiv = True 

    return n

smallMult10 = smallestMultiple(10)

print(smallMult10)