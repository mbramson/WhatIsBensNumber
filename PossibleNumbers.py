"""
Created on Wed May 27 21:21:38 2015

@author: Mathew Bramson
"""

#Sieve by Bruno Astrolino E Silva from stackoverflow.com/questions/2068372 
def primes(n):
	n, correction = n-n%6+6, 2-(n%6>1)
	sieve = [True] * (n/3)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k = 3*i + 1|1
			sieve[    k*k/3        ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
			sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
	return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

#Returns an array of integers less than n which are prime if Answer == True
#or are not prime if Answer == False
#We'll use the sieve of eratosthones defined by primes(n) above.
#Assumes n >= 2
def isPrime(Answer, n):
    Primes = [0,1] + primes(n)
    if Answer:
        return Primes
    else:
        return list(set(range(0,n)) - set(Primes))

#Returns an array of integers less than n which have exactly numFactors unique
#prime factors.    
def TotalUniquePrimeFactors(numFactors,n):
    Primes = primes(n)
    #TODO: Implement
    
#Returns an array of integers less than n which have exactly numFactors total
#prime factors. 
def TotalPrimeFactors(numFactors, n):
    Primes = primes(n)
    #TODO: Implement
    
#This is a specific case of the above two methods relevant to the question Ben
#answers. We just need to calculate all primes below n, and iterate through
#them with two nested for loops, never multiplying the same integers.
def HasTwoTotalUniquePrimeFactors(n):
    Primes = primes(n)
    returnList = []
    for indexi, i in enumerate(Primes):
        for indexj, j in enumerate(Primes[indexi+1:]): #List overflow here
            if i*j < n:
                returnList.append(i*j)
            else:
                break
        
    return sorted(returnList)

print HasTwoTotalUniquePrimeFactors(30)

#TODO: Implement Unit Testing
#Misc Unit Testing
#assert_equals(isPrime(True,20),[0,1,2,3,5,7,11,13,17,19])
#assert_equals(isPrime(False,20),[4,6,8,9,10,12,14,15,16,18])
#assert_equals(HasTwoTotalUniquePrimeFactors(10),[6,10,14,15,21,22,26])