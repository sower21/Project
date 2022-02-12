from tkinter import*
from PIL import Image, ImageTk
import os

#หน้าlig in 
def wdlogin(): 
    global root #
    root = Tk()
    root.title("raednovel")
    root.geometry("350x600")
    img = PhotoImage(file="1.png")
    Label(root, image=img).pack()
#TextBOX
    global usname
    global USN
    usname=StringVar()
    USN = Entry(root,textvariable=usname)
    USN.place(x=50,y=250,width=250,height=25)
    global passw
    global PW
    passw=StringVar()
    PW = Entry(root,textvariable=passw,show='*')
    PW.place(x=50,y=310,width=250,height=25)
#Button create
    username=Label(text="Username",font=15,fg="#fcffff",bg="#1c252a").place(x=50,y=220)
    password=Label(text="Password",font=15,fg="#fcffff",bg="#1c252a").place(x=50,y=280)
    login = Button(text="log in",font=('Athiti',12,'bold'),fg="#5c5449",bg="#ffe263",command=login_verify).place(x=125,y=345,width=100)
    CYA = Button(text="OR create your account",font=('Athiti',9),fg="#ffe263",bg="#1c252a",borderwidth=0 ,command=wdcreateaccount).place(x=75,y=385,width=200)
    root.mainloop()
#เช็ครหัส   
def login_verify():
  global username1
  username1 = usname.get()
  password1 = passw.get()
  USN.delete(0, END)
  PW.delete(0, END)
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    global verify
    verify = file1.read().splitlines()
    if password1 in verify:
        wdhome()
    else:
        password_not_recognised()

  else:
        user_not_found()

def exitca():
    categories.destroy()
# หน้าหมวดหมู่
def wdcategories():
  global categories
  categories = Toplevel()
  categories.title("categories")
  categories.geometry("350x600")
  img = PhotoImage(file="4.png")
  Label(categories, image=img).pack()
  #ปุ่มhome
  photo_home=PhotoImage(file="home.png")  
  p1=Button(categories,image=photo_home, borderwidth=0 ,command=exitca,bg="#1c252a").place(x=150,y=540,height=50,width=50)
  #สร้างปุ่ม
  p2=Button(categories,text="romance",font=('Athiti',15,'bold'),fg="#FFFFFF",bg="#1c252a",borderwidth=0,command=wpage1 ).place(x=100,y=160,width=150)
  p3=Button(categories,text="fantasy",font=('Athiti',15,'bold'),fg="#FFFFFF",bg="#1c252a",borderwidth=0,command=wpage2).place(x=100,y=225,width=150)
  p4=Button(categories,text="horror",font=('Athiti',15,'bold'),fg="#FFFFFF",bg="#1c252a",borderwidth=0,command=wpage3).place(x=100,y=290,width=150)
  p5=Button(categories,text="detective",font=('Athiti',15,'bold'),fg="#FFFFFF",bg="#1c252a",borderwidth=0,command=wpage4).place(x=100,y=355,width=150)
  p6=Button(categories,text="knowledge",font=('Athiti',15,'bold'),fg="#FFFFFF",bg="#1c252a",borderwidth=0,command=wpage5).place(x=100,y=420,width=150)
  categories.mainloop()
#หมวดหมู่นิยาย

#เล่ม 1  romance
def wpage1():
    global page1
    page1 = Toplevel()
    page1.title("page1")
    page1.geometry("350x600")
    img = PhotoImage(file="6.png")
    Label(page1, image=img).pack()
    book1=PhotoImage(file="ปก1.png")
    Label(page1,text="romance",font=('Athiti',15,'bold'),fg="#1c252a").place(x=100,y=20,width=150)
    p1=Button(page1,image=book1, borderwidth=0 , command=rbook1).place(x=10,y=90,height=165,width=116)
    page1.mainloop()

