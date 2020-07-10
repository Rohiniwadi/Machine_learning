from tkinter import *
import random
root = Tk()
list1 = []
list2 =[]
count =0
for i in range(4):
    n=random.randint(1,8)
    list1.append(n)
def draw(color):

     n1=color
     global list2
     list2.append(n1)
     if(len(list2)>4):
         list2=list2[:4]
def check1():
    global count
    c =0
    x1,y1,x,y=190,460-count*40,250,460-count*40
    global list1
    global list2
    for i in range(4):
        for j in range(4):
            if(list1[i]==list2[j]):
                if(i == j):
                    canvas.create_oval(x1,y1,x1+10,y1+10,fill="red")
                    x1=x1-20
                    c+=1
                    break
                else:
                    canvas.create_oval(x1,y1,x1+10,y1+10,fill="white")
                    x1=x1-20
                    break
                list1[j] =0
        
    for i in range(4):
        canvas.create_oval(x,y,x+30,y+30,fill=colors[list2[i]])
        x=x+60
    if(c == 4):
       canvas.delete("all")
       Label(text="You Win",font=('arial',50,"roman"),fg="red").place(x=100,y=250)
        
    count+=1
    list2.clear()
    if(count>10):
       canvas.delete("all")
       Label(text="Game Over",font=('arial',50,"roman"),fg="red").place(x=100,y=250)

def Quit():
    x,y=145,5
    global list1
    for i in range(4):
        canvas.create_oval(x,y,x+30,y+30,fill=colors[list1[i]])
        x=x+60
    Label(text="Game Over",font=('arial',50,"roman"),fg="red").place(x=100,y=250)
    check.configure(state="disabled")
root.title("MasterMind")
root.geometry("550x650+300+30")
label = Label(text="MasterMind",font=('arial',20,'roman')).pack(pady=10)
canvas = Canvas(root,width=550,height=500,bg='grey')
canvas.pack()
colors ={ 1:"red",2:"yellow",3:"blue",4:"orange",5:"cyan",6:"black",7:"green",8:"white"}
b1 =  Button(text=colors[1],bg=colors[1],command=lambda:draw(1)).pack(padx=10,side=LEFT)
b2 =  Button(text=colors[2],bg=colors[2],command=lambda:draw(2)).pack(padx=10,side=LEFT)
b3 =  Button(text=colors[3],bg=colors[3],command=lambda:draw(3)).pack(padx=10,side=LEFT)
b4 =  Button(text=colors[4],bg=colors[4],command=lambda:draw(4)).pack(padx=10,side=LEFT)
b5 =  Button(text=colors[5],bg=colors[5],command=lambda:draw(5)).pack(padx=10,side=LEFT)
b6 =  Button(text=colors[6],bg=colors[6],command=lambda:draw(6)).pack(padx=10,side=LEFT)
b7 =  Button(text=colors[7],bg=colors[7],command=lambda:draw(7)).pack(padx=10,side=LEFT)
b8 =  Button(text=colors[8],bg=colors[8],command=lambda:draw(8)).pack(padx=10,side=LEFT)
check = Button(text='CHECK',bg='grey',command=check1).pack(padx=10,side=LEFT)
B1 = Button(text="I Quit",command=Quit).place(x=250,y=620)
root.mainloop()
