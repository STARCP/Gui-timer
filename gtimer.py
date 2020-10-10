from tkinter import *
import time
from tkinter import messagebox

def showinfo():
    messagebox.showinfo("author","starcp \n r170249 \n rgukt")

def showversion():
    messagebox.showinfo("version","version 1.0")



class Timer():
    def __init__(self):
        self.win=Tk()
        self.win.geometry("500x400")
        self.win.resizable(False,False)
        self.win.title("STAR-TIMER")
        self.menu()
         
        self.hr=StringVar()
        self.mn=StringVar()
        self.ss=StringVar()
        self.is_paused=False

        self.hr.set("00")
        self.mn.set("00")
        self.ss.set("00")



        self.label=Label(self.win,font=("consolas",10),text="housr:")
        self.label.grid(row=0,column=0,padx=(5,5))
        self.h=Entry(self.win,width=5,textvariable=self.hr).grid(row=0,column=1,padx=(0,5))
        self.label1=Label(self.win,font=("consolas",10),text="minutes:")
        self.label1.grid(row=0,column=2,padx=(5,5))
        self.m=Entry(self.win,width=5,textvariable=self.mn).grid(row=0,column=3,padx=(0,5))
        self.label2=Label(self.win,font=("consolas",10),text="seconds:")
        self.label2.grid(row=0,column=4,padx=(0,5))
        self.s=Entry(self.win,width=5,textvariable=self.ss).grid(row=0,column=5)
        self.label3=Label(self.win,text="hello world",font=("consolas",40))
        self.label3.grid(row=1,columnspan=8,pady=(90,10))
        self.btn=Button(self.win,text="Start countdown",command=self.start)
        self.btn.grid(row=0,column=6)

        self.win.bind("<space>",self.start)
        self.btn.bind("<Button-1>",self.start)
        #self.btn.bind("<Enter>",self.start)
        self.win.bind("<Control-c>",self.set)


        self.win.mainloop()


    def menu(self):
        menubar=Menu(self.win)
        file=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="ABOUT",menu=file)
        file.add_command(label="version",command=showversion)
        file.add_command(label="author",command=showinfo)
        help=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="HELP",menu=help)
        help.add_command(label="ctrl+x    pause/play")
        help.add_command(label="space start countdown")






        self.win.config(menu=menubar)



    def start(self,event):
        #self.label.config(text="hello world")
        
        hor=int(self.hr.get())
        mor=int(self.mn.get())
        sor=int(self.ss.get())
        a=str(hor).zfill(2)+":"+str(mor).zfill(2)+":"+str(sor).zfill(2)
        self.label3.config(text=a)
        while(True):
            #print(self.is_paused)
            if not self.is_paused:

                time.sleep(1)
                if(sor<0):
                    sor=59
                    mor=mor-1
                if(mor<0):
                    mor=59
                    hor=hor-1

                if(hor<0):
                    self.label3.config(text="countdown finished",font=("times",30))
                    return;
                a=str(hor).zfill(2)+":"+str(mor).zfill(2)+":"+str(sor).zfill(2)
                self.label3.config(text=a,font=("consolas",40))
                self.win.update()
                sor=sor-1
            else:
                self.win.update()


    def set(self,event):
        if not self.is_paused:
            self.is_paused=True
            self.win.update()
        else:
            self.is_paused=False

            self.win.update()
















if(__name__=="__main__"):
	a=Timer()
