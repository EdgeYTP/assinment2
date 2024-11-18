def check_basket(fruits):
  unique_fruits = set(fruits)

  if len(unique_fruits) > 1:
    print("Mixed Basket")
  else:
    print("Single Type")
basket1 = ["apple", "banana", "orange"]
basket2 = ["apple", "apple"]

check_basket(basket1)
check_basket(basket2) 