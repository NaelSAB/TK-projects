from tkinter import *
from tkinter import messagebox
import random
from typing import final

import pyperclip
import json

from Tools.scripts.mailerdaemon import emparse_list

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_data = data[website]
            messagebox.showinfo(title=website, message=f"Email/Username: {search_data['email']}\nPassword: {search_data['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for the {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    account = entry_account.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": account,
            "password": password
        }
    }

    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(title="missing field", message="please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Those are the details entered: \nEmail/Username: {account}"
                               f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                entry_website.delete(0, END)
                entry_account.delete(0, END)
                entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50)

#images
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(column= 1, row= 0)

# Labels:
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_account = Label(text="Email/Username:")
label_account.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

#Entrys:
entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()
entry_account = Entry(width=35)
entry_account.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

#Buttons:
button_generate_password = Button(text="Search", command=search)
button_generate_password.grid(column=2, row=1, sticky="EW")
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3, sticky="EW")

button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()