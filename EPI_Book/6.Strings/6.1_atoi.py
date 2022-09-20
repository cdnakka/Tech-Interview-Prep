'''
Convert a string to integer without using the int method

A few edge cases:
within integer boundaries <|2^32|
first word in string should be integer

'''

def atoi(A): #string to integer

    result = 0
    for i in range(len(A)):
        result = result*10 + ord(A[i]) - ord('0')
        print(result)
    
        
    return result




if __name__ == '__main__':

    print(atoi("15243"))