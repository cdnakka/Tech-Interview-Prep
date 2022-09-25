'''
Check if a given string is a palindrome
'''

def is_palindrome(s:str) -> bool:

    #i gets incremented and j gets decremented
    i, j = 0, len(str)-1
    while i<j:

        # if not alphanumeric, increment and decrement the respective pointers
        while not s[i].isalnum() and i <j:
            i +=1
        while not s[j].isalnum() and i <j:
            j-=1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i, j = i+1, j-1

    return True

