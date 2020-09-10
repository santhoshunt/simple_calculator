from tkinter import *
from keyboard import *

window=Tk()
window.title("calculator")

e=Entry(window,width=50,borderwidth=7)
e.grid(row=0,column=0,columnspan=4,padx=15,pady=20)
def add():
    e.insert(END,'+')
    return 

def equal():
    val=e.get()
    e.delete(0,END)
    e.insert(0,eval(val))
    return

def click(n):
    e.insert(END,str(n))
    return

def mul():
    e.insert(END,"*")
    return

def div():
    e.insert(END,"/")
    return

def sub():
    e.insert(END,'-')
    return
    
def clear():
    e.delete(0,END)
    return
    
def mod():
    e.insert(END,"%")
    return

def sq():
    e.insert(END,"**")
    return

def rt():
    e.insert(END,"**0.5")
    return
    
def op():
    e.insert(END,"(")
    return

def cl():
    e.insert(END,")")
    return

def dele():
    l=len(e.get())-1
    e.delete(l,END)
    return


#define button
bt1=Button(window,text="1",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(1))
bt2=Button(window,text="2",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(2))
bt3=Button(window,text="3",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(3))
bt4=Button(window,text="4",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(4))
bt5=Button(window,text="5",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(5))
bt6=Button(window,text="6",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(6))
bt7=Button(window,text="7",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(7))
bt8=Button(window,text="8",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(8))
bt9=Button(window,text="9",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(9))
bt10=Button(window,text="0",padx=40,pady=20,bg="#C0C0C0",command=lambda : click(0))
btadd=Button(window,text="+",padx=40,pady=20,bg="#808080",command=add)
bteq=Button(window,text="=",padx=86,pady=20,bg="#808080",command=equal)
btclr=Button(window,text="Clear",padx=77,pady=20,bg="#808080",command=lambda : clear())
btdele=Button(window,text="DEL",padx=33,pady=20,bg="#808080",command=dele)
btdiv=Button(window,text="/",padx=40,pady=20,bg="#808080",command=div)
btmul=Button(window,text="x",padx=40,pady=20,bg="#808080",command=mul)
btmod=Button(window,text="%",padx=19,pady=20,bg="#808080",command=mod)
btsq=Button(window,text="^",padx=20,pady=20,bg="#808080",command=sq)
btrt=Button(window,text="^0.5",padx=13,pady=20,bg="#808080",command=rt)
btop=Button(window,text="(",padx=22,pady=20,bg="#808080",command=op)
btcl=Button(window,text=")",padx=22,pady=20,bg="#808080",command=cl)
btext=Button(window,text="EXIT",padx=13,pady=20,bg="yellow",fg="black",command=lambda : exit())

on_press_key('1',lambda a: click(1))
on_press_key('2',lambda a: click(2))
on_press_key('3',lambda a: click(3))
on_press_key('4',lambda a: click(4))
on_press_key('5',lambda a: click(5))
on_press_key('6',lambda a: click(6))
on_press_key('7',lambda a: click(7))
on_press_key('8',lambda a: click(8))
on_press_key('9',lambda a: click(9))
on_press_key('0',lambda a: click(0))
on_press_key('+',lambda a: click('+'))
on_press_key('/',lambda a: click('/'))
on_press_key('-',lambda a: click('-'))
on_press_key('x',lambda a: click('*'))
#put bt on screen
btext.grid(row=6,column=3)
btmod.grid(row=1,column=3)
btsq.grid(row=3,column=3)
btrt.grid(row=5,column=3)
btmul.grid(row=6,column=0)
btdiv.grid(row=6,column=1)
btdele.grid(row=6,column=2)
btclr.grid(row=4,column=1,columnspan=2)
btadd.grid(row=5,column=0)
bteq.grid(row=5,column=1,columnspan=2)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)
bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)
bt7.grid(row=3,column=0)
bt8.grid(row=3,column=1)
bt9.grid(row=3,column=2)
bt10.grid(row=4,column=0)
btop.grid(row=2,column=3)
btcl.grid(row=4,column=3)



window.mainloop()
