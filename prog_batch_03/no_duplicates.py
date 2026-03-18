#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
list = []
#Input 10 numbers
for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    list.append(num)
#If the number is the same as the previous number, do not print it
    for j in list:
        if list != list[j]:
             print(j)

