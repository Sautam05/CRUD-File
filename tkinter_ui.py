from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os
import shutil


# ---------------- FUNCTIONS ---------------- #

def create_file():
    file_name = entry1.get()
    content = text1.get("1.0", END)

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "FILE ALREADY EXISTS")

    else:
        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE CREATED")


def read_file():
    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'r') as file:
            data = file.read()

        text1.delete("1.0", END)
        text1.insert(END, data)

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def update_file():

    file_name = entry1.get()
    content = text1.get("1.0", END)

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "FILE UPDATED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def delete_file():

    file_name = entry1.get()

    p = Path(file_name)

    if p.exists():

        os.remove(file_name)

        messagebox.showinfo("Success", "FILE DELETED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def rename_file():

    old_name = entry1.get()
    new_name = entry2.get()

    p = Path(old_name)

    if p.exists():

        p.rename(new_name)

        messagebox.showinfo("Success", "FILE RENAMED")

    else:
        messagebox.showerror("Error", "FILE NOT FOUND")


def create_folder():

    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():

        messagebox.showerror("Error", "FOLDER ALREADY EXISTS")

    else:

        p.mkdir()

        messagebox.showinfo("Success", "FOLDER CREATED")


def delete_folder():

    folder_name = entry1.get()

    p = Path(folder_name)

    if p.exists():

        shutil.rmtree(folder_name)

        messagebox.showinfo("Success", "FOLDER DELETED")

    else:

        messagebox.showerror("Error", "FOLDER NOT FOUND")


# ---------------- TKINTER UI ---------------- #

root = Tk()

root.title("CRUD File Handling System")
root.geometry("600x500")
root.config(bg="lightblue")

Label(root, text="File / Folder Name", bg="lightblue",
      font=("Arial", 12)).pack(pady=5)

entry1 = Entry(root, width=50)
entry1.pack(pady=5)

Label(root, text="New File Name (For Rename)",
      bg="lightblue", font=("Arial", 12)).pack(pady=5)

entry2 = Entry(root, width=50)
entry2.pack(pady=5)

Label(root, text="File Content", bg="lightblue",
      font=("Arial", 12)).pack(pady=5)

text1 = Text(root, width=60, height=10)
text1.pack(pady=10)

Button(root, text="Create File", width=20,
       command=create_file).pack(pady=5)

Button(root, text="Read File", width=20,
       command=read_file).pack(pady=5)

Button(root, text="Update File", width=20,
       command=update_file).pack(pady=5)

Button(root, text="Delete File", width=20,
       command=delete_file).pack(pady=5)

Button(root, text="Rename File", width=20,
       command=rename_file).pack(pady=5)

Button(root, text="Create Folder", width=20,
       command=create_folder).pack(pady=5)

Button(root, text="Delete Folder", width=20,
       command=delete_folder).pack(pady=5)

root.mainloop()