def large(n):
    largest = n[0]
    for item in n:
        if item > largest:
            largest = item
    return largest

numbers = (input(">").split())
print(numbers)
print('Large: ',large(numbers))