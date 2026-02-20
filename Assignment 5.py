# # Lab Assignment - 1
#
# # Taking input from user
# numbers = tuple(map(int, input("Enter integers separated by space: ").split()))
#
# print("\nTuple entered:", numbers)
#
# # a) Total number of items
# print("Total number of items:", len(numbers))
#
# # b) Last item
# print("Last item in the tuple:", numbers[-1])
#
# # c) Reverse order
# print("Tuple in reverse order:", numbers[::-1])
#
# # d) Check if integer 5 exists
# if 5 in numbers:
#     print("Yes, 5 is present in the tuple.")
# else:
#     print("No, 5 is not present in the tuple.")
#
# # e) Remove first and last item, sort remaining
# if len(numbers) > 2:
#     remaining = numbers[1:-1]
#     sorted_remaining = tuple(sorted(remaining))
#     print("After removing first and last items and sorting:", sorted_remaining)
# else:
#     print("Not enough elements to remove first and last.")



# Lab Assignment - 2

# Taking price input
prices = tuple(map(float, input("Enter prices separated by space: ").split()))

print("\nPrices entered:", prices)

# a) Total number of items sold
print("Total number of items sold:", len(prices))

# b) Cheapest item
cheapest = min(prices)
print("Cheapest item price:", cheapest)

# c) Costliest item
costliest = max(prices)
print("Costliest item price:", costliest)

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
count_costliest = prices.count(costliest)
print("Number of costliest items sold:", count_costliest)