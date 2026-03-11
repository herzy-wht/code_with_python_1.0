#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Input number from 0 to 1000
num = int(input("Enter a number from 0 to 100: "))
#chack how many digits of is the number
length = len(str(num))
#6 minus the length
diff = 6 - length
# The difference is the number of zeros we need to add
print(num, end='')
for diff in range(diff):
    print(0, end='')