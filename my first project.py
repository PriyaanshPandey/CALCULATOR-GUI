
#basics
from tkinter import *
a=Tk()
import tkinter.messagebox as tm
a.geometry('350x450')
a.minsize(width=350,height=450)
a.maxsize(width=350,height=450)
a.title('                    --MY CALCULATOR--')
def click(event):
    text=event.widget.cget('text')
    if text=='=':
        try:
           enterva.set(eval(enterva.get()))
        except Exception as e:
            print(e)
            enterva.set('ERROR!!')
            tm.showinfo('!!ERROR!!','Its an error press C to start over')
        
    elif text=='C':
        enterva.set('')
        
    else:
        enterva.set(enterva.get()+text)
        
#entry
enterva= StringVar()
enterva.set('')
entryvaenter=Entry(a,textvariable=enterva,font=('Times',30))
entryvaenter.pack(side='top',padx=10,pady=10)
#frames and buttons
f1=Frame(a,bg='grey')
f1.pack()
b9=Button(f1,text='9',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b9.pack(side='left',padx=5,pady=5)
b9.bind("<Button-1>",click)
b8=Button(f1,text='8',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b8.pack(side='left', padx=5,pady=5)
b8.bind("<Button-1>",click)
b7=Button(f1,text='7',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b7.pack(side='left', padx=5,pady=5)
b7.bind("<Button-1>",click)
b0=Button(f1,text='0',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b0.pack(side='left',padx=5,pady=5)
b0.bind("<Button-1>",click)

f2=Frame(a,bg='grey')
f2.pack()
b6=Button(f2,text='6',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b6.pack(side='left',padx=5,pady=5)
b6.bind("<Button-1>",click)
b5=Button(f2,text='5',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b5.pack(side='left', padx=5,pady=5)
b5.bind("<Button-1>",click)
b4=Button(f2,text='4',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b4.pack(side='left', padx=5,pady=5)
b4.bind("<Button-1>",click)
bc=Button(f2,text='C',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
bc.pack(side='left',padx=5,pady=5)
bc.bind("<Button-1>",click)

f3=Frame(a,bg='grey')
f3.pack()
b3=Button(f3,text='3',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b3.pack(side='left',padx=7,pady=5)
b3.bind("<Button-1>",click)
b2=Button(f3,text='2',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b2.pack(side='left', padx=7,pady=5)
b2.bind("<Button-1>",click)
b1=Button(f3,text='1',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
b1.pack(side='left', padx=7,pady=5)
b1.bind("<Button-1>",click)
bsubtr=Button(f3,text='-',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
bsubtr.pack(side='left',padx=5,pady=5)
bsubtr.bind("<Button-1>",click)


f4=Frame(a,bg='grey')
f4.pack()
badd=Button(f4,text='+',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
badd.pack(side='left',padx=7,pady=5)
badd.bind("<Button-1>",click)
bmu=Button(f4,text='*',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
bmu.pack(side='left', padx=7,pady=5)
bmu.bind("<Button-1>",click)
bdiv=Button(f4,text='/',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
bdiv.pack(side='left', padx=7,pady=5)
bdiv.bind("<Button-1>",click)
beq=Button(f4,text='=',font=('comicsans',30),bg='black',fg='white',borderwidth=5,relief=RAISED)
beq.pack(side='left',padx=5,pady=5)
beq.bind("<Button-1>",click)





a.mainloop()
