import os
import sys
from tkinter import Tk, Button, RAISED


def get_os():
    """Detect the operating system."""
    if sys.platform.startswith("win"):
        return "windows"
    elif sys.platform.startswith("linux"):
        return "linux"
    elif sys.platform.startswith("darwin"):
        return "macos"
    else:
        return "unknown"


OS_TYPE = get_os()


def restart():
    """Restart the system based on OS."""
    if OS_TYPE == "windows":
        os.system("shutdown /r /t 1")
    elif OS_TYPE == "linux" or OS_TYPE == "macos":
        os.system("sudo reboot")


def restart_timer():
    """Restart the system with a delay."""
    if OS_TYPE == "windows":
        os.system("shutdown /r /t 20")
    elif OS_TYPE == "linux" or OS_TYPE == "macos":
        os.system("sudo shutdown -r +1")


def logout():
    """Log out the user based on OS."""
    if OS_TYPE == "windows":
        os.system("shutdown -l -f")
    elif OS_TYPE == "linux":
        os.system("pkill -KILL -u $USER")  # Force logout
    elif OS_TYPE == "macos":
        os.system("osascript -e 'tell application \"System Events\" to log out'")


def shutdown():
    """Shutdown the system based on OS."""
    if OS_TYPE == "windows":
        os.system("shutdown /s /t 1")
    elif OS_TYPE == "linux" or OS_TYPE == "macos":
        os.system("sudo shutdown -h now")


if __name__ == "__main__":
    st = Tk()
    st.title("Shutdown App")
    st.geometry("500x500")
    st.config(bg="red")

    r_button = Button(
        st,
        text="Restart",
        font=("Times New Roman", 20, "bold"),
        relief=RAISED,
        cursor="plus",
        command=restart,
    )
    r_button.place(x=150, y=60, height=50, width=200)

    rt_button = Button(
        st,
        text="Restart Timer",
        font=("Times New Roman", 20, "bold"),
        relief=RAISED,
        cursor="plus",
        command=restart_timer,
    )
    rt_button.place(x=150, y=170, height=50, width=200)

    lg_button = Button(
        st,
        text="Logout",
        font=("Times New Roman", 20, "bold"),
        relief=RAISED,
        cursor="plus",
        command=logout,
    )
    lg_button.place(x=150, y=270, height=50, width=200)

    st_button = Button(
        st,
        text="Shutdown",
        font=("Times New Roman", 20, "bold"),
        relief=RAISED,
        cursor="plus",
        command=shutdown,
    )
    st_button.place(x=150, y=370, height=50, width=200)

    st.mainloop()
