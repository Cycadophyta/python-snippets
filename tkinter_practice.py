import tkinter as tk

window = tk.Tk()
frame = tk.Frame()

label = tk.Label(master=frame, text='Name', width=10, height=2)
#button = tk.Button(text='Click', width=25, height=5)
entry = tk.Entry(width = 10)

label.pack()
entry.pack()

name = entry.get()

label2 = tk.Label(text=name)
label2.pack()

window.mainloop()