import os,sys
import time,webbrowser
from datetime import datetime as dt
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import askyesno, showerror, showinfo
#--------------------------------------------------------------
options={'restart':'/r','shutdown':'/s'}
days=["Sat","Sun","Mon","Tue","Wed","Thu","Fri"]
#--------------------------------------------------------------
class app:
    def __init__(self,opt,day):
        self.option=opt
        self.days=day
        self.root=Tk()
        self.root.geometry('400x100')
        self.root.maxsize(400,100)
        self.root.minsize(400,100)
        self.root.title('Timer')
        self.label1=Label(text="Hour:",fg="blue")
        self.label2=Label(text="Min:",fg="red")
        self.label3=Label(text="Sec:",fg="green")
        self.label4=Label(text="Mode",fg="orange")
        self.label5=Label(text="day",fg="purple")
        self.spin1=Spinbox(from_=0,to=23,state='readonly')
        self.spin2=Spinbox(from_=0,to=59,state='readonly')
        self.spin3=Spinbox(from_=0,to=59,state='readonly')
        self.text=StringVar()
        self.text2=StringVar()
        self.mode=Combobox(textvariable=self.text,values=[i for i in self.option],state='readonly')
        self.day=Combobox(textvariable=self.text2,values=self.days,state='readonly')
        self.day.bind("<<ComboboxSelected>>",self.show_message2)
        self.mode.bind('<<ComboboxSelected>>',self.show_message)
        self.button_1=Button(text="Start",fg='brown',command=self.start_event)
        self.button_2=Button(text="Quit",bg='light yellow',command=self.quit_process)
        self.button_3=Button(text="More",fg="blue",command=self.open_git)
        #--------------------------------------------------------------
        self.label1.place(x=0,y=0)
        self.spin1.place(x=40,y=0)
        self.label2.place(x=0,y=30)
        self.spin2.place(x=40,y=30)
        self.label3.place(x=0,y=60)
        self.spin3.place(x=40,y=60)
        self.label4.place(x=180,y=0)
        self.mode.place(x=220,y=0)
        self.label5.place(x=180,y=30)
        self.day.place(x=220,y=30)
        self.button_1.place(x=200,y=57)
        self.button_2.place(x=260,y=57)
        self.button_3.place(x=320,y=57)
        self.root.mainloop()
#--------------------------------------------------------------

    def show_message(self,event):
        text_msg="you selected "+self.mode.get()+" mode"
        showinfo(title="Choice",message=text_msg)
    def show_message2(self,event):
        text_msg="you selected "+self.day.get()
        showinfo(title="Choice",message=text_msg)
    def start_event(self):
        if askyesno("Sure?","Do you agree with starting?"):
            if self.mode.get()=="" or self.day.get()=="":
                showerror("Error","Missing Value for initialize")
            else:
                self.process()
        else:
            pass

    def quit_process(self):
        a=askyesno("Are you sure?","Are you sure about quit?")
        if a:
            sys.exit()
        else:
            pass
    def process(self):
        day_now=dt.now().strftime("%A")
        real_time=time.strftime("%H:%M:%S")
        if int(self.spin1.get())<10:
            h="0"+self.spin1.get()
        else:
            h=self.spin1.get()
        if int(self.spin2.get())<10:
            m="0"+self.spin2.get()
        else:
            m=self.spin2.get()
        if int(self.spin3.get())<10:
            s="0"+self.spin3.get()
        else:
            s=self.spin3.get()
        
        given_time=h+":"+m+":"+s

        if real_time==given_time and self.day.get()==day_now[0:3]:
            os.system(f"shutdown {self.option[self.mode.get()]} /t 1")
        else:
            self.root.after(1000,self.process)
    def open_git(self):
        webbrowser.open_new_tab("github.com/kourosh47")


app1=app(options,days)
