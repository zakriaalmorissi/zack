import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import backend
import sqlite3





# inserting all items from the database to the screen
def view_command():
    global total
    global total_1
    count = 0
    total = 0
    total_1 = 0
    # add the itmes to the screen
    for index in backend.view():
        if count % 2 ==0:
          Tree_table.insert("",tk.END,values=index,tags=("evenrow",))
        else :
            Tree_table.insert("",tk.END,values=index,tags=("oddrow",))
        # increment count
        count += 1

        # index and sum all the payments
        total += int(index[3])
        # show the calculated paytments
        label.config(text=str(total))
        
        # index and sun all of the consumptions
        total_1 += int(index[4])
        # show the sum of all consumptions
        label_1.config(text=str(total_1))

rest = "Search ..."
# restore or update the changes after searching ,deleting  or editing the itmes 
def restore_command():
    # check whether search bar entry has changed
    if enter.get() != rest:
        enter.delete(0,"end")
    
    # set the search bar to normal
    def search_in(n):
           enter.delete(0,"end")    
       
    
    def search_out(n):
        if enter.get() =="":
            enter.insert(0,rest)
     

    enter.bind("<FocusIn>",search_in)
    enter.bind("<FocusOut>",search_out)
    # cleaning the searched items
    Tree_table.delete(*Tree_table.get_children())

   # returning all items to the Treeview
    view_command()


def search_command():
    get_search = enter.get()
    get_search.strip()
    # search for the name in the database
    search = backend.search(name=get_search)
    # check  if the searched item is not found
    if not search:
        noresult = ["?","Not Found"]
        # clear previous data
        Tree_table.delete(*Tree_table.get_children())

        # insert no results text to the user
        Tree_table.insert("",tk.END,values=noresult[:2])

    # check if the searched item is found 
    if search:
        Tree_table.delete(*Tree_table.get_children())
        count = 0
        #insert all searched items to the screen
        for i in range (len(search)):
            if count % 2 ==0:
              Tree_table.insert("",tk.END,values=search[i],tags=("evenrow",))
            
            else:
                 Tree_table.insert("",tk.END,values=search[i],tags=("oddrow",))
            count += 1

        # also search in database if the input is a number
    if get_search.isnumeric():
        # search for the number in the database
        search_num = backend.search(id=get_search)
        # clean the previous data 
        Tree_table.delete(*Tree_table.get_children())

        # insert the searched data
        if search_num:
            count = 0
            for i in range(len(search_num)):
                if count % 2== 0:
                    Tree_table.insert("",tk.END,values=search_num[i],tags=("evenrow",))
                else:
                    Tree_table.insert("",tk.END,values=search_num[i],tags=("oddrow",))
                count += 1

        # show "no results" text if number is not in the database
        if not search_num:
             Tree_table.delete(*Tree_table.get_children())
             Tree_table.insert("",tk.END,values=noresult[:2])
             print(get_search)
             print(search)
             print(search_num)

#____mainipulate selected items ___________
      
def remove_selected_items():
    # get select items
    selected_items = Tree_table.selection()
    # get the values of the selected items
    item_values = Tree_table.item(selected_items, 'values')
    print(item_values)

    #iterate the selected items 
    for index in  selected_items:
        # get the selected item
        selected = item_values[0] 
        # delete the selected item from the listBox
        Tree_table.delete(index)
        # delete the selected item from the data base
        backend.delete(selected)
        label.config(text=str(total))


