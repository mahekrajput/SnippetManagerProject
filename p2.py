import database_operations  # This connects frontend with backend
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Dummy Functions (Replace with database functions after merging)
def save():
    title = title_entry.get()
    language = language_entry.get()
    code = code_text.get("1.0", tk.END).strip()
    tags = tags_entry.get()

    if title and code:
        messagebox.showinfo("Success", "Snippet Saved!")
        update_list()
    else:
        messagebox.showwarning("Error", "Title & Code required!")

def update_list():
    listbox.delete(0, tk.END)
    snippets = [("Bubble Sort", "Python"), ("Quick Sort", "Python")]  # Dummy data
    for snippet in snippets:
        listbox.insert(tk.END, snippet[0])

def delete():
    try:
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])
            messagebox.showinfo("Success", "Snippet Deleted!")
    except:
        messagebox.showwarning("Error", "Select a snippet to delete!")

# GUI Setup
root = tk.Tk()
root.title("Code Snippet Manager")

tk.Label(root, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Language:").grid(row=1, column=0)
language_entry = tk.Entry(root, width=30)
language_entry.grid(row=1, column=1)

tk.Label(root, text="Code:").grid(row=2, column=0)
code_text = scrolledtext.ScrolledText(root, width=40, height=5)
code_text.grid(row=2, column=1)

tk.Label(root, text="Tags:").grid(row=3, column=0)
tags_entry = tk.Entry(root, width=30)
tags_entry.grid(row=3, column=1)

tk.Button(root, text="Save", command=save).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete).grid(row=5, column=1)

tk.Label(root, text="Saved Snippets:").grid(row=6, column=0)
listbox = tk.Listbox(root, width=40, height=5)
listbox.grid(row=6, column=1)

update_list()
root.mainloop()
