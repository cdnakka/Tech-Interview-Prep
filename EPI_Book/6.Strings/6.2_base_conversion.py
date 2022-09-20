'''
Conversion of an integer from one base to another

'''

def base_conversion(num, base)->str:

    if not num: return '0'
    sign = num < 0
    num = abs(num)

    seq = []
    while True:
        seq.append(str(num % base))
        num //= base
        if num == 0: break

    return ('-'*sign + ''.join(seq[::-1]))

#recursive approach

def base_conversion_rec(num, base) -> str:
    if num < 0: return ('-' + base_conversion_rec(-num // base, base))
    if num < base: return str(num)
    return base_conversion_rec(num // base, base) + str(num % base)

if __name__ == '__main__':

    print(base_conversion_rec(306,7))

