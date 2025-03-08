import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

username = str()
difficulty = str()

# Function to retrieve data and perform validation checks
def data_retrieve():
    global username, difficulty
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
    else:
        window.destroy()


#Creating a window
window = tk.Tk()
window.geometry("800x450")
window.title("CS50P Final Project")
window.config(bg="#1E1E1E")
window.resizable(width=False,height=False)

# Changing the logo of window
# icon = ImageTk.PhotoImage(Image.open("favicon.png"))   
# window.iconphoto(True,icon)


# creating widgets 
welcome_label = tk.Label(window,text="Welcome to snake game",bg="#1E1E1E",fg="#c20003",font=("Bevan",35))
username_label = tk.Label(window,text="User Name",bg="#1E1E1E",fg="#0003c2",font=("fantasy",30))
username_form = tk.Entry(window,font=(100))
difficulty_label = tk.Label(window,text="Difficulty Level",bg="#1E1E1E",fg="#75038f",font=("fantasy",30))
difficulty_dropdown = ttk.Combobox(window,values=["Easy","Medium","Hard"],font=(15))
submit = tk.Button(window,text="START",command=data_retrieve,font=("Arial",50),fg="#000000",bg="#e8e800")


# placing widgets
welcome_label.place(x=200,y=30)
username_label.place(x=10,y=130)
username_form.place(x=230,y=138,height=35,width=250)
difficulty_label.place(x=10,y=220)
difficulty_dropdown.place(x=280,y=230,height=30,width=100)
submit.place(width=800,height=100,y=350)
window.mainloop()
