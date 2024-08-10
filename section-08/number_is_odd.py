# You will be provided with a random number in a variable called num .
# Use a conditional statement to check if the number is odd. If num  is odd, print "odd". Otherwise print "even".

from random import randint

num = randint(1, 1000)
# Conditional
output = None
if num % 2 == 0:
    output = 'even'
else:
    output = 'odd'

# Output
print(output)
