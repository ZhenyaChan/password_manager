from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

DEFAULT_USERNAME = "zanechan@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="", message="Oops", detail="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="", message=f"{website}",
                                       detail=f"These are the details entered: \nEmail: {username}"
                                              f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as secret_file:
                    # reading json data from file
                    data = json.load(secret_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as secret_file:
                    json.dump(new_data, secret_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", mode="w") as secret_file:
                    # saving updated data
                    json.dump(data, secret_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH CREDENTIALS ------------------------------- #


def search_credentials():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="", message="Oops", detail="Please make sure you haven't left website field empty.")
    else:
        try:
            with open("data.json", mode="r") as secret_file:
                credentials_dict = json.load(secret_file)
        except FileNotFoundError:
            messagebox.showinfo(title="", message="Error", detail="No Data File Found.")
        else:
            if website in credentials_dict:
                username = credentials_dict[website]["email"]
                password = credentials_dict[website]["password"]
                detail = f"Email: {username}\nPassword: {password}"
            else:
                detail = "No details for the website exists."

            messagebox.showinfo(title="", message=website, detail=detail)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 99, image=img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:", font=("Courier", 14, "bold"))
web_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Courier", 14, "bold"))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Courier", 14, "bold"))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, DEFAULT_USERNAME)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=search_credentials)
search_button.grid(column=2, row=1)

window.mainloop()
