import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os

# Connexion a la base de donnees MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="work"
)

# Creation de la fenetre principale
root = tk.Tk()
root.title("Login")
root.geometry("400x300+300+120")

# Fonction pour verifier les informations de connexion
def login():
    username = username_entry.get()
    password = password_entry.get()

    cursor = mydb.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Connexion reussie!")
        # Masquer la fenetre de connexion
        root.withdraw()
        # Ouvrir la nouvelle fenetre
        open_new_page()
    else:
        messagebox.showerror("Error", "Nom d'utilisateur ou mot de passe incorrect!")

# Fonction pour ouvrir une nouvelle page
def open_new_page():
    # Get the path to the SQL page
    sql_page_path = os.path.join(os.path.dirname(__file__), "read.py")

    # Execute the SQL page
    exec(open(sql_page_path).read())

# Creation des champs de saisie et des etiquettes
username_label = tk.Label(root, text="Nom d'utilisateur:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Mot de passe:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Connexion", command=login)
login_button.pack()

# Execution de la fenetre principale
root.mainloop()