import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.minsize(300, 200)
root.title("Jitsi Music Bot")

#logo
logo = tk.PhotoImage(file="jitsi-logo-blue-grey-text.png")
logoImage = tk.Label(image=logo)
logoImage.pack()

#title
heading = tk.Label(root, text="Jitsi Music Bot", font="Helvetica 20 bold", pady=10)
heading.pack()

#description
description = tk.Label(root, text="A simple music bot for Jitsi", font="Helvetica 10", pady=10)
description.pack()

#Variables
meetLink = tk.StringVar()
chromedriverPath = tk.StringVar()

#function
def start():
    startBtnText.set("Stop Bot")
    print(meetLink.get())
    print(chromedriverPath.get())

#meet link
meetLinkLabel = tk.Label(root, text="Enter the meet link", font="Helvetica 10", pady=10)
meetLinkLabel.pack()

#meet link input
meetLinkInput = tk.Entry(root, width=50, textvariable=meetLink)
meetLinkInput.pack()

#path to chromedriver
chromedriverPathLabel = tk.Label(root, text="Enter the path to chromedriver", font="Helvetica 10", pady=10)
chromedriverPathLabel.pack()

#path to chromedriver input
chromedriverPathInput = tk.Entry(root, width=50, textvariable=chromedriverPath)
chromedriverPathInput.pack()

#start button
startBtnText = tk.StringVar()
startButton = tk.Button(root, textvariable=startBtnText, command=start ,font="Helvetica", bg="#1D76BC", fg="white", height=1, width=12, pady=10)
startBtnText.set("Start Bot")
startButton.pack()

root.mainloop()