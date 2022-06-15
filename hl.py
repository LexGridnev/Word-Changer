import tkinter as tk
root = tk.Tk()
text = tk.Text(root)
text.pack()
text.insert(tk.END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
target = 'ipsum'
start_pos = text.search(target, '1.0', stopindex=tk.END)
print ('{!r}'.format(start_pos))
if start_pos:
    end_pos = '{}+{}c'.format(start_pos, len(target))
    print('{!r}'.format(end_pos))
    text.tag_add('highlight', start_pos, end_pos)
    text.tag_config('highlight', foreground='red')

root.mainloop()