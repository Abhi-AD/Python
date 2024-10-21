# # # Creating  in the dict user data multiple value 
b = {}
n = int(input("Enter a dici number: "))
for i in range(n):
    name = input("Enter a name: ")
    ntc = int(input("Enter a NTC number:  "))
    ncell = int(input("Enter a Ncell number:  "))
    b[name] = [ntc,ncell]
print(b)