#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

most_duplicate = numbers[0]
highest_count = numbers.count(numbers[0])

for num in numbers:
    if numbers.count(num) > highest_count:
        highest_count = numbers.count(num)
        most_duplicate = num

print("Number with the most duplicates:", most_duplicate)