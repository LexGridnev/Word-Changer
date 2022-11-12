#!/usr/bin/env python3

import csv, string
from gc import callbacks
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename




# Get text from Editor
def text_input() -> str: 
    input = txt_edit.get("1.0", tk.END) 
    if input == "": # If nothing is found in Editor
        return "No text found in editor. Please enter text."
    else:
        return input

#Words replace function 
def text_edit():
    txt_edit.configure(state='normal') # enables the text box to be edited
    text = text_input() # assigns the text input to a variable
    file_csv = [i.split(',') for i in csv_edit.get("1.0",tk.END).strip('\n').split("\n", 2)] # splits the csv file into a list, each item in the list is a list of the csv file's items split by the comma
    file_dictionary = dict(file_csv) # assigns the list to a variable
    for i in file_dictionary: # for each item in the dictionary
        text = text.replace(i,file_dictionary[i].strip(" ")) # replaces the item in the text with the item in the dictionary
        
        txt_edit.delete('1.0', tk.END) # deletes the text from the text box
        txt_edit.insert(tk.END,text.replace(i,file_dictionary[i])) # inserts the new text into the text box

    txt_edit.delete('1.0', tk.END) # deletes the text from the text box
    txt_edit.insert(tk.END, text) # inserts the new text into the text box
    txt_edit.configure(state='disabled') # disables the text box from being edited

    file_hl = [i.split(',')[1] for i in csv_edit.get("1.0",tk.END).strip('\n').split("\n", 2)] # splits the csv file into a list, each item in the list is a list of the csv file's items split by the comma
    for target in file_hl: # for each item in the list
        start_pos = txt_edit.search(target, '1.0', stopindex=tk.END) # searches for the item in the text box
        if start_pos: # if the item is found
            end_pos = '{}+{}c'.format(start_pos, len(target)) # assigns the end position of the item to a variable
            txt_edit.tag_add(target, start_pos, end_pos) # adds a tag to the item

    for name in txt_edit.tag_names(index=None): # for each item in the text box
        txt_edit.tag_config(name, foreground='green') # changes the color of the item to green

    #print(text)

#highlight text to replace
def text_hl():
    file_hl = [i.split(',')[0] for i in csv_edit.get("1.0",tk.END).strip('\n').split("\n", 2)]
    print(file_hl)
    for target in file_hl:
        print(target)
        start_pos = txt_edit.search(target, '1.0', stopindex=tk.END)
        
        if start_pos:
            end_pos = '{}+{}c'.format(start_pos, len(target))
            print('{!r}'.format(end_pos))
            txt_edit.tag_add(target, start_pos, end_pos)

    for name in txt_edit.tag_names(index=None):
        print(name,len(name))
        txt_edit.tag_config(name, foreground='red')

def rvr_txt():
    txt_edit.configure(state='normal') # make the text field editable
    csv_txt = csv_edit.get("1.0",tk.END).strip('\n').split("\n") # get the text from the text field, strip the last newline character and split it on each newline character
    text = [i.split(',') for i in csv_txt ] # split each line on the comma
    rvr_txt = [i[::-1] for i in text] # reverse the order of each line
    csv_edit.delete('1.0', tk.END) # delete the text from the text field
    
    for i in rvr_txt: # loop through each line in the reversed text field
        csv_edit.insert(tk.END, i[0].strip(" ") + "," + i[1].strip(" ") + " \n") # insert the reversed text back into the text field with a newline character at the end of each line
        
    if len(text) <= 0: # check if there is any text in the text field
        csv_edit.delete('1.0', tk.END) # delete the text from the text field

    txt_edit.configure(state='disabled') # make the text field non-editable

def open_file():
    """Open a file for editing."""
    txt_edit.configure(state='normal') #edit mode enabled
    txt_edit.delete('1.0', tk.END) #delete all text
    filepath: str = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath: #if no file is selected
        return
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text: str = input_file.read() 
        txt_edit.insert(tk.END, text) 
    txt_edit.configure(state='disabled') #read mode , edit mode disbled
    window.title(f"Open text to edit - {filepath}") 

def is_csv(input_file):
    try:
        with open(input_file, newline='') as csvfile: 
            start = csvfile.read(4096) # read the first 4096 bytes

            # isprintable does not allow newlines, printable does not allow umlauts...
            if not all([c in string.printable or c.isprintable() for c in start]):
                return False # if the file contains non-printable characters, it is not a csv file
            dialect = csv.Sniffer().sniff(start)
            return True
    except csv.Error: # if the file is not a csv file
        # Could not get a csv dialect -> probably not a csv.
        print("Could not get a csv dialect -> probably not a csv.") 
        return False

def open_csv():
    """Open a CSV."""
    filepath = askopenfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    
    csv_edit.delete("1.0", tk.END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        if is_csv(filepath):
            csv_edit.insert(tk.END, text)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Save edited text - {filepath}")

def txt_undo():
    txt_edit.configure(state='normal') 
    txt_edit.edit_undo()
    txt_edit.configure(state='disabled') 
    #print("txt_undo")

def txt_redo():    
    txt_edit.configure(state='normal') 
    txt_edit.edit_redo()
    txt_edit.configure(state='disabled') 
    #print("txt_redo")

window = tk.Tk()
window.title("Simple Words Replacer")
window.rowconfigure(0, minsize=100, weight=0)
window.columnconfigure(0, minsize=100, weight=0)

txt_edit = tk.Text(window,undo = True)
csv_edit = tk.Text(window,undo = True)

frm_buttons = tk.Frame(window)
csv_buttons = tk.Frame(window)
csv_undored = tk.Frame(csv_buttons)
frm_buttons = tk.Frame(window)
frm_undored = tk.Frame(frm_buttons)


btn_open = tk.Button(frm_buttons, text = "Load Text",     command = open_file)
btn_repl = tk.Button(frm_buttons, text = "Replace words", command = text_edit)
btn_save = tk.Button(frm_buttons, text = "Save As ...",   command = save_file)
btn_csv  = tk.Button(csv_buttons, text = "Load CSV",      command = open_csv)
btn_hl   = tk.Button(csv_buttons, text = "Highlight",     command = text_hl)
btn_rvr  = tk.Button(csv_buttons, text = "Revert",        command = rvr_txt)
btn_undo = tk.Button(csv_undored, text = "⊲",             command = csv_edit.edit_undo)
btn_redo = tk.Button(csv_undored, text = "⊳",             command = csv_edit.edit_redo)
btn_und  = tk.Button(frm_undored, text = "⊲",             command = txt_undo)
btn_red  = tk.Button(frm_undored, text = "⊳",             command = txt_redo)


btn_open.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
btn_repl.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
btn_save.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

btn_csv.grid (row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_hl.grid  (row=2, column=0, sticky="nsew",   padx=5, pady=5)
btn_rvr.grid (row=3, column=0, sticky="nsew",   padx=5, pady=5)


btn_undo.grid(row=0, column=0, sticky="nsew",    padx=5, pady=5)
btn_redo.grid(row=0, column=1, sticky="nsew",    padx=5, pady=5)
btn_und.grid(row=0, column=0, sticky="ns",    padx=5, pady=5)
btn_red.grid(row=0, column=1, sticky="ns",    padx=5, pady=5)


frm_buttons.grid(row=0, column=0, sticky="nsew")
csv_buttons.grid(row=0, column=3, sticky="nsew")
csv_undored.grid(row=0, column=0, sticky="nsew")
frm_undored.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")
csv_edit.grid(row=0, column=2, sticky="nsew")

#window.after(50000, window.destroy)
window.mainloop()