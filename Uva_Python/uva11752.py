import math


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

primes = primes_sieve1(65536)

lista = []
a_lista = []

for p in primes:
	for j in range(2,65):
		c = p**j
		if c < 2**64:
			if c in lista:
				if c not in a_lista:
					a_lista.append(c)
			else:
				lista.append(c)

		else:
			break

a = sorted(a_lista)

for e in a:
	print(e)

