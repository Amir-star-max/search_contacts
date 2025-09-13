from tkinter import *
from tkinter import messagebox
from Data_base import *
#=========================Win==================================

win = Tk()
win.title('Contacts')
win.iconbitmap("D:\Programing\Mix Icon Pack\Smooth Series\mobile telephone.ico")
width = 600
height = 350
screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()
x = (screen_w / 2) - (width / 2)
y = (screen_h / 2) - (height / 2)
win.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
win.config(bg='grey')
win.resizable(0,0)
#=======================Functions====================================
def change():
    import random
    global color
    hex_num = '0123456789ABCDEF'
    color_code = '#'
    for _ in range(6):
        color_code += random.choice(hex_num)
    win.configure(bg=color_code) 
    lbl_name.configure(bg=color_code)       
    lbl_lname.configure(bg=color_code)       
    lbl_address.configure(bg=color_code)       
    lbl_phone.configure(bg=color_code)
    btn_change_color.configure(fg=color_code)       
    btn_insert.configure(fg=color_code)       
    btn_remove.configure(fg=color_code)       
    btn_clear.configure(fg=color_code)       
    btn_update.configure(fg=color_code)       
    btn_exit.configure(fg=color_code)       
    btn_show_list.configure(fg=color_code)       
    btn_search.configure(fg=color_code)       

def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)
    ent_name.focus_set()


def exit():
    q = messagebox.askquestion('Exit',
                               'Are you sure to exit ?')
    if q == 'yes':
        win.destroy()
        messagebox.showinfo('Done',
                            'Programm Finished .')    
        

    # if not tel.isdigit() or len(tel) != 11:
    #     messagebox.showerror('Phone Error',
    #                          'Please fill phone feild correctly !')
    #     ent_phone.delete(0,END)
    # elif name == NONE or lname == NONE or add == NONE or tel == NONE:
    #     messagebox.showerror('Epmty Error',
    #                          'Please fill all of the feilds !') 
    # else:  
    #     # messagebox.showinfo('Done',
    #     #                     f'{name},s Data has been added to Database !')  

data = Database('d:/form')        
def insert_database():
    global data
    name  = ent_name.get().strip().capitalize()
    lname = ent_lname.get().strip().capitalize()
    add   = ent_address.get().strip().capitalize()
    tel   = ent_phone.get()
    data.insert(name,lname,add,tel)  

def insert():
    name  = ent_name.get().strip().capitalize()
    lname = ent_lname.get().strip().capitalize()
    add   = ent_address.get().strip().capitalize()
    tel   = ent_phone.get()
    if not name or not lname or not add or not tel:
        messagebox.showerror('Epmty Error',
                             'Please fill all of the feilds !') 
        return
    if not tel.isdigit() or len(tel) != 11:
        messagebox.showerror('Phone Error',
                             'Please fill phone feild correctly !')
        ent_phone.delete(0,END)
        return
     
    messagebox.showinfo('Done',
                            f'{name},s Data has been added to Listbox !')  
    lst_contact.insert(END,f'{name} - {lname} - {add} - {tel}')
    insert_database()
    clear()


def show():
    lst_contacts.delete(0,END)
    records = data.select()
    records.sort(key=lambda x : x[0])
    for rec in records:
        lst_contacts.insert(END,rec)
    lst_contact.delete(0,END)    


def select_records(event):
    clear()
    index = lst_contacts.curselection()
    global selected_record
    selected_record = lst_contacts.get(index)
    ent_name.insert(0,selected_record[1])
    ent_lname.insert(0,selected_record[2])
    ent_address.insert(0,selected_record[3])
    ent_phone.insert(0,selected_record[4])

def update():
    name = ent_name.get()
    lname = ent_lname.get()
    add = ent_address.get()
    tel = ent_phone.get()
    if not name or not lname or not add or not tel:
        messagebox.showerror('Update Error',
                             'Please select an item to update .')
        return
    index = lst_contacts.curselection()
    selected_record = lst_contacts.get(index)
    data.update(selected_record[0],name,lname,add,tel)
    messagebox.showinfo('Done',
                        'Item has been updated !')
    clear()
    show()

