#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_num = 0

for i in range (10):
    #input number
    num = int(input(f"Enter the number {i}: "))

    #identify if it's odd or not then plus 1
    if num % 2 != 0:
        odd_num += 1

#then the cycle continues until 10th number
print(odd_num)