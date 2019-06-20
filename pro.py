from tkinter import *
from PIL import ImageTk,Image
from scroling import *
from tkinter import messagebox


root=Tk()
root.geometry('1920x1080+0+0')
root.title('Blood Bank ')
frame = Frame(root,width=1920,height=1080,bg='light green')
frame.place(x=0,y=0)

ing=ImageTk.PhotoImage(Image.open('front1.jpg'))
label = Label(frame,image=ing,width=1920,height=1080)
label.place(x=0,y=0)


button1 = Button(frame,text='Admin',width=20,height=2,bd=3,bg='grey',fg='black',relief=SUNKEN,command=lambda :admin(frame,root))
button1.config(font=20)
button1.place(x=300,y=400)

button2 = Button(frame,text='User',width=20,height=2,bd=3,bg='grey',fg='black',relief=SUNKEN, command= lambda :User(frame,root))
button2.config(font=20)
button2.place(x=1400,y=400)


button3 = Button(frame,text='Exit',width=20,height=2,bd=3,bg='grey',fg='black',relief=SUNKEN,command= lambda :exit())
button3.config(font=20)
button3.place(x=850,y=900)



def admin(frame,root):

    frame.destroy()

    frame1 = Frame(root,width=1920, height=1080,bg='grey')
    frame1.place(x=0,y=0)

    label = Label(frame1, text='Wellcome to the admin profile', width=40, height=5)
    label.config(font=30)
    label.place(x=500,y=70)

    ing1= ImageTk.PhotoImage(Image.open('admin.jpg'))
    label1= Label(frame1,image=ing1, width=1920, height=1080)
    label1.place(x=0,y=0)


    label2 = Label(frame1, text='Login_id',  width=20, height=3, bg='grey', fg='black')
    label2.config(font=20)
    label2.place(x=500, y=50)
    label3 = Label(frame1,text='Name', width=20,height=3,bg='grey', fg='black')
    label3.config(font=20)
    label3.place(x=500,y=150)
    label4 = Label(frame1,text='Age', width=20,height=3,bg='grey', fg='black')
    label4.config(font=20)
    label4.place(x=500,y=250)
    label5 = Label(frame1,text='Phone_no', width=20,height=3,bg='grey', fg='black')
    label5.config(font=20)
    label5.place(x=500,y=350)
    label6 = Label(frame1,text='Email', width=20,height=3,bg='grey', fg='black')
    label6.config(font=20)
    label6.place(x=500,y=450)
    label7 = Label(frame1,text='Adhar no ', width=20,height=3,bg='grey', fg='black')
    label7.config(font=20)
    label7.place(x=500,y=550)


    a = StringVar()
    entry1 = Entry(frame1,textvariable=a ,width=30,bd=5,bg='grey',fg='black')
    entry1.config(font=20)
    entry1.place(x=800,y=50)
    entry2 = Entry(frame1, width=30, bd=5,bg='grey',fg='black')
    entry2.config(font=20)
    entry2.place(x=800,y=150)
    entry3 = Entry(frame1, width=30, bd=5,bg='grey',fg='black')
    entry3.config(font=20)
    entry3.place(x=800,y=250)
    entry4 = Entry(frame1, width=30, bd=5,bg='grey',fg='black')
    entry4.config(font=20)
    entry4.place(x=800,y=350)
    entry5 = Entry(frame1, width=30, bd=5,bg='grey',fg='black')
    entry5.config(font=20)
    entry5.place(x=800,y=450)
    entry6 = Entry(frame1, width=30, insertwidth=10,bd=5, bg='grey', fg='black')
    entry6.config(font=20)
    entry6.place(x=800, y=550)



    button = Button(frame1, text='Submit', width=30, height=3, bg='grey', fg='black',command=lambda :account(a,entry1,entry2,entry3,entry4,entry5,entry6))
    button.place(x=500, y=700)

    button1 = Button(frame1, text='Exit', width=30, height=3, bg='grey', fg='black',command =lambda :Exit(frame1,frame))
    button1.place(x=800, y=700)


    frame1.mainloop()

