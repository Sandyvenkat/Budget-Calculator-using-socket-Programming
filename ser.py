import socket
from tkinter import *
from socket import *

import pyscreenshot
import img2pdf
from tkinter.messagebox import showerror

from tkinter import filedialog
import urllib
from urllib.request import urlopen
from tkinter.messagebox import *

from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import base64
import os

import sys
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG="!DISCONNECTED"
import threading


def Download():
    takescreenshot=pyscreenshot.grab(bbox=(300,15, 1800, 1000))
    ScreenshotPath = r'C:\Users\sandy\PycharmProjects\calgui\a3.png'
    takescreenshot.save(ScreenshotPath)
    Img = open(ScreenshotPath, "rb")

    Pdf = open("sample.pdf", "wb")

    Pdf.write(img2pdf.convert(Img))

    Img.close()

    Pdf.close()

def sender():

    def send():
        f=open("user3.txt","r")
        nam=f.readline()
        f.close()
        body = '''Hello'''+nam+'''
        This is your forecast of income and expenditure
        '''
        sender = 'sandymyself07@gmail.com'
        password = 'brpfjertdpffutqc'
        mail = Email.get()
        receiver = mail

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'Analysis of your Income and Expenses'

        message.attach(MIMEText(body, 'plain'))

        pdfname = "sample.pdf"
        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()

        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()

    mailaddress = Tk()
    mailaddress.title("Send to")
    mailaddress.geometry("500x300")


    m = Label(mailaddress, text='Email Address', font=('Georgia', 12))
    m.place(x=60, y=50)

    email = StringVar()
    Email = Entry(mailaddress, textvariable=email, width="25", font=('Georgia', 12))
    Email.place(x=200, y=50)

    Button(mailaddress, text="SEND", bg='white', fg='black', height=2, width=13, font=('Georgia', 14), command=send).place(x=100, y=130)






