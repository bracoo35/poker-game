'''
TO-DO: 

add button for different/reset flops, showing turn, river

 '''



from tkinter import *
from PIL import ImageTk,Image
import random


class Card:


    def __init__ (self, value, suit):   #correct value parameter will be 0-12, suit will be 0-3
        self.value = value
        self.suit = suit

    def __repr__(self):
            value_name = ""
            suit_name = ""
            if self.value == 0:
                value_name = "2"
            if self.value == 1:
                value_name = "3"
            if self.value == 2:
                value_name = "4"
            if self.value == 3:
                value_name = "5"
            if self.value == 4:
                value_name = "6"
            if self.value == 5:
                value_name = "7"
            if self.value == 6:
                value_name = "8"
            if self.value == 7:
                value_name = "9"
            if self.value == 8:
                value_name = "10"
            if self.value == 9:
                value_name = "jack"
            if self.value == 10:
                value_name = "queen"
            if self.value == 11:
                value_name = "king"
            if self.value == 12:
                value_name = "ace"
            if self.suit == 0:
                suit_name = "diamonds"
            if self.suit == 1:
                suit_name = "clubs"
            if self.suit == 2:
                suit_name = "hearts"
            if self.suit == 3:
                suit_name = "spades"


            return value_name + '_of_' + suit_name   # or could use: return 'a {self.color} of'.format(self=self)      

flop_cards = []
turn_card = []
river_card = []

class Deck(list):  
    def __init__(self):
        super().__init__()
        suits = list(range(4))          #creates a list variable named suits with length of 4 elements
        values = list(range(13))
        for j in suits:
            for i in values:
                self.append(Card(i,j))

    def __repr__(self):
        return f"{len(self)} cards remaining in deck."

    def shuffle(self):
        random.shuffle(self)
        print("Deck shuffled.")

    def deal_flop(self):
        flop_cards.append(self.pop(0))
        flop_cards.append(self.pop(0))
        flop_cards.append(self.pop(0))

    def deal_turn(self):
        turn_card.append(self.pop(0))  

    def deal_river(self):
        river_card.append(self.pop(0))  

    def burn(self):
        self.pop(0)

deck = Deck()
deck.shuffle()
deck.deal_flop()
deck.deal_turn()
deck.deal_river()


root = Tk()
root.title('this is title')
root.geometry('700x700')


my_img1 = ImageTk.PhotoImage(Image.open("cards/" + str(flop_cards[0]) + ".png").resize((135,175))) 
my_img2 = ImageTk.PhotoImage(Image.open("cards/" + str(flop_cards[1]) + ".png").resize((135,175)))
my_img3 = ImageTk.PhotoImage(Image.open("cards/" + str(flop_cards[2]) + ".png").resize((135,175)))
my_img4 = ImageTk.PhotoImage(Image.open("cards/" + str(turn_card[0]) + ".png").resize((135,175)))
my_img5 = ImageTk.PhotoImage(Image.open("cards/" + str(river_card[0]) + ".png").resize((135,175)))


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0 )

my_label2 = Label(image=my_img2)
my_label2.grid(row=0, column=1 )

my_label3 = Label(image=my_img3)
my_label3.grid(row=0, column=2 )

my_label4 = Label(image=my_img4)
my_label4.grid(row=0, column=3 )

my_label5 = Label(image=my_img5)
my_label5.grid(row=0, column=4 )

root.mainloop()