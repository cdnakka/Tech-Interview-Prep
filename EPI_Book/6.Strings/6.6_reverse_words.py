'''
reverse words in a sentence

#reverse each word and then reverse entire string

input: "ram is costly" 
output: "costly is ram"
'''
#from tracemalloc import start


def reverse_words(s):

    #start, finish = 0, len(s)-1
    def reverse_range(s, start, finish):
        while start < finish:
            s[start] , s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    #reversing the whole string
    reverse_range(s, 0, len(s) -1)

    #reversing words separated by whitespaces:
    start = 0
    while True:
        finish = start
        #cover up length of a word using finish
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        
        if finish == len(s):
            break

        #update each word
        reverse_range(s, start, finish-1)
        start = finish + 1

    #last word gets missed since we're initializing finish wrt start
    reverse_range(s, start, len(s) - 1)

    return s

if __name__ == '__main__':

    a = ['a','c',' ','d','b','b',' ','c','a']
    #size = 7
    print(reverse_words(a))