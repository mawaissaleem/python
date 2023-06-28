from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import requests

dashboard = Tk()
dashboard.title("Storeman Dashboard")
storeName = "Shoe Store Inventory Management System"

def delete():
    print("Inside Delete")
    if(entry_article_code.get() == ""):
        MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
        con = mysql.connect(host="localhost", user="root", database="rest_try")
        cursor = con.cursor()
        cursor.execute("delete from product where article='"+ entry_article_code.get() +"'")
        cursor.execute("commit");
        
        entry_article_code.delete(0, 'end')
        entry_shoe_colour.delete(0, 'end')
        entry_shoe_size.delete(0, 'end')
        entry_shoe_type.delete(0, 'end')
        entry_gender.delete(0, 'end')
        entry_qty.delete(0, 'end')
        MessageBox.showinfo("Status", "Successfully Deleted")
        con.close();
    

def update():
   print("inside update")
   article= entry_article_code.get()
   shoe_colour= entry_shoe_colour.get()
   shoe_size= entry_shoe_size.get()
   shoe_type= entry_shoe_type.get()
   gender= entry_gender.get()
   qty= entry_qty.get()
   if(article == ""):
      MessageBox.showinfo("ALERT", "Please enter ID to find the Product Details!")
   else:   
      if(article == ""):
          MessageBox.showinfo("ALERT", "Please enter fields you want to update!")
      else:
          con = mysql.connect(host="localhost", user="root", database="rest_try")
          cursor = con.cursor()
          cursor.execute("update product set shoe_colour = '"+ shoe_colour +"', shoe_size= '"+ shoe_size+"', shoe_type= '"+ shoe_type+"', gender= '"+ gender+"', qty= '"+ qty+"' where article = '"+ article +"'")
          cursor.execute("commit");
  
          MessageBox.showinfo("Status", "Successfully Updated")
          con.close();
    
def save():
        print("inside save")
        
        con=mysql.connect(host="localhost",user="root",database="rest_try") 
        cursor=con.cursor()
        
        savequery = "select * from product"
        val1= ('', entry_article_code.get(), entry_shoe_colour.get(), entry_shoe_size.get(), entry_shoe_type.get(), entry_gender.get(),entry_qty.get())
        print(type(val1[0]), type(val1[1]),type(val1[2]),type(val1[3]),type(val1[4]),type(val1[5]), type(val1[6]))
      
        query1 = 'INSERT INTO product (id, article, shoe_colour, shoe_size, shoe_type, gender, qty) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        val1= ('', entry_article_code.get(), entry_shoe_colour.get(), entry_shoe_size.get(), entry_shoe_type.get(), entry_gender.get(),entry_qty.get())
        cursor.execute(query1,val1)
        cursor.execute("commit")
        
        print("Save executed")
        MessageBox.showinfo("Status", "Product Details Added Successfully")
        con.close();


def searchData():
    url = 'http://127.0.0.1:5000/product/' + articleNumber.get()
    print(url)
    x = requests.get(url)
    x.raise_for_status()
    # access JSOn content
    jsonResponse = x.json()
    print("Entire JSON response")
    print(jsonResponse)
    size_of_array = len(jsonResponse['shoe_colour'])
    if size_of_array==0:
        MessageBox.showinfo("Status", "Product not found")
    else:
        for i in range(size_of_array):
        
            shoe_colour_Label = Label(dashboard, text="Shoe Colour: " + jsonResponse['shoe_colour'][i])
            shoe_type_Label = Label(dashboard, text="Shoe Type: " + jsonResponse['shoe_type'][i])
            shoe_size_Label = Label(dashboard, text="Shoe Size: " + str(jsonResponse['shoe_size'][i]))
            gender_Label = Label(dashboard, text="Category: " + str(jsonResponse['gender'][i]))
            qty_Label = Label(dashboard, text="Quantity: " + str(jsonResponse['qty'][i]))
        
            shoe_colour_Label.grid(row=9+i, column=0, padx=10, pady=10)
            shoe_type_Label.grid(row=9+i, column=1, padx=10, pady=10)
            shoe_size_Label.grid(row=9+i, column=2, padx=10, pady=10)
            gender_Label.grid(row=9+i, column=3, padx=10, pady=10)
            qty_Label.grid(row=9+i, column=4, padx=10, pady=10)        


def logout():
    url = 'http://127.0.0.1:5000/logout'
    print(url)

    x = requests.get(url)
    x.raise_for_status()
    # access JSOn content
    jsonResponse = x.json()
    print("Entire JSON response")
    print(jsonResponse)
    dashboard.destroy()
    import login


titleLabel = Label(dashboard, text=storeName, font=('Tahoma', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

article_code = Label(dashboard, text="Article Code", font=('Tahoma', 15))
shoe_colour = Label(dashboard, text="Shoe Colour", font=('Tahoma', 15))
shoe_size = Label(dashboard, text="Shoe Size", font=('Tahoma', 15))
shoe_type = Label(dashboard, text="Shoe Type", font=('Tahoma', 15))
gender = Label(dashboard, text="Category", font=('Tahoma', 15))
qty = Label(dashboard, text="Quantity", font=('Tahoma', 15))
article_code.grid(row=1, column=0, padx=10, pady=10)
shoe_colour.grid(row=2, column=0, padx=10, pady=10)
shoe_size.grid(row=3, column=0, padx=10, pady=10)
shoe_type.grid(row=4, column=0, padx=10, pady=10)
gender.grid(row=5, column=0, padx=10, pady=10)
qty.grid(row=6, column=0, padx=10, pady=10)

entry_article_code = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_shoe_colour = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_shoe_size = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_shoe_type = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_gender = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_qty = Entry(dashboard, width=25, bd=5, font=('Tahoma', 15))
entry_article_code.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entry_shoe_colour.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entry_shoe_size.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entry_shoe_type.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
entry_gender.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
entry_qty.grid(row=6, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    dashboard, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Tahoma', 15), bg="#ffffff", command=save)
buttonEnter.grid(row=7, column=1, columnspan=1)

buttonUpdate = Button(
    dashboard, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Tahoma', 15), bg="#ffffff", command=update)
buttonUpdate.grid(row=7, column=2, columnspan=1)

buttonDelete = Button(
    dashboard, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Tahoma', 15), bg="#ffffff", command=delete)
buttonDelete.grid(row=7, column=3, columnspan=1)

searchLabel = Label(
    dashboard, text="Article Number", font=('Arial bold', 15))
searchLabel.grid(row=8, column=0, padx=10, pady=10)

articleNumber = StringVar()
entrySearch = Entry(dashboard, width=25, bd=5, font=(
    'Tahoma', 15), bg="#ffffff", textvariable=articleNumber)
entrySearch.grid(row=8, column=1, columnspan=3, padx=5, pady=5)

buttonSearch = Button(
    dashboard, text="Search", padx=5, pady=5, width=5,
    bd=3, font=('Tahoma', 15), bg="#ffffff", command=searchData)
buttonSearch.grid(row=8, column=4, columnspan=1)

buttonLogout = Button(
    dashboard, text="Log Out", padx=5, pady=5, width=5,
    bd=3, font=('Tahoma', 15), bg="#ffffff", command=logout)
buttonLogout.grid(row=7, column=4, columnspan=1)

dashboard.mainloop()