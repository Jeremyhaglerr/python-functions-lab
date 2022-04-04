

# Challenge 1
#Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n

def sum_to(x):
  total = 0
  for number in range(1, x + 1):
    total += number
  return total

print(sum_to(67))



