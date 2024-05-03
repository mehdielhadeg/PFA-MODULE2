import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector
import os
from datetime import datetime

def add_employee():
    id = id_entry.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    img_path = img_entry.get()
    entrydate = entrydate_entry.get()
    Departement = Departement_entry.get()
    Position = Position_entry.get()

    # Add logic to validate input fields
    if id and firstname and lastname and img_path:
        try:
            with open(img_path, "rb") as f:
                img_data = f.read()
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file not found!")
            return
        
        

        connection = mysql.connector.connect(host="localhost", user="root", password="", database="work")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employes (id,firstname, lastname, img, entry_date, Departement, Position) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, firstname, lastname, img_data, entrydate, Departement, Position))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Employee added successfully!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Please fill all fields")

def clear_fields():
    id_entry.delete(0, tk.END)
    firstname_entry.delete(0, tk.END)
    lastname_entry.delete(0, tk.END)
    img_entry.delete(0, tk.END)
    entrydate_entry.delete(0, tk.END)
    Departement_entry.delete(0, tk.END)
    Position_entry.delete(0, tk.END)

def browse_image():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    img_entry.delete(0, tk.END)
    img_entry.insert(0, img_path)

# Create the main window
root = tk.Tk()
root.title("Add Employee")
root.geometry("400x300+300+120")

# Labels and entry fields for employee details
tk.Label(root, text="id:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="First Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
firstname_entry = tk.Entry(root)
firstname_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
lastname_entry = tk.Entry(root)
lastname_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Image:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
img_entry = tk.Entry(root)
img_entry.grid(row=3, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.grid(row=3, column=2, padx=5, pady=5)

tk.Label(root, text="Entry Date:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
entrydate_entry = tk.Entry(root)
entrydate_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Departement:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
Departement_entry = tk.Entry(root)
Departement_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Position:").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
Position_entry = tk.Entry(root)
Position_entry.grid(row=6, column=1, padx=5, pady=5)

# Button to add employee
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=7, column=0, columnspan=2, pady=10)

# Button to open the read page
def open_read_page():
    os.system("python read.py")  

read_button = tk.Button(root, text="Go to READ Page", command=open_read_page)
read_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
