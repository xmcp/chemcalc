#coding=utf-8
from tkinter import *
from tkinter.ttk import *
from chemcalc import parser

tk=Tk()
tk.title('LiangXin™ Calculator by @xmcp')
tk.resizable(False,False)

var=StringVar()
result=StringVar(value='ChemCalc Powered')
tips=StringVar(value='https://github.com/xmcp/chemcalc')

NORMAL='#000000'
GRAY='#999999'

def calc(*_):
    try:
        res=parser.parse(var.get())
    except Exception as e:
        tips.set(str(e))
        outp['foreground']=GRAY
    else:
        result.set(('%.5f'%res).rstrip('0'))
        outp['foreground']=NORMAL
        tips.set('→ %s'%res)

inp=Entry(tk,textvariable=var,width=40,font='Consolas -22')
inp.grid(row=0,column=0,pady=10,padx=20)
inp.bind('<KeyPress>',lambda *_:tk.after(1,calc))
inp.focus_force()

outp=Label(tk,textvariable=result,font='Consolas -26',foreground=NORMAL)
outp.grid(row=1,column=0)

outs=Label(tk,textvariable=tips,font='Consolas -13')
outs.grid(row=2,column=0,pady=10)

mainloop()
