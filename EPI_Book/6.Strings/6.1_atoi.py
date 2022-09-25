'''
Convert a string to integer without using the int method

A few edge cases:
within integer boundaries <|2^32|
first word in string should be integer

'''

def atoi(A): #string to integer

    result = 0
    #covering up edge cases
    if len(A) == 0 :return 0
    A = list(A.strip())
    #leading whitespaces

    sign = -1 if A[0]=='-' else 1
    if A[0] in ['+', '-']: del A[0]
    for i in range(len(A)):
        result = result*10 + ord(A[i]) - ord('0')
        print(result)
    
        
    return max( -2**31, min(sign*result, 2**31 -1))




if __name__ == '__main__':

    print(atoi("-15243"))