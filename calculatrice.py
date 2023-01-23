from tkinter import *
from math import *
import re

def lastIndex(string):
    lastElement = str(string)[-1]
    return str(string).index(lastElement)

def insert(n):
    textAffichage = txtAffichage.get
    txtAffichage.insert(lastIndex(textAffichage),n)

def clear(): 
    txtAffichage.delete(0,END)

def calcul():
    if "√" in txtAffichage.get(): 
        operation = txtAffichage.get()
        solved = [sqrt(float(sqrts)) for sqrts in [x.replace('√','') for x in re.split('[+\-]',operation) if '√' in x]]
        txtAffichage.delete(0,END)
        txtAffichage.insert(0,str(solved))
    else : 
        operation = txtAffichage.get()
        calcul = eval(operation)
        txtAffichage.delete(0,END)
        txtAffichage.insert(0,calcul)

cal = Tk()
cal.title("Calculatrice Python")
cal.iconbitmap("image/images.ico")
txtAffichage = Entry(cal, font=('arial',22,'bold'), width=15,bd=20,insertwidth=4,bg="sky blue",
                    justify="right")

txtAffichage.grid(columnspan=4)


btn=["%","**2","√","/","7","8","9","*","4","5","6","-","1","2","3","+","C","0",".","="]
i=0
row = 1
column = 0 
while(i < len(btn)):
    if btn[i] == "=": 
        Button(cal,padx=20,pady=13,bd=6,fg="black",font=('arial',10),text=btn[i],bg="skyblue",command=lambda i=i: calcul() ).grid(row=row,column=column)
        column +=1
        i+=1 
    elif btn[i] == "C":
        Button(cal,padx=20,pady=13,bd=6,fg="black",font=('arial',10),text=btn[i],bg="skyblue",command=lambda i=i: clear() ).grid(row=row,column=column)
        column +=1
        i+=1 
    else:
        Button(cal,padx=20,pady=13,bd=6,fg="black",font=('arial',10),text=btn[i],bg="skyblue",command=lambda i=i: insert(btn[i]) ).grid(row=row,column=column)
        column +=1
        i+=1 

    if column > 3 : 
        column = 0 
        row +=1

cal.mainloop()