def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        global chatlog1
        global chatlog2
        global chatlog3
        global chatlog4
        global chatlog5
        global chatlog6
        global chatlog7
        global chatlog8
        global chatlog9
        global chatlog10
        global chatlog11
        global chatlog12
        global chatlog13
        global chatlog14
        global chatlog15
        global chatlog16
        global chatlog17
        global chatlog18
        global chatlog19
        global chatlog20
        global chatlog21
        global chatlog22
        global chatlog23
        global chatlog24

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

        gui = Tk()
        # title for the window
        f = open("user3.txt", "r")
        nam = f.readline()
        f.close()
        gui.title("Client "+str(nam))

        gui.configure(bg='#88CEFA')
        # set size for the window
        """img = PhotoImage(file="back.png")
        label = Label(
            gui,
            image=img
        )
        label.place(x=0, y=0)"""

        width_value = gui.winfo_screenwidth()
        height_value = gui.winfo_screenheight()
        gui.geometry("%dx%d+0+0" % (width_value, height_value))

        # image=PhotoImage(file='C:\\Users\\sandy\\OneDrive\\Documents\\scienceproject\\calci.JPG')

        # text space to display message
        chatlog00 = Text(gui, bg='white')
        chatlog00.config(state=DISABLED)
        chatlog01 = Text(gui, bg='white')
        chatlog01.config(state=DISABLED)

        chatlog1 = Text(gui, bg='white')
        chatlog1.config(state=DISABLED)
        chatlog2 = Text(gui, bg='white')
        chatlog2.config(state=DISABLED)
        chatlog3 = Text(gui, bg='white')
        chatlog3.config(state=DISABLED)
        chatlog4 = Text(gui, bg='white')
        chatlog4.config(state=DISABLED)
        chatlog5 = Text(gui, bg='white')
        chatlog5.config(state=DISABLED)
        chatlog6 = Text(gui, bg='white')
        chatlog6.config(state=DISABLED)
        chatlog7 = Text(gui, bg='white')
        chatlog7.config(state=DISABLED)
        chatlog8 = Text(gui, bg='white')
        chatlog8.config(state=DISABLED)
        chatlog9 = Text(gui, bg='white')
        chatlog9.config(state=DISABLED)
        chatlog10 = Text(gui, bg='white')
        chatlog10.config(state=DISABLED)
        chatlog11 = Text(gui, bg='white')
        chatlog11.config(state=DISABLED)
        chatlog12 = Text(gui, bg='white')
        chatlog12.config(state=DISABLED)
        chatlog13 = Text(gui, bg='white')
        chatlog13.config(state=DISABLED)
        chatlog14 = Text(gui, bg='white')
        chatlog14.config(state=DISABLED)
        chatlog15 = Text(gui, bg='white')
        chatlog15.config(state=DISABLED)
        chatlog16 = Text(gui, bg='white')
        chatlog16.config(state=DISABLED)
        chatlog17 = Text(gui, bg='white')
        chatlog17.config(state=DISABLED)
        chatlog18 = Text(gui, bg='white')
        chatlog18.config(state=DISABLED)
        chatlog19 = Text(gui, bg='white')
        chatlog19.config(state=DISABLED)
        chatlog20 = Text(gui, bg='white')
        chatlog20.config(state=DISABLED)
        chatlog21 = Text(gui, bg='white')
        chatlog21.config(state=DISABLED)
        chatlog22 = Text(gui, bg='white')
        chatlog22.config(state=DISABLED)
        chatlog23 = Text(gui, bg='white')
        chatlog23.config(state=DISABLED)
        chatlog24 = Text(gui, bg='white')
        chatlog24.config(state=DISABLED)
        chatlog24 = Text(gui, bg='white')
        chatlog24.config(state=DISABLED)

        # label=Label(gui,text="Download", bg='orange', fg='red')

        label00 = Label(gui, text='Monthly')
        label00.config(bg='#88CEFA', fg='black', font=('Century', 12))
        label01 = Label(gui, text='Anually')
        label01.config(bg='#88CEFA', fg='black', font=('Century', 12))
        label0 = Label(gui, text='Total Income Before Taxes')
        label0.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label1 = Label(gui, text='Total Income After Taxes')
        label1.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label2 = Label(gui, text='Total Expenses')
        label2.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label3 = Label(gui, text='Net(Defict)')
        label3.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label4 = Label(gui, text=' Expenses')
        label4.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label000 = Label(gui, text='Monthly')
        label000.config(bg='#88CEFA', fg='black', font=('Century', 12))
        label001 = Label(gui, text='Anually')
        label001.config(bg='#88CEFA', fg='black', font=('Century', 12))
        label5 = Label(gui, text='Housing & Utilities')
        label5.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label6 = Label(gui, text='Transportation')
        label6.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label7 = Label(gui, text='Living Expenses')
        label7.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label8 = Label(gui, text='Healthcare')
        label8.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label9 = Label(gui, text='Children & Education')
        label9.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label10 = Label(gui, text='Miscellaneuos Expenses')
        label10.config(bg='#88CEFA', fg='black', font=('Georgia', 12))
        label11 = Label(gui, text="Expenses Breakdown")
        label11.config(bg='#88CEFA', fg='black', font=('Century', 12))

        # sendButton = Button(gui, bg='orange', fg='red', text='SUBMIT')# command=send)
        # textbox1 = Text(gui, bg='white')
        # textbox2 = Text(gui, bg='white')
        # textbox3 = Text(gui, bg='white')

        # label.place(x=240,y=300)
        label00.place(x=810, y=10)
        label01.place(x=970, y=10)
        label0.place(x=500, y=50)
        label1.place(x=500, y=88)
        label2.place(x=500, y=126)
        label3.place(x=500, y=164)
        label4.place(x=500, y=210)
        label000.place(x=810, y=220)
        label001.place(x=970, y=220)
        label5.place(x=500, y=260)
        label6.place(x=500, y=298)
        label7.place(x=500, y=336)
        label8.place(x=500, y=374)
        label9.place(x=500, y=412)
        label10.place(x=500, y=450)
        label11.place(x=650, y=488)
        """"label11.place(x=40, y=350)
        label12.place(x=10, y=380)
        label13.place(x=40, y=410)
        label14.place(x=40, y=440)
        label15.place(x=40, y=470)
        label16.place(x=10, y=500)
        label17.place(x=40, y=530)
        label18.place(x=10, y=560)
        label19.place(x=40, y=590)
        label20.place(x=40, y=620)
        label21.place(x=10, y=650)
        label22.place(x=40, y=680)
        label23.place(x=40, y=710)
        label24.place(x=40, y=740)"""
        # textbox1.place(x=180,y=50,height=20,width=265)
        # textbox2.place(x=180,y=80,height=20,width=265)
        # textbox3.place(x=180,y=110,height=20,width=265)

        # receiveButton = Button(gui, bg='orange', fg='red', text='RECEIVE',command=receive)

        # chatlog00.place(x=180, y=50, height=20, width=265)
        # chatlog01.place(x=180, y=50, height=20, width=265)

        chatlog1.place(x=810, y=50, height=20, width=100)
        chatlog2.place(x=970, y=50, height=20, width=100)
        chatlog3.place(x=810, y=88, height=20, width=100)
        chatlog4.place(x=970, y=88, height=20, width=100)
        chatlog6.place(x=810, y=126, height=20, width=100)
        chatlog7.place(x=970, y=126, height=20, width=100)
        chatlog8.place(x=810, y=164, height=20, width=100)
        chatlog10.place(x=970, y=164, height=20, width=100)
        chatlog11.place(x=810, y=260, height=20, width=100)
        chatlog12.place(x=970, y=260, height=20, width=100)
        chatlog13.place(x=810, y=298, height=20, width=100)
        chatlog14.place(x=970, y=298, height=20, width=100)
        chatlog15.place(x=810, y=336, height=20, width=100)
        chatlog16.place(x=970, y=336, height=20, width=100)
        chatlog17.place(x=810, y=374, height=20, width=100)
        chatlog18.place(x=970, y=374, height=20, width=100)
        chatlog19.place(x=810, y=412, height=20, width=100)
        chatlog20.place(x=970, y=412, height=20, width=100)
        chatlog21.place(x=810, y=450, height=20, width=100)
        chatlog22.place(x=970, y=450, height=20, width=100)
        """chatlog23.place(x=180, y=710, height=20, width=265)
        chatlog24.place(x=180, y=740, height=20, width=265)"""
        # chatlog24.place(x=180, y=770, height=20, width=265)
        # textbox.place(x=6, y=380, height=20, width=265)"""

        # receiveButton.place(x=215, y=790, height=20, width=50)

        # _thread.start_new_thread(receive, ())
        # to keep the window in the loop
        while True:
            msg1 = conn.recv(1024)
            msg1 = msg1.decode('ascii')
            print(msg1)
            msg1 = int(msg1)
            print("1:", msg1)

            msg2 = conn.recv(1024)
            msg2 = msg2.decode('ascii')
            msg2 = msg2.split("\n")
            print(msg2)
            msg2.pop()
            print(msg2)
            msg21 = int(msg2[0])
            print("2:", msg21)
            print("3:", msg2[0])

            msg10 = int(msg1 + msg21)
            msg220 = int(msg10 * 12)

            chatlog1.config(state=NORMAL)
            chatlog1.insert(END, msg10)
            chatlog1.config(state=DISABLED)

            chatlog2.config(state=NORMAL)
            chatlog2.insert(END, msg220)
            chatlog2.config(state=DISABLED)

            '''list0=[]
            list1=[]
            list2=[]

            list0.append(" ")
            list0.append("Total Before Tax Income")
            list0.append("Total After Tax Income")
            list0.append("Net(Defict)")

            list1.append("Monthly")
            list2.append("Annualy")

            list1.append(msg10)
            list2.append(msg20)'''

            msg3 = conn.recv(1024)
            msg3 = msg3.decode('ascii')
            print("error:", msg3)
            # msg33=int(msg2[1])
            # print("4:",msg3)

            msg11 = int(msg10 - (msg10 * int(msg3)) / 100)
            print("MOnth:", msg11)
            msg222 = int(msg11 * 12)
            print("5:", msg222)

            '''list1.append(msg11)
            list2.append(msg22)'''

            chatlog3.config(state=NORMAL)
            chatlog3.insert(END, msg11)
            chatlog3.config(state=DISABLED)

            chatlog4.config(state=NORMAL)
            chatlog4.insert(END, msg222)
            chatlog4.config(state=DISABLED)

            msg6 = conn.recv(1024)
            msg6 = msg6.decode('ascii')
            print("error:", msg6)
            # msg66 = int(msg2[2])
            # print("4:", msg2[2])

            msg7 = conn.recv(1024)
            msg7 = msg7.decode('ascii')
            print("error:", msg7)
            # msg77 = int(msg2[3])
            # print("4:", msg2[3])

            msg8 = conn.recv(1024)
            msg8 = msg8.decode('ascii')
            print("error:", msg8)
            # msg88 = int(msg2[4])
            # print("4:", msg2[4])

            msg13 = conn.recv(1024)
            msg13 = msg13.decode('ascii')
            print("error:", msg13)
            # msg99 = int(msg2[5])
            # print("4:", msg2[5])

            msg14 = conn.recv(1024)
            msg14 = msg14.decode('ascii')
            print("error:", msg14)
            # msg100 = int(msg2[6])
            # print("4:", msg2[6])

            msg15 = conn.recv(1024)
            msg15 = msg15.decode('ascii')
            print("error:", msg15)
            # msg101 = int(msg2[7])
            # print("4:", msg2[7])

            msg17 = conn.recv(1024)
            msg17 = msg17.decode('ascii')
            print("error:", msg17)
            # msg102 = int(msg2[8])
            # print("4:", msg2[8])

            msg19 = conn.recv(1024)
            msg19 = msg19.decode('ascii')
            print("error:", msg19)
            # msg103 = int(msg2[9])
            # print("4:", msg2[9])

            msg20 = conn.recv(1024)
            msg20 = msg20.decode('ascii')
            print("error:", msg20)
            # msg104 = int(msg2[10])
            # print("4:", msg2[10])

            msg22 = conn.recv(1024)
            msg22 = msg22.decode('ascii')
            print("error:", msg22)
            # msg105 = int(msg2[11])
            # print("4:", msg2[11])

            msg23 = conn.recv(1024)
            msg23 = msg23.decode('ascii')
            print("error:", msg23)
            # msg106 = int(msg2[12])
            # print("16:", msg2[12])

            msg24 = conn.recv(1024)
            msg24 = msg24.decode('ascii')
            print("error:", msg24)
            # msg107 = int(msg2[13])
            # print("17:", msg2[13])

            msg25 = conn.recv(1024)
            msg25 = msg25.decode('ascii')
            print("error:", msg25)
            # msg108 = int(msg2[14])
            # print("17:", msg2[14])

            msg26 = conn.recv(1024)
            msg26 = msg26.decode('ascii')
            print("error:", msg26)
            # msg109 = int(msg2[15])
            # print("17:", msg2[15])

            total = int(int(msg6) + int(msg7) + int(msg8) + int(msg13) + int(msg14) + int(msg15) + int(msg17) + int(
                msg19) + int(msg20) + int(msg22) + int(msg23) + int(msg24) + int(msg25) + int(msg26))
            print(total)
            total1 = int(total * 12)
            chatlog6.config(state=NORMAL)
            chatlog6.insert(END, total)
            chatlog6.config(state=DISABLED)

            chatlog7.config(state=NORMAL)
            chatlog7.insert(END, total1)
            chatlog7.config(state=DISABLED)

            netM = msg1 - total
            netA = netM * 12

            list0 = []
            list1 = []
            list2 = []
            list3 = []

            list0.append(' ')
            list0.append('Total Income Before Tax')
            list0.append('Total Income After Tax')
            list0.append('Net(Defict)')

            list1.append('Monthly')
            list1.append(msg10)
            list1.append(msg11)
            list1.append(netM)

            list2.append('Annualy')
            list2.append(msg220)
            list2.append(msg222)
            list2.append(netA)

            chatlog8.config(state=NORMAL)
            chatlog8.insert(END, netM)
            chatlog8.config(state=DISABLED)

            chatlog10.config(state=NORMAL)
            chatlog10.insert(END, netA)
            chatlog10.config(state=DISABLED)

            msg123 = int(int(msg6) + int(msg7) + int(msg8))
            msg234 = int(int(msg13) + int(msg14))
            msg345 = int(int(msg15) + int(msg17) + int(msg19))
            msg456 = int(msg20)
            msg567 = int(int(msg22) + int(msg23))
            msg678 = int(int(msg24) + int(msg25) + int(msg26))

            msg321 = int(msg123 * 12)
            msg432 = int(msg234 * 12)
            msg543 = int(msg345 * 12)
            msg654 = int(msg456 * 12)
            msg765 = int(msg567 * 12)
            msg876 = int(msg678 * 12)

            chatlog11.config(state=NORMAL)
            chatlog11.insert(END, msg123)
            chatlog11.config(state=DISABLED)

            chatlog12.config(state=NORMAL)
            chatlog12.insert(END, msg321)
            chatlog12.config(state=DISABLED)

            chatlog13.config(state=NORMAL)
            chatlog13.insert(END, msg234)
            chatlog13.config(state=DISABLED)

            chatlog14.config(state=NORMAL)
            chatlog14.insert(END, msg432)
            chatlog14.config(state=DISABLED)

            chatlog15.config(state=NORMAL)
            chatlog15.insert(END, msg345)
            chatlog15.config(state=DISABLED)

            chatlog16.config(state=NORMAL)
            chatlog16.insert(END, msg543)
            chatlog16.config(state=DISABLED)

            chatlog17.config(state=NORMAL)
            chatlog17.insert(END, msg456)
            chatlog17.config(state=DISABLED)

            chatlog18.config(state=NORMAL)
            chatlog18.insert(END, msg654)
            chatlog18.config(state=DISABLED)

            chatlog19.config(state=NORMAL)
            chatlog19.insert(END, msg567)
            chatlog19.config(state=DISABLED)

            chatlog20.config(state=NORMAL)
            chatlog20.insert(END, msg765)
            chatlog20.config(state=DISABLED)

            chatlog21.config(state=NORMAL)
            chatlog21.insert(END, msg678)
            chatlog21.config(state=DISABLED)

            chatlog22.config(state=NORMAL)
            chatlog22.insert(END, msg876)
            chatlog22.config(state=DISABLED)

            def prop(n, m):
                return 360.0 * n / m

            den = int(msg123 + msg234 + msg345 + msg456 + msg567 + msg678)

            msg170 = int((msg123 * 100) / den)
            msg171 = int((msg234 * 100) / den)
            msg172 = int((msg345 * 100) / den)
            msg173 = int((msg456 * 100) / den)
            msg174 = int((msg567 * 100) / den)
            msg175 = int((msg678 * 100) / den)
            data = [msg170, msg171, msg172, msg173, msg174, msg175]
            deni = msg170 + msg171 + msg172 + msg173 + msg174 + msg175

            msg701 = int(msg170 + msg171)
            msg7012 = int(msg701 + msg172)
            msg0123 = int(msg7012 + msg173)
            msg01234 = int(msg0123 + msg174)
            c = Canvas(gui, bg='#88CEFA', width=202, height=202)

            c.pack()
            c.place_configure(x=500, y=520)
            c.create_arc((2, 2, 200, 200), fill="red", outline="red", start=prop(0, deni), extent=prop(msg170, deni))
            c.create_arc((2, 2, 200, 200), fill="blue", outline="blue", start=prop(msg170, deni),
                         extent=prop(msg171, deni))
            c.create_arc((2, 2, 200, 200), fill="yellow", outline="yellow", start=prop(msg701, deni),
                         extent=prop(msg172, deni))
            c.create_arc((2, 2, 200, 200), fill="green", outline="green", start=prop(msg7012, deni),
                         extent=prop(msg173, deni))
            c.create_arc((2, 2, 200, 200), fill="DarkOrchid1", outline="DarkOrchid1", start=prop(msg0123, deni),
                         extent=prop(msg174, deni))
            c.create_arc((2, 2, 200, 200), fill="orange", outline="orange", start=prop(msg01234, deni),
                         extent=prop(msg175, deni))
            # c.create_arc((2, 2, 152, 152), fill = 'blue', outline = 'blue', start = prop(0), extent = prop(0))"""

            # = Button(gui,bg='orange',fg='red',text='ShowFlowChart',command=show(amt))
            # showFlowchart.place(x=250,y=480,height=30,width=90)
            c1 = Canvas(gui, bg='#88CEFA', width=220, height=195)
            c1.pack()
            c1.place_configure(x=810, y=520)
            c1.create_rectangle((5, 5, 20, 20), fill='red')
            c1.create_text(90, 9, text="Housing & Utilities")

            c1.create_rectangle((5, 35, 20, 50), fill='blue')
            c1.create_text(80, 39, text="Transportation")

            c1.create_rectangle((5, 65, 20, 80), fill='yellow')
            c1.create_text(80, 69, text="Living Expenses")

            c1.create_rectangle((5, 95, 20, 110), fill='green')
            c1.create_text(70, 99, text="Healthcare")

            c1.create_rectangle((5, 125, 20, 140), fill='DarkOrchid1')
            c1.create_text(100, 129, text="Children & Education")

            c1.create_rectangle((5, 155, 20, 170), fill='orange')
            c1.create_text(116, 159, text="Miscellaneous & Expenses")

            DownloadButton = Button(gui, bg='orange', fg='red', text='Save', command=Download)
            DownloadButton.place(x=600, y=780, height=30, width=60)

            sendButton = Button(gui, bg='orange', fg='red', text='Send', command=sender)
            sendButton.place(x=860, y=780, height=30, width=60)

            gui.mainloop()

    conn.close()
def initialize_server():
    s=socket(AF_INET,SOCK_STREAM)
    host = "localhost"
    port = 3344
    s.bind((host,port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()




if __name__=='__main__':
 conn=initialize_server()


