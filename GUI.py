from tkinter import *
def function(t):
    print("Great work")
window = Tk()
window.bind("<q>", function)
window.mainloop()