from tkinter import *
from PIL import Image, ImageTk
import  gender_classifier 

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

root = Tk()
root.title("Title")
root.geometry('600x600')

frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("image.gif")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

center_frame = Frame(frame, relief='raised')
center_frame.place( relx=0.5,rely=0.2,anchor=CENTER)

Label(center_frame, text='      Gender classification        ',font=(' Times new roman',22)).pack()
Button(frame,text='START',font=(' Times new roman',22),command=gender_classifier.classifie).place(x=250,y=450)
root.mainloop()
