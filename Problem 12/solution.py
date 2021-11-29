# Leander van Beek
# Problem 12

def Tn(n):

    return 0.5 * n*(n+1)

n = 1
counter = 0
i = 1

N = 20 # sought after number of divisors

while True:

    n_triangle = Tn(n)

    if n_triangle % i == 0 and i < n_triangle:
        counter += 1

    elif i == n_triangle:

        print("The number of divisors for the T_{0} = {1} is {2}".format(n, int(n_triangle), counter))

        if counter > N:
            print("The first triangular number with more than {0} divisors is T_{1} = {2} with {3} divisors".format(N, n, int(n_triangle), counter))
            break;

        counter = 0
        n += 1
        i = 0

    i += 1