import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import Combobox







root = tk.Tk()
root.title("ZackApp")
root.geometry("1000x700+110+110")
icon = ImageTk.PhotoImage(Image.open("images/app.png"))
root.iconphoto(False,icon)
#______________________________________________________________________------------------___________--------------------------___________________________________

def back():
    root.destroy()
    import login
    pass


button_image = ImageTk.PhotoImage(Image.open("images/back.jpg"))
butn = tk.Button(root,image=button_image,command=back)
butn.place(x=2,y=2)


frame_1 = tk.Frame(root,width=360,height=500,bg="white")
frame_1.place(x=100,y=100)
frame_2_image = ImageTk.PhotoImage(Image.open("images/photo_1.png"))
frame_2 = tk.Frame(root,bg="white",width=390,height=500)
frame_2.place(x=550,y=100)
tk.Label(frame_2,image=frame_2_image).pack()
tk.Label(root,text="Register Here ",bg="#06283D",fg="red",width=35,height=3,font=("Arial bold",11)).place(x=100,y=20)

#_______________________----------------_________________________________________________________________________----------------_____________________________


def register_info():
    fullname = full_name.get()
    number =  phone_number.get()
    age_num = age.get()
    password_input = password.get()
    password_confirm_input = password_confirm.get()
    if fullname.strip() == "Full Name":
        message = messagebox.showerror("Error","Please input your name")

    elif len(fullname) <=5:
        message = messagebox.showerror("Error","Very short name. Please enter your full name ")

    elif not number.isdigit():
         message = messagebox.showerror("Error","Invalide number")

    elif len(number) !=9:
        message = messagebox.showerror("Error","Number must be equal to 9")
    
    elif not number.startswith("77"):
        if not number.startswith("73"):
           message = messagebox.showerror("Error","Wrong number")

    elif not age_num.isdigit():
        message = messagebox.showerror("Error","Invalide age")
    
    elif len(password_input) < 5 :
        message = messagebox.showerror("Error","Very weak password")

    elif password_input.strip() != password_confirm_input.strip():
        message = messagebox("Error","Your confirm password is not correct !")

    else:
        import main
        
        

    


   # message = messagebox.showinfo("Success","Registered successfully")






def rest():
    full_name.delete(0,"end")
    full_name.insert(0,"Full Name")
    phone_number.delete(0,"end")
    phone_number.insert(0,"Phone number")
    age.delete(0,"end")
    age.insert(0,"Age")
    password.delete(0,"end")
    password.insert(0,"Password")
    password_confirm.delete(0,"end")
    password_confirm.insert(0,"Confirm password")
    



def name_enter(e):

    full_name.delete(0,"end")


def name_out(n):

    if full_name.get() == "":
        full_name.insert(0,"Full Name")

def number_in(e):
    
    phone_number.delete(0,"end")

def number_out(x):
    
   if  phone_number.get() == "":
       phone_number.insert(0,"Phone Number")

def age_in(e):

    age.delete(0,"end")

def age_out(e):

    if age.get() == "":
        age.insert(0,"Age")

def password_in(n):

    password.delete(0,"end")

def password_out(n):

    if password.get() =="":
        password.insert(0,"Password")


def confirm_in(n):

    password_confirm.delete(0,"end")

    

def confirm_out(n):

    if password_confirm.get() =="":
        password_confirm.insert(0,"Confirm password")

#______________________________________________________--------______________________________________


full_name = tk.Entry(frame_1,width=35,border=0,bg="white",fg="black",font=("Microsoft YaHei UI Light",11))
full_name.place(x=50,y=26)
full_name.insert(0,"Full Name")
full_name.bind("<FocusIn>",name_enter)
full_name.bind("<FocusOut>",name_out)
tk.Frame(frame_1,bg="black",width=215,height=2).place(x=50,y=50)

phone_number = tk.Entry(frame_1,bg="white",fg="black",width=35,border=0,font=("Microsoft YaHei UI Light",11))
phone_number.place(x=50,y=72)
phone_number.insert(0,"Phone Number")
phone_number.bind("<FocusIn>",number_in)
phone_number.bind("<FocusOut>",number_out)
tk.Frame(frame_1,width=215,height=2,bg="black").place(x=50,y=95)


age = tk.Entry(frame_1,width=10,bg="white",fg="black",border=0,font=("Microsoft Yahei UI Light",11))
age.insert(0,"Age")
age.bind("<FocusIn>",age_in)
age.bind("<FocusOut>",age_out)
age.place(x=50,y=115)
tk.Frame(frame_1,width=70,height=2,bg="black").place(x=50,y=140)

sex = Combobox(frame_1,values=["Male","Female"],width=10,state="r",font=("Arial Bold",9))
sex.place(x=150,y=126)
sex.set("Male")

password = tk.Entry(frame_1,width=35,bg="white",fg="black",border=0,font=("Microsoft Yahei UI Light",11))
password.insert(0,"Password")
password.bind("<FocusIn>",password_in)
password.bind("<FocusOut>",password_out)
password.place(x=50,y=165)
tk.Frame(frame_1,width=220,height=2,bg="black").place(x=50,y=191)

password_confirm = tk.Entry(frame_1,width=35,bg="white",fg="black",border=0,font=("Microsoft Yahei UI Light",11))
password_confirm.insert(0,"Confirm password")
password_confirm.bind("<FocusIn>",confirm_in)
password_confirm.bind("<FocusOut>",confirm_out)
password_confirm.place(x=50,y=206)
tk.Frame(frame_1,width=220,height=2,bg="black").place(x=50,y=236)

#__________________________________________________________________________________________________________________________

#image_button = ImageTk.PhotoImage(Image.open("images/register.png"))
button = tk.Button(frame_1,text="Register",width=19,font=("Microsoft YaHei UI Light",12),activebackground="red",command=register_info)
button.place(x=75,y=390)
button_clear = tk.Button(frame_1,text="Reset",width=21,font=("Microsoft YaHei UI Light",11),activebackground="red",command=rest)
button_clear.place(x=75,y=438)











root.mainloop()






