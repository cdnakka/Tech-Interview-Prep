'''
Computing the parity of a word is useful for a simple way to check errors in communication. 
Parity of a binary word is 1 if the number of 1's in a word is odd. 
'''

def parity_check(n):

    parity = False
    
    #edge cases?
    while n:
        if n & 1 == 1:

            #flip parity
            parity = not parity

        n = n >> 1
    
    return parity

if __name__ == '__main__':

    n = 8
    print(f'the binary representation of {n} is {bin(n)}')
    #depending on output format
    #print(f'the parity of {n} is {parity_check(n)}')
    if parity_check(n):
        print("Parity is odd")
    else:
        print("parity is even")
