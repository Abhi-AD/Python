# # # two number is add the operator overloding
class Data:
    def __init__(self,a):
        self.a = a
    
    def __str__(self):
        return f"{self.a}"
    
    def __add__(self, b):
        x = self.a + b.a
        return(x)
p1 = Data(int(input("Enter a first number: ")))
p2 = Data(int(input("Enter a second number: ")))
print(p1+p2)