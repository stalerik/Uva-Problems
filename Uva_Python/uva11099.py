import sys
import math
file = sys.stdin.read()
lines = file.split("\n") 



def primes_sieve1(start, limit):
    limitn = limit+1
    primes = dict()
    for i in range((start+1), limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def next_factored(lista):
	res = 1
	for e in lista:
		res *= e
	res *= lista[0]

	print(res)

primes = [2]

for e in lines:
	if e == '1':
		print(1)
	else:
		temp = []
		n = int(e)
		if n > primes[-1]:
			primes = primes + primes_sieve1(primes[-1], n)
		
		for prime in primes:
			if n == 1:
				break
			while n % prime == 0:
				temp.append(prime)
				n = (n/prime)

		
		next_factored(temp)
		
