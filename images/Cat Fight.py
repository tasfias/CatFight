from tkinter import *
from tkinter import messagebox
import time
import math

class Orange: #Create a class for the character Orange Cat
    def __init__(self, canvas, x, y, imagePath):
        global damage1 #Public attribute to be used in attack methods
        global guarding1 #Public attribute to check if the character is guarding
        guarding1 = False #Set to false initially as character isn't guarding
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(200, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0: #Make sure left side of character does not go past the left of the screen
            self.canvas.move(self.imageID, -10, 0) #Move the character image left

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width(): #Make sure right side of character does not go past the right of the screen
            self.canvas.move(self.imageID, 10, 0) #Move the character image right

    def getLeft(self):
        return self.canvas.coords(self.imageID)[0] #Get the coordinates of the left side of the character image

    def getTop(self):
        return self.canvas.coords(self.imageID)[1] #Get the coordinates of the top side of the character image

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth #Get the coordinates of the right side of the character image

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight #Get the coordinates of the bottom side of the character image

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1] #Store the current y coordinates of the character image
        jumpDistance = 50 #Store how many pixels for the character to jump
        self.canvas.move(self.imageID, 0, -jumpDistance) #Make the character move up by the value stored in jumpDistance
        self.canvas.after(200, lambda: self.canvas.move(self.imageID, 0, jumpDistance)) #Return the character back to its original position after 200ms

    def guard(self, event):
        global guarding1 #Public attribute to check if the character is guarding
        guarding1 = True #Make the character guard

    def unguard(self, event):
        global guarding1
        guarding1 = False #Stop the character from guarding

    def calcEnergy(self):
        if self.energy1 != 500:
            self.energy1 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display new value of self.energy1 on screen
            lEnergy.place(x=200, y=95)
        else:
            self.energy1 == 500 #Make sure value stored in self.energy1 doesn't go above 500

    def normalAtk(self):
        damage1 = 20
        if selection2 == 1:
            distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2) #Calculate distance between player 1 and player 2
            if distance <= 425: #Check if distance is close enough to attack
                Orange2.takeDamage(self, damage1) #Opponent takes damage if so
        elif selection2 == 2:
            distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
            if distance <= 425:
                White2.takeDamage(self, damage1)
        elif selection2 == 3:
            distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
            if distance <= 425:
                Black2.takeDamage(self, damage1)
            
    def specialAtk(self):
        if self.energy1 >= 50: #Check if energy is sufficient to be able to perform attack
            self.energy1 -= 50 #Deplete energy regardless if close enough to attack
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Update new value of self.energy1 on screen
            lEnergy.place(x=200, y=95)
            damage1 = 70
            if selection2 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 300:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
                if distance <= 300:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
                if distance <= 300:
                    Black2.takeDamage(self, damage1)

    def ultAtk(self):
        if self.energy1 >= 100:
            self.energy1 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            damage1 = 135
            if selection2 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 215:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
                if distance <= 215:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
                if distance <= 215:
                    Black2.takeDamage(self, damage1)

    def takeDamage(self, damage2):
        if guarding1 == False: #Check if character isn't guarding
            if self.health1 >= damage2: #Check if character has enough health to take the full damage
                self.health1 -= damage2
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Update health on screen
                lHealth.place(x=200, y=42)
            else:
                self.health1 = 0 #Make sure health doesn't go below 0
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Update health on screen
                lHealth.place(x=200, y=42)
                self.winners.append("Player 2") #Add Player 2 to the list winners as Player 1 has lost (health=0)
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white') #Display the list on screen to show who won the last round
                lose.place(x=320, y=180)
                self.start_new_round()      

class Orange2:
    def __init__(self, canvas, x, y, imagePath):
        global damage2
        global guarding2
        guarding2 = False
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(675, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0:
            self.canvas.move(self.imageID, -10, 0)

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width():
            self.canvas.move(self.imageID, 10, 0)
            
    def getLeft(self):
        return self.canvas.coords(self.imageID)[0]

    def getTop(self):
        return self.canvas.coords(self.imageID)[1]

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1]
        jumpDistance = 50
        self.canvas.move(self.imageID, 0, -jumpDistance)
        self.canvas.after(500, lambda: self.canvas.move(self.imageID, 0, jumpDistance))

    def guard(self, event):
        global guarding2
        guarding2 = True

    def unguard(self, event):
        global guarding2
        guarding2 = False
        
    def calcEnergy(self):
        if self.energy2 != 500:
            self.energy2 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
            pOrange.place(x=712, y=95)
        else:
            self.energy2 == 500

    def normalAtk(self):
        damage2 = 20
        if selection1 == 1:
            distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2)
            if distance <= 425:
                Orange.takeDamage(self, damage2)
        elif selection1 == 2:
            distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
            if distance <= 425:
                White.takeDamage(self, damage2)
        elif selection1 == 3:
            distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
            if distance <= 425:
                Black.takeDamage(self, damage2)

    def specialAtk(self):
        if self.energy2 >= 50:
            self.energy2 -= 50
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
            pOrange.place(x=712, y=95)
            damage2 = 70
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 300:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 300:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 300:
                    Black.takeDamage(self, damage2)

    def ultAtk(self):
        if self.energy2 >= 100:
            self.energy2 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
            pOrange.place(x=712, y=95)
            damage2 = 135
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.orange2.getRight()) ** 2 + (self.orange.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 215:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 215:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 215:
                    Black.takeDamage(self, damage2)

    def takeDamage(self, damage1):
        if guarding2 == False:
            if self.health2 >= damage1:
                self.health2 -= damage1
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
                pOrange.place(x=712, y=95)
            else:
                self.health2 = 0
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
                pOrange.place(x=712, y=95)
                self.winners.append("Player 1")
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()
        
class White:
    def __init__(self, canvas, x, y, imagePath):
        global damage1
        global guarding1
        guarding1 = False
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(200, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0:
            self.canvas.move(self.imageID, -10, 0)

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width():
            self.canvas.move(self.imageID, 10, 0)

    def getLeft(self):
        return self.canvas.coords(self.imageID)[0]

    def getTop(self):
        return self.canvas.coords(self.imageID)[1]

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1]
        jumpDistance = 50
        self.canvas.move(self.imageID, 0, -jumpDistance)
        self.canvas.after(500, lambda: self.canvas.move(self.imageID, 0, jumpDistance))

    def guard(self, event):
        global guarding1
        guarding1 = True

    def unguard(self, event):
        global guarding1
        guarding1 = False

    def calcEnergy(self):
        if self.energy1 != 500:
            self.energy1 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
        else:
            self.energy1 == 500
            
    def normalAtk(self):
        damage1 = 35
        if selection2 == 1:
            distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
            if distance <= 400:
                Orange2.takeDamage(self, damage1)
        elif selection2 == 2:
            distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
            if distance <= 400:
                White2.takeDamage(self, damage1)
        elif selection2 == 3:
            distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
            if distance <= 400:
                Black2.takeDamage(self, damage1)

    def specialAtk(self):
        if self.energy1 >= 50:
            self.energy1 -= 50
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            damage1 = 60
            if selection2 == 1:
                distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 310:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
                if distance <= 310:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
                if distance <= 310:
                    Black2.takeDamage(self, damage1)

    def ultAtk(self):
        if self.energy1 >= 100:
            self.energy1 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            damage1 = 130
            if selection2 == 1:
                distance = math.sqrt((self.white.getLeft() - self.orange2.getRight()) ** 2 + (self.white.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 230:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
                if distance <= 230:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
                if distance <= 230:
                    Black2.takeDamage(self, damage1)

    def takeDamage(self, damage2):
        if guarding1 == False:
            if self.health1 >= damage2:
                self.health1 -= damage2
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=200, y=42)
            else:
                self.health1 = 0
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=200, y=42)
                self.winners.append("Player 2")
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()

class White2: 
    def __init__(self, canvas, x, y, imagePath):
        global damage2
        global guarding2
        guarding2 = False
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(675, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0:
            self.canvas.move(self.imageID, -10, 0)

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width():
            self.canvas.move(self.imageID, 10, 0)

    def getLeft(self):
        return self.canvas.coords(self.imageID)[0]

    def getTop(self):
        return self.canvas.coords(self.imageID)[1]

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1]
        jumpDistance = 50
        self.canvas.move(self.imageID, 0, -jumpDistance)
        self.canvas.after(500, lambda: self.canvas.move(self.imageID, 0, jumpDistance))

    def guard(self, event):
        global guarding2
        guarding2 = True

    def unguard(self, event):
        global guarding2
        guarding2 = False

    def calcEnergy(self):
        if self.energy2 != 500:
            self.energy2 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
            pWhite.place(x=729, y=95)
        else:
            self.energy2 == 500

    def normalAtk(self):
        damage2 = 35
        if selection1 == 1:
            distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
            if distance <= 400:
                Orange.takeDamage(self, damage2)
        elif selection1 == 2:
            distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
            if distance <= 400:
                White.takeDamage(self, damage2)
        elif selection1 == 3:
            distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
            if distance <= 400:
                Black.takeDamage(self, damage2)

    def specialAtk(self):
        if self.energy2 >= 50:
            self.energy2 -= 50
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
            pWhite.place(x=729, y=95)
            damage2 = 60
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
                if distance <= 310:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
                if distance <= 310:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
                if distance <= 310:
                    Black.takeDamage(self, damage2)

    def ultAtk(self):
        if self.energy2 >= 100:
            self.energy2 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
            pWhite.place(x=729, y=95)
            damage2 = 130
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.white2.getRight()) ** 2 + (self.orange.getTop() - self.white2.getTop()) ** 2)
                if distance <= 230:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.white2.getRight()) ** 2 + (self.white.getTop() - self.white2.getTop()) ** 2)
                if distance <= 230:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
                if distance <= 230:
                    Black.takeDamage(self, damage2)

    def takeDamage(self, damage1):
        if guarding2 == False:
            if self.health2 >= damage1:
                self.health2 -= damage1
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
                pWhite.place(x=729, y=95)
            else:
                self.health2 = 0
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
                pWhite.place(x=729, y=95)
                self.winners.append("Player 1")
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()
        
