import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")  # Set the window size

tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update the task list
def update_listbox():
    clear_listbox()
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to clear the task list
def clear_listbox():
    listbox.delete(0, tk.END)

# Function to remove a selected task
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_listbox()

# Function for task filtering
def filter_tasks():
    keyword = filter_entry.get().lower()
    filtered_tasks = [task for task in tasks if keyword in task.lower()]
    clear_listbox()
    for task in filtered_tasks:
        listbox.insert(tk.END, task)

entry = tk.Entry(app, width=30)
add_button = tk.Button(app, text="Add", width=10, command=add_task)
delete_button = tk.Button(app, text="Delete", width=10, command=delete_task)

# Entry field and button for filtering
filter_label = tk.Label(app, text="Filter Tasks:")
filter_entry = tk.Entry(app, width=30)
filter_button = tk.Button(app, text="Filter", width=10, command=filter_tasks)

listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=50)

entry.pack(pady=10)
add_button.pack()
delete_button.pack()
filter_label.pack()
filter_entry.pack()
filter_button.pack()
listbox.pack()

# Basic color theme
app.configure(bg="#e6e6e6")
entry.configure(bg="white")
add_button.configure(bg="#008CBA", fg="white")
delete_button.configure(bg="#FF3333", fg="white")
filter_button.configure(bg="#00CC66", fg="white")
listbox.configure(bg="#f0f0f0")

app.mainloop()
