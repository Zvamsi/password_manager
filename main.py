from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

from pywin.framework.help import helpIDMap


# ----------------------------SEARCH DATA  ------------------------------------#
def find_password():
    website=website_entry.get()
    try:
        with open('data.json','r') as file:
            data=json.load(file)
            mail=data[website]['email']
            password=data[website]['password']
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='File not found 404...')
    except KeyError:
        messagebox.showinfo(title='oops',message='The info you are looking for is not present in database')
    else:
        messagebox.showinfo(title=website.title(),message=f'Mail: {mail}\nPassword: {password}')





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list=[random.choice(letters) for _ in range(nr_letters)]
    symbol_list=[random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=letters_list+symbol_list+numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    print(password)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    password=password_entry.get()
    username=email_username_entry.get()

    new_data={
        website:{
            'email':username,
            'password':password,
        }
    }

    if website=='' or username=='':
        messagebox.showinfo(title='OOPs',message='One or more mandatory fields are empty please check out')
        return

    try:
        with open('data.json','r') as file:
            # Reading the data from file
            data=json.load(file)
            # Updating the data from file
            data.update(new_data)
            # Writing the new data into file
    except FileNotFoundError:
        with open('data.json','w') as file:
            json.dump(new_data,file,indent=4)
    else:
        with open('data.json','w') as file:
            json.dump(data,file,indent=4)

    website_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

# CREATING CANVAS
lockImage=PhotoImage(file='logo.png')
canvas=Canvas(height=200,width=200)
canvas.create_image(100,100,image=lockImage)
canvas.grid(column=1,row=0)

# Labels

website_label=Label(text='Website: ')
website_label.grid(column=0,row=1)

email_username_label=Label(text='Email/Username: ')
email_username_label.grid(column=0,row=2)

password_label=Label(text='Password: ')
password_label.grid(column=0,row=3)

# Entries

website_entry=Entry(width=25)
website_entry.focus()
website_entry.grid(column=1,row=1)

email_username_entry=Entry(width=49)
email_username_entry.insert(0,'vv264545@gmail.com')
email_username_entry.grid(column=1,row=2,columnspan=2,pady=10)

password_entry=Entry(width=25)
password_entry.grid(column=1,row=3)

# Buttons

generate_button=Button(text='Generate Password',command=generate_password,width=15)
generate_button.grid(column=2,row=3,pady=5)

add_button=Button(text='Add',width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text='Search',command=find_password,width=18)
search_button.grid(column=2,row=1)


try:
    window.mainloop()
except KeyboardInterrupt:
    print("The program ended gracefully")