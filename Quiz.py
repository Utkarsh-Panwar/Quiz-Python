# -*- coding: utf-8 -*-
import threading
import time
from tkinter import *

root = Tk()
frame=Frame(root)

h=IntVar()
m=IntVar()
s=IntVar()
totalvar=IntVar()

question =[
    
     " Q. Who is the inventor of Java ?",
     " Q. who is the inventor of Python ?",
     " Q. Which of the following is used for Android Development?",
     " Q. What is the capital of USA ?",
     " Q. Who is the Prime Minister of India ?"
     
     ]
    
option=[
        
     "a. James gosling",
     "b. Brendan Eich",
     "c. Donald Chamberlin",
     "d. Chris Lattener",
     
     "a. Tim David",    
     "b. Bjarne Stroustrup",
     "c. Guido Van Rossum",
     "d. Anders Hejlsberg",
     
     "a. C#",
     "b. Ruby",
     "c. Swift",
     "d. Kotlin",
     
     "a. Denver",
     "b. Cleveland",
     "c. New York",
     "d. Washington D.C",
     
     "a. Rahul Gandhi",
     "b. Narendra Modi",
     "c. Manmohan Singh",
     "d. Arvind Kejriwal"]
    
ans=[0,2,3,3,1]

timevar=StringVar()
timevar.set("Total time is 5 minutes")
timelabel=Label(frame,textvariable=timevar,bg="Black",
                font=("Consolas", 16,'bold'),fg="orange").grid(row=0,sticky=W)

var=StringVar()
var.set("Time Passed : ")
timelabel2=Label(frame,textvariable=var,bg="Black",
                 font=("Consolas", 16,'bold'),fg="Orange").grid(row = 0,column=1,padx=100)

qvar=StringVar()
qabel=Label(frame,text="",textvariable=qvar,bg="Orange",
            font=("Consolas", 16,'bold'),fg="Black").grid(row = 1, sticky=W,pady=40)

selected = IntVar()
optvar=IntVar()

r1=StringVar()
rad1 = Radiobutton(frame,text='',textvariable=r1, value=0, 
                   variable=selected,bg="Black",fg="orange",font=("Consolas", 16,'bold')).grid(
                       row = 2, sticky=W,pady=10)
r2=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r2 ,value=1, 
                   variable=selected,bg="orange",fg="Black",font=("Consolas", 16,'bold')).grid(
                       row = 3, sticky=W,pady=10)
r3=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r3, value=2,
                   variable=selected,bg="Black",fg="orange",font=("Consolas", 16,'bold')).grid(
                       row = 4, sticky=W,pady=10)
r4=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r4, value=3, 
                   variable=selected,bg="orange",fg="Black",font=("Consolas", 16,'bold')).grid(
                       row = 5, sticky=W,pady=10)

frame.pack(side=LEFT)

def exam_start(seconds):
     
     for x in range(300):
         time.sleep(seconds)
         s.set(s.get()+1)
         qvar.set(question[m.get()])
         r1.set(option[optvar.get()])
         r2.set(option[optvar.get()+1])
         r3.set(option[optvar.get()+2])
         r4.set(option[optvar.get()+3])
         if(s.get()==59):
             if(ans[m.get()]==selected.get()):
                 totalvar.set(totalvar.get()+10)
             m.set(m.get()+1)
             optvar.set(optvar.get()+4)
             s.set(0)
             
                 
         if(m.get()==5):
            a=(totalvar.get()/50)*100
            timevar.set("You get "+str(a)+" % marks")
             
         var.set("Time Passed : "+str(h.get())+" : "+str(m.get())+" : "+str(s.get()))
         
         
my_thread = threading.Thread(target=exam_start, args=(1,))
my_thread.start()

root.geometry("800x600")
frame.configure(bg="#ffffcc")
root.configure (bg="#ffffcc")
root.title("Quiz Contest")


root.mainloop()

