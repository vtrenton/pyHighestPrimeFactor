#!/usr/bin/env python

import math
## SIEVE OF ERATOSTHENES - FIND ALL PRIMES UP TO SQRT(N)
def getList (sievelimit):
    # up to two should be set to false
    sievelist = [False]*2

    # set 2 and above to True for futher evaluation
    for i in range(2, sievelimit):
        sievelist.append(True)
    # return the list of true values
    return sievelist

# find all the non-primes in the list and set them to false
def getprimes (nolist, sievelimit):
    for i in range(len(nolist)):
        if nolist[i]:
            # we want to start off setting i^2 to false
            x = i*i
            # start with i^2 and iterate to the limit by i setting all to false
            for j in range(x, sievelimit, i):
               nolist[j] = False

    return nolist

## FIND FACTORS OF N (n%i == 0)
def getfactors(primelist, userinput):
    primfactlist = []
    for i in range(len(primelist)):
        if primelist[i]:
            # use the mod to determine if there are any remainders
            if userinput%i==0:
                primfactlist.append(i)

    return primfactlist

## MAIN FUNCTION
def main():
    # gather a seed number from the user
    # we want to validate user input to assure that a certain range of numbers is entered
    while True:
        try:
            print "Please enter a number to find it's highest prime factor (enter 0 to exit)"
            n = long(raw_input("Please enter a value: "))
            break
        except:
            print "please enter a value between 1 and 9223372036854775807"
    
    # let the user out of the program
    if n == 0:
        exit(0)

    # get a list of all of the primes if there are any
    primes = getprimes(getList(n), n)
    # bring the prime factor list to main
    outputlist = getfactors(primes, n)
   
    if len(outputlist) > 0:
        print "\nlist of prime factorials:"
        for i in outputlist:
            print i
        
        highestprime = outputlist[len(outputlist)-1]
        print '\nthis is the highest prime factorial of %i:' % n
        print highestprime
    else:
        print "\nThis number contains no prime factorials"

if __name__ == '__main__':
    main()
