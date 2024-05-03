import tkinter as tk
import subprocess

def open_login_page():
    subprocess.Popen(["python", "login.py"])
    
def open_main_page():
    subprocess.Popen(["python", "main.py"])

def open_page_one():
    open_login_page()
    
def open_page_two():
    open_main_page()

root = tk.Tk()
root.title("Main Page")
root.geometry("600x300")

# Header frame
header_frame = tk.Frame(root)
header_frame.pack()

# Title label
title_label = tk.Label(header_frame, text="Hello! Please choose what you want", font=("Arial", 20))
title_label.pack(pady=10)



# Buttons to navigate between pages
button_page_one = tk.Button(root, text="CRUD", command=open_page_one)
button_page_one.pack(side="left", padx=10)

button_page_two = tk.Button(root, text="ATTENDANCE", command=open_page_two)
button_page_two.pack(side="right", padx=10)

root.mainloop()


