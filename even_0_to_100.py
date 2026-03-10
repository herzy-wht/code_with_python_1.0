#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
even_num = 0
#print number o to 100
for i in range (101):
    # Identify if it's even then add one
    if i % 2 == 0:
        even_num += 1
print(even_num)

