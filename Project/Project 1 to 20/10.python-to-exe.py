import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, filepath)


def convert_to_exe():
    py_file = entry_path.get()
    if not py_file:
        messagebox.showerror("Error", "Please select a Python file.")
        return

    command = f'pyinstaller --onefile "{py_file}"'
    subprocess.run(command, shell=True)
    messagebox.showinfo("Success", "Conversion completed! Check the 'dist' folder.")


# GUI Setup
root = tk.Tk()
root.title("Python to EXE Converter")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_path = tk.Entry(frame, width=40)
entry_path.pack(side=tk.LEFT, padx=10)

btn_browse = tk.Button(frame, text="Browse", command=select_file)
btn_browse.pack(side=tk.LEFT)

btn_convert = tk.Button(root, text="Convert to EXE", command=convert_to_exe)
btn_convert.pack(pady=20)

root.mainloop()
