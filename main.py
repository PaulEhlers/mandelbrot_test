from tkinter import *
from Mandelbrot import Mandelbrot

master = Tk()
master["bg"] = "#000000"
master.configure(background='black')
master.title("Hello!")
height = 700
width = 1200


can = Canvas(master, width=width, height=height)
can.pack()
img = PhotoImage(width=width, height=height)
can.create_image((width/2, height/2), anchor=CENTER, image=img, state="normal")
mandel = Mandelbrot()
iterations = 50
for x in range (width):
    for y in range (height):
        ax = 2.25*(x-width/1.3)/width
        ay = 2.25*(y-height/2)/height
        n, r, i = mandel.calc_mandelbrot(ax, ay, 10, iterations)
        if n < 50:
            rgb = int(n/iterations*256)
            color = '#%02x%02x%02x' % (rgb, rgb, rgb)
            img.put(color, (x, y))
        else:
            img.put("#000000", (x, y))

can.configure(background='black')
master.mainloop()

