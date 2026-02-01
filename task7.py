
while True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start <= end:
        break
    else:
        print("Invalid input! Start number should be less than or equal to end number.")

print("Prime numbers between", start, "and", end, "are:")


for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
