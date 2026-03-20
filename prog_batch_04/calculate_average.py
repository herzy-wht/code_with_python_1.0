#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:  # Check if list is not empty
    average = sum(numbers) / len(numbers)
    print("Average of the numbers:", average)
else:
    print("No numbers were entered.")