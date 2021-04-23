# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk


class Falsapos:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Cálculo de raices XD")
        self.window.geometry("1030x570")
        
        self.a=DoubleVar(value=0.0)
        self.b=DoubleVar(value=0.0)
        self.fa=DoubleVar(value=0.0)
        self.fb=DoubleVar(value=0.0)
        self.tol=DoubleVar(value=0.0)
        self.it=IntVar(value=0)
        self.n=DoubleVar()
        self.p=DoubleVar()
        self.aproxv=DoubleVar()
        self.aprox=DoubleVar()
        self.comval=IntVar()
        
        
        self.lbl0=Label(self.window,text='Método de falsa posición')
        self.lbl0.place(x=10, y=10)
        self.lbl1=Label(self.window,text='Ingrese el valor del parámetro a:')
        self.lbl1.place(x=10, y=70)
        self.lbl2=Label(self.window,text='Ingrese el valor del parámetro b:')
        self.lbl2.place(x=10, y=100)
        self.lbl3=Label(self.window,text='Ingrese el numero de iteraciones:')
        self.lbl3.place(x=10, y=130)
        self.lbl4=Label(self.window,text='Método de bisección')
        self.lbl4.place(x=420, y=10)
        self.lbl5=Label(self.window,text='Método de Newton-Raphson')
        self.lbl5.place(x=720, y=10)
        self.lbl6=Label(self.window,text='Ingrese la aproximación:') 
        self.lbl6.place(x=700, y=130)

   
        self.t1=Entry(self.window,textvariable=self.a)
        self.t1.place(x=230, y=70,width='50')
        self.t2=Entry(self.window,textvariable=self.b)
        self.t2.place(x=230, y=100,width='50')
        self.t3=Entry(self.window,textvariable=self.it)
        self.t3.place(x=230, y=130,width='50')
        self.t4=Entry(self.window,textvariable=self.aprox)
        self.t4.place(x=870, y=130,width='50')
        
        
        self.b1=Button(self.window,text='calcular', command=self.calcular)
        self.b1.place(x=10, y=160)
        self.b2=Button(self.window,text='Graficar aproximaciones', command=self.grafic)
        self.b2.place(x=450, y=530)
        self.b3=Button(self.window,text='calcular', command=self.bisection)
        self.b3.place(x=380, y=160)
        self.b4=Button(self.window,text='calcular', command=self.NewtonR)
        self.b4.place(x=700, y=160)
        
    

        self.textA=scrolledtext.ScrolledText(self.window,width=40,height=20)
        self.textA.place(x=10, y=190)
        self.textB=scrolledtext.ScrolledText(self.window,width=40,height=20)
        self.textB.place(x=380, y=190)
        self.textC=scrolledtext.ScrolledText(self.window,width=40,height=20)
        self.textC.place(x=700, y=190)
        
        
        self.combobox1=ttk.Combobox(self.window,textvariable=self.comval,state="readonly")
        self.combobox1.place(x=10,y=40)
        self.combobox1['values']=('e^(-x)-x','x^(3)-2x-5','2x^(3)+3x^(2)-12x-30','x^(3)-x-1','5x^(2)+7x-52')
        self.combobox1.current(0)
        self.window.mainloop()  
        
    def grafic(self):
            comval=int(self.combobox1.current())
            if(comval==0):
                x= np.arange(-100, 100, 0.001)
                y = np.exp(-x)-x
                plt.plot(x,y)
                plt.plot([float(self.n.get())],[0],'go')
                plt.plot([float(self.p.get())],[0],'bo')
                plt.plot([float(self.aproxv.get())],[0],'ro')
                plt.ylim(-float(self.func(float(self.n.get()),comval))-5,float(self.func(self.n.get(),comval))+5)
                plt.xlim((-0.5)*float(self.n.get()),(2*float(self.n.get())))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.show()
            elif(comval==1):
                x = np.arange(-100,100,0.001)
                y = (x*x*x)-(2*x)-5
                plt.plot(x,y)
                plt.plot([float(self.n.get())],[0],'go')
                plt.plot([float(self.p.get())],[0],'bo')
                plt.plot([float(self.aproxv.get())],[0],'ro')
                plt.ylim(-float(self.func(float(self.n.get()),comval))-5,float(self.func(self.n.get(),comval))+5)
                plt.xlim((-0.5)*float(self.n.get()),(2*float(self.n.get())))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.show()
            elif(comval==2):
                x = np.arange(-100,100,0.001)
                y = (2*(x*x*x))+(3*(x*x))-(12*x)-30
                plt.plot(x,y)
                plt.plot([float(self.n.get())],[0],'go')
                plt.plot([float(self.p.get())],[0],'bo')
                plt.plot([float(self.aproxv.get())],[0],'ro')
                plt.ylim(-float(self.func(float(self.n.get()),comval))-5,float(self.func(self.n.get(),comval))+5)
                plt.xlim((-0.5)*float(self.n.get()),(2*float(self.n.get())))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.show()
            elif(comval==3):
                x = np.arange(-100,100,0.001)
                y = (x*x*x)-x-1
                plt.plot(x,y)
                plt.plot([float(self.n.get())],[0],'go')
                plt.plot([float(self.p.get())],[0],'bo')
                plt.plot([float(self.aproxv.get())],[0],'ro')
                plt.ylim(-float(self.func(float(self.n.get()),comval))-5,float(self.func(self.n.get(),comval))+5)
                plt.xlim((-0.5)*float(self.n.get()),(2*float(self.n.get())))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.show()
            elif(comval==4):
                x = np.arange(-100,100,0.001)
                y = (5*(x*x))+(7*x)-52
                plt.plot(x,y)
                plt.plot([float(self.n.get())],[0],'go')
                plt.plot([float(self.p.get())],[0],'bo')
                plt.plot([float(self.aproxv.get())],[0],'ro')
                plt.ylim(-float(self.func(float(self.n.get()),comval))-5,float(self.func(self.n.get(),comval))+5)
                plt.xlim((-0.5)*float(self.n.get()),(2*float(self.n.get())))
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.show()
      
    def derivf(self,x,y):
            if(y==0):
                return (-math.exp(-x))-1
            elif(y==1):
                return ((3*math.pow(x,2))-(2))
            elif(y==2):
                return (6*(math.pow(x,2)))+(6*x)-12
            elif(y==3):
                return (3*math.pow(x,2))-1
            elif(y==4):
                return (10*x)+7
        
    def func(self,x,y):
            if(y==0):
                return (math.exp(-x))-x
            elif(y==1):
                return (math.pow(x,3)-(2*x)-5)
            elif(y==2):
                return (2*(math.pow(x,3)))+(3*(math.pow(x,2)))-(12*x)-30
            elif(y==3):
                return (math.pow(x,3))-x-1
            elif(y==4):
                return (5*math.pow(x,2))+(7*x)-52
            
    def NewtonR(self):
        it=int(self.t3.get())
        aprox=float(self.t4.get())
        comval=int(self.combobox1.current())
        self.textC.config(state="normal")
        self.textC.delete(1.0,END)
        for i in range(1,it+1):
            self.textC.insert(INSERT,"Iteración: "+str(i)+"\n")
            aprox=aprox-((self.func(aprox,comval))/self.derivf(aprox,comval))
            self.aproxv.set(aprox)
            self.textC.insert(INSERT,"La raíz es: "+str(aprox)+"\n")
            self.textC.insert(INSERT,"\n")
           
        
        
         
    def bisection(self):
        a=float(self.t1.get())
        b=float(self.t2.get())
        it=int(self.t3.get())
        comval=int(self.combobox1.current())
        fa=self.func(a,comval)
        self.textB.config(state="normal")
        self.textB.delete(1.0,END)
        for x in range(1,it+1):
            self.textB.insert(INSERT,"Iteración: "+str(x)+"\n")
            p=((a+b)/2)
            self.p.set(p)
            fp=self.func(p,comval)
            if fp == 0 :
                   self.textB.insert(INSERT,"La raíz es: "+str(p)+"\n")
                   break
            elif(self.func(a,comval)*self.func(p,comval)>0):
               a=p
               fa=fp
            else:
                  b=p
            self.textB.insert(INSERT,"La raíz es: "+str(p)+"\n")
            self.textB.insert(INSERT,"\n")
           
                
    def calcular(self):
        a=float(self.t1.get())
        b=float(self.t2.get())
        it=int(self.t3.get())
        comval=int(self.combobox1.current())
        if self.func(a,comval)* self.func(b,comval)>=0:
                self.textA.config(state="normal")
                self.textA.delete(1.0,END)
                self.textA.insert(INSERT,"El intervalo no es el adecuado \n")
                self.textA.config(state='disable')
                
        else:
            self.textA.config(state="normal")
            self.textA.delete(1.0,END)
            self.textA.config(state='disable')
            for x in range(1,it+1):
                    self.textA.config(state="normal")
                    self.textA.insert(INSERT,"\n")
                    self.textA.insert(INSERT,"Iteración: "+str(x)+"\n")
                    self.textA.insert(INSERT,"a: "+self.t1.get()+"\n")
                    self.textA.insert(INSERT,"b: "+self.t2.get()+"\n")
                    self.textA.insert(INSERT,"F(a): "+str(self.func(a,comval))+"\n")
                    self.textA.insert(INSERT,"F(b): "+str(self.func(b,comval))+"\n")
                    n=a-((self.func(a,comval)*(a-b))/(self.func(a,comval)-self.func(b,comval)))
                    self.n.set(n)
                    if self.func(a,comval)*self.func(n,comval) == 0:
                            self.textA.insert(INSERT,"La raíz es: "+str(n)+"\n")
                            break
                    elif(self.func(a,comval)*self.func(n,comval)<0):
                        b=n
                    else:
                        a=n
                    self.textA.insert(INSERT,"La raíz es: "+str(n)+"\n")
                    self.textA.insert(INSERT,"\n")
                    self.textA.config(state='disable')
        
                
def main():
    objeto=Falsapos()
    return 0

if __name__ == '__main__':
    main()