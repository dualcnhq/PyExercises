
# Write a snippet of code that approaches the number pi. 
# It should print out it's progress to the console every 10000 iterations. 
# Here is the math: pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 

import math

def main():
  sum = 0
  n = 10000
  for i in range(n):
    sum = sum + 4.0 * (-1) ** i / (2 * i + 1)
    accuracy = 100 * abs(math.pi - sum) / sum

    print "The approximation of pi with", n, "terms is", sum
    print "The accuracy of this approximation is", accuracy, "%."

main()
