#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#Print 0 to 100
for i in range (1, 100):
    #Identify if the number is divisible by 10 then print nothing
    if i % 10 == 0:
        print(end='')
    else:
        print(i)
