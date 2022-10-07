'''
Tests if a given integer is a palindrome
'''
import math


def isPalindrome(x: int) -> bool:
    
    if x <= 0:
        return x == 0 #test 0 edge case


    # integer length
    len = math.floor(math.log10(x))
    print(len)

    # msd
    i = 0
    while i < len:
        print("i = ", i)

        if (x % 10)  != ( x // math.pow(10, len)):
            print("X:", x)
            return False
        print('passed val:', x)
        x = x // 10
        x = x % math.pow(10, len -1)
        print("treated X:", x)
        len = len - 2
        if len == 0 : 
            return True


    return True

# ( 130001 // math.pow(10, len - 1))
if __name__ == '__main__':

    n = 1000001

    #depending on output format

    if isPalindrome(n) == 1:
        print("Palindrome")
    else:
        print("Not a Palindrome")