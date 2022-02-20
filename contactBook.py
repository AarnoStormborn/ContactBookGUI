from tkinter import *
from tkinter import messagebox
from createDB import create_database
import sqlite3

root = Tk()

root.title("Contact Book")

frame = LabelFrame(padx=20, pady=20)
frame.pack(padx=100, pady=100)

db = create_database()
db.dbcreate()

def addRecord():
    connect = sqlite3.connect('contact_book')
    cursor = connect.cursor()

    try:
        cursor.execute("INSERT INTO contacts VALUES (:id_num, :f_name, :l_name, :conNum, :email)",
                        {
                        'id_num': id_num.get(),
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'conNum': conNum.get(),
                        'email': email.get()
                        })

        email.delete(0, END)
        conNum.delete(0, END)
        l_name.delete(0, END)
        f_name.delete(0, END)
        id_num.delete(0, END)
        
    except sqlite3.IntegrityError:
        messagebox.showerror("Primary Key Error", "ID number already exists!")

    connect.commit()
    connect.close()



def showRecords():
    connect = sqlite3.connect('contact_book')
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()

    connect.commit()
    connect.close()

    recordsWindow = Toplevel()
    id_num_label = Label(recordsWindow, text="ID Number", font='bold')
    id_num_label.grid(row=0, column=0, padx=(0,10))
    f_name_label = Label(recordsWindow, text="First Name", font='bold')
    f_name_label.grid(row=0, column=1, padx=10)
    l_name_label = Label(recordsWindow, text="Last Name", font='bold')
    l_name_label.grid(row=0, column=2, padx=10)
    conNum_label = Label(recordsWindow, text="Contact Number", font='bold')
    conNum_label.grid(row=0, column=3, padx=10)
    email_label = Label(recordsWindow, text="Email ID", font='bold')
    email_label.grid(row=0, column=4, padx=10)
    
    print_record = ''
    i=1
    for record in records:
        i += 1
        id_num_label = Label(recordsWindow, text=record[0])
        id_num_label.grid(row=i, column=0)
        f_name_label = Label(recordsWindow, text=record[1])
        f_name_label.grid(row=i, column=1, padx=(0, 10))
        l_name_label = Label(recordsWindow, text=record[2])
        l_name_label.grid(row=i, column=2, padx=10)
        conNum_label = Label(recordsWindow, text=record[3])
        conNum_label.grid(row=i, column=3, padx=10)
        email_label = Label(recordsWindow, text=record[4])
        email_label.grid(row=i, column=4, padx=10)

#Create entry fields
id_num = Entry(frame, width=30)
id_num.grid(row=0, column=1, padx=10)
f_name = Entry(frame, width=30)
f_name.grid(row=1, column=1, padx=10)
l_name = Entry(frame, width=30)
l_name.grid(row=2, column=1)
conNum = Entry(frame, width=30)
conNum.grid(row=3, column=1)
email = Entry(frame, width=30)
email.grid(row=4, column=1)

#Create Labels for entry fields
id_num_label = Label(frame, text="ID Number:")
id_num_label.grid(row=0, column=0)
f_name_label = Label(frame, text="First Name:")
f_name_label.grid(row=1, column=0)
l_name_label = Label(frame, text="Last Name:")
l_name_label.grid(row=2, column=0)
conNum_label = Label(frame, text="Contact Number:")
conNum_label.grid(row=3, column=0)
email_label = Label(frame, text="Email ID:")
email_label.grid(row=4, column=0)

#buttons
recordButton = Button(frame, text="Add", command=addRecord)
recordButton.grid(row=5, column=0, columnspan=2, ipadx=50, pady=(20,0))

showRecordButton = Button(frame, text="Show All", command=showRecords)
showRecordButton.grid(row=6, column=0, columnspan=2, ipadx=50, pady=20)

root.mainloop()
