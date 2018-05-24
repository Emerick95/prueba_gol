from tkinter import *
tk= Tk()
canvas =Canvas(tk,width=800, height=400)
canvas.pack()

my_image=PhotoImage(file="porteria.gif")
canvas.create_image(0,0,anchor=NW,image=my_image)

my_imagex=PhotoImage(file="pelota.gif")
canvas.create_image(700,100,anchor=NW,image=my_imagex)


def movetriangle(event):
    if event.keysym=='Up':
        canvas.move(2,0,-3)
        print(str(canvas.move))
    elif event.keysym=='Down':
        canvas.move(2,0,3)
    elif event.keysym=='Left':
        canvas.move(2,-3,0)
    else:
        canvas.move(2,3,0)
        

canvas.bind_all('<KeyPress-Up>',movetriangle)
canvas.bind_all('<KeyPress-Down>',movetriangle)
canvas.bind_all("<KeyPress-Left>", movetriangle)
canvas.bind_all("<KeyPress-Right>", movetriangle)

tk.mainloop()