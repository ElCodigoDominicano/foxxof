"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Alfredo Elias Rivas
Date:   03/21/2021
"""


import currency


a = input('3-letter code for original currency: ')
b = input('3-letter code for the new currency: ')
c = float(input('Amount of the original currency: '))

d = currency.exchange(a,b,c)

print('You can exchange',c ,a+' for',round(d,3) ,b+'.')
