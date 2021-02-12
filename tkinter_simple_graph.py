# Imports

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
# Imports end

LARGE_FONT = ('Verdana', 12)

class GUI(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default='')
        tk.Tk.wm_title(self, 'GUI')
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(
            self, text='PageOne',
            command=lambda: controller.show_frame(PageOne)
        )
        button.pack()
        
        button2 = ttk.Button(
            self, text='PageTwo',
            command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(
            self, text='Back to Home',
            command=lambda: controller.show_frame(StartPage)
        )
        button.pack()
        
        button2 = tk.Button(
            self, text='Page Two',
            command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()
        
        
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(
            self, text='Back to Home',
            command=lambda: controller.show_frame(StartPage)
        )
        button.pack()
        
        button2 = ttk.Button(
            self, text='Page One',
            command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()


class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(
            self, text='Back to Home',
            command=lambda: controller.show_frame(StartPage)
        )
        button.pack()
        
        f = Figure(figsize=(5,5), dpi=100)

app = GUI()
app.mainloop()