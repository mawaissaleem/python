from tkinter import *
import requests


def getvalue():
    print(f"The value of username is {username.get()}")
    print(f"The value of password is {password.get()}")
    # login_screen.destroy()
    
    entered_username = username.get()
    entered_password = password.get()


    url = 'http://127.0.0.1:5000/login'
    myobj = {
    "username" : entered_username,
    "password" : entered_password
    }

    x = requests.post(url, json = myobj)
    x.raise_for_status()
    # access JSOn content
    jsonResponse = x.json()
    print("Entire JSON response")
    print(jsonResponse)

    if jsonResponse['status'] == 200:
        if entered_username=='admin':
            login_screen.destroy()
            import dashboard_admin
        else:
            # if the user is storeman then open dashboard that does not contain all features.
            login_screen.destroy()
            import storeman_dashboard
    elif jsonResponse['status'] == 401:
        print("incorrect username or password")
        Label(login_screen, text="incorrect usrname or password").pack(side=BOTTOM)

login_screen = Tk()
login_screen.title("Login")
login_screen.geometry("300x210")
Label(login_screen, text="Please enter login details").pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Username").pack()

username = StringVar()
password = StringVar()

username_login_entry = Entry(login_screen, textvariable=username)
username_login_entry.pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Password").pack()
password__login_entry = Entry(
    login_screen, textvariable=password, show='*')
password__login_entry.pack()
Label(login_screen, text="").pack()
Button(login_screen, text="Login", width=10, height=1, command=getvalue).pack()
login_screen.mainloop()



