#!/usr/bin/env python3

import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Get text from Editor
def text_input():
    input = txt_edit.get("1.0",tk.END)
    return input



#Words replace function 
def text_edit():
    txt_edit.configure(state='normal')
    text = text_input()
    file_csv = [i.split(',') for i in csv_edit.get("1.0",tk.END).strip('\n').split("\n", 2)]
    print(file_csv)
    file_dictionary = dict(file_csv)
    print(file_dictionary)
    for i in file_dictionary:
        text = text.replace(i,file_dictionary[i])
    txt_edit.delete('1.0', tk.END)
    txt_edit.insert(tk.END, text)
    txt_edit.configure(state='disabled')

    #print(text)

def open_file():
    """Open a file for editing."""
    txt_edit.configure(state='normal')
    txt_edit.delete('1.0', tk.END)
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        txt_edit.configure(state='disabled') #read mode , edit mode disbled
    window.title(f"Open text to edit - {filepath}")


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
        csv_edit.insert(tk.END, text)
    window_csv.title(f"words to replace")


#############################3
'''
new_path = open("mytest.csv", "w")

file_dictionary = {
              "Hui":"Vasiliy",
              "pizda":"Nadezda",
              "poezda":"prjatki",
                                 }

z = csv.writer(new_path)
for new_k, new_v in file_dictionary.items():
    z.writerow([new_k, new_v])

new_path.close()


'''
##############################

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

window = tk.Tk()
window.title("Simple Words Replacer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

window_csv = tk.Tk()
window_csv.title("Simple Words Replacer")
window_csv.rowconfigure(0, minsize=800, weight=0)
window_csv.columnconfigure(0, minsize=50, weight=0)

txt_edit = tk.Text(window)
csv_edit = tk.Text(window_csv)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
csv_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Load Text", command = open_file)
btn_csv =  tk.Button(csv_buttons, text="Load CSV", command = open_csv)
btn_repl = tk.Button(frm_buttons, text="Replace words", command = text_edit)
btn_save = tk.Button(frm_buttons, text="Save As ...", command = save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_csv.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_repl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
csv_buttons.grid(row=0, column=2, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
csv_edit.grid(row=0, column=1, sticky="nsew")

window_csv.mainloop()
window.mainloop()



    
