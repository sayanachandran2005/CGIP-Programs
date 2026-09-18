import tkinter as tk

# User input
tx = int(input("Enter translation in X direction: "))
ty = int(input("Enter translation in Y direction: "))

# Original rectangle coordinates
x1, y1 = 200, 150
x2, y2 = 300, 250

# Calculate translated coordinates
new_x1 = x1 + tx
new_y1 = y1 + ty
new_x2 = x2 + tx
new_y2 = y2 + ty

# Create window AFTER taking input
root = tk.Tk()
root.title("2D Translation")

canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# Draw original object
canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Draw translated object
canvas.create_rectangle(
    new_x1, new_y1, new_x2, new_y2,
    fill="red"
)

root.mainloop()