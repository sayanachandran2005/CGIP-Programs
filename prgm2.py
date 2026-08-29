import matplotlib.pyplot as plt

# Bresenham Line Drawing Algorithm
def bresenham_line(x1, y1, x2, y2):

    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x = x1
    y = y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:

        p = 2 * dy - dx

        for _ in range(dx):

            points.append((x, y))

            x += sx

            if p >= 0:
                y += sy
                p -= 2 * dx

            p += 2 * dy

    else:

        p = 2 * dx - dy

        for _ in range(dy):

            points.append((x, y))

            y += sy

            if p >= 0:
                x += sx
                p -= 2 * dy

            p += 2 * dx

    points.append((x2, y2))

    return points


# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Generate points
points = bresenham_line(x1, y1, x2, y2)


# Display points
print("Bresenham Pixel Coordinates:")
print(points)


# Plot
x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

plt.figure(figsize=(7, 6))

plt.scatter(
    x_values,
    y_values,
    color="blue",
    s=100
)

plt.plot(
    x_values,
    y_values,
    color="black"
)

plt.title("Bresenham Line Drawing Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.xticks(range(min(x_values) - 1, max(x_values) + 2))
plt.yticks(range(min(y_values) - 1, max(y_values) + 2))

plt.show()
