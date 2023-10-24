# Create a version of the Rectangle class that is safe by assuring that both width and height are positive values (how you do that is up to you). Expand it with methods that calculate its surface area and its circumference. Also, provide a method that returns the bottom-right corner of the rectangle as a Point. Finally, create a method that gets a second Rectangle object as a parameter, and returns the overlapping area of the two rectangles as a new Rectangle object (the last one is much harder than the other ones).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, bottomLeftCornerX, bottomLeftCornerY):
        if width == 0 | height == 0:
            print("There is no rectangle with zero width of height")
        elif width < 0:
            self.bottomLeftCornerX = bottomLeftCornerX + width
            self.width = abs(width)
        elif height < 0:
            self.bottomLeftCornerY = bottomLeftCornerY + height
            self.height = abs(height)
        else:
            self.bottomLeftCornerX = bottomLeftCornerX
            self.bottomLeftCornerY = bottomLeftCornerY
            self.width = abs(width)
            self.height = abs(height)

    def surface_area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)

    def get_bottom_right_corner(self):
        x = self.bottomLeftCornerX + self.width
        y = self.bottomLeftCornerY
        return Point(x, y)

    def overlapping_area(self, other_rect):
        # Calculate the x and y ranges of the overlapping area
        x1 = max(self.bottomLeftCornerX, other_rect.bottomLeftCornerX)
        y1 = max(self.bottomLeftCornerY, other_rect.bottomLeftCornerY)
        x2 = min(self.bottomLeftCornerX+self.width, other_rect.bottomLeftCornerX+other_rect.width)
        y2 = min(self.bottomLeftCornerX+self.height, other_rect.bottomLeftCornerX+other_rect.height)

        # Check if there is an overlap
        if x1 < x2 and y1 < y2:
            width = x2 - x1
            height = y2 - y1
            return Rectangle(width, height, x1, y1)
        else:
            return None

# Example usage
rect1 = Rectangle(4, 5, 4, 5)
rect2 = Rectangle(3, 4, 0, 0)

print("Surface Area of rect1:", rect1.surface_area())
print("Circumference of rect1:", rect1.circumference())
print("Bottom Right Corner of rect1: x=", rect1.get_bottom_right_corner().x, "y=", rect1.get_bottom_right_corner().y)

overlapping = rect1.overlapping_area(rect2)
if overlapping:
    print("Overlapping Rectangle Area:", overlapping.surface_area())
else:
    print("No overlapping area between rect1 and rect2.")
