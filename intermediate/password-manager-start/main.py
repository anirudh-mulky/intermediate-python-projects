from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for item in range(nr_letters)]
    pass_symbols = [random.choice(symbols for item in range(nr_symbols))]
    pass_numbers = [random.choice(numbers) for item in range(nr_numbers)]
    final = pass_letters+pass_numbers+pass_symbols

    random.shuffle(final)

    password = "".join(final)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",message=f"Do you want to save?")

        if is_ok:
            messagebox.showinfo(message="Your data is saved")
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pass Last")
window.config(padx=50,pady=20)




canvas = Canvas(width=600,height=400)
lockimage = PhotoImage(file="/Users/anirudhmulky/Desktop/python/password-manager-start/lock.png")
canvas.create_image(300,120,image = lockimage)
canvas.grid(row=0,column=2)

website_label = Label(text="Website:")
website_label.place(x=55,y=270)

email_label = Label(text="Email/Username:")
email_label.place(x=30,y=300)

password_label = Label(text="Password:")
password_label.place(x=50,y=330)

website_entry = Entry(width=35)
website_entry.place(x=150,y=270)
website_entry.focus()#to set the cursor

email_entry = Entry(width=35)
email_entry.place(x=150,y=300)

password_entry = Entry(width=21)
password_entry.place(x=150,y=330)

generate_button = Button(text="Generate Password",width=11,command=gen)
generate_button.place(x=350,y=328)

add_button = Button(text="Add",width=18,command=save)
add_button.place(x=151,y=360)

window.mainloop()