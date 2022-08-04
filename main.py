import json
import tkinter
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle

WHITESMOKE = 'whitesmoke'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '_']

    password_list = []

    [password_list.append(choice(letters)) for letter in range(randint(8, 10))]

    [password_list.append(choice(numbers)) for number in range(randint(2, 4))]

    [password_list.append(choice(symbols)) for symbol in range(randint(2, 4))]

    shuffle(password_list)

    # Turn items in password_list into a single string with .join()
    password = ''.join(password_list)
    # Populate the password entry field with the newly generated password
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()
    new_data = {website_info: {
        'email': email_info,
        'password': password_info
    }}

    if len(website_info) == 0 or len(email_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title='Error', message='Please enter information into all fields')
    else:
        try:
            with open('password.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('password.json', 'w') as file:
                json.dump(new_data, file, indent=4)
                file.close()
                messagebox.showinfo(title='Success', message='Password successfully saved to file!')
        else:
            # Updating old data with new data
            data.update(new_data)
            # Write updated data to file
            with open('password.json', 'w') as file:
                json.dump(data, file, indent=4)
                file.close()
                messagebox.showinfo(title='Success', message='File successfully updated! New info saved.')
    clear_inputs()


def clear_inputs():
    website_input.delete(0, tkinter.END)
    email_input.delete(0, tkinter.END)
    password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('MyPass - Password Manager')
window.config(padx=50, pady=50, bg=WHITESMOKE)

canvas = tkinter.Canvas(width=200, height=200, bg=WHITESMOKE, highlightthickness=0)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text='Website: ')
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text='Email/Username: ')
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password: ')
password_label.grid(column=0, row=3)

website_input = tkinter.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

generate_password_button = tkinter.Button(text='Generate Password', bg='light blue', command=generate_password)
generate_password_button.grid(column=2, row=3)

save_password_button = tkinter.Button(text='Save Password', bg='light green', command=add_password)
save_password_button.grid(column=1, row=4)

window.mainloop()
