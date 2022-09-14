def classify_triangle(a,b,c):
    if (a == 0 or b == 0 or c == 0):
        return "A triangle must have 3 sides of non-zero length."
    elif a == b == c:
        return "Equilateral"
    elif (a**2 + b**2) == c**2:
        return "Right"
    elif (a == b or a == c or b == c):
        return "Isosceles"
    else:
        return "Scalene"
