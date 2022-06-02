#!/usr/bin/env python3

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename



dictionary = {
              "Hui":"Vasiliy",
              "pizda":"Nadezda",
              "poezda":"prjatki",
                                 }



def text_edit():
    with open ("hui.txt") as t:
        text = t.readlines()[0]
        print(text)
        t.close()


    for i in dictionary:
        text=text.replace(i,dictionary[i])
    txt_edit.delete('1.0', tk.END)
    txt_edit.insert(tk.END, text)

    print(text)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Open text to edit - {filepath}")


def open_csv():
    """Open a CSV."""
    filepath = askopenfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        #txt_edit.insert(tk.END, text)
    window.title(f"Load words to replace - {filepath}")    

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

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Load Text", command=open_file)
btn_csv =  tk.Button(frm_buttons, text="Load CSV", command=open_csv)
btn_repl = tk.Button(frm_buttons, text="Replace words", command=text_edit)
btn_save = tk.Button(frm_buttons, text="Save As ...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_csv.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_repl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()



    
