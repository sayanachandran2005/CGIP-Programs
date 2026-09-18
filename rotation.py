import tkinter as tk
import math

# User input
angle = float(input("Enter rotation angle in degrees: "))

# Original triangle points
points = [
    (250, 150),
    (350, 150),
    (300, 250)
]

# Rotation center
cx = 300
cy = 200

# Convert angle from degrees to radians
theta = math.radians(angle)

rotated_points = []

# Calculate rotated coordinates
for x, y in points:

    # Move point relative to rotation center
    x_temp = x - cx
    y_temp = y - cy

    # Rotation formula
    x_new = x_temp * math.cos(theta) - y_temp * math.sin(theta)
    y_new = x_temp * math.sin(theta) + y_temp * math.cos(theta)

    # Move point back
    x_new = x_new + cx
    y_new = y_new + cy

    rotated_points.append((x_new, y_new))

# Create window
root = tk.Tk()
root.title("2D Rotation")

canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# Draw original triangle
canvas.create_polygon(points, fill="blue")

# Draw rotated triangle
canvas.create_polygon(rotated_points, fill="red")

root.mainloop()