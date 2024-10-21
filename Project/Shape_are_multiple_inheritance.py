class Shape:
    def __init__(self):
        self.color = input("Enter a shape color: ")
    
    def get_color(self):
        return f"This shape's color is {self.color}"
    
class Circle(Shape):
    def area(self):
        r = float(input("Please enter a Circle radius: "))
        a = 3.14 * r**2
        return a

class Rectangle(Shape):
    def area(self):
        l = int(input("Enter a Rectangle length: "))
        b = int(input("Enter a Rectangle breadth: "))
        h = int(input("Enter a Rectangle height: "))
        _area = l * b*h
        return _area


# Create a Circle instance
circle = Circle()
circle_color = circle.get_color()
circle_area = circle.area()

# Create a Rectangle instance
rectangle = Rectangle()
rectangle_color = rectangle.get_color()
rectangle_area = rectangle.area()

# Print the results
print(f"Circle Color: {circle_color}")
print(f"Circle Area: {circle_area}")

print(f"Rectangle Color: {rectangle_color}")
print(f"Rectangle Area: {rectangle_area}")
