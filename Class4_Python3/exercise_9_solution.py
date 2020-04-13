# write a loop which randomly generates
# either a 1 or a 2
#
# store the amount of times a 1 was generated in
# the variable "heads" and the amount of times a 2
# was generated in the variable "tails"
#
# let the loop run 100 times.
# what percentage of the time did you get
# tails/heads?
#
# then let the loop run 10 000 times.
# what percentage did you get now?
#
# to generate random integers us the random library
# and the function random.randint(a,b)
#
# randint(a,b) -> Return a random integer N such that a <= N <= b

# you can find more about the random library here:
# https://docs.python.org/3/library/random.html

import random

tails = 0
heads = 0
for i in range(100):
    x = random.randint(1,2)
    if x == 1:
        heads +=1
    else:
        tails +=1
    proportions = heads/(i+1)
    print("proportions of heads to amount of trials:", proportions)

print(heads)
print(tails)
