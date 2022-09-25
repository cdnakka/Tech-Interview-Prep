'''
Convert an integer to ta string without uusing the predefined methods

'''

def itoa(A):

    sign = '-' if A < 0 else ''
    A = -A if A < 0 else A
    s = []
    while True:
        s.append(chr(ord('0') + A % 10))
        A //= 10
        print(A)
        if A == 0:
            break
        
    return(sign + ''.join(reversed(s)))




if __name__ == '__main__':

    print(itoa(-15243))