class Black:
    def __init__(self, canvas, x, y, imagePath):
        global damage1
        global guarding1
        guarding1 = False
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(200, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0:
            self.canvas.move(self.imageID, -10, 0)

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width():
            self.canvas.move(self.imageID, 10, 0)

    def getLeft(self):
        return self.canvas.coords(self.imageID)[0]

    def getTop(self):
        return self.canvas.coords(self.imageID)[1]

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1]
        jumpDistance = 50
        self.canvas.move(self.imageID, 0, -jumpDistance)
        self.canvas.after(500, lambda: self.canvas.move(self.imageID, 0, jumpDistance))

    def guard(self, event):
        global guarding1
        guarding1 = True

    def unguard(self, event):
        global guarding1
        guarding1 = False

    def calcEnergy(self):
        if self.energy1 != 500:
            self.energy1 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
        else:
            self.energy1 == 500
            
    def normalAtk(self):
        damage1 = 25
        if selection2 == 1:
            distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
            if distance <= 410:
                Orange2.takeDamage(self, damage1)
        elif selection2 == 2:
            distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
            if distance <= 410:
                White2.takeDamage(self, damage1)
        elif selection2 == 3:
            distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
            if distance <= 410:
                Black2.takeDamage(self, damage1)

    def specialAtk(self):
        if self.energy1 >= 50:
            self.energy1 -= 50
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            damage1 = 50
            if selection2 == 1:
                distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 330:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
                if distance <= 330:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
                if distance <= 330:
                    Black2.takeDamage(self, damage1)

    def ultAtk(self):
        if self.energy1 >= 100:
            self.energy1 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            damage1 = 150
            if selection2 == 1:
                distance = math.sqrt((self.black.getLeft() - self.orange2.getRight()) ** 2 + (self.black.getTop() - self.orange2.getTop()) ** 2)
                if distance <= 200:
                    Orange2.takeDamage(self, damage1)
            elif selection2 == 2:
                distance = math.sqrt((self.black.getLeft() - self.white2.getRight()) ** 2 + (self.black.getTop() - self.white2.getTop()) ** 2)
                if distance <= 200:
                    White2.takeDamage(self, damage1)
            elif selection2 == 3:
                distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
                if distance <= 200:
                    Black2.takeDamage(self, damage1)

    def takeDamage(self, damage2):
        if guarding1 == False:
            if self.health1 >= damage2:
                self.health1 -= damage2
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=200, y=42)
            else:
                self.health1 = 0
                lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=200, y=42)
                self.winners.append("Player 2")
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()      

class Black2:
    def __init__(self, canvas, x, y, imagePath):
        global damage2
        global guarding2
        guarding2 = False
        self.canvas = canvas
        self.image = PhotoImage(file=imagePath)
        self.imageID = self.canvas.create_image(675, 380, image=self.image)
        self.imageWidth = self.image.width()
        self.imageHeight = self.image.height()

    def move_left(self, event):
        if self.getLeft() > 0:
            self.canvas.move(self.imageID, -10, 0)

    def move_right(self, event):
        if self.getRight() < self.canvas.winfo_width():
            self.canvas.move(self.imageID, 10, 0)

    def getLeft(self):
        return self.canvas.coords(self.imageID)[0]

    def getTop(self):
        return self.canvas.coords(self.imageID)[1]

    def getRight(self):
        return self.canvas.coords(self.imageID)[0] + self.imageWidth

    def getBottom(self):
        return self.canvas.coords(self.imageID)[1] + self.imageHeight

    def jump(self, event):
        current_y = self.canvas.coords(self.imageID)[1]
        jumpDistance = 50
        self.canvas.move(self.imageID, 0, -jumpDistance)
        self.canvas.after(500, lambda: self.canvas.move(self.imageID, 0, jumpDistance))

    def guard(self, event):
        global guarding2
        guarding2 = True

    def unguard(self, event):
        global guarding2
        guarding2 = False

    def calcEnergy(self):
        if self.energy2 != 500:
            self.energy2 += 10
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
            pBlack.place(x=729, y=95)
        else:
            self.energy2 == 500

    def normalAtk(self):
        damage2 = 25
        if selection1 == 1:
            distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
            if distance <= 400:
                Orange.takeDamage(self, damage2)
        elif selection1 == 2:
            distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
            if distance <= 400:
                White.takeDamage(self, damage2)
        elif selection1 == 3:
            distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
            if distance <= 400:
                Black.takeDamage(self, damage2)

    def specialAtk(self):
        if self.energy2 >= 50:
            self.energy2 -= 50
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
            pBlack.place(x=729, y=95)
            damage2 = 50
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
                if distance <= 300:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
                if distance <= 300:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
                if distance <= 300:
                    Black.takeDamage(self, damage2)

    def ultAtk(self):
        if self.energy2 >= 100:
            self.energy2 -= 100
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
            pBlack.place(x=729, y=95)
            damage2 = 150
            if selection1 == 1:
                distance = math.sqrt((self.orange.getLeft() - self.black2.getRight()) ** 2 + (self.orange.getTop() - self.black2.getTop()) ** 2)
                if distance <= 200:
                    Orange.takeDamage(self, damage2)
            elif selection1 == 2:
                distance = math.sqrt((self.white.getLeft() - self.black2.getRight()) ** 2 + (self.white.getTop() - self.black2.getTop()) ** 2)
                if distance <= 200:
                    White.takeDamage(self, damage2)
            elif selection1 == 3:
                distance = math.sqrt((self.black.getLeft() - self.black2.getRight()) ** 2 + (self.black.getTop() - self.black2.getTop()) ** 2)
                if distance <= 200:
                    Black.takeDamage(self, damage2)

    def takeDamage(self, damage1):
        if guarding2 == False:
            if self.health2 >= damage1:
                self.health2 -= damage1
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
                pBlack.place(x=729, y=95)
            else:
                self.health2 = 0
                lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
                lHealth.place(x=540, y=42)
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
                pBlack.place(x=729, y=95)
                self.winners.append("Player 1")
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()
            

