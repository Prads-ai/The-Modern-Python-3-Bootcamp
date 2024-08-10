# This program generates random numbers and if the number is 7 it prints out lucky otherwise unlucky.

from random import randint

number_genarator = randint(1,10)
if number_genarator == 7:
    print('lucky')
else:
    print('unlucky')

