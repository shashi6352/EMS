from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database
import os

###functions part

def delete_all():
    result=messagebox.askyesno("Confirm", "Are you sure you want to delete all the records?")
    if result:
        database.deleteall_records()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set("Search By")


def search_employee():
    if searchEntry.get()=="":
        messagebox.showerror("Error", "Enter value to search")
    elif searchBox.get()=="Search By":
        messagebox.showerror("Error", "Please select an Option")
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert("", END, values=employee)



def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select Data to Delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror("Error", "Data Deleted")


def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select Data to Update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Successful","Data Updated")


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])
        

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set("Web Developer")
    genderBox.set("Male")
    salaryEntry.delete(0,END)
def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("",END,values=employee)




def add_employee():
    if idEntry.get()=="" or phoneEntry.get()=="" or nameEntry.get()=="" or salaryEntry.get()=="":
        messagebox.showerror("Error", "All fields are required.")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error", "Id already exists.")
    elif not idEntry.get().startswith("EMP"):
        messagebox.showerror("Error", "Invalid ID format. Use EMP followed by number (eg. EMP1).")

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success", "Employee Added Successfully.")


###GUIs part
window=CTk()
window.geometry("930x530+100+100")
window.resizable(False,False)
window.title("Employee Management System")
window.configure(fg_color="#01033B")


logo=CTkImage(Image.open("bg.JPG"), size=(930, 158))
logoLabel=CTkLabel(window,image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window, fg_color="#01033B")
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text="ID:",font=("arial",18,"bold"), text_color="white")
idLabel.grid(row=0,column=0,padx=10,pady=10, sticky=W)

idEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text="Name:",font=("arial",18,"bold"), text_color="white")
nameLabel.grid(row=1,column=0,padx=10, pady=10, sticky=W)

nameEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text="Phone:",font=("arial",18,"bold"), text_color="white")
phoneLabel.grid(row=2,column=0,padx=10,pady=10, sticky=W)

phoneEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text="Role:",font=("arial",18,"bold"), text_color="white")
roleLabel.grid(row=3,column=0,padx=10, pady=10, sticky=W)

role_options = ["Web Developer", "Cloud Architect", "Technical Writer", "Network Engineer", "DevOps Engineer",
                "Data Engineer", "Data Scientist", "Business Analyst", "IT Consultant", "UX/UI Designer"]
roleBox=CTkComboBox(leftFrame, values=role_options, font=("arial",15,"bold"), width=180, state="readonly")
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])


genderLabel=CTkLabel(leftFrame,text="Gender:",font=("arial",18,"bold"),text_color="white")
genderLabel.grid(row=4,column=0,padx=10, pady=10, sticky=W)

gender_options = ["Male", "Female", "Other"]
genderBox=CTkComboBox(leftFrame, values=gender_options, font=("arial",15,"bold"), width=180, state="readonly")
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text="Salary:",font=("arial",18,"bold"), text_color="white")
salaryLabel.grid(row=5,column=0,padx=10,pady=10, sticky=W)

salaryEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]
searchBox=CTkComboBox(rightFrame, values=search_options, state="readonly",width=180,font=("arial",15,"bold"))
searchBox.grid(row=0,column=0)
searchBox.set("Search By")

searchEntry=CTkEntry(rightFrame,font=("arial",15,"bold"),width=180)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame, text="Search", width=100, command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame, text="Show All", width=100, command=show_all)
showallButton.grid(row=0,column=3, pady=5)

tree=ttk.Treeview(rightFrame,height=11)
tree.grid(row=1,column=0,columnspan=4)
#
tree["columns"]=("ID","Name","Phone","Role","Gender","Salary")
tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")

tree.config(show="headings")

tree.column("ID", width=100)
tree.column("Name", width=100)
tree.column("Phone", width=100)
tree.column("Role", width=100)
tree.column("Gender", width=100)
tree.column("Salary", width=100)

style = ttk.Style()
style.configure("Treeview.Heading", font=("arial",15,"bold"))
style.configure("Treeview", font=("arial",9,"bold"),rowheight=20,background="#01033B",foreground="white")

#adding scroll bar
scrollBar=ttk.Scrollbar(rightFrame,orient=VERTICAL, command=tree.yview)
scrollBar.grid(row=1,column=4,sticky=NS)

tree.configure(yscrollcommand=scrollBar.set)


# Adding button create button frame
buttonFrame=CTkFrame(window,fg_color="#01033B")
buttonFrame.grid(row=2,column=0,columnspan=2,pady=20, padx=10)

newButton=CTkButton(buttonFrame,text="New", font=("arial",15,"bold"), width=160, corner_radius=15, command=lambda:clear(True))
newButton.grid(row=0,column=0, pady=5)

addButton=CTkButton(buttonFrame,text="Add", font=("arial",15,"bold"), width=160, corner_radius=15, command=add_employee)
addButton.grid(row=0,column=1, pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text="Update", font=("arial",15,"bold"), width=160, corner_radius=15, command=update_employee)
updateButton.grid(row=0,column=2, pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text="Delete", font=("arial",15,"bold"), width=160, corner_radius=15, command=delete_employee)
deleteButton.grid(row=0,column=3, pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text="Delete All", font=("arial",15,"bold"), width=160, corner_radius=15, command=delete_all)
deleteallButton.grid(row=0,column=4, pady=5,padx=5)



treeview_data()

window.bind("<ButtonRelease>", selection)

window.mainloop()