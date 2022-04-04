

# Challenge 1
#Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n

def sum_to(x):
  total = 0
  for number in range(1, x + 1):
    total += number
  return total

print(sum_to(67))



# Challenge 2
# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(numbers):
  largest = 0
  for number in numbers:
    if number > largest:
      largest = number
  return largest


print(largest([10, 4, 2, 231, 91, 54]))