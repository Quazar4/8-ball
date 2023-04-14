# Magic 8 Ball
from tkinter import *
import random
app = Tk()
app.title("🎱 Magic 8 Ball")
app.geometry("241x180")
outputs = ["                Yes                ", "                  No                  ", "       It is decidedly so      ", "       Supposedly not      ", "Hazy reply, Try again", "      Without a doubt     "]
app.configure(background="Black")

Label(app, text="Ask a question and run", fg="white", bg="black", font="Times 24").grid(row=1, column=1)
Label(app, text="", bg="black").grid(row = 2, column=1)
def rerun():
    global x
    for i in range(1):


        text = StringVar()
        Label(app, textvariable=text, fg="Green", bg="black", font="Times 24").grid(row=6, column=1)
        text.set(random.choice(outputs))

Label(app, text="Answer:", fg="blue", bg="black", font="Times 24").grid(row=5, column=1)

buttontext = StringVar()
Button(app, textvariable=buttontext, command=rerun, width=6, height=2).grid(row=4, column=1)
buttontext.set("Run")

app.mainloop()

