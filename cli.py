from tkinter import  *
from socket import *
from functools import partial
from tkinter.messagebox import showerror

import time
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG="!DISCONNECTED"

def create1_window():
    nam=name.get()
    out=open("user3.txt",'w')
    out.write(nam)
    out.close()
    old_window.destroy()



    def initialize_client():
        s = socket(AF_INET, SOCK_STREAM)
        host=ip.get()
        port = 3344

        s.connect((host,port))
        print(f"[Connected] Client connected to server at {host}:{port}")
        return s

    def send():

        global textbox1
        global textbox2
        global textbox3
        global textbox4
        global textbox5
        global textbox6
        global textbox7
        global textbox8
        global textbox9
        global textbox10
        global textbox11
        global textbox12
        global textbox13
        global textbox14
        global textbox15
        global textbox16
        global textbox17
        global textbox18
        global textbox19
        global textbox20
        global textbox21
        global textbox22
        global textbox23
        global textbox24
        global textbox25

        # get the message
        msg1 = textbox1.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg1.encode('ascii'))
        textbox1.delete("0.0", END)
        time.sleep(0.2)

        msg2 = textbox2.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg2.encode('ascii'))
        textbox2.delete("0.0", END)
        time.sleep(0.2)


        msg3 = textbox3.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg3.encode('ascii'))
        textbox3.delete("0.0", END)
        time.sleep(0.2)



        msg6 = textbox6.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg6.encode('ascii'))
        textbox6.delete("0.0", END)
        time.sleep(0.2)


        msg7 = textbox7.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg7.encode('ascii'))
        textbox7.delete("0.0", END)
        time.sleep(0.2)


        msg8 = textbox8.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg8.encode('ascii'))
        textbox8.delete("0.0", END)
        time.sleep(0.2)


        msg10 = textbox10.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg10.encode('ascii'))
        textbox10.delete("0.0", END)
        time.sleep(0.2)


        msg11 = textbox11.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg11.encode('ascii'))
        textbox11.delete("0.0", END)
        time.sleep(0.2)


        msg13 = textbox13.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg13.encode('ascii'))
        textbox13.delete("0.0", END)
        time.sleep(0.2)


        msg14 = textbox14.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg14.encode('ascii'))
        textbox14.delete("0.0", END)
        time.sleep(0.2)


        msg15 = textbox15.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg15.encode('ascii'))
        textbox15.delete("0.0", END)
        time.sleep(0.2)


        msg17 = textbox17.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg17.encode('ascii'))
        textbox17.delete("0.0", END)
        time.sleep(0.2)



        msg19 = textbox19.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg19.encode('ascii'))
        textbox19.delete("0.0", END)
        time.sleep(0.2)


        msg20 = textbox20.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg20.encode('ascii'))
        textbox20.delete("0.0", END)
        time.sleep(0.2)


        msg22 = textbox22.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg22.encode('ascii'))
        textbox22.delete("0.0", END)
        time.sleep(0.2)


        msg23 = textbox23.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg23.encode('ascii'))
        textbox23.delete("0.0", END)
        time.sleep(0.2)


        msg24 = textbox24.get("0.0", END)
        # update_chat(msg1,0)
        s.send(msg24.encode('ascii'))
        textbox24.delete("0.0", END)
        time.sleep(0.2)


    def gui():
        global textbox1
        global textbox2
        global textbox3
        global textbox4
        global textbox5
        global textbox6
        global textbox7
        global textbox8
        global textbox9
        global textbox10
        global textbox11
        global textbox12
        global textbox13
        global textbox14
        global textbox15
        global textbox16
        global textbox17
        global textbox18
        global textbox19
        global textbox20
        global textbox21
        global textbox22
        global textbox23
        global textbox24
        global textbox25

        gui = Tk()
        gui.title("Server")
        gui.configure(bg='#9CD8E2')
        widt_value = gui.winfo_screenwidth()
        heigh_value = gui.winfo_screenheight()
        gui.geometry("%dx%d+0+0" % (widt_value, heigh_value))
        gui.config(bg='yellow')

        img = PhotoImage(file="newwall.png")
        label = Label(
            gui,
            image=img
        )
        label.place(x=0, y=0)

        label0 = Label(gui, text='Incomes Before Taxes                               ')
        label1 = Label(gui, text='Salary & Earned Income')
        label2 = Label(gui, text='Other Income')
        label3 = Label(gui, text='Income Tax Rate(in %)')
        label4 = Label(gui, text=' Expenses')
        label5 = Label(gui, text='Housing & Utilities')
        label6 = Label(gui, text='Rental')
        label7 = Label(gui, text='Home Maintenance(repair,cleaning...)')
        label8 = Label(gui, text='Utilities(electricity,gas,water,cable...)')
        label9 = Label(gui, text='Transportation')
        label10 = Label(gui, text='Gasoline')
        label11 = Label(gui, text='Other Transportation costs(ticket,t*axi,etc..)')
        label12 = Label(gui, text='Living Expenses')
        label13 = Label(gui, text='Food ')
        label14 = Label(gui, text='Clothing')
        label15 = Label(gui, text='Other ')
        label16 = Label(gui, text='Healthcare')
        label17 = Label(gui, text='Medical Spending ')
        label18 = Label(gui, text='Children & Education ')
        label19 = Label(gui, text='Tution & Supplies ')
        label20 = Label(gui, text='Other Spending ')
        label21 = Label(gui, text='Miscellaneuos Expenses ')
        label22 = Label(gui, text='Entertainment & Tickets')
        label23 = Label(gui, text='Travel & Vacation')
        label24 = Label(gui, text='Other Expenses ')

        textbox1 = Text(gui, bg='white')
        textbox2 = Text(gui, bg='white')
        textbox3 = Text(gui, bg='white')
        textbox4 = Text(gui, bg='white')
        textbox5 = Text(gui, bg='white')
        textbox6 = Text(gui, bg='white')
        textbox7 = Text(gui, bg='white')
        textbox8 = Text(gui, bg='white')
        textbox9 = Text(gui, bg='white')
        textbox10 = Text(gui, bg='white')
        textbox11 = Text(gui, bg='white')
        textbox12 = Text(gui, bg='white')
        textbox13 = Text(gui, bg='white')
        textbox14 = Text(gui, bg='white')
        textbox15 = Text(gui, bg='white')
        textbox16 = Text(gui, bg='white')
        textbox17  = Text(gui, bg='white')
        textbox18 = Text(gui, bg='white')
        textbox19 = Text(gui, bg='white')
        textbox20 = Text(gui, bg='white')
        textbox21 = Text(gui, bg='white')
        textbox22 = Text(gui, bg='white')
        textbox23 = Text(gui, bg='white')
        textbox24 = Text(gui, bg='white')
        textbox25 = Text(gui, bg='white')
        label0.place(x=10, y=10)
        label0.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label1.place(x=40, y=50)
        label1.config(bg='#9CD8E2', fg='black')
        label2.place(x=40, y=80)
        label2.config(bg='#9CD8E2', fg='black')
        label3.place(x=40, y=110)
        label3.config(bg='#9CD8E2', fg='black')
        label4.place(x=10, y=140)
        label4.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label5.place(x=10, y=170)
        label5.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label6.place(x=40, y=200)
        label6.config(bg='#9CD8E2', fg='black')
        label7.place(x=40, y=230)
        label7.config(bg='#9CD8E2', fg='black')
        label8.place(x=40, y=260)
        label8.config(bg='#9CD8E2', fg='black')
        label9.place(x=10, y=290)
        label9.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label10.place(x=40, y=320)
        label10.config(bg='#9CD8E2', fg='black')
        label11.place(x=40, y=350)
        label11.config(bg='#9CD8E2', fg='black')
        label12.place(x=10, y=380)
        label12.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label13.place(x=40, y=410)
        label13.config(bg='#9CD8E2', fg='black')
        label14.place(x=40, y=440)
        label14.config(bg='#9CD8E2', fg='black')
        label15.place(x=40, y=470)
        label15.config(bg='#9CD8E2', fg='black')
        label16.place(x=10, y=500)
        label16.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label17.place(x=40, y=530)
        label17.config(bg='#9CD8E2', fg='black')
        label18.place(x=10, y=560)
        label18.config(bg='#9CD8E2', fg='black',font=('Georgia', 12))
        label19.place(x=40, y=590)
        label19.config(bg='#9CD8E2', fg='black')
        label20.place(x=40, y=620)
        label20.config(bg='#9CD8E2', fg='black')
        label21.place(x=10, y=650)
        label21.config(bg='#7FCEDB', fg='black',font=('Georgia', 12))
        label22.place(x=40, y=680)
        label22.config(bg='#7FCEDB', fg='black')
        label23.place(x=40, y=710)
        label23.config(bg='#7FCEDB', fg='black')
        label24.place(x=40, y=740)
        label24.config(bg='#7FCEDB', fg='black')
        textbox1.place(x=300, y=50, height=20, width=265)
        textbox2.place(x=300, y=80, height=20, width=265)
        textbox3.place(x=300, y=110, height=20, width=265)
        textbox6.place(x=300, y=200, height=20, width=265)
        textbox7.place(x=300, y=230, height=20, width=265)
        textbox8.place(x=300, y=260, height=20, width=265)
        textbox10.place(x=300, y=320, height=20, width=265)
        textbox11.place(x=300, y=350, height=20, width=265)
        textbox13.place(x=300, y=410, height=20, width=265)
        textbox14.place(x=300, y=440, height=20, width=265)
        textbox15.place(x=300, y=470, height=20, width=265)
        textbox17.place(x=300, y=530, height=20, width=265)
        textbox19.place(x=300, y=590, height=20, width=265)
        textbox20.place(x=300, y=620, height=20, width=265)
        textbox22.place(x=300, y=680, height=20, width=265)
        textbox23.place(x=300, y=710, height=20, width=265)
        textbox24.place(x=300, y=740, height=20, width=265)
        sendButton = Button(gui, bg='orange', fg='red', text='SUBMIT', command=send)
        sendButton.place(x=215, y=770, height=20, width=50)

        gui.mainloop()

    if __name__ == '__main__':
        chatlog = textbox1 = None
        textbox1 = None
        textbox2 = None
        textbox3 = None
        textbox4 = None
        textbox5 = None
        textbox6 = None
        textbox7 = None
        textbox8 = None
        textbox9 = None
        textbox10 = None
        textbox11 = None
        textbox12 = None
        textbox13 = None
        textbox14 = None
        textbox15 = None
        textbox16 = None
        textbox17 = None
        textbox18 = None
        textbox19 = None
        textbox20 = None
        textbox21 = None
        textbox22 = None
        textbox23 = None
        textbox24 = None



        s = initialize_client()
        gui()

