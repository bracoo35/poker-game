from tkinter import *
from PIL import ImageTk,Image
#using pillow has extra step for displaying img, have to add image to another thing(ex:label), 
# then display that thing

#jeremiah9000 at lines 1050 shows how he deals cards

class Card:
    def __init__ (self, value, suit):
        self.value = value
        self.suit = suit

c = Card(5, 'H')
print(c.suit, c.value)



'''
root = Tk()
root.title('this is title')
root.geometry('1000x800')



my_img1 = ImageTk.PhotoImage(Image.open("images/AS.png"))
my_label = Label(image=my_img1)

image_list = [my_img1]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    return

def back():
    return 

button_back = Button(root, text='<<')
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>')

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()

'''