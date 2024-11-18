# ```plaintext
# Function findMinAndMax(arr):
#  Set min to the first element of arr
#  Set max to the first element of arr
#  For each element in arr:
#  If element is less than min:
#  Set min to element
#  If element is greater than max:
#  Set max to element
#  Print min
#  Print max
# End Function
def findMinAndMax(arr):
    min_value = arr[0]
    max_value = arr[0]

    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    print("Minimum value:", min_value)
    print("Maximum value:", max_value)

# Example usage:
my_array = [5, 2, 9, 1, 7]
findMinAndMax(my_array)