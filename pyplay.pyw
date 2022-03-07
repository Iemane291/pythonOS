import os

from tkinter import *
from playsound import playsound

window = Tk()
window.title("pyPlay")
window.geometry("500x500")

chosenSound = Listbox(window)
chosenSound.pack()


randomThing = 0
for i in os.listdir('pyPlay/sounds'):
    if i != 'readme.txt' and i.endswith(".mp3") or i.endswith(".wav"):
        randomThing += 1
        chosenSound.insert(randomThing, i)

def playSound():
    for i in chosenSound.curselection():
        playsound("pyPlay/sounds/"+chosenSound.get(i))



label1 = Label(window, text="Select the sound you would like to play.", height=2).pack()

playButton = Button(window, text="Play selected sound", command=playSound)
playButton.pack()

window.mainloop()