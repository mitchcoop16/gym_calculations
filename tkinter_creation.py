from tkinter import *
from tkinter import ttk

class Tkinter_creation():

    #require frame, label text, command, row, column
    #Creates a new button
    def create_button(frame, label_text, com, r, c):
        new_button = Button(frame, text=label_text, command=com)
        new_button.grid(column=c, row=r, sticky='nswe')

    #require frame, label text, text variable, row, column
    #Creates a label and an Entry to the right of it
    def create_entry_label(frame, label_text, txt_var, r, c):
        new_label = Label(frame, text=label_text)
        new_entry = Entry(frame, textvariable=txt_var)
        new_label.grid(column=c-1, row=r, sticky='w', padx=5, pady=5)
        new_entry.grid(column=c, row=r, sticky='nswe', padx=5, pady=5)
        
    #require frame, label text, row, column
    #Creates a new label
    def create_label(frame, label_text, r, c):
        new_label = Label(frame, text=label_text)
        new_label.grid(column=c, row=r, sticky='w', padx=5, pady=5)

    #require frame, label text, variable name, value of variable, row, column
    #Creates a new radio button
    def create_radio_button(frame, label_text, var, val, r, c):
        new_rbutton = Radiobutton(frame, text=label_text, variable=var, value=val)
        new_rbutton.grid(column=c, row=r)

    #requires frame, width, textvariable, row, column, values
    #creates a new combo box
    def create_combo_box(frame, w, tx, r, c, values):
        new_combo_box = ttk.Combobox(frame, width = w, textvariable = tx)
        new_combo_box.grid(column=c, row=r)
        new_combo_box['values'] = (values)
        new_combo_box.current(0)
        