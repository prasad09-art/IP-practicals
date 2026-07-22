#Q6: Area and perimeter calculato

import math

length = float(input("Enter Rectangel Length:"))
breadth = float(input("Enter Rectangel Breadth:"))

area_rect = length * breadth

perimeter_react = 2 * (length + breadth)

radius = float(input("Enter circle radius:"))

area_circle = math.pi * radius ** 2
circumference = 2* math.pi * radius

print("\nRectangel")
print("Area =", area_rect)
print("Perimeter =", perimeter_react)


print("\nCircle")
print("Area =", round(area_circle, 2))
print("circumference =", round(circumference, 2))
