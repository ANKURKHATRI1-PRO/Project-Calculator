from tkinter import *
Val=""
def Btnclick(number):
    global Val 
    Val=Val+str(number)
    data.set(Val)
         
def buttonClear():
    global Val
    Val=""
    data.set("")

def BtnEquals():
    global Val  
    try:
        result = str(eval(Val))
        data.set(result)
        Val = result
    except:
        data.set("=")
        Val =""    

def Btnpercent():
    global Val
    try:

        Val = str(float(Val) / 100)
        data.set(Val)
    except:
        data.set("Error")
        Val=""

def BtnDot():
    global Val
    if '.' not in Val:
        Val = Val + '.'     
        data.set(Val)

def BtnSquare():
    global Val
    try:
        Val = str(float(Val) ** 2)
        data.set(Val)
    except:
        data.set("Error")
        Val = ""

def BtnCube():
    global Val
    try:
        Val = str(float(Val) ** 3)
        data.set(Val)
    except:
        data.set("Error")
        Val = ""


root = Tk()
root.title( "Akur's calculator")
root.geometry("361x381+500+200")
root.configure(bg="dark grey")

data =StringVar()

display=Entry(root,textvariable=data,bd=4,bg="powder blue",justify="right",font=("ariel",22))
display.grid(row=0,columnspan=5)
Button_font =("arial", 18, "bold")

Btn7=Button(root,text="7",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(7))
Btn7.grid(row=1,column=0)
Btn8=Button(root,text="8",font=("ariel",12,"bold"),bd=10,height=2,width=6, command=lambda:Btnclick(8))
Btn8.grid(row=1,column=1)
Btn9=Button(root,text="9",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(9))
Btn9.grid(row=1,column=2)
Btn_add=Button(root,text="+",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick("+"))
Btn_add.grid(row=1,column=3)
Btn4=Button(root,text="4",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(4))
Btn4.grid(row=2,column=0)
Btn5=Button(root,text="5",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(5))
Btn5.grid(row=2,column=1)
Btn6=Button(root,text="6",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(6))
Btn6.grid(row=2,column=2)
Btn_sub=Button(root,text="-",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick("-"))
Btn_sub.grid(row=2,column=3)
Btn1=Button(root,text="1",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(1))
Btn1.grid(row=3,column=0)
Btn2=Button(root,text="2",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(2))
Btn2.grid(row=3,column=1)
Btn3=Button(root,text="3",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(3))
Btn3.grid(row=3,column=2)
Btn_mul=Button(root,text="*",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick("*"))
Btn_mul.grid(row=3,column=3)
Btnc=Button(root,text="clear",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=buttonClear, bg="light blue")
Btnc.grid(row=4,column=0)
Btn0=Button(root,text="0",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick(0))
Btn0.grid(row=4,column=1)
Btn_div=Button(root,text="/",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick("/"))
Btn_div.grid(row=4,column=2)
Btn_Equals=Button(root,text="=",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=BtnEquals)
Btn_Equals.grid(row=4,column=3)
Btn_percent=Button(root,text="%",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=Btnpercent)
Btn_percent.grid(row=5,column=0)
Btn_Dot=Button(root,text=".",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=lambda:Btnclick("."))
Btn_Dot.grid(row=5,column=1)
Btn_Square=Button(root,text="x2 ",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=BtnSquare)
Btn_Square.grid(row=5,column=2)
Btn_Cube=Button(root,text="x3",font=("ariel",12,"bold"),bd=10,height=2,width=6,command=BtnCube)
Btn_Cube.grid(row=5,column=3)


root.mainloop()