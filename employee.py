from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3


def main():
    root = Toplevel()
    root.geometry('1100x500+220+130')
    root.title('Inventory Management System | Developed by Ayush ,Sangeet and Sonim')

    root.config(bg='white')
    root.focus_force()

    # All variables


    var_searchby = StringVar()
    var_searchtxt = StringVar()
    var_emp_id = StringVar()
    var_emp_id.set('')
    var_gender = StringVar()
    var_contact = StringVar()
    var_contact.set('')
    var_name = StringVar()
    var_name.set('')
    var_dob = StringVar()
    var_dob.set('')
    var_doj = StringVar()
    var_doj.set('')
    var_email = StringVar()
    var_email.set('')
    var_pass = StringVar()
    var_pass.set('')
    var_utype = StringVar()
    var_address = StringVar()
    var_address.set('')
    var_salary = StringVar()
    var_salary.set('')

    def database():
        a = sqlite3.connect('test.db')
        c = a.cursor()

        c.execute('INSERT INTO addresses VALUES (:a,:b,:d,:e,:f,:g,:h,:i,:j,:k,:l)', {
            'a': var_emp_id.get(),
            'b': var_name.get(),
            'd': var_email.get(),
            'e': var_gender.get(),
            'f': var_contact.get(),
            'g': var_dob.get(),
            'h': var_doj.get(),
            'i': var_pass.get(),
            'j': var_utype.get(),
            'k': var_address.get(),
            'l': var_salary.get(),

        })

    # searchFrame

    SearchFrame = LabelFrame(root, text='search Employee',
                             font=('goudy old style', 12))
    SearchFrame.place(x=250, y=20, width=600, height=70)

    # options

    cmb_search = ttk.Combobox(
        SearchFrame,
        textvariable=var_searchby,
        values=('Select', 'E-mail', 'Name', 'Contact'),
        state='readonly',
        justify=CENTER,
        font=('goudy old style', 15),
    )
    cmb_search.place(x=10, y=10, width=180)
    cmb_search.current(0)

    txt_search = Entry(SearchFrame, textvariable=var_searchtxt,
                       font=('goudy old style', 15), bg='lightyellow'
                       ).place(x=200, y=10)
    txt_search = Button(
        SearchFrame,
        text='search',
        font=('goudy old style', 15),
        bg='#4caf50',
        fg='white',
        cursor='hand2',
    ).place(x=410, y=9, width=150, height=30)

    # title

    title = Label(root, text='Employee Details', bg='#0f4d7d',
                  font=('goudy old style', 15), fg='white').place(x=50,
                                                                  y=100, width=1000)

    # content
    # row1

    lbl_empid = Label(root, text='Emp ID', bg='white',
                      font=('goudy old style', 15)).place(x=50, y=150)
    lbl_gender = Label(root, text='Gender', bg='white',
                       font=('goudy old style', 15)).place(x=350, y=150)
    lbl_contact = Label(root, text='Contact', bg='white',
                        font=('goudy old style', 15)).place(x=750,
                                                            y=150)

    txt_empid = Entry(root, textvariable=var_emp_id, bg='lightyellow',
                      font=('goudy old style', 15)).place(x=150, y=150,
                                                          width=180)
    txt_contact = Entry(root, textvariable=var_contact, bg='lightyellow'
                        , font=('goudy old style', 15)).place(x=850,
                                                              y=150, width=180)

    cmb_gender = ttk.Combobox(
        root,
        textvariable=var_gender,
        values=('Select', 'Male', 'Female', 'Other'),
        state='readonly',
        justify=CENTER,
        font=('goudy old style', 15),
    )
    cmb_gender.place(x=500, y=150, width=180)
    var_gender.set(cmb_gender.get())



    # row2

    lbl_name = Label(root, text='Name', bg='white',
                     font=('goudy old style', 15)).place(x=50, y=190)
    lbl_dob = Label(root, text='D.O.B', bg='white',
                    font=('goudy old style', 15)).place(x=350, y=190)
    lbl_doj = Label(root, text='D.O.J', bg='white',
                    font=('goudy old style', 15)).place(x=750, y=190)

    txt_name = Entry(root, textvariable=var_name, bg='lightyellow',
                     font=('goudy old style', 15)).place(x=150, y=190,
                                                         width=180)
    txt_dob = Entry(root, textvariable=var_dob, bg='lightyellow',
                    font=('goudy old style', 15)).place(x=500, y=190,
                                                        width=180)
    txt_doj = Entry(root, textvariable=var_doj, bg='lightyellow',
                    font=('goudy old style', 15)).place(x=850, y=190,
                                                        width=180)

    # row3

    lbl_email = Label(root, text='E-mail', bg='white',
                      font=('goudy old style', 15)).place(x=50, y=220)
    lbl_password = Label(root, text='Password', bg='white',
                         font=('goudy old style', 15)).place(x=350,
                                                             y=220)
    lbl_usertype = Label(root, text='UserType', bg='white',
                         font=('goudy old style', 15)).place(x=750,
                                                             y=220)

    txt_email = Entry(root, textvariable=var_email, bg='lightyellow',
                      font=('goudy old style', 15)).place(x=150, y=220,
                                                          width=180)
    txt_password = Entry(root, textvariable=var_pass, bg='lightyellow',
                         font=('goudy old style', 15)).place(x=500,
                                                             y=220, width=180)

    cmb_usertype = ttk.Combobox(
        root,
        textvariable=var_utype,
        values=('Admin', 'Employee'),
        state='readonly',
        justify=CENTER,
        font=('goudy old style', 15),
    )
    cmb_usertype.place(x=850, y=220, width=180)
    var_utype.set(cmb_usertype.get())

    # row4

    lbl_address = Label(root, text='Address', bg='white',
                        font=('goudy old style', 15)).place(x=50, y=250)
    lbl_salary = Label(root, text='Salary', bg='white',
                       font=('goudy old style', 15)).place(x=500, y=250)

    txt_address = Entry(root, textvariable=var_address, bg='lightyellow'
                        , font=('goudy old style', 15)).place(x=150,
                                                              y=250, width=300, height=60)
    txt_salary = Entry(root, textvariable=var_salary, bg='lightyellow',
                       font=('goudy old style', 15)).place(x=570,
                                                           y=250, width=180)

    # Buttons

    btn_save = Button(
        root,
        text='Save',
        font=('goudy old style', 15),
        bg='#2196f3',
        fg='white',
        bd=1,
        cursor='hand2',
        command=database
    ).place(x=570, y=290, width=100)
    btn_update = Button(
        root,
        text='Update',
        font=('goudy old style', 15),
        bg='#4caf50',
        fg='white',
        bd=1,
        cursor='hand2',
    ).place(x=680, y=290, width=100)
    btn_delete = Button(
        root,
        text='Delete',
        font=('goudy old style', 15),
        bg='#f44336',
        fg='white',
        bd=1,
        cursor='hand2',
    ).place(x=790, y=290, width=100)
    btn_clear = Button(
        root,
        text='Clear',
        font=('goudy old style', 15),
        bg='#607d8b',
        fg='white',
        bd=1,
        cursor='hand2',
    ).place(x=905, y=290, width=100)

    # Employee Details

    emp_frame = Frame(root, bd=3, relief=RIDGE)
    emp_frame.place(x=0, y=350, relwidth=1, height=150)

    scrolly = Scrollbar(emp_frame, orient=VERTICAL)
    scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

    EmployeeTable = ttk.Treeview(emp_frame, columns=(
        'eid',
        'name',
        'email',
        'gender',
        'contact',
        'dob',
        'doj',
        'pass',
        'utype',
        'address',
        'salary',
    ), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.config(command=EmployeeTable.xview)
    scrolly.config(command=EmployeeTable.yview)
    EmployeeTable.heading('eid', text='Employee ID')
    EmployeeTable.heading('name', text='Name')
    EmployeeTable.heading('email', text='E-mail')
    EmployeeTable.heading('gender', text='Gender')
    EmployeeTable.heading('contact', text='Contact')
    EmployeeTable.heading('dob', text='D.0.B')
    EmployeeTable.heading('doj', text='D.0.J')
    EmployeeTable.heading('pass', text='Password')
    EmployeeTable.heading('utype', text='User Type')
    EmployeeTable.heading('address', text='Address')
    EmployeeTable.heading('salary', text='Salary')

    EmployeeTable['show'] = 'headings'

    EmployeeTable.column('eid', width=90)
    EmployeeTable.column('name', width=100)
    EmployeeTable.column('email', width=100)
    EmployeeTable.column('gender', width=100)
    EmployeeTable.column('contact', width=100)
    EmployeeTable.column('dob', width=100)
    EmployeeTable.column('doj', width=100)
    EmployeeTable.column('pass', width=100)
    EmployeeTable.column('utype', width=100)
    EmployeeTable.column('address', width=100)
    EmployeeTable.column('salary', width=100)

    EmployeeTable.pack(fill=BOTH, expand=1)

    root.mainloop()

