# I just robbed a bank with some of my friends.
# We got away with $19,867,324,678,987.99, and now we have to split it up 5 ways.
# Using the cash  variable I've already defined for you, print out the dollar amount each robber gets to keep.
# (divide cash  by 5 and print the answer out)
# p.s. I haven't actually robbed a bank.  Yet.

money = 19_867_324_678_987.99
robbers = 5
cash = money / robbers

print(f"Each robber will have ${cash:.2f}")