from tkinter import *
from googletrans import LANGUAGES
from tkinter import ttk
from googletrans import Translator
root = Tk()
root.geometry("500x500")
root.configure(bg = "teal")
root.title("Project 181")
list1 = list(LANGUAGES.values())

dropdown = ttk.Combobox(root, state = "readonly", values = list1)
dropdown.place(relx = 0.7, rely = 0.2, anchor = CENTER)
dropdown.set("english")
output = Label(root, text = "Output", bg = "teal", font = ("Bahnscrift Light", 15, "bold"))
output.place(relx = 0.3, rely = 0.6, anchor = CENTER)
dropdown2 = ttk.Combobox(root, state = "readonly", value = list1, width = 3)
dropdown2.place(relx = 0.7, rely = 0.6, anchor = CENTER)
dropdown2.set("Choose output language")
text = Text(root, bg = "teal", font = ("Bhanschrift Light", 15), wrap = WORD, height = 20, width = 10, padx = 15, pady = 15)
text.place(relx = 0.5, rely = 0.4, anchor = CENTER)
text2 = Text(root, bg = "teal", font = ("Bhanschrift Light",15), wrap = WORD, height = 20, width = 10, padx = 15, pady = 15)
text2.place(relx = 0.5, rely = 0.6, anhcor = CENTER)

def Translate() :
    d1 = dropdown.get()
    d2 = dropdown2.get()
    txt = text.get()
    txt2 = text2.get()
    tr = Translator()
    
    try :
        trn = translator.translate(text = txt, src = d1, dest = d2)
        text2.delete(1.0,END)
        text2.insert(END, translated.text)
        
    except :
        print("Try again")

btn1 = Button(root, text = "Translate", font = ("Helvetica",15), bg = "white", fg = "black", activebackground = "teal", relief = FLAT, pady = 5, command = Translate)
btn1.lace(relx = 0.5, rely = 0.8, anchor = CENTER)
footer = Label(root, text = "Created BY the WhiteHatJR Team", bg = "grey")
footer.place(relx = 0.5, rely = 0.9)
root.mainloop()