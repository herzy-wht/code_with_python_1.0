#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_num = 0
#Input the 10 numbers
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    #Identify if it's even then plus one
    if num % 2 == 0:
        even_num += 1
print(even_num)

