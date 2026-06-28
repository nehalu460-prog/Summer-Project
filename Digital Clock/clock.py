from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")

def update_time():
    time_string = strftime("%I:%M:%S %p")
    date_string = strftime("%d-%m-%Y")

    time_label.config(text=time_string)
    date_label.config(text=date_string)

    time_label.after(1000, update_time)

time_label = Label(
    root,
    font=("Arial", 45, "bold"),
    bg="black",
    fg="cyan"
)
time_label.pack(pady=20)

date_label = Label(
    root,
    font=("Arial", 18),
    bg="black",
    fg="white"
)
date_label.pack()

update_time()

root.mainloop()