def rbook1():
    page1.destroy()
    global b1
    b1 = Toplevel()
    b1.title("Book1")
    b1.geometry("350x600")
    my_text = Text(b1,width=350,height=600)
    my_text.pack()
    f1 = open("romance.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    b1.mainloop()

 #เล่ม 2  fantasy   
def wpage2():
    global page2
    page2 = Toplevel()
    page2.title("page2")
    page2.geometry("350x600")
    img = PhotoImage(file="6.png")
    Label(page2, image=img).pack()
    book2=PhotoImage(file="ปก4.png")
    Label(page2,text="fantasy",font=('Athiti',15,'bold'),fg="#1c252a").place(x=100,y=20,width=150)
    p1=Button(page2,image=book2, borderwidth=0 , command=rbook2).place(x=10,y=90,height=165,width=116)
    page2.mainloop()
    
def rbook2():
    page2.destroy()
    global b2
    b2 = Toplevel()
    b2.title("Book2")
    b2.geometry("350x600")
    my_text = Text(b2,width=350,height=600)
    my_text.pack()
    f1 = open("fantasy.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    b2.mainloop()

#เล่ม 3 horror
def wpage3():
    global page3
    page3 = Toplevel()
    page3.title("page3")
    page3.geometry("350x600")
    img = PhotoImage(file="6.png")
    Label(page3, image=img).pack()
    book3=PhotoImage(file="ปก3.png")
    Label(page3,text="horror",font=('Athiti',15,'bold'),fg="#1c252a").place(x=100,y=20,width=150)
    p1=Button(page3,image=book3, borderwidth=0 , command=rbook3).place(x=10,y=90,height=165,width=116)
    page3.mainloop()

def rbook3():
    page3.destroy()
    global b3
    b3 = Toplevel()
    b3.title("Book3")
    b3.geometry("350x600")
    my_text = Text(b3,width=350,height=600)
    my_text.pack()
    f1 = open("horror.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    b3.mainloop()   
#เล่ม 4 detective
def wpage4():
    global page4
    page4 = Toplevel()
    page4.title("page4")
    page4.geometry("350x600")
    img = PhotoImage(file="6.png")
    book4=PhotoImage(file="ปก5.png")
    Label(page4, image=img).pack()
    Label(page4,text="detective",font=('Athiti',15,'bold'),fg="#1c252a").place(x=100,y=20,width=150)
    p1=Button(page4,image=book4, borderwidth=0 , command=rbook4).place(x=10,y=90,height=165,width=116)
    page4.mainloop()

def rbook4():
    page4.destroy()
    global b4
    b4 = Toplevel()
    b4.title("Book4")
    b4.geometry("350x600")
    my_text = Text(b4,width=350,height=600)
    my_text.pack()
    f1 = open("detective.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    b4.mainloop() 

#เล่ม 5  knowledge
def wpage5():
    global page5
    page5 = Toplevel()
    page5.title("page5")
    page5.geometry("350x600")
    img = PhotoImage(file="6.png")
    Label(page5, image=img).pack()
    book5=PhotoImage(file="ปก2.png")
    Label(page5,text="knowledge",font=('Athiti',15,'bold'),fg="#1c252a").place(x=100,y=20,width=150)
    p1=Button(page5,image=book5, borderwidth=0 , command=rbook5).place(x=10,y=90,height=165,width=116)
    page5.mainloop()

def rbook5():
    page5.destroy()
    global b5
    b5 = Toplevel()
    b5.title("Book5")
    b5.geometry("350x600")
    my_text = Text(b5,width=350,height=600)
    my_text.pack()
    f1 = open("knowledge.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    b5.mainloop() 

#จบหมวดหมู่นิยาย

#หน้าหลัก
def wdhome():
  root.destroy()
  global home
  home = Tk()
  home.title("home")
  home.geometry("350x600")
  img = PhotoImage(file="3.png")
  Label(home, image=img).pack()
  
  b1=Button(home, text = "Categories",bg="#737373" ,fg = "#fdd059",font=('Athiti',10,'bold'),command=wdcategories).place(x=10,y=5)
  book1=PhotoImage(file="ปก1.png")
  p1=Button(home,image=book1, borderwidth=0 ,command= rmbook1).place(x=10,y=410,height=165,width=116)
  book2=PhotoImage(file="ปก2.png")
  p2=Button(home,image=book2, borderwidth=0 ,command= rmbook2).place(x=160,y=410,height=165,width=116)
  book3=PhotoImage(file="ปก3.png")
  p3=Button(home,image=book3, borderwidth=0,command= rmbook3).place(x=310,y=410,height=165,width=116)
  bookre=PhotoImage(file="ปกm.png")
  prepare_class=Label(home,image=bookre, borderwidth=0).place(x=105,y=80,height=198,width=139)
  bread=Button(home, text = "Read",bg="#737373" ,fg = "#fdd059",font=('Athiti',10,'bold'),command=readmain).place(x=155,y=280)
  iconuser=PhotoImage(file="ii1.png")
  p2=Button(home,image=iconuser, borderwidth=0 ,bg="#82b894",command=wdUser ).place(x=290,y=5,height=50,width=50)
  home.mainloop()

#อ่านนิยายหน้าหลัก
def readmain():
    global rm
    rm = Toplevel()
    rm.title("Book4")
    rm.geometry("350x600")
    my_text = Text(rm,width=350,height=600)
    my_text.pack()
    f1 = open("fantasy.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    rm.mainloop()
def rmbook1():
    global rm1
    rm1 = Toplevel()
    rm1.title("Book1")
    rm1.geometry("350x600")
    my_text = Text(rm1,width=350,height=600)
    my_text.pack()
    f1 = open("romance.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    rm1.mainloop()

def rmbook2():
    global rm2
    rm2 = Toplevel()
    rm2.title("Book1")
    rm2.geometry("350x600")
    my_text = Text(rm2,width=350,height=600)
    my_text.pack()
    f1 = open("knowledge.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    rm2.mainloop()

def rmbook3():
    global rm3
    rm3 = Toplevel()
    rm3.title("Book1")
    rm3.geometry("350x600")
    my_text = Text(rm3,width=350,height=600)
    my_text.pack()
    f1 = open("horror.txt",'r',encoding="utf-8")
    s = f1.read()
    my_text.insert(END,s)
    f1.close()
    rm3.mainloop()

#หน้าผู้ใช้ออกจากระบบ
def exitprogram():
    User.destroy()
    home.destroy()
def wdcross():
    User.destroy()
def wdUser():
    global User    
    User = Toplevel()
    User.geometry("350x600")
    img = PhotoImage(file="5.png")
    Label(User, image=img).pack()
    User.title("User")
#ข้อความ label
    label1 = Label(User,text=username1,bg="#1c252a",fg="#fcffff",font=('Athiti',20,'bold')).place(x=150 , y=80)
    file1 = open(username1, "r")
    textinuser = file1.read().splitlines()
    email= Label(User,text="E-mail : "+textinuser[3],bg="#1c252a",fg="#fcffff",font=('Athiti',15)).place(x=50,y=220)
    phone= Label(User,text="Phone Number : "+textinuser[2],bg="#1c252a",fg="#fcffff",font=('Athiti',15)).place(x=50,y=250)
# button ปุ่มกด
    cross=PhotoImage(file="c.png")
    p2 = Button(User,image=cross, borderwidth=0 ,bg="#1c252a",command=wdcross ).place(x=0,y=0,height=30,width=30)
    logout = Button(User, text= 'Logout',font=('Athiti',20,'bold') ,bg="#fdd059", command = exitprogram ).place(x=100,y=500,width=150)
    User.mainloop()


def password_not_recognised():
  global screen4
  screen4 = Toplevel(root)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()
  screen4.mainloop()  

def user_not_found():
  global screen5
  screen5 = Toplevel(root)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()
  screen5.mainloop() 

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

#สร้างบัญชี  
def wdcreateaccount():
    root.destroy() 
    global createacc 
    createacc = Tk()
    createacc.geometry("350x600")
    img = PhotoImage(file="2.png")
    Label(createacc, image=img).pack()


    username=Label(createacc,text="Username",font=('Athiti',15),fg="#fcffff",bg="#1c252a").place(x=50,y=145)
    global txtun
    global etusername
    txtun=StringVar()
    etusername=Entry(createacc,textvariable=txtun)
    etusername.place(x=50,y=175,width=250)

    password=Label(createacc,text="Password",font=('Athiti',15),fg="#fcffff",bg="#1c252a").place(x=50,y=195)
    global txtpw
    global etpw
    txtpw=StringVar()
    etpw=Entry(createacc,textvariable=txtpw,show='*')
    etpw.place(x=50,y=225,width=250)

    cfpassword=Label(createacc,text="Confirm Password",font=('Athiti',15),fg="#fcffff",bg="#1c252a").place(x=50,y=245)
    global txtpw2
    global etcfpw
    txtpw2=StringVar()
    etcfpw=Entry(createacc,textvariable=txtpw2 ,show='*')
    etcfpw.place(x=50,y=275,width=250)

    email=Label(createacc,text="E-mail",font=('Athiti',15),fg="#fcffff",bg="#1c252a").place(x=50,y=295)
    global txtem
    global etem
    txtem=StringVar()
    etem=Entry(createacc,textvariable=txtem)
    etem.place(x=50,y=325,width=250)

    phonenum=Label(createacc,text="Phone number",font=('Athiti',15),fg="#fcffff",bg="#1c252a").place(x=50,y=345)
    global txtphnum
    global etpn
    txtphnum=StringVar()
    etpn=Entry(createacc,textvariable=txtphnum)
    etpn.place(x=50,y=375,width=250)

    global language
    language=IntVar()
    accept=Checkbutton(createacc,text="accept policy",font=('Athiti',10),variable=language,fg="#9692a4",bg="#1c252a").place(x=120,y=420)

    #button create
    buttoncreate=Button(createacc,text="create",font=('Athiti',12,'bold'),fg="#5c5449",bg="#ffe263",command=check).place(x=125,y=450,width=100)
    createacc.mainloop()

def check(): #function button create
    username_info = txtun.get()
    password_info = txtpw.get()
    confirmpassword_info = txtpw2.get()
    account_info = txtphnum.get()
    email_info = txtem.get()
    if password_info == confirmpassword_info:
        if language.get()==1:
            file = open(username_info, "w")
            file.write(username_info+"\n")
            file.write(password_info+"\n")
            file.write(account_info+"\n")
            file.write(email_info+"\n")
            file.close()
            register_sucess()
        else:
            register_failed()
    else:
        register_failed()
        etpw.delete(0, END)
        etcfpw.delete(0, END)
# Designing popup for register success
def register_sucess():
    global register_success_screen
    register_success_screen = Toplevel()
    register_success_screen.title("Success")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text = "register_sucess").pack()
    Button(register_success_screen, text = "OK", command =delete_register_success).pack()
    register_success_screen.mainloop()
#Designing popup for register failed
def register_failed():
    global register_success_screen
    register_success_screen = Toplevel()
    register_success_screen.title("Failed")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text = "register_failed").pack()
    Button(register_success_screen, text="OK", command=delete_register_failed).pack()
    register_success_screen.mainloop()
# Deleting popups
def delete_register_success():
    register_success_screen.destroy()
    createacc.destroy()
    wdlogin()
def delete_register_failed():
    register_success_screen.destroy()

wdlogin()