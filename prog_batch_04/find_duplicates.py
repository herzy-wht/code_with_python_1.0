#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Numbers with duplicate:")
for num in duplicates:
    print(num)