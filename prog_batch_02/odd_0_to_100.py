#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
num = 0
#Print 0 to 100
while num != 100:
    #Identify if it's odd then print
    num += 1
    if num % 2 != 0:
        print(num)
