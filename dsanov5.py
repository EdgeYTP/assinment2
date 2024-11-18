def reverse_evens(A):
  even_numbers = []

  for num in A:
    if num % 2 == 0:
      even_numbers.append(num)

  K = len(even_numbers)
  print(K)

  even_numbers.reverse()

  for num in even_numbers:
    print(num, end=" ")
  print()

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
reverse_evens(numbers)  # Output: 4 8 6 4 2