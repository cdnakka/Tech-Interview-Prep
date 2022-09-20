'''
Computing the parity of a word is useful for a simple way to check errors in communication. 
Parity of a binary word is 1 if the number of 1's in a word is odd. 
'''

def parity_check(n): #O(n)

    parity = False
    
    #edge cases?
    while n:
        if n & 1 == 1:

            #flip parity
            parity = not parity

        n = n >> 1
    
    return parity

def parity_check_2(n): #O(k) where k are the number of bits set to 1. improves best case and worst case complexity

    result = 0
    
    #edge cases?
    while n:
        result ^= 1
        n &= n-1    #dropping lowest set bit of n
            
    return result

def parity_check_3(x): #O(logn) n is the word size

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
           
    return x & 1

if __name__ == '__main__':

    n = 8
    print(f'the binary representation of {n} is {bin(n)}')
    #depending on output format
    #print(f'the parity of {n} is {parity_check(n)}')
    if parity_check_3(n) == 1:
        print("Parity is odd")
    else:
        print("parity is even")
