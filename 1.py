import tkinter as tk

win = tk.Tk()
win.title('приветствие')

label1 = tk.Label(
    text = 'name: ',
    fg = "white",
    bg = "#F999B7",
    width = 20,
    height = 1
)
label1.pack()

entry1=tk.Entry(fg="black",bg="#F9C5D5",width=7)

entry1.pack()

border_effects = {"sunken": tk.SUNKEN,}

for relief_name, relief in border_effects.items():
    frame1=tk.Frame(master=win, relief=relief, borderwidth=5)

    text1 = tk.Text(
        master=frame1,
        fg="black",
        bg="#F9C5D5",
        height=10,
        width=15
    )
    text1.pack()
    label2=tk.Label(master=frame1, text=relief_name)
    label2.pack()
    frame1.pack(side=tk.RIGHT)

button1 = tk.Button(
    master=win,
    text='жми',
    width=10,
    height=2,
    fg="black",
    bg="#FEE3EC"
)
button1.pack(side=tk.RIGHT)

win.mainloop()
# win.destroy()