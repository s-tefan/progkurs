import tkinter as tk
from tkinter import ttk

def submit():
    print("Välkommen,", namn.get())
    ttk.Label(frm, text=f'Välkommen, {namn.get()}!').grid(column=0, row=2)
    namn.set('')

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="Namn?").grid(column=0, row=1)
namn = tk.StringVar()
namn_label = ttk.Label(frm, text='Namn')
namn_entry = ttk.Entry(frm, textvariable = namn)
namn_entry.grid(column=1, row = 1)
sub_btn = ttk.Button(frm, text="Submit", command = submit).grid(column=2, row=1)

root.mainloop()
