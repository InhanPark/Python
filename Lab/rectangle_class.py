#Define a class Rectangle with attributes width and height,
#and methods to calculate the area and perimeter.

class Rectangle:
    """Get area and perimeter of rectangle"""
    def __init__(self, width, height):
        """Core data structure of Rectangle class"""
        self.width = width      #Width of rectangle
        self.height = height    #height of rectangle
    
    def area(self):
        """Calculate area of Rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter of Rectangle"""
        return (self.width * 2) + (self.height * 2)

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    print(rect.area())       # Output: 20
    print(rect.perimeter())  # Output: 18
