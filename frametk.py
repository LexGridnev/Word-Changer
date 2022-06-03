import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(window, bg='gold')
frame1.pack(fill=tk.X)
frame1.columnconfigure(0, weight=1)
frame2 = tk.Frame(window, padx=15, pady=15)
frame2.pack()

frame1label1 = tk.Label(frame1, bg='gold', text='Top label')
frame1label1.grid(row=0, column=0)
frame2label = tk.Label(frame2, text='Bottom label')
frame2label.pack()

window.mainloop()