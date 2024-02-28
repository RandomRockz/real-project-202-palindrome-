import socket
from threading import Thread
import random
from tkinter import *
quiz=["What is 30/6 equal to?", " What was the first supercontinent called?", "When was Georeg Washington born?","Who won Super Bowl LVIII?"]
answers=[5,"pangaea","2/22/1732","kansas city chiefs"]
nickname=input("choose your nickname - ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
client.connect((ip_address,port))
print("Connected :)")


class Gui:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.userLabel=Label(self.login, text="Login", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
        self.userLabel.place(relx=0.2,rely=0.07)
        self.username=Entry(self.login, text="", bd=2, width=22)
        self.username.place(relx=0.3, rely=0.07)
        self.button=Button(self.login, text="CONTINUE",font="Helvetica 14 bold", command=lambda:self.goAhead(self.username.get()))
        self.button.place(relx=0.25,rely=0.5)
        self.Window.mainloop()
    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv = Thread(target=self.recv)
        rcv.start()
    def recv ():
        while True:
            try:
                message=client.recv(2048).decode("utf-8")
                if message=="NICKNAME":
                    client.send(nickname.encode("utf-8"))
                else:
                    print(message)
            except:
                print("Error Occured :(")
                client.close()
            break


g=Gui()
def write_function ():
    while True:
        message='{},{}'.format(nickname,input(""))
        client.send(message.encode("utf-8"))
#receive_thread=Thread(target=recv)
#receive_thread.start()
write_thread=Thread(target=write_function)
write_thread.start()
random_num = random.randint(0,len(quiz))
print(quiz[random_num])
user_answer=input()
if user_answer==answers[random_num]:
    print("Correct")
else:
    print("Wrong")
quiz.remove(quiz[random_num])
answers.remove(answers[random_num])