'''
Return the reverse of an integer. 
ex. input if -341 returns -143

'''

def reverse_bits(x):

    #default cases, set positive for easy operations
    result, x_remaining  = 0, abs(x) 

    #main loop
    while x_remaining:

        result = result * 10 + x_remaining % 10

        x_remaining //= 10

    #flip sign if negative to start with
    return result if x>0 else -result

if __name__ == '__main__':

    x = -405
    print(f'{x} when its digits are reversed is {reverse_bits(x)}')