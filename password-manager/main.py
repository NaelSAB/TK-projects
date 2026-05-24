from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(title="missing field", message="please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Those are the details entered: \nEmail/Username: {account}"
                               f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {account} | {password}\n")
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
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()
entry_account = Entry(width=35)
entry_account.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

#Buttons:
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3, sticky="EW")

button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()