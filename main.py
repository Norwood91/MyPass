import tkinter

WHITESMOKE = 'whitesmoke'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Create txt file
# file = open('password.txt', 'w')
def add_password():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()

    file = open('password.txt', 'a')
    file.write(f'Website: {website_info} | Email: {email_info} | Password: {password_info}')
    file.close()


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

generate_password_button = tkinter.Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

save_password_button = tkinter.Button(text='Save Password', bg='light green', command=add_password)
save_password_button.grid(column=1, row=4)

window.mainloop()
