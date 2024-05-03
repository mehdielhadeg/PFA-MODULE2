import tkinter as tk
from tkinter import ttk
import mysql.connector
import os



listBox = None

def read_data():
    global listBox  
    listBox.delete(*listBox.get_children())  # Clear existing data
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="work")
    cursor = connection.cursor()
    cursor.execute("SELECT id, firstname, lastname, entry_date, Departement, Position FROM employes")
    records = cursor.fetchall()
    for record in records:
        listBox.insert("", "end", values=record)
    connection.close()

    
   


def delete_record():
    selected_item = listBox.selection()[0]
    record_id = listBox.item(selected_item)['values'][0]  # Get ID of selected record
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="work")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employes WHERE id = %s", (record_id,))
    connection.commit()
    connection.close()
    read_data()  # Refresh the records after deletion

def search():
    search_name = search_entry.get().strip().lower()
    if not search_name:
        return  # Do nothing if search query is empty
    
    # Clear selection and focus
    listBox.selection_remove(listBox.selection())
    listBox.selection_set(())
    listBox.focus("")
    
    for item in listBox.get_children():
        values = listBox.item(item)['values']
        if search_name in values[1].lower():
            listBox.selection_add(item)
            listBox.focus(item)
            listBox.see(item)  # Ensure the selected item is visible in the treeview


# Create the main window
root = tk.Tk()
root.title("Employee Records")

# Create Treeview widget
listBox = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "Entry Date", "Departement", "Position"), show="headings")
listBox.heading("ID", text="ID")
listBox.heading("First Name", text="First Name")
listBox.heading("Last Name", text="Last Name")

listBox.heading("Entry Date", text="Entry Date")
listBox.heading("Departement", text="Departement")
listBox.heading("Position", text="Position")
listBox.pack(pady=10)

# Button to read records
read_button = tk.Button(root, text="Read Records", command=read_data)
read_button.pack(pady=5)

# Button to update selected record
#update_button = tk.Button(root, text="Update Record", command= )
#update_button.pack(pady=5)

# Button to delete selected record
delete_button = tk.Button(root, text="Delete Record", command=delete_record)
delete_button.pack(pady=5)

#add button
def open_create_page():
    os.system("python create.py")
add_button = tk.Button(root, text="ADD new Record", command=open_create_page)
add_button.pack(pady=5)


# Search entry
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=15)

# Button to search by name
search_button = tk.Button(root, text="Search by name", command=search)
search_button.pack(pady=5)

# Run the Tkinter event loop

root.mainloop()