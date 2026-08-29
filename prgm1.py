import matplotlib.pyplot as plt

def draw_dda_line(x1, y1, x2, y2):
    # 1. Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1
    
    
    # We step along the axis with the larger absolute change
    steps = int(max(abs(dx), abs(dy)))
    
    # 3. Calculate the increment values for x and y
    x_inc = dx / steps if steps != 0 else 0
    y_inc = dy / steps if steps != 0 else 0
    
    # 4. Initialize starting points
    x = x1
    y = y1
    
    # Lists to store the rounded pixel coordinates for plotting
    x_pixels = []
    y_pixels = []
    
    print(f"Total Steps: {steps}")
    print("Generated Pixel Coordinates:")
    
    # 5. Generate points along the line
    for _ in range(steps + 1):
        # Round the values to get the nearest integer pixel
        px, py = round(x), round(y)
        x_pixels.append(px)
        y_pixels.append(py)
        
        print(f"({px}, {py})")
        
        # Accumulate the fractional increments
        x += x_inc
        y += y_inc
        
    # 6. Visualize the output using Matplotlib
    plt.figure(figsize=(6, 6))
    plt.scatter(x_pixels, y_pixels, color='red', zorder=5, label='Pixels')
    plt.plot(x_pixels, y_pixels, color='blue', alpha=0.5, label='DDA Line Path')
    
    # Format the grid to mirror individual screen pixels
    plt.title('DDA Line Drawing Algorithm')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True, which='both', linestyle='--', color='gray')
    plt.xticks(range(min(x_pixels)-1, max(x_pixels)+2))
    plt.yticks(range(min(y_pixels)-1, max(y_pixels)+2))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

# Example usage: Draw a line from (2, 4) to (8, 12)
draw_dda_line(2, 4, 8, 12)
