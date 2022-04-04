

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


# Challenge 3
# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(string, substring):
  return string.count(substring)

print(occurrences('fleep floop', 'e'))


# Challenge 4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*arguments):
  total = 1
  for argument in arguments:
    total *= argument
  return total

print(product(-1, 4))