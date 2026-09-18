import tkinter as tk

# User input
sx = float(input("Enter scaling factor in X direction: "))
sy = float(input("Enter scaling factor in Y direction: "))

# Original rectangle
x1, y1 = 100, 100
x2, y2 = 200, 200

# Scaling
new_x1 = x1 * sx
new_y1 = y1 * sy
new_x2 = x2 * sx
new_y2 = y2 * sy

# Create window
root = tk.Tk()
root.title("2D Scaling")

canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# Original object
canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Scaled object
canvas.create_rectangle(
    new_x1, new_y1, new_x2, new_y2,
    fill="red"
)

root.mainloop()