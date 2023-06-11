# Write a python program to count the number of string where the string length is 2 or more and the first and last character are same from a given list of string
data = ['maya', 'hello', 'ghopti', 'madam', 'miss', 'level']
count = 0
for string in data:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print("The number of strings that meet the criteria is:", count)
