def reverse_odds(A):
  odd_numbers = []

  for num in A:
    if num % 2 != 0:
      odd_numbers.append(num)

  print(len(odd_numbers))
  odd_numbers.reverse()

  for num in odd_numbers:
    print(num)

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7]
reverse_odds(numbers)