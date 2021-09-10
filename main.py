from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('1350x700+0+0')
root.title('Inventory Management System | Developed by Ayush ,Sangeet and Sonim'
           )
root.config(bg='white')

# =====title===#

icon_title = PhotoImage()  # photo haru rkhanabaki cha
title = Label(
    root,
    text='Inventory Management System',
    font=('times new roman', 40, 'bold'),
    bg='#010c48',
    fg='white',
    anchor='w',
    padx=20,
    ).place(x=0, y=0, relwidth=1, height=70)

# ===Button_Logout==

btn_logout = Button(root, text='logout', font=('times new roman', 15,
                    'bold'), bg='yellow', cursor='hand2').place(x=1150,
        y=10, height=50, width=150)

# ===clock===

lbl_clock = title = Label(root,
                          text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS'
                          , font=('times new roman', 15), bg='#4d636d',
                          fg='white')
lbl_clock.place(x=0, y=70, relwidth=1, height=30)


def employee():
    import employee
    employee.main()


# =====Left Menu===

MenuLogo = Image.open('yoyoho.png')
MenuLogo = MenuLogo.resize((250, 200), Image.ANTIALIAS)
MenuLogo = ImageTk.PhotoImage(MenuLogo)

LeftMenu = Frame(root, bd=2, relief=RIDGE, bg='white')
LeftMenu.place(x=0, y=102, width=200, height=565)

lbl_menuLogo = Label(LeftMenu, image=MenuLogo)
lbl_menuLogo.pack(side=TOP, fill=X)

lbl_menu = Label(LeftMenu, text='Menu', font=('times new roman', 20),
                 bg='#009688').pack(side=TOP, fill=X)

btn_employee = Button(
    LeftMenu,
    text='Employee',
    command=employee,
    anchor='w',
    font=('times new roman', 20, 'bold'),
    bg='white',
    bd=3,
    cursor='hand2',
    padx=20,
    ).pack(side=TOP, fill=X)
btn_supplier = Button(
    LeftMenu,
    text='Supplier',
    anchor='w',
    font=('times new roman', 20, 'bold'),
    bg='white',
    bd=3,
    cursor='hand2',
    padx=20,
    ).pack(side=TOP, fill=X)
btn_Category = Button(
    LeftMenu,
    text='Category',
    anchor='w',
    font=('times new roman', 20, 'bold'),
    bg='white',
    bd=3,
    cursor='hand2',
    padx=20,
    ).pack(side=TOP, fill=X)
btn_Sales = Button(
    LeftMenu,
    text='Sales',
    anchor='w',
    font=('times new roman', 20, 'bold'),
    bg='white',
    bd=3,
    cursor='hand2',
    padx=20,
    ).pack(side=TOP, fill=X)
btn_Exit = Button(
    LeftMenu,
    text='Exit',
    anchor='w',
    font=('times new roman', 20, 'bold'),
    bg='white',
    bd=3,
    cursor='hand2',
    padx=20,
    ).pack(side=TOP, fill=X)

# ====content====

lbl_employee = Label(
    root,
    text='Total Employee\n[ 0 ]',
    bg='#33bbf9',
    fg='white',
    bd=5,
    relief=RIDGE,
    font=('goudy old style', 20, 'bold'),
    )
lbl_employee.place(x=300, y=120, height=150, width=300)

lbl_supplier = Label(
    root,
    text='Total Supplier\n[ 0 ]',
    bg='#ff5722',
    fg='white',
    bd=5,
    relief=RIDGE,
    font=('goudy old style', 20, 'bold'),
    )
lbl_supplier.place(x=650, y=120, height=150, width=300)

lbl_category = Label(
    root,
    text='Total Category\n[ 0 ]',
    bg='#009688',
    fg='white',
    bd=5,
    relief=RIDGE,
    font=('goudy old style', 20, 'bold'),
    )
lbl_category.place(x=1000, y=120, height=150, width=300)

lbl_product = Label(
    root,
    text='Total Product\n[ 0 ]',
    bg='#607d8b',
    fg='white',
    bd=5,
    relief=RIDGE,
    font=('goudy old style', 20, 'bold'),
    )
lbl_product.place(x=300, y=300, height=150, width=300)

lbl_Sales = Label(
    root,
    text='Total Sales\n[ 0 ]',
    bg='#ffc107',
    fg='white',
    bd=5,
    relief=RIDGE,
    font=('goudy old style', 20, 'bold'),
    )
lbl_Sales.place(x=650, y=300, height=150, width=300)

# ===Footer===

lbl_footer = title = Label(root,
                           text='IMS-Inventory Management System | Made by Ayush,Sangeet and Sonim'
                           , font=('times new roman', 15), bg='#4d636d'
                           , fg='white').pack(side=BOTTOM, fill=X)

root.mainloop()
