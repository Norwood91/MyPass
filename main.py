import tkinter

WHITESMOKE = 'whitesmoke'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('MyPass')
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


email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)


password_input = tkinter.Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)


generate_password_button = tkinter.Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)


add_button = tkinter.Button(text='Save Password', bg='light green')
add_button.grid(column=1, row=4)

window.mainloop()