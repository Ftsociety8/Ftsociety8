from tkinter import *
from mysql.connector import connect, Error

def sign_up():
    username = ent_user.get()
    password = ent_pass.get()
    values = (username, password)
    if username != '' and password != '':
        try:
            with connect(
                host='localhost',
                user='root',
                password='12345678',
                database='bigsmoke',
                port=3306
            ) as connection:
                select_sql = 'SELECT * FROM users'
                with connection.cursor() as crsr:
                    crsr.execute(select_sql)
                    data = crsr.fetchall()
                    for user in data:
                        if user[0] == username:
                            lbl_wlc.config(text='This username is already registered.', fg='red', font=('b nazanin', 12, 'bold'))
                            break
                    else:
                        insert_sql = '''
                        INSERT INTO users (username, passwd)
                        VALUES (%s, %s)
                        '''
                        crsr.execute(insert_sql, values)
                        connection.commit()
                        lbl_wlc.config(text='Username and password registered successfully.', fg='green', font=('b zar', 12, 'bold'))
        except Error as e:
            print(e)
    else:
        lbl_wlc.config(text='Please enter username and password correctly.', fg='Blue', font=('b nazanin', 12, 'bold'))

def log_in():
    username = ent_user.get()
    password = ent_pass.get()
    values = (username, password)

    def delete_user():
        
        for info in data:
                if info[0] == username and info[1] == password:
                    delete_query2 = '''
                    DELETE FROM users
                    WHERE username = %s 
                    '''
                    crsr.execute(delete_query2, values)
                    lbl_delete.config(text='Successfully deleted!')
        else:
            lbl_delete.config(text='Incorrect username or password')
        with connection.cursor() as crsr:
            crsr.execute(delete_query, values)
            data = crsr.fetchall()
            

    def update_info():
        new_password = entlf_update2.get()
        conf_password = entlf_upadate3.get()
        curnt_password = entlf_update.get()
        try: 
            if curntpassword ==  password and password != new_password and new_password == conf_password:
                update_query = '''
                UPDATE users SET 
                 passwd = %s
                WHERE username = %s 
                '''
                update_values = (new_password, username, password)
                with connection.cursor() as crsr:
                    crsr.execute(update_query, update_values)
                    connection.commit()
                    lbl_updatepass.config(text='Successfully saved!')
        except Error as e:
            print(e)
           
                        

    with connect(
        host='localhost',
        user='root',
        password='12345678',
        database='bigsmoke',
        port=3306
    ) as connection:
        with connection.cursor() as crsr:
            select_query = 'SELECT * FROM users'
            crsr.execute(select_query)
            result = crsr.fetchall()
            for infos in result:
                if infos[0] == username and infos[1] == password:
                    win2 = Toplevel(win)
                    w = 500
                    h = 500
                    ws = win2.winfo_screenwidth()
                    hs = win2.winfo_screenheight()
                    x = (ws/2) - (w/2)
                    y = (hs/2) - (h/2)
                    win2.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    lblf_update = LabelFrame(win2, text='update')
                    lbl_updatepass = Label(lblf_update, text='current password:')
                    entlf_update = Entry(lblf_update)
                    lbl_updatepass1 = Label(lblf_update, text='New password:')
                    entlf__update2 = Entry(lblf_update)
                    lbl_updatepass2 = Label(lblf_update, text='Confirm password:')
                    entlf__update3 = Entry(lblf_update)
                    btn_update = Button(lblf_update,text='Update', bg='green', command=update_info)
                    lblf_delete = LabelFrame(win2, text='delete')
                    lbl_delete = Label(lblf_delete,text='If you are sure about deleting your account, enter your current password:')
                    ent_delete = Entry(lblf_delete)
                    btn_delete = Button(lblf_delete,text='Delete', bg='red', command=delete_user)
                    lblf_update.pack()
                    lbl_updatepass.pack()
                    entlf   _update.pack()
                    lbl_updatepass1.pack()
                    entlf_update2.pack()
                    lbl_updatepass2.pack()
                    entlf__update3.pack()
                    btn_update.pack()
                    lblf_delete.pack()
                    lbl_delete.pack()
                    ent_delete.pack()
                    btn_delete.pack()
                    breack

win = Tk()
win.title('tkinter project')
w = 500
h = 500
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
win.geometry('%dx%d+%d+%d' % (w, h, x, y))
lbl_user = Label(win, text='Username:')
lbl_pass = Label(win, text='Password:')
ent_user = Entry(win)
ent_pass = Entry(win)
btn_signup = Button(win, text='Sign up', fg='white', bg='black', command=sign_up)
btn_signin = Button(win, text='Log in', fg='white', bg='black', command=log_in)
lbl_wlc = Label(win)
lbl_user.pack()
ent_user.pack()
lbl_pass.pack()
ent_pass.pack()
btn_signup.pack()
btn_signin.pack()
lbl_wlc.pack()
win.mainloop()