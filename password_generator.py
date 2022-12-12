import pyperclip, string
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


#initialize global variables
#hard coded email and secrets file location
HC_EMAIL = 'corvus@0xc0rvu5.com'
SECRET_FILE = r'password.txt'
#window relevant
WINDOW = Tk()
#entries
EMAIL_OR_USERNAME_ENTRY = Entry(width=48)
PASSWORD_ENTRY = Entry(width=30)
WEBSITE_ENTRY = Entry(width=48)
#labels
EMAIL_OR_USERNAME = Label(text='Email/Username:')
P_PROMPT = Label(text='Password:')
WEBSITE = Label(text='Website:')
#photo
PHOTO = PhotoImage(file='lock.png')


def generate_password():
    '''Generate a password 18-24 characters long.'''
    letters = [i for i in (string.ascii_lowercase + string.ascii_uppercase)]
    numbers = [str(i) for i in range(10)]
    symbols = [i for i in string.punctuation]

    p_letters = [choice(letters) for _ in range(randint(10, 12))]
    p_symbols = [choice(symbols) for _ in range(randint(4, 6))]
    p_numbers = [choice(numbers) for _ in range(randint(4, 6))]

    password_list = p_letters + p_symbols + p_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    PASSWORD_ENTRY.insert(0, password)
    pyperclip.copy(password)


def save():
    '''Save the website, email and password supplied.'''
    website = WEBSITE_ENTRY.get()
    email = EMAIL_OR_USERNAME_ENTRY.get()
    password = PASSWORD_ENTRY.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='Please enter valid info')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Email: {email}\nPassword: {password}\n       Continue?')

        if is_ok:
            messagebox.showinfo(title='Verification', message='Complete!')
            with open(f'{SECRET_FILE}', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                WEBSITE_ENTRY.delete(0, END)
                PASSWORD_ENTRY.delete(0, END)


#global variable located here because python does not support hoisting
#buttons
ADD = Button(text='Add', width=46, command=save)
GENERATE_PASSWORD = Button(text='Generate Password', width=15, command=generate_password)


#window configurations
WINDOW.title('Password Manager')
WINDOW.config(padx=50, pady=50)
ADD.grid(column=1, row=4, columnspan=36)
EMAIL_OR_USERNAME.grid(column=0, row=2)
GENERATE_PASSWORD.grid(column=2, row=3)
P_PROMPT.grid(column=0, row=3)
WEBSITE.grid(column=0, row=1)
EMAIL_OR_USERNAME_ENTRY.grid(column=1, row=2, columnspan=35)
PASSWORD_ENTRY.grid(column=1, row=3)
WEBSITE_ENTRY.grid(column=1, row=1, columnspan=35)
#focus on website input at start
WEBSITE_ENTRY.focus()
#insert hard-coded email at start
EMAIL_OR_USERNAME_ENTRY.insert(0, f'{HC_EMAIL}')


#canvas at bottom to ensure proper window functionality
CANVAS = Canvas(width=300, height=200)
CANVAS.grid(column=1, row=0, columnspan=200, padx=20)
CANVAS.create_image(100, 100, image=PHOTO)


#necessary for tkinter windows
WINDOW.mainloop()