def main_system():
    global system
    global frm
    global frm_1
    global frm_2
    global Tree_table
    global enter
    global label
    global label_1

    system = tk.Tk()
    # specify the sixe and positon of the window in the screen
    system.geometry("1750x960+50+50") # width X height + X position + Y position 

    # create the app icon
    icon = ImageTk.PhotoImage(Image.open("images/app.png"))
    system.iconphoto(False,icon)
    system.resizable(False,False)
    system.title("ZackApp")


    #________--- Main Frames ----__________

    frm = tk.Frame(system,width=110,height=1000,bg="#06283D")
    frm.place(x=1,y=10)
    frm_1 = tk.Frame(system,width=959,height=770,bg="white")
    frm_1.place(x=115,y=100)
    frm_3 = tk.Frame(system,width=945,height=45)
    frm_3.place(x=115,y=50)

    tk.Label(frm_3,text="Products Menu",width=50,font=("Arial Bold",15),bd=2).pack(fill=tk.Y,anchor=tk.CENTER)

    # frame for Sales 
    frm_2 = tk.Frame(system,width=520,height=760,bg='white')
    frm_2.place(x=1205,y=100)
    

    #-----ScrollBara and TreeView-----------

    # scrollbar the treetable
    scroll_bar = ttk.Scrollbar(frm_1)
    scroll_bar.place(x=940,y=1,relheight=1)

    # create a treeview
    Tree_table = ttk.Treeview(frm_1,columns=("ID","Names","Prices","Quntity","Total Price"),show="headings",yscrollcommand=scroll_bar.set,selectmode="extended")  
    # create  headings
    Tree_table.heading("Names",text="Names",anchor=tk.CENTER)
    Tree_table.heading("ID",text="ID",anchor=tk.CENTER)
    Tree_table.heading("Prices",text="Prices",anchor=tk.CENTER)
    Tree_table.heading("Quntity",text="Quntity")
    Tree_table.heading("Total Price",text="Total Price")
    # create columns
    Tree_table.column("#0",width=80,minwidth=20)
    Tree_table.column("Names",anchor=tk.CENTER,width=260)
    Tree_table.column("ID",anchor=tk.CENTER,width=40)
    Tree_table.column("Prices",anchor=tk.CENTER,width=300)
    Tree_table.column("Quntity",anchor=tk.CENTER,width=190)
    Tree_table.column("Total Price",anchor=tk.CENTER,width=150)

    # create a colorful striped row
    Tree_table.tag_configure("oddrow",background="white")
    Tree_table.tag_configure("evenrow",background="lightblue")
    
    # set the height of the table on the way that matches the the length of the Frame
    Tree_table.configure(height=70)
    Tree_table.place(x=1,y=1)
    scroll_bar.config(command=Tree_table.yview)

    # set label that shows the sum of all quatities 
    label = tk.Label(system,text="Label",width=25,bg="white",bd=1)
    label.place(x=575,y=892)
    tk.Label(system,text="Total Quntity:",bd=1,font=("Microsoft Yahei UI Light",10),bg="#ADD8E6").place(x=477,y=890)
    # label to show the sum of all prices
    label_1 = tk.Label(system,text="Label",width=25,bd=1,bg="white")
    label_1.place(x=890,y=892)
    tk.Label(system,text="Total Price:",bd=1,font=("Microsoft Yahei UI Light",10),bg="#ADD8E6").place(x=812,y=890)


     #------Search Entry---------
    def search_in(n):
        enter.delete(0,"end")

    def search_out(n):
        if enter.get() == "":
            enter.insert(0,rest)

    def show_suggestions(event):
        # get the current entry from the search bar
        query = text.get()
        
        if query != rest or query != "":
            Tree_table.delete(*Tree_table.get_children())
            # search for the current item in the database
            cur.execute("SELECT * FROM book WHERE name LIKE ? ",(f"%{query}%",))
            suggestions = cur.fetchall()
            count = 0
            for suggestion in suggestions :
                    if count % 2 ==0:
                        Tree_table.insert("",tk.END,values=suggestion[:5], tags="evenrow") 

                    else:
                        Tree_table.insert("",tk.END,values=suggestion[:5], tags="oddrow") 
                    count += 1

        if query.isnumeric():
            num = query
            num.strip()
            cusrer = conn.cursor()
            # search by the id number
            if len(num) < 9:

                 Tree_table.delete(*Tree_table.get_children())
                 cusrer.execute("SELECT * FROM book WHERE id LIKE ?",(num,))
                 suggest = cusrer.fetchall()
                 # insert the found the results into the treeview
                 for suggestion in suggest:
                        Tree_table.insert("",tk.END,values=suggestion[:5])
            

    # create a search Entry
    text = tk.StringVar()
    enter = tk.Entry(system,textvariable=text,width=80,bd=1,bg="white",font=("Microsoft Yahei UI Light",15))
    enter.insert(0,rest)
    enter.bind("<FocusIn>",search_in)
    enter.bind("<FocusOut>",search_out)
    enter.place(x=115,y=13)

    # show suggestionsw while searching 
    enter.bind("<KeyRelease>",show_suggestions)
    # get connected to the data base
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()
    

   
             
    

def button_search():
    global butto_im
    global search_btn
    butto_im = ImageTk.PhotoImage(Image.open("images/mon_icon.png"))
    search_btn = tk.Button(system,image=butto_im,command= search_command)
    search_btn.place(x=1047,y=14)



def buttons():
    global user_btn
    global statistics
    global return_button 
    global setting_btn
    global home_btn
    global add_product
    #buttons to manipulate the main system
    def pop_up():
        window = tk.Toplevel(system)
        #remove the defualt cancel button and and title from the window
        window.overrideredirect(1)
        # specify the pop up window size and position
        window.geometry("100x200")

        btn = tk.Button(window,text='Cancel',command=window.destroy)
        btn.pack()
    def add():
        Tree_table.place_forget()

    def home():
        Tree_table.place(x=1,y=1)

    home_btn = tk.Button(frm,text="Home",width=14,command=home)
    home_btn.place(x=1,y=5)

    add_product = tk.Button(frm, text="Add products", width=14,command=add)
    add_product.place(x=1,y=41)

    history_button = tk.Button(frm,text="History",width=14)
    history_button.place(x=1,y=80)

    user_btn = tk.Button(frm,text="USER",width=14)
    user_btn.place(x=1,y=130)

    setting_btn = tk.Button(frm,text="Setting",width=14,command=pop_up)
    setting_btn.place(x=1,y=170)

    statistics = tk.Button(frm,text="Statistics",width=14)
    statistics.place(x=1,y=210)

   
   

