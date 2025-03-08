import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Function to retrieve data and perform validation checks
def data_retrieve():
    # retrieving data
    username = username_form.get()   
    difficulty = difficulty_dropdown.get()
    # Validation checks
    if username == "" and difficulty=="":
        messagebox.showwarning(title="Error",message="Please enter name and select level")
    elif difficulty == "":
        messagebox.showwarning(title="Error",message="Please select level")
    elif username == "":
        messagebox.showwarning(title="Error",message="Please enter name")



#Creating a window
window = tk.Tk()
window.geometry("800x300")
window.title("CS50P Final Project")
window.config(bg="#1E1E1E")
window.resizable(width=False,height=False)



# creating widgets 
welcome_label = tk.Label(window,text="Welcome to snake game",bg="#1E1E1E",fg="#c20003",font=("Bevan",30),pady=20)
username_label = tk.Label(window,text="Username",bg="#1E1E1E",fg="#0003c2",font=("fantasy",20))
username_form = tk.Entry(window,width=30)
difficulty_label = tk.Label(window,text="Difficulty Level",bg="#1E1E1E",fg="#75038f",font=("fantasy",20),pady=20)
difficulty_dropdown = ttk.Combobox(window,values=["Easy","Medium","Hard"])
submit = tk.Button(window,text="Start",command=data_retrieve,font=("Arial",20),fg="#000000",bg="#e8e800")


# placing widgets
welcome_label.grid(row=0,column=3)
username_label.grid(row=1,column=0)
username_form.grid(row=1,column=1)
difficulty_label.grid(row=2,column=0)
difficulty_dropdown.grid(row=2,column=1)
submit.grid(row=3,column=3,sticky="news",pady=40)
window.mainloop()
