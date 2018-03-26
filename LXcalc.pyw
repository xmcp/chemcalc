#coding=utf-8
from tkinter import *
from tkinter.ttk import *
import chemcalc

tk=Tk()
tk.title('LiangXin™ Calculator by @xmcp')
tk.resizable(False,False)

var=StringVar()
result=StringVar(value='ChemCalc Powered')
tips=StringVar(value='https://github.com/xmcp/chemcalc')

NORMAL='#000000'
GRAY='#999999'

def calc(save_res):
    try:
        res=chemcalc.parser.parse(var.get())
    except Exception as e:
        tips.set(str(e))
        outp['foreground']=GRAY
    else:
        result.set(('%.5f'%res).rstrip('0'))
        outp['foreground']=NORMAL
        tips.set('→ %s'%res)
        if save_res:
            chemcalc.global_last=res

def keypress(e):
    tk.after(1,lambda:calc(e.keysym=='Return'))
        
inp=Entry(tk,textvariable=var,width=40,font='Consolas -22')
inp.grid(row=0,column=0,pady=10,padx=20)
inp.bind('<KeyPress>',keypress)
inp.focus_force()

outp=Label(tk,textvariable=result,font='Consolas -24',foreground=NORMAL)
outp.grid(row=1,column=0)

outs=Label(tk,textvariable=tips,font='Consolas -14')
outs.grid(row=2,column=0,pady=10)

mainloop()
