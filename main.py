import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import time
import random

should_exit = False

window = tk.Tk()
window.title("Disappearing Text Writing App")
window.geometry("800x600")


def save_file():
    content = text_area.get(1.0, "end")

    filepath = tk.filedialog.asksaveasfilename(defaultextension=".txt")

    with open(filepath, "w") as file:
        file.write(content)


def on_focus_in():
    if "Write your text here..." in text_area.get(1.0, "end"):
        text_area.delete(1.0, "end")


def check_time():
    global should_exit
    if time.time() >= end:
        should_exit = True
        window.destroy()
    else:
        text_area.after(1000, check_time)


def reset_timer(event):
    global start, end, should_exit
    start = time.time()
    end = start + random.randint(5, 10)
    should_exit = False
    text_area.after(1000, check_time)


# def on_focus_out():
#     if text_area.get(1.0, "end") == "":
#         text_area.insert(1.0, "Write your text here...")


text_area = tk.Text(window, width=96, height=30, wrap='word')
text_area.insert(1.0, "Write your text here...")
text_area.bind("<Key>", reset_timer)
text_area.pack(pady=10)

text_focus_in = text_area.bind('<Button-1>', lambda x: on_focus_in())
# text_focus_out = text_area.bind('<FocusOut>', lambda x: on_focus_out())

save_btn = tk.Button(window, text="Save", command=save_file)
save_btn.pack(pady=10)

window.mainloop()
