import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.minsize(400, 380)
root.title("Jitsi Music Bot")

#logo
logo = tk.PhotoImage(file="jitsi-logo-blue-grey-text.png")
logoImage = tk.Label(image=logo)
logoImage.pack(pady=10)

#title
heading = tk.Label(root, text="Jitsi Music Bot", font="opensans 20 bold", pady=10)
heading.pack()

#description
description = tk.Label(root, text="A simple music bot for Jitsi", font="opensans 10", pady=10)
description.pack()

#Variables
meetLink = tk.StringVar()
chromedriverPath = tk.StringVar()

#function
def start():
    startBtnText.set("Stop Bot")
    print(meetLink.get())
    print(chromedriverPath.get())

#meet link input
meetLinkLabel = tk.Label(root, text="Enter the meet link", font="opensans 10", pady=10)
meetLinkLabel.pack()
meetLinkInput = tk.Entry(root, width=50, textvariable=meetLink)
meetLinkInput.pack()

#path to chromedriver input
chromedriverPathLabel = tk.Label(root, text="Enter the path to chromedriver", font="opensans 10", pady=10)
chromedriverPathLabel.pack()
chromedriverPathInput = tk.Entry(root, width=50, textvariable=chromedriverPath)
chromedriverPathInput.pack()

#start button
startBtnText = tk.StringVar()
startButton = tk.Button(root, textvariable=startBtnText, command=start ,font="opensans", bg="#1D76BC", fg="white", height=1, width=12)
startBtnText.set("Start Bot")
startButton.pack(pady=20)

root.mainloop()