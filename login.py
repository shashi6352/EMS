from customtkinter import *
##module that have all tkinter command
from PIL import Image #library for image
from tkinter import messagebox

def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All fields are required.")
    elif usernameEntry.get() == "Shashi" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success", "You have successfully logged in.")
        root.destroy()
        import ems
    else:
        messagebox.showerror("Error", "Invalid credentials.")

root=CTk()
# define root variable
root.geometry("930x478") #define geometry
root.resizable(0,0)
root.title("login page")
image=CTkImage(Image.open("Image.jpg"), size=(930,478)) #this command yet not give the image on tab
imageLabel=CTkLabel(root, image=image,text="")
imageLabel.place(x=0,y=0)#location of image on root
headinglabel=CTkLabel(root,text="Employee Management System",bg_color="#01033B",font=("Goudy Old Style",30,"bold"),text_color="#FFFFFF")
headinglabel.place(x=10,y=5)
usernameEntry=CTkEntry(root,placeholder_text="Enter Your Username",width=180)
usernameEntry.place(x=50,y=50)
passwordEntry=CTkEntry(root,placeholder_text="Enter Your Password",width=180,show="*")
passwordEntry.place(x=50,y=100)
loginButton=CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=70,y=150)
root.mainloop()#define mainloop #make sure to write every thing before this mainloop



