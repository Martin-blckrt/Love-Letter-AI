from PIL import Image, ImageTk
import tkinter as tk


def play2players():
    print("2 players")


root = tk.Tk()

canvas = tk.Canvas(master=root)

background = Image.open("assets/Background.png")
img = ImageTk.PhotoImage(background, size=(500, 200))
bg = canvas.create_image(0, 0, image=img)
canvas.pack()

"""
image = Image.open("assets/cards/Back-min.png")
btnPhoto = ImageTk.PhotoImage(image)

imgBtn = tk.Button(canvas, image=btnPhoto) # check command argument
imgBtn.pack()
"""

root.mainloop()


