'''
Compute power of a number.
x^y

Brute force solution of multiplying a number with itself takes O(2^n) complexity for bits required to represent y
'''

def pow(x, y):

    #default values
    result, power = 1, y
    # if negative power
    if y <0:
        power, x = - power, 1.0/x

    while power:
        # adding power operations which arent a factor of 2
        if power & 1 == 1:
            result *= x
        #squaring x with itself and subtracting power by 1 as we loop through
        x, power  = x*x, power >> 1

    return result

if __name__ == '__main__':

    x = 2
    y = 3
    print(f'{x} raised to the power {y} is {pow(x,y)}')