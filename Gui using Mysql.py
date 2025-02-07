from tkinter import *
import mysql.connector as mysql
def di(row):
    if row is not None:
            lb2=Label(f,text=f'id={row[0]} name={row[1]} marks={row[2]}')
            lb2.place(x=100,y=200)
    else:
            lb3=Label(f,text="no such record")
            lb3.place(x=100,y=200)

def datab(data):
    mydb=mysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="class"
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from studentt where id=%d;"%int(data))
    row=mycursor.fetchone()
    di(row)
def recieve_data(event):
    data=e1.get()
    datab(data)

root=Tk()
root.geometry("400x400")
f=Frame(root,height=300,width=300)
f.pack()
lb1=Label(f,text="Enter Your id:")
lb1.place(x=100,y=100)
e1=Entry(f)
e1.place(x=180,y=100)
e1.bind('<Return>',recieve_data)
root.mainloop()