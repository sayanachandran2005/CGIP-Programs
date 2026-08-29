import matplotlib.pyplot as plt

# Midpoint Circle Drawing Algorithm
def midpoint_circle(xc, yc, r):

    points = []

    x = 0
    y = r

    p = 1 - r

    while x <= y:

        # 8-way symmetry
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),

            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

        x += 1

        if p < 0:

            p += 2 * x + 1

        else:

            y -= 1
            p += 2 * (x - y) + 1

    return points


# Input
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))

r = int(input("Enter radius: "))


# Generate circle points
points = midpoint_circle(xc, yc, r)


# Display points
print("Midpoint Circle Pixel Coordinates:")
print(points)


# Plot
x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

plt.figure(figsize=(7, 7))

plt.scatter(
    x_values,
    y_values,
    color="purple",
    s=100
)

plt.title("Midpoint Circle Generation Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.axis("equal")

plt.show()
