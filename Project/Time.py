import tkinter as tk
import time
import math

# Create a window
root = tk.Tk()
root.title("Analog Watch")

# Set the dimensions of the window
root.geometry("400x400")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw the clock face
canvas.create_oval(50, 50, 350, 350, fill="white", outline="black", width=2)


# Function to draw the clock hands
def draw_clock():
    canvas.delete("hands")  # Delete previous hands

    # Get current time
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the angles of the clock hands
    hour_angle = (360 / 12) * (hours % 12 + minutes / 60)
    minute_angle = (360 / 60) * minutes
    second_angle = (360 / 60) * seconds

    # Draw the hour hand (length 60px)
    canvas.create_line(
        200,
        200,
        200 + 60 * math.cos(math.radians(hour_angle - 90)),
        200 + 60 * math.sin(math.radians(hour_angle - 90)),
        width=6,
        fill="black",
        tags="hands",
    )

    # Draw the minute hand (length 90px)
    canvas.create_line(
        200,
        200,
        200 + 90 * math.cos(math.radians(minute_angle - 90)),
        200 + 90 * math.sin(math.radians(minute_angle - 90)),
        width=4,
        fill="blue",
        tags="hands",
    )

    # Draw the second hand (length 100px)
    canvas.create_line(
        200,
        200,
        200 + 100 * math.cos(math.radians(second_angle - 90)),
        200 + 100 * math.sin(math.radians(second_angle - 90)),
        width=2,
        fill="red",
        tags="hands",
    )

    # Draw clock numbers: 12, 3, 6, 9
    canvas.create_text(200, 50, text="12", font=("Helvetica", 12, "bold"))
    canvas.create_text(350, 200, text="3", font=("Helvetica", 12, "bold"))
    canvas.create_text(200, 350, text="6", font=("Helvetica", 12, "bold"))
    canvas.create_text(50, 200, text="9", font=("Helvetica", 12, "bold"))

    # Redraw the clock every 1000 ms (1 second)
    root.after(1000, draw_clock)


# Start the clock
draw_clock()

# Run the Tkinter event loop
root.mainloop()
