from tkinter import *
# import json
import requests
# from flask import jsonify

def getvalue():
    print(f"The value of username is {username.get()}")
    print(f"The value of password is {password.get()}")
    # login_screen.destroy()
    
    entered_username = username.get()
    entered_password = password.get()
    entered_re_password = re_password.get()

    if entered_password != entered_re_password:
        Label(login_screen, text="password does not match").pack()        
    else:
        url = 'http://127.0.0.1:5000/add_storeman'
        myobj = {
        "username" : entered_username,
        "password" : entered_password,
        "cnfrm_password": entered_re_password
        }

        x = requests.post(url, json = myobj)
        x.raise_for_status()
        # access JSOn content
        jsonResponse = x.json()
        print("Entire JSON response")
        print(jsonResponse)

        if jsonResponse['status'] == 200:            
            login_screen.destroy()
            import dashboard2


login_screen = Tk()
login_screen.title("Sign Up")
login_screen.geometry("300x250")
Label(login_screen, text="Please enter details").pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Username").pack()

username = StringVar()
password = StringVar()
re_password = StringVar()

username_signup_entry = Entry(login_screen, textvariable=username)
username_signup_entry.pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Password").pack()
password__signup_entry = Entry(
    login_screen, textvariable=password, show='*')
password__signup_entry.pack()
Label(login_screen, text="retype Password").pack()
re_password__signup_entry = Entry(
    login_screen, textvariable=re_password, show='*')
re_password__signup_entry.pack()
Label(login_screen, text="").pack()
Button(login_screen, text="Sign Up", width=10, height=1, command=getvalue).pack()
login_screen.mainloop()



