# WAP to find factorial number
number = int(input("Enter a Factorial number:   "))
for i in range(1,number):
    number*=i
    print(number)