#-----------------------------Importing Libraries--------------------------

from tkinter import *
import random, string
import pyperclip

#-----------------------------initialize window----------------------------

root =Tk()
root.geometry("1000x500")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.config(bg="cornsilk3")

#----------------------------------Heading----------------------------------

heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 20 bold',bg='yellow').pack()
Label(root, text ='made by JATIN KUMAR', font ='arial 15 bold',bg='skyblue').pack(side = BOTTOM)


#----------------------------Select password length---------------------------

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 12 bold',bg='lightgreen').pack(pady=15)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 25 , textvariable = pass_len ,font='bold', width = 10, bg='pink').pack(pady=1)



#------------------------------Define function---------------------------------

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)



#--------------------------------Button------------------------------------------

Button(root, text = "GENERATE PASSWORD" , command = Generator, bg="lightgreen" ).pack(pady=15)

Entry(root , textvariable = pass_str ,width=40,bg='pink').pack(pady=5)

#---------------------------Function to copy-------------------------------------

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD',bg='grey' ,command = Copy_password).pack(pady=5)

#-----------------------Loop to run program--------------------------------------

root.mainloop()