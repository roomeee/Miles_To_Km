import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    mile = entry_int.get()
    km = mile *1.61
    output_string.set(km)


window = ttk.Window(themename= 'journal')
window.title('demo')
window.geometry('300x150')

title_label = ttk.Label(master=window, text= 'Miles to kilometers', font= 'Arial 24 bold')
title_label.pack()

input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable= entry_int)
button = ttk.Button(master= input_frame, text='Convert', command=convert)
entry.pack(side = "left", padx = 10)
button.pack(side= "left")
input_frame.pack(pady= 10)


output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font= 'Arial 23', textvariable=output_string)
output_label.pack(pady=5)
window.mainloop()