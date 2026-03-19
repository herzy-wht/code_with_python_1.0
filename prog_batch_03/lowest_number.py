#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
lowest = None

while True:
    try:
        num = int(input("Enter a number: "))

        if lowest is None or num < lowest:
            lowest = num

    except:
        print("Invalid input. Program stopped.")
        break

# Display lowest number
if lowest is not None:
    print("Lowest number:", lowest)
else:
    print("No valid numbers entered.")