class Game(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Cat Fight")
        self.master.geometry("863x600")

        self.bg = PhotoImage(file="starting.png")  #Keep a reference to the PhotoImage object
        label1 = Label(self.master, image=self.bg) #Display the image as the background of the window
        label1.place(x=0, y=0)

        global timeLimit #Public attributes to be used in other methods
        global rounds
        timeLimit = 90 #Make 90 the default value
        rounds = 3 #Make 3 the default value

        global selection1
        global selection2
        selection1 = 0 #Make 0 the default value
        selection2 = 0

        self.winners = [] #List to store the winner of each round
        self.actualWinner = None #Attribute to store the end winner
        
        settings = Button(self.master, text='Settings', fg='#DA6BFF', bg='#6BFFA9', bd=1, font=('Modern 17 bold'),
                          command=self.options, height=2, width=8)
        settings.place(x=25, y=25)
        
        instructions = Button(self.master, text='How to play', fg='#DA6BFF', bg='#6BFFA9', bd=1, font=('Modern 17 bold'),
                              command=self.howToPlay, height=1, width=15)
        instructions.place(x=140, y=40)
        
        start = Button(self.master, text='Start', fg='#FF746C', bg='#6BFFA9', bd=5, font=('Modern 35 bold'),
                       command=self.charaSelect1, height=1, width=8)
        start.place(x=350, y=470)

    def howToPlay(self):
        inst = Frame(root, bg='#6D97FF')
        inst.pack(fill="both", expand="yes")
        
        top = Label(inst, text = "How to play", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
        top.pack(pady=20)
        
        left = Label(inst, text="Player 1", bg='#FF6D9E', fg='white', font=('Modern 25 bold'))
        left.place(x=100, y=105)
        
        right = Label(inst, text="Player 2", bg='#FF6D9E', fg='white', font=('Modern 25 bold'))
        right.place(x=450, y=105)
        
        p1Move = Label(inst, text="Move", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p1Move.place(x=100, y=180)
        
        p2Move = Label(inst, text="Move", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p2Move.place(x=450, y=180)

        p1Guard = Label(inst, text="Guard", bg='#FF6D9E', fg='white', font=('Modern 12'))
        p1Guard.place(x=330, y=170)

        p2Guard = Label(inst, text="Guard", bg='#FF6D9E', fg='white', font=('Modern 12'))
        p2Guard.place(x=680, y=170)

        p1Normal = Label(inst, text="Normal attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p1Normal.place(x=100, y=270)
        
        p2Normal = Label(inst, text="Normal attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p2Normal.place(x=450, y=270)

        p1Special = Label(inst, text="Special attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p1Special.place(x=100, y=350)
        
        p2Special = Label(inst, text="Special attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p2Special.place(x=450, y=350)

        p1Ult = Label(inst, text="Ultimate attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p1Ult.place(x=100, y=430)
        
        p2Ult = Label(inst, text="Ultimate attack", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p2Ult.place(x=450, y=430)

        p1Charge = Label(inst, text="Charge energy", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p1Charge.place(x=100, y=510)
        
        p2Charge = Label(inst, text="Charge energy", bg='#FF6D9E', fg='white', font=('Modern 20'))
        p2Charge.place(x=450, y=510)

        close = Button(inst, text='X', fg='white', bg='#FF746C', bd=1, font=('Modern 20 bold'), #Close the frame when the button is clicked
                      command = inst.pack_forget, height=1, width=4)
        close.place(x=750, y=20)
        
        wasd = PhotoImage(file="wasd.png")
        wasd.image = wasd
        wasd_label = Label(inst, image=wasd, bd=0)
        wasd_label.place(x=200, y=160)

        arrows = PhotoImage(file="arrows.png")
        arrows.image = arrows
        arrows_label = Label(inst, image=arrows, bd=0)
        arrows_label.place(x=550, y=160)

        s = PhotoImage(file="s.png")
        s.image = s
        s_label = Label(inst, image=s, bg='#6D97FF', bd=0)
        s_label.place(x=335, y=205)

        down = PhotoImage(file="down.png")
        down.image = down
        down_label = Label(inst, image=down, bg='#6D97FF', bd=0)
        down_label.place(x=685, y=205)

        e = PhotoImage(file="e.png")
        e.image = e
        e_label = Label(inst, image=e, bd=0)
        e_label.place(x=265, y=240)

        b = PhotoImage(file="b.png")
        b.image = b
        b_label = Label(inst, image=b, bd=0)
        b_label.place(x=615, y=240)

        r = PhotoImage(file="r.png")
        r.image = r
        r_label = Label(inst, image=r, bd=0)
        r_label.place(x=265, y=320)

        n = PhotoImage(file="n.png")
        n.image = n
        n_label = Label(inst, image=n, bd=0)
        n_label.place(x=615, y=320)

        t = PhotoImage(file="t.png")
        t.image = t
        t_label = Label(inst, image=t, bd=0)
        t_label.place(x=265, y=400)

        m = PhotoImage(file="m.png")
        m.image = m
        m_label = Label(inst, image=m, bd=0)
        m_label.place(x=615, y=400)

        q = PhotoImage(file="q.png")
        q.image = q
        q_label = Label(inst, image=q, bd=0)
        q_label.place(x=265, y=480)

        l = PhotoImage(file="l.png")
        l.image = l
        l_label = Label(inst, image=l, bd=0)
        l_label.place(x=615, y=480)

    def options(self):
        sett = Frame(root, bg='#6D97FF')
        sett.pack(fill="both", expand="yes")
        top = Label(sett, text = "Settings", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
        top.pack(pady=20)
    
        roundsTitle = Label(sett, text="Rounds", bg='#FF6D9E', fg='white', font=('Modern 25 bold'))
        roundsTitle.pack(pady=45)
        rounds1 = Button(sett, text='1', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.oneRound, height=2, width=8)
        rounds1.place(x=170,y=220)
        rounds3 = Button(sett, text='3', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.threeRound, height=2, width=8)
        rounds3.place(x=390, y=220)
        rounds5 = Button(sett, text='5', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.fiveRound, height=2, width=8)
        rounds5.place(x=600,y=220)

        timeLimit = Label(sett, text="Time limit", bg='#FF6D9E', fg='white', font=('Modern 25 bold'))
        timeLimit.pack(pady=120)
        time60 = Button(sett, text='60s', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.sixty, height=2, width=8)
        time60.place(x=160,y=440)
        time90 = Button(sett, text='90s', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.ninety, height=2, width=8)
        time90.place(x=310,y=440)
        time120 = Button(sett, text='120s', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.one20, height=2, width=8)
        time120.place(x=460,y=440)
        timeInf = Button(sett, text='∞', fg='white', bg='#FF6D9E', bd=1, font=('Modern 15 bold'),
                      command = self.infinite, height=2, width=8)
        timeInf.place(x=610,y=440)
        close = Button(sett, text='X', fg='white', bg='#FF746C', bd=1, font=('Modern 20 bold'), #Close the frame with the button is clicked
                      command = sett.pack_forget, height=1, width=4)
        close.place(x=750, y=20)

    def oneRound(self):
        global rounds #Public attribute to be used in other methods
        rounds = 1 #Store player's choice of rounds clicked in buttons in options method

    def threeRound(self):
        global rounds
        rounds = 3

    def fiveRound(self):
        global rounds
        rounds = 5

    def sixty(self):
        global timeLimit #Public attribute to be used in other methods
        timeLimit = 60 #Store player's choice of time limit clicked in buttons in options method

    def ninety(self):
        global timeLimit
        timeLimit = 90

    def one20(self):
        global timeLimit
        timeLimit = 120

    def infinite(self):
        global timeLimit
        timeLimit = 'infinite'

    def charaSelect1(self):
        global start
        start = Frame(root, bg='#68ffa9')
        start.pack(fill="both", expand="yes")

        wCat = PhotoImage(file="white2.png")
        wCat.image = wCat #Store reference to image
        wCat_label = Label(start, image=wCat, bd=0) #Create label to display image
        white = Button(start, image=wCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                      command = self.wChar1, height=170, width=170)
        white.place(x=350,y=385)

        oCat = PhotoImage(file="orange2.png")
        oCat.image = oCat
        oCat_label = Label(start, image=oCat, bd=0)
        orange = Button(start, image=oCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                      command = self.oChar1, height=170, width=170)
        orange.place(x=100,y=385)

        bCat = PhotoImage(file="black2.png")
        bCat.image = bCat
        bCat_label = Label(start, image=bCat, bd=0)
        black = Button(start, image=bCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                      command = self.bChar1, height=170, width=170)
        black.place(x=595,y=385)
    
        rectangle = Canvas(start, width=863, height=320, bg='#FF6D9E', bd=0)
        rectangle.place(x=0, y=0)
        info = Canvas(start, width=220, height=260, bg='#68ffa9', bd=0)
        info.place(x=590, y=35)
        top = Label(start, text = "Player 1", bg='#68ffa9', fg='#DA6BFF', font=('Modern 35 bold'))
        top.place(x=40, y=35)

        back = Button(start, text='Back', fg='#DA6BFF', bg='#68ffa9', bd=1, font=('Modern 17 bold'),
                      command = start.destroy, height=1, width=8)
        back.place(x=40,y=160)

        toP2 = Button(start, text='Next', fg='#DA6BFF', bg='#68ffa9', bd=1, font=('Modern 17 bold'),
                      command = self.charaSelect2, height=2, width=8)
        toP2.place(x=40,y=230)

    def charaSelect2(self):
        if selection1 == 0:
            messagebox.showwarning("Alert", "Must choose a character") #Make sure player cannot progress if a character hasn't been chosen
        else:  
            global player2
            player2 = Frame(start, bg='#68ffa9')
            player2.pack(fill="both", expand="yes")

            wCat = PhotoImage(file="white2.png")
            wCat.image = wCat
            wCat_label = Label(player2, image=wCat, bd=0)
            white = Button(player2, image=wCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                          command = self.wChar2, height=170, width=170)
            white.place(x=350,y=385)

            oCat = PhotoImage(file="orange2.png")
            oCat.image = oCat
            oCat_label = Label(player2, image=oCat, bd=0)
            orange = Button(player2, image=oCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                          command = self.oChar2, height=170, width=170)
            orange.place(x=100,y=385)

            bCat = PhotoImage(file="black2.png")
            bCat.image = bCat
            bCat_label = Label(player2, image=bCat, bd=0)
            black = Button(player2, image=bCat, bg='#f9e8ff', bd=1, font=('Modern 17 bold'),
                          command = self.bChar2, height=170, width=170)
            black.place(x=595,y=385)
            
            r = Canvas(player2, width=863, height=320, bg='#FF6D9E', bd=0)
            r.place(x=0,y=0)
            info = Canvas(player2, width=220, height=260, bg='#68ffa9', bd=0)
            info.place(x=590, y=35)
            top = Label(player2, text = "Player 2", bg='#68ffa9', fg='#DA6BFF', font=('Modern 35 bold'))
            top.place(x=40, y=35)

            back = Button(player2, text='Back', fg='#DA6BFF', bg='#68ffa9', bd=1, font=('Modern 17 bold'),
                          command = player2.destroy, height=1, width=8)
            back.place(x=40,y=160)

            toGame = Button(player2, text='Start game', fg='#DA6BFF', bg='#68ffa9', bd=1, font=('Modern 17 bold'),
                          command = self.battle, height=2, width=12)
            toGame.place(x=40,y=230) 

    def oChar1(self):
        global selection1 #Public attribute to be used in other methods to check which character has been chosen
        selection1 = 1
        
        photo = PhotoImage(file="oCS2.png")
        photo.image = photo
        photo_label = Label(start, image=photo, bg='#FF6D9E',bd=0) #Display the chosen character on screen
        photo_label.place(x=260, y=30)
        
        details = Label(start, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold')) #Display the character's details on screen
        details.place(x=600, y=45)
        nAtk = Label(start, text = "Normal Attack      20", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(start, text = "Special Attack      70", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(start, text = "Ultimate Attack    135", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)
        
    def oChar2(self):
        global selection2
        selection2 = 1
        
        photo = PhotoImage(file="oCS2.png")
        photo.image = photo
        photo_label = Label(player2, image=photo, bg='#FF6D9E',bd=0)
        photo_label.place(x=260, y=30)

        details = Label(player2, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold'))
        details.place(x=600, y=45)
        nAtk = Label(player2, text = "Normal Attack      20", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(player2, text = "Special Attack      70", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(player2, text = "Ultimate Attack    135", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)

    def wChar1(self):
        global selection1
        selection1 = 2
        
        photo = PhotoImage(file="wCS2.png")
        photo.image = photo
        photo_label = Label(start, image=photo, bg='#FF6D9E',bd=0)
        photo_label.place(x=260, y=30)
        
        details = Label(start, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold'))
        details.place(x=600, y=45)
        nAtk = Label(start, text = "Normal Attack      35", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(start, text = "Special Attack      60", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(start, text = "Ultimate Attack    130", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)

    def wChar2(self):
        global selection2
        selection2 = 2
        
        photo = PhotoImage(file="wCS2.png")
        photo.image = photo
        photo_label = Label(player2, image=photo, bg='#FF6D9E',bd=0)
        photo_label.place(x=260, y=30)

        details = Label(player2, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold'))
        details.place(x=600, y=45)
        nAtk = Label(player2, text = "Normal Attack      35", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(player2, text = "Special Attack      60", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(player2, text = "Ultimate Attack    130", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)

    def bChar1(self):
        global selection1
        selection1 = 3
        
        photo = PhotoImage(file="bCS2.png")
        photo.image = photo
        photo_label = Label(start, image=photo, bg='#FF6D9E',bd=0)
        photo_label.place(x=260, y=30)
        
        details = Label(start, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold'))
        details.place(x=600, y=45)
        nAtk = Label(start, text = "Normal Attack      25", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(start, text = "Special Attack      50", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(start, text = "Ultimate Attack    150", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)

    def bChar2(self):
        global selection2
        selection2 = 3
        
        photo = PhotoImage(file="bCS2.png")
        photo.image = photo
        photo_label = Label(player2, image=photo, bg='#FF6D9E',bd=0)
        photo_label.place(x=260, y=30)

        details = Label(player2, text = "Details", bg='#68ffa9', fg='#DA6BFF', font=('Modern 20 bold'))
        details.place(x=600, y=45)
        nAtk = Label(player2, text = "Normal Attack      25", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        nAtk.place(x=600, y=110)
        sAtk = Label(player2, text = "Special Attack      50", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        sAtk.place(x=600, y=180)
        uAtk = Label(player2, text = "Ultimate Attack    150", bg='#68ffa9', fg='#DA6BFF', font=('Modern 17'))
        uAtk.place(x=600, y=250)

    def battle(self):
        if selection2 == 0:
            messagebox.showwarning("Alert", "Must choose a character") #Make sure player cannot progress if a character hasn't been chosen
        else:
            self.canvas = Canvas(player2, bg='#6D97FF', width=863, height=600)
            self.canvas.pack()

            rectangle = Canvas(self.canvas, width=863, height=402, bg='#FF6D9E', bd=0)
            rectangle.place(x=0, y=439)

            global check #Public attribute to be used in other methods
            check = 1 #Stores 1 to keep track which screen is currently displayed on screen

            top1 = Label(self.canvas, text = "Player 1", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top1.place(x=40, y=35)

            self.start_label = Label(self.canvas, text="Start!", font=('Modern 70 bold'), bg='#FF6D9E', fg='white')
            self.start_label.place(x=350, y=200)
            self.start_label.after(2000, self.start_label.place_forget) #Remove label after 2 seconds

            self.round_no = 1 #Store current round

            self.round_label = Label(self.canvas, text=f"Round {self.round_no}", font=('Modern 20 bold'), bg='#FF6D9E', fg='white') #Display current round on screen
            self.round_label.place(x=405, y=140)

            self.health1 = 1000
            self.energy1 = 500
            lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display current health on screen for player 1
            lHealth.place(x=200, y=42)
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display current energy on screen for player 1
            lEnergy.place(x=200, y=95)
            
            self.health2 = 1000
            self.energy2 = 500
            lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display current health on screen for player 2
            lHealth.place(x=540, y=42)
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display current energy on screen for player 2
            lEnergy.place(x=550, y=95)

            self.paused = False #Make sure game isn't paused when the battle starts

            if selection1 == 1: #Check which character has been chosen
                pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
                pOrange.place(x=40, y=95)

                self.orange = Orange(self.canvas, 200, 380, "oFight.png") #Display character image on screen
                self.master.bind("<w>", self.orange.jump) #Bind the keys to the character class methods 
                self.master.bind("<a>", self.orange.move_left)
                self.master.bind("<d>", self.orange.move_right)
                self.master.bind("<KeyPress-s>", self.orange.guard)
                self.master.bind("<KeyRelease-s>", self.orange.unguard)

                self.master.bind('<q>',
                                 lambda _: Orange.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: Orange.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: Orange.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: Orange.ultAtk(self))
     
            elif selection1 == 2:
                pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
                pWhite.place(x=40, y=95)

                self.white = White(self.canvas, 200, 380, "wFight.png")
                self.master.bind("<w>", self.white.jump)
                self.master.bind("<a>", self.white.move_left)
                self.master.bind("<d>", self.white.move_right)
                self.master.bind("<KeyPress-s>", self.white.guard)
                self.master.bind("<KeyRelease-s>", self.white.unguard)

                self.master.bind('<q>',
                                 lambda _: White.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: White.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: White.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: White.ultAtk(self))
                
            elif selection1 == 3:
                pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
                pBlack.place(x=40, y=95)

                self.black = Black(self.canvas, 200, 380, "bFight.png")
                self.master.bind("<w>", self.black.jump)
                self.master.bind("<a>", self.black.move_left)
                self.master.bind("<d>", self.black.move_right)
                self.master.bind("<KeyPress-s>", self.black.guard)
                self.master.bind("<KeyRelease-s>", self.black.unguard)

                self.master.bind('<q>',
                                 lambda _: Black.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: Black.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: Black.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: Black.ultAtk(self))
                  
            if selection2 == 1:
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
                pOrange.place(x=712, y=95)

                self.orange2 = Orange2(self.canvas, 675, 380, "oFight2.png")
                self.master.bind("<Up>", self.orange2.jump)
                self.master.bind("<Left>", self.orange2.move_left)
                self.master.bind("<Right>", self.orange2.move_right)
                self.master.bind("<KeyPress-Down>", self.orange2.guard)
                self.master.bind("<KeyRelease-Down>", self.orange2.unguard)

                self.master.bind('<l>',
                                 lambda _: Orange2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: Orange2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: Orange2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: Orange2.ultAtk(self))
            
            elif selection2 == 2: 
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
                pWhite.place(x=729, y=95)

                self.white2 = White2(self.canvas, 675, 380, "wFight2.png")
                self.master.bind("<Up>", self.white2.jump)
                self.master.bind("<Left>", self.white2.move_left)
                self.master.bind("<Right>", self.white2.move_right)
                self.master.bind("<KeyPress-Down>", self.white2.guard)
                self.master.bind("<KeyRelease-Down>", self.white2.unguard)

                self.master.bind('<l>',
                                 lambda _: White2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: White2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: White2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: White2.ultAtk(self))
            
            elif selection2 == 3:
                top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
                top2.place(x=700, y=35)
                pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
                pBlack.place(x=729, y=95)

                self.black2 = Black2(self.canvas, 675, 380, "bFight2.png")
                self.master.bind("<Up>", self.black2.jump)
                self.master.bind("<Left>", self.black2.move_left)
                self.master.bind("<Right>", self.black2.move_right)
                self.master.bind("<KeyPress-Down>", self.black2.guard)
                self.master.bind("<KeyRelease-Down>", self.black2.unguard)

                self.master.bind('<l>',
                                 lambda _: Black2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: Black2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: Black2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: Black2.ultAtk(self))

            if timeLimit != 'infinite': #Check player's time limit selection
                self.time_limit = timeLimit #Set time limit to player's choice or default
                self.start_time = None
                self.remaining_time = self.time_limit
                self.start_timer()

                self.timer_label = Label(self.canvas, text="", font=('Modern 60 bold'), bg='#FF6D9E', fg='white') #Display time on screen
                self.timer_label.place(x=410, y=40)
                self.update_timer()
            else:
                self.timer_label = Label(self.canvas, text="∞", font=('Modern 60 bold'), bg='#FF6D9E', fg='white') #Otherwise do not start a timer and display infinity symbol on screen
                self.timer_label.place(x=410, y=40)

            self.pause = Button(self.canvas, text='Pause', bg='#6D97FF', fg='white', bd=1, font=('Modern 15 bold'), #Display pause button screen
                      command = self.pause_game, height=2, width=6)
            self.pause.place(x=410,y=490)

    def start_timer(self):
        self.start_time = time.time()

    def update_timer(self):
        if not self.paused: #Check if game isn't paused
            self.timer_label.config(text=str(self.remaining_time)) #Update timer on screen
            self.remaining_time -= 1
            if self.remaining_time < 0: #Check if the time has run out
                self.remaining_time = 0 #Make sure the time doesn't go below 0 on screen
                if self.health1 > self.health2: #Check which player has the most health
                    self.winners.append("Player 1") #Add player with the most health into the winners list
                elif self.health2 > self.health1:
                    self.winners.append("Player 2")
                else:
                    self.winners.append("Draw") #Otherwise add 'Draw' to the list
                lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white')
                lose.place(x=320, y=180)
                self.start_new_round()
        self.canvas.after(1000, self.update_timer) #Update the timer after every seconds

    def pause_game(self):
        if not self.paused: #Check if the game isn't already paused
            self.paused = True #Pause the game
            self.show_pause_frame()
            self.pause_characters()
            self.pause_timer()

    def resume_game(self):
        if self.paused: #Check if the game is paused
            self.paused = False #Unpause the game
            self.hide_pause_frame()
            self.resume_characters()
            self.resume_timer()

    def show_pause_frame(self):
        self.pause_frame = Frame(self.canvas, bg="#DA6BFF", bd=100)
        self.pause_frame.place(relx=0.5, rely=0.5, anchor="center")

        pause = Label(self.pause_frame, text="Pause", bg='#6D97FF', fg='white', font=('Modern 25 bold'))
        pause.pack(pady=20)

        resume_button = Button(self.pause_frame, text="Resume", fg='white', bg='#FF746C', bd=1, font=('Modern 17 bold'),
                               command=self.resume_game)
        resume_button.pack(pady=20)

        retry_button = Button(self.pause_frame, text="Retry", fg='white', bg='#FF746C', bd=1, font=('Modern 17 bold'),
                               command=self.retry)
        retry_button.pack(pady=20)

        inst_button = Button(self.pause_frame, text="How to play", fg='white', bg='#FF746C', bd=1, font=('Modern 17 bold'),
                               command=self.instructions)
        inst_button.pack(pady=20)

        chara_button = Button(self.pause_frame, text="Back to character selection", fg='white', bg='#FF746C', bd=1, font=('Modern 17 bold'),
                               command=self.battle_chara)
        chara_button.pack(pady=20)

        start_button = Button(self.pause_frame, text="Back to starting page", fg='white', bg='#FF746C', bd=1, font=('Modern 17 bold'),
                               command=self.battle_back)
        start_button.pack(pady=20)

    def instructions(self):
        howToPlay = Frame(self.canvas, bg="#6D97FF", bd=100)
        howToPlay.place(relx=0.5, rely=0.5, anchor="center")

        top = Label(howToPlay, text = "How to play", bg='#FF6D9E', fg='white', font=('Modern 20 bold'))
        top.pack(pady=10)
        
        left = Label(howToPlay, text="Player 1", bg='#FF6D9E', fg='white', font=('Modern 15 bold'))
        left.pack(pady=10)

        wasd2 = PhotoImage(file="wasd2.png")
        wasd2.image = wasd2
        wasd2_label = Label(howToPlay, image=wasd2, bg="#6D97FF", bd=0)
        wasd2_label.pack(pady=10)

        p1Atks = PhotoImage(file="p1Atks.png")
        p1Atks.image = p1Atks
        p1Atks_label = Label(howToPlay, image=p1Atks, bg="#6D97FF", bd=0)
        p1Atks_label.pack(pady=10)
        
        right = Label(howToPlay, text="Player 2", bg='#FF6D9E', fg='white', font=('Modern 15 bold'))
        right.pack(pady=10)

        arrows2 = PhotoImage(file="arrows2.png")
        arrows2.image = arrows2
        arrows2_label = Label(howToPlay, image=arrows2, bg="#6D97FF", bd=0)
        arrows2_label.pack(pady=10)
        
        p2Atks = PhotoImage(file="p2Atks.png")
        p2Atks.image = p2Atks
        p2Atks_label = Label(howToPlay, image=p2Atks, bg="#6D97FF", bd=0)
        p2Atks_label.pack(pady=10)

        close = Button(howToPlay, text='Close', fg='white', bg='#FF746C', bd=1, font=('Modern 20 bold'),
                      command = howToPlay.place_forget, height=1, width=4)
        close.pack(pady=10)
        
    def hide_pause_frame(self):
        self.pause_frame.place_forget() #Remove the pause frame from the screen

    def pause_timer(self):
        self.paused = True

    def resume_timer(self):
        self.paused = False   

    def pause_characters(self):
        self.master.unbind("<w>") #Unbind the keys of the characters so that they can't be used
        self.master.unbind("<a>")
        self.master.unbind("<d>")
        self.master.unbind("<e>")
        self.master.unbind("<r>")
        self.master.unbind("<t>")
        self.master.unbind("<q>")
        self.master.unbind("<Left>")
        self.master.unbind("<Right>")
        self.master.unbind("<Up>")
        self.master.unbind("<b>")
        self.master.unbind("<n>")
        self.master.unbind("<m>")
        self.master.unbind("<l>")
        self.master.unbind("<s>")
        self.master.unbind("<Down>")

    def resume_characters(self):
        if selection1 == 1: 
            self.master.bind("<w>", self.orange.jump) #Bind the keys to the characters so that they can be used again
            self.master.bind("<a>", self.orange.move_left)
            self.master.bind("<d>", self.orange.move_right)
            self.master.bind("<KeyPress-s>", self.orange.guard)
            self.master.bind("<KeyRelease-s>", self.orange.unguard)

            self.master.bind('<q>',
                             lambda _: Orange.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Orange.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Orange.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Orange.ultAtk(self))
            
        elif selection1 == 2:
            self.master.bind("<w>", self.white.jump)
            self.master.bind("<a>", self.white.move_left)
            self.master.bind("<d>", self.white.move_right)
            self.master.bind("<KeyPress-s>", self.white.guard)
            self.master.bind("<KeyRelease-s>", self.white.unguard)

            self.master.bind('<q>',
                             lambda _: White.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: White.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: White.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: White.ultAtk(self))
            
        elif selection1 == 3:
            self.master.bind("<w>", self.black.jump)
            self.master.bind("<a>", self.black.move_left)
            self.master.bind("<d>", self.black.move_right)
            self.master.bind("<KeyPress-s>", self.black.guard)
            self.master.bind("<KeyRelease-s>", self.black.unguard)

            self.master.bind('<q>',
                             lambda _: Black.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Black.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Black.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Black.ultAtk(self))
            
        if selection2 == 1:
            self.master.bind("<Up>", self.orange2.jump)
            self.master.bind("<Left>", self.orange2.move_left)
            self.master.bind("<Right>", self.orange2.move_right)
            self.master.bind("<KeyPress-Down>", self.orange2.guard)
            self.master.bind("<KeyRelease-Down>", self.orange2.unguard)

            self.master.bind('<l>',
                             lambda _: Orange2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Orange2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Orange2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Orange2.ultAtk(self))
        
        elif selection2 == 2:
            self.master.bind("<Up>", self.white2.jump)
            self.master.bind("<Left>", self.white2.move_left)
            self.master.bind("<Right>", self.white2.move_right)
            self.master.bind("<KeyPress-Down>", self.white2.guard)
            self.master.bind("<KeyRelease-Down>", self.white2.unguard)

            self.master.bind('<l>',
                             lambda _: White2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: White2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: White2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: White2.ultAtk(self))
        
        elif selection2 == 3:
            self.master.bind("<Up>", self.black2.jump)
            self.master.bind("<Left>", self.black2.move_left)
            self.master.bind("<Right>", self.black2.move_right)
            self.master.bind("<KeyPress-Down>", self.black2.guard)
            self.master.bind("<KeyRelease-Down>", self.black2.unguard)

            self.master.bind('<l>',
                             lambda _: Black2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Black2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Black2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Black2.ultAtk(self))

    def retry(self):
        self.resume_game() #Resume game after it was paused

        lose = Label(self.canvas, text='                                                ', font=('Modern 12'), bg='#6D97FF', fg='white')
        lose.place(x=320, y=180)

        self.winners = [] #Reset the winners list
        self.actualWinner = None #Reset the overall winner

        lose = Label(self.canvas, text=self.winners, font=('Modern 12'), bg='#FF6D9E', fg='white') #Reset winners on screen
        lose.place(x=320, y=180)
        
        self.health1 = 1000 #Reset the attributes
        self.energy1 = 500
        self.health2 = 1000
        self.energy2 = 500
        lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold')) #Display values in attributes on screen
        lHealth.place(x=200, y=42)
        lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lEnergy.place(x=200, y=95)
        lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lHealth.place(x=540, y=42)
        lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lEnergy.place(x=550, y=95)

        self.start_label = Label(self.canvas, text="Start!", font=('Modern 70 bold'), bg='#FF6D9E', fg='white')
        self.start_label.place(x=350, y=200)
        self.start_label.after(2000, self.start_label.place_forget)

        self.round_no = 1 #Reset the round number

        self.round_label = Label(self.canvas, text=f"Round {self.round_no}", font=('Modern 20 bold'), bg='#FF6D9E', fg='white') #Display the round number on screen
        self.round_label.place(x=405, y=140)

        if timeLimit != 'infinite':
            if self.start_time is not None:
                self.canvas.after_cancel(self.canvas.after(1000, self.update_timer)) #Stop the current timer if it's running
            self.start_time = None
            self.remaining_time = self.time_limit #Reset the timer
            self.start_timer() #Start the timer again

        if selection1 == 1: #Check which character has been chosen
            self.orange.canvas.delete(self.orange.imageID) #Remove the current character object from the screen

            self.orange = Orange(self.canvas, 200, 380, "oFight.png") #Display character image on screen at the reset position
            self.master.bind("<w>", self.orange.jump) #Bind the keys to the character class methods 
            self.master.bind("<a>", self.orange.move_left)
            self.master.bind("<d>", self.orange.move_right)
            self.master.bind("<KeyPress-s>", self.orange.guard)
            self.master.bind("<KeyRelease-s>", self.orange.unguard)

            self.master.bind('<q>',
                             lambda _: Orange.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Orange.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Orange.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Orange.ultAtk(self))
 
        elif selection1 == 2:
            self.white.canvas.delete(self.white.imageID)

            self.white = White(self.canvas, 200, 380, "wFight.png")
            self.master.bind("<w>", self.white.jump)
            self.master.bind("<a>", self.white.move_left)
            self.master.bind("<d>", self.white.move_right)
            self.master.bind("<KeyPress-s>", self.white.guard)
            self.master.bind("<KeyRelease-s>", self.white.unguard)

            self.master.bind('<q>',
                             lambda _: White.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: White.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: White.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: White.ultAtk(self))
            
        elif selection1 == 3:
            self.black.canvas.delete(self.black.imageID)

            self.black = Black(self.canvas, 200, 380, "bFight.png")
            self.master.bind("<w>", self.black.jump)
            self.master.bind("<a>", self.black.move_left)
            self.master.bind("<d>", self.black.move_right)
            self.master.bind("<KeyPress-s>", self.black.guard)
            self.master.bind("<KeyRelease-s>", self.black.unguard)

            self.master.bind('<q>',
                             lambda _: Black.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Black.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Black.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Black.ultAtk(self))
              
        if selection2 == 1:
            self.orange2.canvas.delete(self.orange2.imageID)

            self.orange2 = Orange2(self.canvas, 675, 380, "oFight2.png")
            self.master.bind("<Up>", self.orange2.jump)
            self.master.bind("<Left>", self.orange2.move_left)
            self.master.bind("<Right>", self.orange2.move_right)
            self.master.bind("<KeyPress-Down>", self.orange2.guard)
            self.master.bind("<KeyRelease-Down>", self.orange2.unguard)

            self.master.bind('<l>',
                             lambda _: Orange2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Orange2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Orange2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Orange2.ultAtk(self))
        
        elif selection2 == 2: 
            self.white2.canvas.delete(self.white2.imageID)

            self.white2 = White2(self.canvas, 675, 380, "wFight2.png")
            self.master.bind("<Up>", self.white2.jump)
            self.master.bind("<Left>", self.white2.move_left)
            self.master.bind("<Right>", self.white2.move_right)
            self.master.bind("<KeyPress-Down>", self.white2.guard)
            self.master.bind("<KeyRelease-Down>", self.white2.unguard)

            self.master.bind('<l>',
                             lambda _: White2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: White2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: White2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: White2.ultAtk(self))
        
        elif selection2 == 3:
            self.black2.canvas.delete(self.black2.imageID)

            self.black2 = Black2(self.canvas, 675, 380, "bFight2.png")
            self.master.bind("<Up>", self.black2.jump)
            self.master.bind("<Left>", self.black2.move_left)
            self.master.bind("<Right>", self.black2.move_right)
            self.master.bind("<KeyPress-Down>", self.black2.guard)
            self.master.bind("<KeyRelease-Down>", self.black2.unguard)

            self.master.bind('<l>',
                             lambda _: Black2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Black2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Black2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Black2.ultAtk(self))

    def start_new_round(self):
        if self.round_no == rounds: #Check if the round number has reached the amount chosen by the player
            self.end_battle()
        else:
            self.health1 = 1000 #Reset the attributes
            self.energy1 = 500
            self.health2 = 1000
            self.energy2 = 500
            lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lHealth.place(x=200, y=42)
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=200, y=95)
            lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lHealth.place(x=540, y=42)
            lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
            lEnergy.place(x=550, y=95)
            
            self.round_no += 1 #Increment the round number by one for the next round
            self.round_label.config(text=f"Round {self.round_no}") #Display the new round number on screen
            
            self.start_label = Label(self.canvas, text="", font=('Modern 70 bold'), bg='#FF6D9E', fg='white')
            self.start_label.place(x=260, y=200)
            self.start_label.config(text=f"Round {self.round_no} !")
            self.start_label.after(2000, self.start_label.place_forget)

            if timeLimit != 'infinite':                
                if self.start_time is not None:
                    self.canvas.after_cancel(self.canvas.after(1000, self.update_timer)) #Stop the current timer if it's running                
                self.start_time = None
                self.remaining_time = self.time_limit #Reset the timer                
                self.start_timer() #Start the timer again

            if selection1 == 1: #Check which character has been chosen
                self.orange.canvas.delete(self.orange.imageID) #Remove the current character object from the screen

                self.orange = Orange(self.canvas, 200, 380, "oFight.png") #Display character image on screen at the reset position
                self.master.bind("<w>", self.orange.jump) #Bind the keys to the character class methods 
                self.master.bind("<a>", self.orange.move_left)
                self.master.bind("<d>", self.orange.move_right)
                self.master.bind("<KeyPress-s>", self.orange.guard)
                self.master.bind("<KeyRelease-s>", self.orange.unguard)

                self.master.bind('<q>',
                                 lambda _: Orange.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: Orange.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: Orange.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: Orange.ultAtk(self))
     
            elif selection1 == 2:
                self.white.canvas.delete(self.white.imageID)

                self.white = White(self.canvas, 200, 380, "wFight.png")
                self.master.bind("<w>", self.white.jump)
                self.master.bind("<a>", self.white.move_left)
                self.master.bind("<d>", self.white.move_right)
                self.master.bind("<KeyPress-s>", self.white.guard)
                self.master.bind("<KeyRelease-s>", self.white.unguard)

                self.master.bind('<q>',
                                 lambda _: White.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: White.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: White.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: White.ultAtk(self))
                
            elif selection1 == 3:
                self.black.canvas.delete(self.black.imageID)

                self.black = Black(self.canvas, 200, 380, "bFight.png")
                self.master.bind("<w>", self.black.jump)
                self.master.bind("<a>", self.black.move_left)
                self.master.bind("<d>", self.black.move_right)
                self.master.bind("<KeyPress-s>", self.black.guard)
                self.master.bind("<KeyRelease-s>", self.black.unguard)

                self.master.bind('<q>',
                                 lambda _: Black.calcEnergy(self))
                self.master.bind('<e>',
                                 lambda _: Black.normalAtk(self))
                self.master.bind('<r>',
                                 lambda _: Black.specialAtk(self))
                self.master.bind('<t>',
                                 lambda _: Black.ultAtk(self))
                  
            if selection2 == 1:
                self.orange2.canvas.delete(self.orange2.imageID)

                self.orange2 = Orange2(self.canvas, 675, 380, "oFight2.png")
                self.master.bind("<Up>", self.orange2.jump)
                self.master.bind("<Left>", self.orange2.move_left)
                self.master.bind("<Right>", self.orange2.move_right)
                self.master.bind("<KeyPress-Down>", self.orange2.guard)
                self.master.bind("<KeyRelease-Down>", self.orange2.unguard)

                self.master.bind('<l>',
                                 lambda _: Orange2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: Orange2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: Orange2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: Orange2.ultAtk(self))
            
            elif selection2 == 2: 
                self.white2.canvas.delete(self.white2.imageID)

                self.white2 = White2(self.canvas, 675, 380, "wFight2.png")
                self.master.bind("<Up>", self.white2.jump)
                self.master.bind("<Left>", self.white2.move_left)
                self.master.bind("<Right>", self.white2.move_right)
                self.master.bind("<KeyPress-Down>", self.white2.guard)
                self.master.bind("<KeyRelease-Down>", self.white2.unguard)

                self.master.bind('<l>',
                                 lambda _: White2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: White2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: White2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: White2.ultAtk(self))
            
            elif selection2 == 3:
                self.black2.canvas.delete(self.black2.imageID)

                self.black2 = Black2(self.canvas, 675, 380, "bFight2.png")
                self.master.bind("<Up>", self.black2.jump)
                self.master.bind("<Left>", self.black2.move_left)
                self.master.bind("<Right>", self.black2.move_right)
                self.master.bind("<KeyPress-Down>", self.black2.guard)
                self.master.bind("<KeyRelease-Down>", self.black2.unguard)

                self.master.bind('<l>',
                                 lambda _: Black2.calcEnergy(self))
                self.master.bind('<b>',
                                 lambda _: Black2.normalAtk(self))
                self.master.bind('<n>',
                                 lambda _: Black2.specialAtk(self))
                self.master.bind('<m>',
                                 lambda _: Black2.ultAtk(self))

    def end_battle(self):
        self.pause_timer()
        self.pause_characters()

        self.end = Frame(self.canvas, bg='#FF746C')
        self.end.pack(fill="both", expand=True)

        if check == 1: #Check if the end battle screen is opening from the battle canvas
            self.end_screen = Frame(player2, bg='#FF746C')
            self.end_screen.pack(fill="both", expand=True)
        elif check == 2: #Check if the battle screen is opening from a battle that has been retried
            self.end_screen = Frame(self.end_screen, bg='#FF746C') 
            self.end_screen.pack(fill="both", expand=True)
        
        player1_wins = self.winners.count("Player 1") #Store how many times Player 1 has won stored in the winners list
        player2_wins = self.winners.count("Player 2") #Store how many times Player 2 has won stored in the winners list
        if player1_wins > player2_wins:
            self.actualWinner = "Player 1" 
            winner_label = Label(self.end_screen, text="Player 1 wins!", font=('Modern 50 bold'), bg='#DA6BFF', fg='white') #Declare Player 1 as the overall winner is they have more wins than Player 2
            winner_label.place(x=20, y=20)
        elif player1_wins < player2_wins:
            self.actualWinner = "Player 2"
            winner_label = Label(self.end_screen, text="Player 2 wins!", font=('Modern 50 bold'), bg='#DA6BFF', fg='white') #Declare Player 2 as the overall winner is they have more wins than Player 1
            winner_label.place(x=20, y=20)
        else:
            self.actualWinner = "Draw"
            winner_label = Label(self.end_screen, text="Draw!", font=('Modern 50 bold'), bg='#DA6BFF', fg='white') #Declare a draw otherwise
            winner_label.place(x=20, y=20)

        if self.actualWinner == "Player 1":
            if selection1 == 1:
                winner = PhotoImage(file="oWin.png") #Display winning image of Orange Cat if Player 1 won and is Orange Cat
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0) 
                winner_label.place(x=10, y=130)
                if selection2 == 1:
                    loser = PhotoImage(file="oLose.png") #Display losing image of Orange Cat if Player 2 lost and is Orange Cat
                elif selection2 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection2 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
            elif selection1 == 2:
                winner = PhotoImage(file="wWin.png")
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0)
                winner_label.place(x=10, y=130)
                if selection2 == 1:
                    loser = PhotoImage(file="oLose.png")
                elif selection2 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection2 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
            elif selection1 == 3:
                winner = PhotoImage(file="bWin.png")
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0)
                winner_label.place(x=10, y=130)
                if selection2 == 1:
                    loser = PhotoImage(file="oLose.png")
                elif selection2 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection2 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
        elif self.actualWinner == "Player 2":
            if selection2 == 1:
                winner = PhotoImage(file="oWin.png")
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0) #Display winning image of Orange Cat if Player 2 won and is Orange Cat
                winner_label.place(x=10, y=130)
                if selection1 == 1:
                    loser = PhotoImage(file="oLose.png")
                elif selection1 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection1 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
            elif selection2 == 2:
                winner = PhotoImage(file="wWin.png")
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0)
                winner_label.place(x=10, y=130)
                if selection1 == 1:
                    loser = PhotoImage(file="oLose.png")
                elif selection1 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection1 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
            elif selection2 == 3:
                winner = PhotoImage(file="bWin.png")
                winner.image = winner
                winner_label = Label(self.end_screen, image=winner, bg='#FF746C',bd=0)
                winner_label.place(x=10, y=130)
                if selection1 == 1:
                    loser = PhotoImage(file="oLose.png")
                elif selection1 == 2:
                    loser = PhotoImage(file="wLose.png")
                elif selection1 == 3:
                    loser = PhotoImage(file="bLose.png")
                loser.image = loser
                loser_label = Label(self.end_screen, image=loser, bg='#FF746C',bd=0)
                loser_label.place(x=300, y=200)
        else: #Otherwise if a draw display losing images for both players
            if selection1 == 1:
                draw1 = PhotoImage(file="oLose.png")
            elif selection1 == 2:
                draw1 = PhotoImage(file="wLose.png")
            elif selection1 == 3:
                draw1 = PhotoImage(file="bLose.png")
            draw1.image = draw1
            draw1_label = Label(self.end_screen, image=draw1, bg='#FF746C',bd=0)
            draw1_label.place(x=40, y=200)

            if selection2 == 1:
                draw2 = PhotoImage(file="oLose.png")
            elif selection2 == 2:
                draw2 = PhotoImage(file="wLose.png")
            elif selection2 == 3:
                draw2 = PhotoImage(file="bLose.png")
            draw2.image = draw2
            draw2_label = Label(self.end_screen, image=draw2, bg='#FF746C',bd=0)
            draw2_label.place(x=270, y=200)
            
        self.winners = [] #Reset winners list
        self.actualWinner = None #Reset the overall winner

        select = Canvas(self.end_screen, width=300, height=350, bg='#6D97FF', bd=0)
        select.place(x=510, y=120)
        
        retry_button = Button(select, text="Retry", fg='white', bg='#DA6BFF', bd=1, font=('Modern 17 bold'),
                               command=self.end_retry)
        retry_button.place(x=130, y=50)
        chara_button = Button(select, text="Back to character selection", fg='white', bg='#DA6BFF', bd=1, font=('Modern 17 bold'),
                               command=self.end_chara)
        chara_button.place(x=30, y=145)

        start_button = Button(select, text="Back to starting page", fg='white', bg='#DA6BFF', bd=1, font=('Modern 17 bold'),
                               command=self.end_back )
        start_button.place(x=60, y=240)

    def end_retry(self):
        self.canvas = Canvas(self.end_screen, bg='#6D97FF', width=863, height=600)
        self.canvas.pack()

        rectangle = Canvas(self.canvas, width=863, height=402, bg='#FF6D9E', bd=0)
        rectangle.place(x=0, y=439)

        global check
        check = 2 #Store 2 to keep track which screen is currently displayed on screen

        self.winners = [] #Reset winners list
        self.actualWinner = None #Reset the overall winner

        top1 = Label(self.canvas, text = "Player 1", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
        top1.place(x=40, y=35)

        self.start_label = Label(self.canvas, text="Start!", font=('Modern 70 bold'), bg='#FF6D9E', fg='white')
        self.start_label.place(x=350, y=200)
        self.start_label.after(2000, self.start_label.place_forget)

        self.round_no = 1 #Reset round number

        self.round_label = Label(self.canvas, text=f"Round {self.round_no}", font=('Modern 20 bold'), bg='#FF6D9E', fg='white')
        self.round_label.place(x=405, y=140)

        self.health1 = 1000 #Reset character attributes
        self.energy1 = 500
        lHealth = Label(self.canvas, text = ('Health:', self.health1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lHealth.place(x=200, y=42)
        lEnergy = Label(self.canvas, text = ('Energy:', self.energy1, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lEnergy.place(x=200, y=95)
        
        self.health2 = 1000
        self.energy2 = 500
        lHealth = Label(self.canvas, text = ('Health:', self.health2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lHealth.place(x=540, y=42)
        lEnergy = Label(self.canvas, text = ('Energy:', self.energy2, '   '), bg='#6D97FF', fg='white', font=('Modern 20 bold'))
        lEnergy.place(x=550, y=95)

        self.paused = False #Make sure game isn't paused

        if selection1 == 1: 
            pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
            pOrange.place(x=40, y=95)

            self.orange = Orange(self.canvas, 200, 380, "oFight.png") #Display character images on screen
            self.master.bind("<w>", self.orange.jump) #Bind keys to character's class method
            self.master.bind("<a>", self.orange.move_left)
            self.master.bind("<d>", self.orange.move_right)
            self.master.bind("<KeyPress-s>", self.orange.guard)
            self.master.bind("<KeyRelease-s>", self.orange.unguard)

            self.master.bind('<q>',
                             lambda _: Orange.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Orange.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Orange.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Orange.ultAtk(self))
 
        elif selection1 == 2:
            pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
            pWhite.place(x=40, y=95)

            self.white = White(self.canvas, 200, 380, "wFight.png")
            self.master.bind("<w>", self.white.jump)
            self.master.bind("<a>", self.white.move_left)
            self.master.bind("<d>", self.white.move_right)
            self.master.bind("<KeyPress-s>", self.white.guard)
            self.master.bind("<KeyRelease-s>", self.white.unguard)

            self.master.bind('<q>',
                             lambda _: White.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: White.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: White.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: White.ultAtk(self))
            
        elif selection1 == 3:
            pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
            pBlack.place(x=40, y=95)

            self.black = Black(self.canvas, 200, 380, "bFight.png")
            self.master.bind("<w>", self.black.jump)
            self.master.bind("<a>", self.black.move_left)
            self.master.bind("<d>", self.black.move_right)
            self.master.bind("<KeyPress-s>", self.black.guard)
            self.master.bind("<KeyRelease-s>", self.black.unguard)

            self.master.bind('<q>',
                             lambda _: Black.calcEnergy(self))
            self.master.bind('<e>',
                             lambda _: Black.normalAtk(self))
            self.master.bind('<r>',
                             lambda _: Black.specialAtk(self))
            self.master.bind('<t>',
                             lambda _: Black.ultAtk(self))
              
        if selection2 == 1:
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pOrange = Label(self.canvas, text = "Orange Cat", bg='#FF746C', fg='white', font=('Modern 20 bold'))
            pOrange.place(x=712, y=95)

            self.orange2 = Orange2(self.canvas, 675, 380, "oFight2.png")
            self.master.bind("<Up>", self.orange2.jump)
            self.master.bind("<Left>", self.orange2.move_left)
            self.master.bind("<Right>", self.orange2.move_right)
            self.master.bind("<KeyPress-Down>", self.orange2.guard)
            self.master.bind("<KeyRelease-Down>", self.orange2.unguard)

            self.master.bind('<l>',
                             lambda _: Orange2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Orange2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Orange2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Orange2.ultAtk(self))
        
        elif selection2 == 2: 
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pWhite = Label(self.canvas, text = "White Cat", bg='#F7E0FE', fg='white', font=('Modern 20 bold'))
            pWhite.place(x=729, y=95)

            self.white2 = White2(self.canvas, 675, 380, "wFight2.png")
            self.master.bind("<Up>", self.white2.jump)
            self.master.bind("<Left>", self.white2.move_left)
            self.master.bind("<Right>", self.white2.move_right)
            self.master.bind("<KeyPress-Down>", self.white2.guard)
            self.master.bind("<KeyRelease-Down>", self.white2.unguard)

            self.master.bind('<l>',
                             lambda _: White2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: White2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: White2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: White2.ultAtk(self))
        
        elif selection2 == 3:
            top2 = Label(self.canvas, text = "Player 2", bg='#FF6D9E', fg='white', font=('Modern 30 bold'))
            top2.place(x=700, y=35)
            pBlack = Label(self.canvas, text = "Black Cat", bg='#0D111D', fg='white', font=('Modern 20 bold'))
            pBlack.place(x=729, y=95)

            self.black2 = Black2(self.canvas, 675, 380, "bFight2.png")
            self.master.bind("<Up>", self.black2.jump)
            self.master.bind("<Left>", self.black2.move_left)
            self.master.bind("<Right>", self.black2.move_right)
            self.master.bind("<KeyPress-Down>", self.black2.guard)
            self.master.bind("<KeyRelease-Down>", self.black2.unguard)

            self.master.bind('<l>',
                             lambda _: Black2.calcEnergy(self))
            self.master.bind('<b>',
                             lambda _: Black2.normalAtk(self))
            self.master.bind('<n>',
                             lambda _: Black2.specialAtk(self))
            self.master.bind('<m>',
                             lambda _: Black2.ultAtk(self))

        if timeLimit != 'infinite': #Check player's time limit choice
            self.start_time = None
            self.remaining_time = self.time_limit #Reset timer
            self.start_timer() #Start timer again
            self.timer_label = Label(self.canvas, text="", font=('Modern 60 bold'), bg='#FF6D9E', fg='white') #Display timer on screen
            self.timer_label.place(x=410, y=40)
        else:
            self.timer_label = Label(self.canvas, text="∞", font=('Modern 60 bold'), bg='#FF6D9E', fg='white') #Otherwise display infinity symbol in place of timer
            self.timer_label.place(x=410, y=40)

        self.pause = Button(self.canvas, text='Pause', bg='#6D97FF', fg='white', bd=1, font=('Modern 15 bold'),
                  command = self.pause_game, height=2, width=6)
        self.pause.place(x=410,y=490)

    def end_chara(self):
        global selection1
        global selection2
        selection1 = 0 #Reset selections
        selection2 = 0
        self.end_screen.destroy() #Go back to character selection frame from end battle frame
        self.canvas.destroy()
        player2.destroy()
        start.destroy()
        self.charaSelect1()

    def end_back(self):
        global selection1
        global selection2
        selection1 = 0 #Reset selections
        selection2 = 0
        self.end_screen.destroy() #Go back to starting screen from end battle frame
        self.canvas.destroy()
        player2.destroy()
        start.destroy()

    def battle_chara(self):
        global selection1
        global selection2
        selection1 = 0 #Reset selections
        selection2 = 0
        self.canvas.destroy() #Go back to character selection frame from battle
        player2.destroy()
        start.destroy()
        self.charaSelect1()

    def battle_back(self):
        global selection1
        global selection2
        selection1 = 0 #Reset selections
        selection2 = 0
        self.canvas.destroy() #Go back to starting screen from battle
        player2.destroy()
        start.destroy()
        
if __name__ == '__main__':
    root = Tk()
    game = Game(root)
    game.mainloop()
