#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#Print 0 to 100
for i in range (1, 100):
    #Identify if the number is not divisible by 5 then print
    if i % 5 != 0:
        print(i)