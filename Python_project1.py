import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task: 
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        picked = listbox.curselection()[0]
        listbox.delete(picked)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def check_task():
    try:
        # Gets the index of the selected item
        chosen = listbox.curselection()[0]
        
        # Gets the current value of the selected item
        presentval = listbox.get(chosen)
        
        # Check mark symbol
        check_mark = "\u2713"
        
        # Adds a check mark if not added
        if not presentval.startswith(check_mark):
            newval = f"{check_mark} {presentval}"
            listbox.delete(chosen)
            listbox.insert(chosen, newval)
    except IndexError:
        tk.messagebox.showwarning("Warning", "Please select an item to check.")

# Creating the main window
window = tk.Tk()
window.title("To Do List")
window.geometry('400x300')

# Label for entry field
label = tk.Label(window, text="Enter your task:")
label.grid(column=0, row=0, padx=10, pady=10)

# Entry field for adding tasks
entry = tk.Entry(window, width=40)
entry.grid(column=1, row=0, padx=10, pady=10)

# Button to add tasks
btn_add = tk.Button(window, text="Add Task", command=add_task)
btn_add.grid(column=0, row=1, padx=10, pady=10)

# Button to delete tasks
btn_delete = tk.Button(window, text="Delete Task", command=delete_task)
btn_delete.grid(column=1, row=1, padx=10, pady=10)

# Button to mark tasks as checked
btn_check = tk.Button(window, text="Check Task", command=check_task)
btn_check.grid(column=0, row=3, padx=10, pady=10)

# Listbox to display tasks
listbox = tk.Listbox(window, width=50, height=10)
listbox.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Bind keys to functions
window.bind('<Return>', add_task)   # Enter key
window.bind('<BackSpace>', delete_task)  # Delete key
window.bind('<c>', check_task)      # 'c' key

# Running the main event loop
window.mainloop()
