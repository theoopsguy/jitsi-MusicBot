import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.minsize(300, 200)

logo = tk.PhotoImage(file="jitsi-logo-blue-grey-text.png")
label = tk.Label(image=logo)
label.pack()

heading = tk.Label(root, text="Jitsi Music Bot", font="Helvetica 20 bold")
heading.pack()

root.mainloop()