def account(a,entry1,entry2,entry3,entry4,entry5,entry6):
    import string
    import random
    c=' '
    b = string.digits
    for i in range(8):
        c =c + random.choice(b)
    a=a.set(c)

    g = entry1.get()
    b = entry2.get()
    c = entry3.get()
    d = entry4.get()
    e = entry5.get()
    f = entry6.get()

    """import mysql.connector
    #from mysql.connector import error
    #from mysql.connector import errorcode
    con = mysql.connector.connect(host='localhost',database='login',user='root',password='kanik')
    query = ("INSERT INTO `login4`(login_id,name,age,ph_no,email,adhar) VALUES (%s,%s,%s,%s,%s,%s)",(g, b, c, d, e, f))

    cursor = con.cursor()
    result = cursor.execute(query)
    con.commit()
    print("Record inserted successfully into python_users table")
    print(result)
"""

    import sqlite3
    con=sqlite3.connect('Login Record')
    con.execute("create table if not exists login7(login_id BIGINT[10],name varchar[20],age INT[3],ph_no BIGINT[10],email Varchar[50],adhar BIGINT[15])")
    query="insert into login7(login_id,name,age,ph_no,email,adhar) values('{}','{}','{}','{}','{}'.'{}')".format(g,b,c,d,e,f)
    i=con.execute(query)
    con.commit()
    m=con.execute('select*from login7')
    print(list(m))
    print('Successfully Inserted')
    con.close()

def User(frame,root,):
    frame.destroy()

    frame4 = Frame(root,width=1920, height=1080,bg='orchid3')
    frame4.place(x=0,y=0)

    ing3 = ImageTk.PhotoImage(Image.open('user.png'))
    label8 = Label(frame4,image=ing3,width=1920,height=1080)
    label8.place(x=0,y=0)


    label = Label(frame4, text='Login id', width=30, height=3, bd=3, bg='brown', fg='white')
    label.config(font=40)
    label.place(x=550, y=400)

    entry = Entry(frame4,width=30,bd=3, bg='brown', fg='white')
    entry.config(font=50)
    entry.place(x=1100,y=420)


    button = Button(frame4,text='Process',width=25, height=2,bd=3, bg='brown', fg='white', command =lambda :Process(frame4,root,entry))
    button.config(font=40)
    button.place(x=550,y=650)

    button = Button(frame4, text='Help', width=25, height=2, bd=3, bg='brown', fg='white',command = lambda :Help(frame4,root))
    button.config(font=40)
    button.place(x=1100, y=650)


    frame4.mainloop()



def Exit(frame1,frame):
    frame1.destroy()
    frame3 = Frame(frame,width=1920,height=1080,bg='red')
    frame3.place(x=0,y=0)


    frame3.mainloop()


def Process(frame4,root,entry):
    a=entry.get()
    b=[]

    import sqlite3
    from sqlite3 import Error

    def create_connection(login1):
        try:
            conn = sqlite3.connect(login1)
            return conn
        except Error as e:
            print(e)

    def select_login1(conn):
        cur = conn.cursor()
        cur.execute("SELECT Login_id FROM login1 ")

        rows = cur.fetchall()

        for row in rows:
           b.insert(row)



        frame4.destroy()
        frame5 = Frame(root,width=1920, height=1080,bg='khaki1')
        frame5.place(x=0, y=0)

        ing = ImageTk.PhotoImage(Image.open('process.jpg'))
        label = Label(frame5,image=ing,width=1680, height=1050)
        label.place(x=70,y=0)

        label1 = Label(frame5, text='Password',width=20, height= 2,bg='grey',fg='black',bd=2)
        label1.config(font=40)
        label1.place(x=500,y=400)

        entry1 = Entry(frame5,width=20,bg='grey',fg='black',bd=2)
        entry1.place(x=1125,y=400)


        button = Button(frame5,text='Submit',width=25, height=2,bd=3, bg='grey', fg='black',command = lambda:run(frame5,root))
        button.config(font=40)
        button.place(x=775,y=800)



    frame5.mainloop()

