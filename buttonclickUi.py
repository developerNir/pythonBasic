
import tkinter as tk
win = tk.Tk()
y =0

def sayHi():
    print("what is your name")
    print("\n Nirapadak")


win.geometry("200x200")

b = tk.Button(
    win,
    text="Click",
    command=sayHi
)


b.pack()
win.mainloop()