def delete():
    lst = lst_contacts.get(0,END)
    if not lst:
        messagebox.showerror('Listbox Error',
                             'Please Show Database Listbox,s Items First;\nThen Select an item to delete . ')
        return
    index = lst_contacts.curselection()
    selected_record = lst_contacts.get(index)
    if not index:
        messagebox.showerror('Listbox Error',
                             'Please select an item to delete .')
        return
    confirm = messagebox.askquestion('Warning',
                               'Are you sure to delete this item from database ?')
    if confirm == 'yes':
        data.delete(selected_record[0])
        show()
        clear()

def search_record():
    lst_contact.delete(0,END)
    records = data.search(ent_search.get())
    if records:
        for rec in records:
            lst_contact.insert(END,rec)        

        
#============================Widgetts=====================================================
#=====================Labels==================================

lbl_name = Label(win,text='Name:',
                 font='arial 14 bold')
lbl_name.place(x=10 , y=10)
lbl_name.config(bg='grey')

lbl_lname = Label(win,text='Lastname:',
                  font='arial 14 bold')
lbl_lname.place(x=10 , y=70)
lbl_lname.config(bg='grey')

lbl_address = Label(win,text='Address:',
                    font='arial 14 bold')
lbl_address.place(x=320 , y=10)
lbl_address.config(bg='grey')

lbl_phone = Label(win,text='Phone:',
                  font='arial 14 bold')
lbl_phone.place(x=320 , y=70)
lbl_phone.config(bg='grey')

#=========================Entries==================================

ent_name = Entry(win,width=15,
                 font='arial 14',
                 justify=LEFT)
ent_name.place(x=120 , y=12)

ent_lname = Entry(win,width=15,
                  font='arial 14',
                  justify=LEFT)
ent_lname.place(x=120 , y=69)

ent_address = Entry(win,width=15,
                    font='arial 14',
                    justify=LEFT)
ent_address.place(x=420 , y=12)

ent_phone = Entry(win,width=15,
                    font='arial 14',
                    justify=LEFT)
ent_phone.place(x=420 , y=69)

#=========================Buttons==================================

btn_insert = Button(win,width=15,
                    text='Insert',
                    command=insert)
btn_insert.place(x=15 , y=120)

btn_remove = Button(win,width=15,
                    text='Remove',
                    command=delete)
btn_remove.place(x=135 , y=120)

btn_update = Button(win,width=15,
                    text='Update',
                    command=update)
btn_update.place(x=255 , y=120)

btn_clear = Button(win,width=15,
                    text='Clear',
                    command=clear)
btn_clear.place(x=375 , y=120)

btn_exit = Button(win,width=13,
                    text='Exit',
                    command=exit)
btn_exit.place(x=495 , y=120)

btn_show_list = Button(win,width=15,
                    text='Show all contacts',
                    command=show)
btn_show_list.place(x=15 , y=160)

btn_search = Button(win,width=15,
                    text='Search',
                    command=search_record)
# btn_search.place(x=15 , y=120)

btn_change_color = Button(win,width=15,
                    text='Change_color',
                    command=change)
btn_change_color.place(x=450 , y=160)

btn_search.place(x=135 , y=160)

ent_search = Entry(win,width=15,
                   font='arial 14')
ent_search.place(x=260 , y=159)

#==========================Scrollbar=================================
scb_1 = Scrollbar(win,
                orient=VERTICAL,)
scb_1.place(x=282,y=190,height=157)

scb_2 = Scrollbar(win,
                  orient=VERTICAL)
scb_2.place(x=572 , y=190 , height=157)
#========================Listbox===================================

lst_contacts = Listbox(win,width=37,height=9,xscrollcommand=scb_1.set,font='arial 10 bold')
lst_contacts.grid_propagate(False)
lst_contacts.place(x=15 , y=190)
lst_contacts.bind('<<ListboxSelect>>',select_records)

lst_contact = Listbox(win,width=37,height=9,xscrollcommand=scb_2.set,font='arial 10 bold')
lst_contact.grid_propagate(False)
lst_contact.place(x=305 , y=190)


scb_1.config(command=lst_contact.xview)
scb_2.config(command=lst_contacts.xview)

#===========================================================


win.mainloop()