def run(frame5,root):
    frame5.destroy()
    frame6 = Frame(root,width=1920, height=1080,bg='khaki1')
    frame6.place(x=0,y=0)

    button = Button(frame6, text='Add',width=30, height=3,bg='brown',fg='grey',command=lambda: add(frame6,root))
    button.place(x=550,y=300)

    button = Button(frame6, text='Show', width=30, height=3, bg='brown', fg='grey',command = lambda :show(frame6,root))
    button.place(x=1200, y=300)

    frame6.mainloop()
def add(frame6,root):
    frame6.destroy()
    frame = Frame(root,width=1920, height=1080,bg='khaki1')
    frame.place(x=0,y=0)

    ing= ImageTk.PhotoImage(Image.open('kk.jpg'))
    label =Label(frame, image=ing,width=1920,height=1080)
    label.place(x=0,y=0)

    label1= Label(frame, text='Name',width=30,height=3,bg='brown',fg='grey',bd=3)
    label1.place(x=250,y=250)

    label2 = Label(frame, text='Date', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=350)

    label2 = Label(frame, text='Age', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=450)

    label2 = Label(frame, text='Blood_group', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=550)

    label2 = Label(frame, text='Email', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=650)

    label2 = Label(frame, text='Contact', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=750)

    label2 = Label(frame, text='Address', width=30, height=3, bg='brown', fg='grey', bd=3)
    label2.place(x=250, y=850)

    e1= Entry(frame,width=30, bg='brown', fg='grey', bd=4)
    e1.place(x=1500,y=250)

    e2 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e2.place(x=1500, y=350)

    e3 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e3.place(x=1500, y=450)

    e4 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e4.place(x=1500, y=550)

    e5 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e5.place(x=1500, y=650)

    e6 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e6.place(x=1500, y=750)

    e7 = Entry(frame, width=30, bg='brown', fg='grey', bd=4)
    e7.place(x=1500, y=850)


    button = Button(frame,text='Submit',width=30, height=3, bg='brown', fg='grey', bd=3,command = lambda :submit(e1,e2,e3,e4,e5,e6,e7))
    button.place(x=600,y=900)

    button = Button(frame, text='Exit', width=30, height=3, bg='brown', fg='grey', bd=3,command = lambda :exit())
    button.place(x=1100, y=900)


    frame.mainloop()
def submit(e1,e2,e3,e4,e5,e6,e7):
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()
    g = e7.get()

    import sqlite3
    con = sqlite3.connect('Blood_record')
    con.execute("create table if not exists blood3(Name VARCHAR[20],Date INT[10],age VARCHAR[3],bloodgroup VARCHAR[3],email VARCHAR[50],contact INT[10],Address VARCHAR[50]")
    query = "insert into blood3(Name,Date,age,bloodgroup,email,contact,Address) values(?,?,?,?,?,?,?)".format(a, b, c, d, e, f, g)
    l = con.execute(query)
    con.commit()
    m = con.execute('select*from blood3')
    print(list(m))
    print('Successfully Inserted')
    con.close()

def show(frame6,root):
    frame6.destroy()
    frame = Frame(root,bg='grey',width=1920, height=1080)
    frame.place(x=0,y=0)

    ing = ImageTk.PhotoImage(Image.open('show.png'))
    label = Label(frame,image=ing,width=1920,height=1080)
    label.place(x=0,y=0)

    scrolling_area = Scrolling_Area(frame, height=500, width=900,bg='khaki1')
    scrolling_area.place(x=550,y=100)

    button= Button(frame,text='Back',width=30,height=3,bg='deep sky blue',fg='red',command =lambda: run(frame5,root))
    button.place(x=600,y=800)

    button = Button(frame, text='Print', width=30, height=3, bg='deep sky blue', fg='red')
    button.place(x=1100, y=800)


    frame.mainloop()


root.mainloop()