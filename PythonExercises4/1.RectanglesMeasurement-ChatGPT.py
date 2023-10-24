class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, bottom_left_corner):
        if width <= 0 or height <= 0:
            raise ValueError("Both width and height must be positive values.")
        self.width = width
        self.height = height
        self.bottom_left_corner = bottom_left_corner

    def surface_area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)

    def get_bottom_right_corner(self):
        x = self.bottom_left_corner.x + self.width
        y = self.bottom_left_corner.y
        return Point(x, y)

    def overlapping_area(self, other_rect):
        # Calculate the x and y ranges of the overlapping area
        x1 = max(self.bottom_left_corner.x, other_rect.bottom_left_corner.x)
        y1 = max(self.bottom_left_corner.y, other_rect.bottom_left_corner.y)
        x2 = min(self.get_bottom_right_corner().x, other_rect.get_bottom_right_corner().x)
        y2 = min(self.bottom_left_corner.y + self.height, other_rect.bottom_left_corner.y + other_rect.height)

        # Check if there is an overlap
        if x1 < x2 and y1 < y2:
            width = x2 - x1
            height = y2 - y1
            return Rectangle(width, height, Point(x1, y1))
        else:
            return None

# Example usage
rect1 = Rectangle(4, 5, Point(1, 2))
rect2 = Rectangle(3, 4, Point(2, 3))

print("Surface Area of rect1:", rect1.surface_area())
print("Circumference of rect1:", rect1.circumference())
print("Bottom Right Corner of rect1:", rect1.get_bottom_right_corner())

overlapping = rect1.overlapping_area(rect2)
if overlapping:
    print("Overlapping Rectangle Area:", overlapping.surface_area())
else:
    print("No overlapping area between rect1 and rect2.")