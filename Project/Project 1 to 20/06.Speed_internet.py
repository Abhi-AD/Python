from tkinter import Tk, Label, Button, RAISED
import speedtest
import threading
import time


def speedcheck():
    def run_speedtest():
        # Show "Waiting..." before starting the test
        down_speed.config(text="Waiting...")
        upload_speed.config(text="Waiting...")
        sp = speedtest.Speedtest()
        sp.get_best_server()
        down = f"{round(sp.download() / (10**6), 3)} Mbps"
        up = f"{round(sp.upload() / (10**6), 3)} Mbps"
        # Update UI labels with results
        down_speed.config(text=down)
        upload_speed.config(text=up)

    # Run speed test in a separate thread to prevent UI freezing
    threading.Thread(target=run_speedtest, daemon=True).start()


# Initialize Tkinter window
sp = Tk()
sp.title("Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

# Title Label
Label(
    sp,
    text="Internet Speed Test",
    font=("Times New Roman", 20, "bold"),
    bg="blue",
    fg="#ffffff",
).place(x=60, y=40, height=50, width=380)

# Download Speed Label
Label(
    sp,
    text="Download Speed",
    font=("Times New Roman", 20, "bold"),
    bg="blue",
    fg="#ffffff",
).place(x=60, y=130, height=50, width=380)

down_speed = Label(
    sp, text="00 Mbps", font=("Times New Roman", 20, "bold"), bg="blue", fg="#ffffff"
)
down_speed.place(x=60, y=200, height=50, width=380)

# Upload Speed Label
Label(
    sp,
    text="Upload Speed",
    font=("Times New Roman", 20, "bold"),
    bg="blue",
    fg="#ffffff",
).place(x=60, y=290, height=50, width=380)

upload_speed = Label(
    sp, text="00 Mbps", font=("Times New Roman", 20, "bold"), bg="blue", fg="#ffffff"
)
upload_speed.place(x=60, y=360, height=50, width=380)

# Button to check speed
Button(
    sp,
    text="Check Speed",
    font=("Times New Roman", 20, "bold"),
    bg="red",
    fg="#ffffff",
    relief=RAISED,
    command=speedcheck,
).place(x=60, y=450, height=50, width=380)

sp.mainloop()
