# Leander van Beek
# Problem 7
# 10001st prime

import numpy as np

def sieve(N):
	# function sieve
	# Uses Eratosthenes sieve to come up with prime numbers
	# int N: Upper limit for numbers to scan for primes
	# primes: list of found primes

	N = np.ceil(N) # Make sure we have an integer
	numbers = np.arange(2, N)

	for i in np.arange(2, N//2):
		# In the list of numbers, cross out every 2nd, 3rd, 4th, 5th, ..., nth number
		# Left are the prime numbers
		numbers[(int(i)-1)*2::int(i)] = 0 # Set to zero if not a prime

	primes = numbers[numbers != 0] # Remove the zeros

	return primes


N_prime = 10001 # Index of prime number to find
upperLimit = 1.5 * N_prime * np.log(N_prime) # Prime number theorem w/ margin: p_n ~ n * log(n)

primes = sieve(upperLimit)

print("Amount of primes found: ", len(primes))
print("The {0}th prime is {1}".format(N_prime, int(primes[N_prime-1])))
