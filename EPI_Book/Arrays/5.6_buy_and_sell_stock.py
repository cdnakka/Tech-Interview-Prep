'''
Given the opening stock prices over a few given days, what is the best entry and exit point for maximum profit?

ex:
    <310,315,275,295,260,270,290,230,255,250>.
'''
from typing import List
def buy_and_sell(A: List[int]) -> List[int]:

    minimum_sofar, max_profit, max_value = A[0], 0, A[0]

    for price in A:
        minimum_sofar = min(price, minimum_sofar)
        max_profit = max(max_profit, (price - minimum_sofar))
        #max_value = minimum_sofar + max_profit
    
    return [max_profit]

if __name__ == '__main__':

    A = [310,315,275,295,260,270,290,230,255,250]
    buy_sell = buy_and_sell(A)
    print(buy_sell)