old_window=Tk()
old_window.title("BUDGET CALCULATOR")
width_value = old_window.winfo_screenwidth()
height_value = old_window.winfo_screenheight()
old_window.geometry("%dx%d+0+0" % (width_value, height_value))
old_window.config(bg='yellow')

img1 = PhotoImage(file="budba.png")
label = Label(
    old_window,
    image=img1
)
label.place(x=0, y=0)



name_label = Label(text="Username", bg="#FFEEDD",font=('Georgia', 16))
name_label.place(x=85, y=500,height=30,width=100)
ip_label = Label(text="IP Address", bg="#FFEEDD",font=('Georgia', 16))
ip_label.place(x=85, y=550,height=28,width=120)

name = StringVar()
ip = StringVar()


name_entry = Entry(textvariable=name,width="25", font=('Georgia', 12))
ip_entry = Entry(textvariable=ip, width="25", font=('Georgia', 12))


name_entry.place(x=230, y=500)
ip_entry.place(x=230, y=550)
def login():
    uname = name.get()
    uip = ip.get()
    check_counter = 0
    if uname == "":
        warn = "Username can't be empty"
    else:
        check_counter += 1
    if uip == "":
        warn = "IP address can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uip=="127.0.0.1"):
            create1_window()

        else:
           showerror('Login Status', 'invalid Email')
    else:
          showerror('', warn)

Button(old_window, text="CREATE A BUDGET", bg='white', fg='black', height=3, width=16, font=('Georgia', 14),command=login).place(x=150, y=600)
old_window.mainloop()