# --------------------Widgets for the Sales Menu--------------------------------------------------------------------------
    tk.Label(system,text="Cart Menu",font=("Arial Bold ",17),bd=2).place(x=1370,y=50)
    sale_name = tk.Entry(frm_2,width=35,background='white')
    sale_name.place(x=60,y=50)
    tk.Label(frm_2,text="Name :",bd=0,font=('Microfost Yahei UI Light',10)).place(x=8,y=50)
    sale_price = tk.Entry(frm_2,width=20, background="white")
    sale_price.place(x=60,y=90)
    tk.Label(frm_2,text="Price :",bd=0,font=('Microfost Yahei UI Light',10)).place(x=8,y=90)
    sale_total = tk.Entry(frm_2,width=25, background="white")
    sale_total.place(x=295,y=90)
    tk.Label(frm_2,text="Tolal price :",bd=0,font=('Microfost Yahei UI Light',10)).place(x=220,y=90)

    sale_quntity = tk.Entry(frm_2, width=22, background="white")
    sale_quntity.place(x=82,y=132)
    tk.Label(frm_2, text="Quntity :",font=('Microsoft Yahei UI Light',10)).place(x=8,y=130)
    sale_id = tk.Entry(frm_2, width=20, background="white")
    sale_id.place(x=75,y=172)
    tk.Label(frm_2, text="Item ID :",font=('Microsoft Yahei UI Light',10)).place(x=8,y=170)
    
    # tabel tree to list all the current sales 
    sales_table = ttk.Treeview(frm_2, columns=("Names","ID","Price","Quantity","Total Price"),show="headings")
    sales_table.heading("Names",text="Names",anchor=tk.CENTER)
    sales_table.heading("ID",text="ID",anchor=tk.CENTER)
    sales_table.heading("Price",text="Price",anchor=tk.CENTER)
    sales_table.heading("Quantity",text="Quantity")
    sales_table.heading("Total Price",text="Total Price")

    sales_table.column("Names",width=150,anchor=tk.CENTER)
    sales_table.column("ID",width=40,anchor=tk.CENTER)
    sales_table.column("Price",width=100,anchor=tk.CENTER)
    sales_table.column('Quantity',width=100,anchor=tk.CENTER)
    sales_table.column("Total Price",width=120,anchor=tk.CENTER)
    sales_table.place(x=3,y=290)
    sales_table.config(height=20)

    def selected_items():
        query = Tree_table.selection()
        queried_values = Tree_table.item(query,"values")
        name = sale_name.get()
    
        if not name:
            sale_id.insert(0,queried_values[0])
            sale_name.insert(0,queried_values[1])
            sale_price.insert(0,queried_values[2])
            sale_quntity.insert(0,queried_values[3])
            sale_total.insert(0,queried_values[4])

        if name :
            add()
            clear()
    
    def add():
        name = sale_name.get()
        qun = sale_quntity.get()

        if name and qun:
            products = [(sale_name.get(),sale_id.get() ,sale_price.get()
                    ,sale_quntity.get() ,sale_total.get())] 
            for product in products:
                sales_table.insert("",tk.END, values=product)
                clear()

    def clear():
        sale_name.delete(0,"end")
        sale_id.delete(0,"end")
        sale_price.delete(0,"end")
        sale_quntity.delete(0, "end")
        sale_total.delete(0, "end")

    def remove():
        sales_table.delete(*sales_table.get_children())


    add_selected = tk.Button(system, text="Add Selected",width=15,bg="#E6E6FA",command=selected_items)
    add_selected.place(x=1084,y=120)

    return_button = tk.Button(system,text="X",width=3,fg="black",font=("Arial Bold ",11),command=restore_command)
    return_button.place(x=1084,y=13)
    

    add_button = tk.Button(frm_2,text="Add to Cart",width=25,bg="#E6E6FA",font=("Arial Bold",10),command=add)
    add_button.place(x=10,y=253)

    clear_button = tk.Button(frm_2,text="Clear",width=25,font=("Arial Bold",10),bg="#f0687c",command=clear)
    clear_button.place(x=255,y=253)

    clear_cart = tk.Button(system,text="Clear Cart",width=16,command=remove,bg="#f0687c")
    clear_cart.place(x=1280,y=880)

    edit_cart = tk.Button(system,text="Edit",width=16,bg='#E6E6FA')
    edit_cart.place(x=1440,y=880)

    print_cart = tk.Button(system,text="Print",width=16,bg="#E6E6FA")
    print_cart.place(x=1600,y=880)

    

            
main_system()
view_command()
button_search()
buttons()

system.mainloop() 