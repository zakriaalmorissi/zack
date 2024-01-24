import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3



bkground ="#06283D"
framebg = "#EDEDED"
framefg = "#06283D"


app=tk.Tk()
app.title("ZackApp")
app.geometry("700x500+100+100")
app.config(bg=bkground)
app.resizable(False,False)

#icon image 

icon_image = ImageTk.PhotoImage(Image.open("images/app.png"))
app.iconphoto(False,icon_image)

frame = tk.Frame(app)
frame.pack(fill=tk.Y)

def click():
    user_1 = user.get()
    password_1 = password.get()
    while True:
        if user_1 == "Username":
            message = messagebox.showerror(title="Error",message="No Username !")
            break
        elif user_1 =="":
            message = messagebox.showerror(title="Empty Use",message="please input your username !")
            break
        elif password_1 == "":
            message = messagebox.showerror(title="Empty password",message="please input your password !")
            break
        elif password_1 =="Password":
            message = messagebox.showerror(title="Error",message="No password !")
            break

        else:
           move()
           break

def move():
    app.destroy()
    import main_sys
    
#------- new frame -----------------------------------------------------      


def sign_up():
    app.destroy()
    import register
    
    
def back():
    pass



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---backgroundimage 

backgroundimage = ImageTk.PhotoImage(Image.open("images/log.png"))
tk.Label(frame,image=backgroundimage).pack(anchor="center")

#----User Entry ----
def user_enter(e):
    user.delete(0,"end")
    
def user_back(e):
    if user.get()=="":
        user.insert(0,"Username")

user = tk.Entry(frame,width=19,border=0,font=("Arial Bold",12))
user.insert(0,"Username")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_back)
user.place(x=96,y=181)

#----password-----
def password_in(n):
    password.delete(0,"end")

def password_out(n):
    if password.get()=="":
        password.insert(0,"Password")
password = tk.Entry(frame,width=20,border=0,font=("Arial Bold",12))
password.insert(0,"Password")
password.bind("<FocusIn>",password_in)
password.bind("<FocusOut>",password_out)
password.place(x=96,y=240)


#----- hide password----
button_mode = True
def hide():
    global button_mode
    if button_mode:
        eye_btn.config(image=close_eye,activebackground="white")
        password.config(show="*",font=("Arial Bold",15))
        button_mode = False
    else:
        eye_btn.config(image=openeye,activebackground="green")
        password.config(show="")
        button_mode = True


openeye= ImageTk.PhotoImage(Image.open("images/eye_open1.png"))
close_eye = ImageTk.PhotoImage(Image.open("images/closed-eye-0.jpg"))
eye_btn = tk.Button(frame,image=openeye,bg='white',border=0,command=hide)
eye_btn.place(x=320,y=244)
 

#----Button click

button_image = ImageTk.PhotoImage(Image.open("images/button.png"))
button = tk.Button(frame,image=button_image,command=click)
button.place(x=140,y=310)

tk.Label(frame,text="Create an account",bg="white",border=0,font=("Microsoft YaHei UI Light",10)).place(x=136,y=382)
button_signup = tk.Button(frame,text="Sign up?",font=("Arial Bold",8),fg="#06288D",bg="white",border=0,command=sign_up)
button_signup.place(x=262,y=382)












app.mainloop()