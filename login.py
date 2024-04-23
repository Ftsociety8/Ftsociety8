from tkinter import *
import csv

def sign_up():
    username = ent_user.get()
    password = ent_pass.get()
    if username !='' and password != '':
        with open('Storage.csv') as f:
            f_reader = csv.reader(f)
            next(f_reader)
            for row in f_reader:
                if row[0]== username:
                    lbl_wlc.config(text='این نام کاربری قبلا ثبت شده است ',fg='red',font=('B nazanin',12,'bold'))
                    break
            else:
                with open('Storage.csv','a',newline='') as f2:
                    f2_writer = csv.writer(f2)
                    f2_writer.writerow([username,password])
                    lbl_wlc.config(text='حساب شما با موفقیت ثبت شد.',fg='green',font=('b nazanin',12,'bold'))
    else:
        lbl_wlc.config(text='لطفا نام کاربری و رمز عبور را به درستی وارد نمایید',fg='Blue',font=('b nazanin',12,'bold'))

def log_in():
    username = ent_user.get()
    password = ent_pass.get()
    with open('Storage.csv') as f:
        f_reader = csv.reader(f)
        next(f_reader)

        for row in f_reader:
            if row[0]== username :
                lbl_wlc.config(text= f'خوش آمدید {username}',fg='green',font=('B Zar',12,'bold'))
                break
        else:
                lbl_wlc.config(text='نام کاربری یا رمز درست نمیباشد',fg='red',font=('b nazanin',12,'bold'))
win = Tk()
win.title('tkinter project')

w = 500
h = 500
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()

x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

win.geometry( '%dx%d+%d+%d'% (w,h,x,y))

lbl_user = Label(win,text='Username :')
lbl_pass = Label(win,text='Password :')
ent_user = Entry(win)
ent_pass = Entry(win)
btn_signup = Button(win,text='Sign up',fg = 'white',bg='black',command=sign_up)
btn_signin = Button(win,text='Log in',fg = 'white',bg='black',command= log_in)
lbl_wlc = Label(win)

lbl_user.pack()
ent_user.pack()
lbl_pass.pack()
ent_pass.pack()
btn_signup.pack()
btn_signin.pack()
lbl_wlc.pack()

win.mainloop()