from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    if filename:
        with open(filename, 'w') as f:
            f.write(t)
    else:
        saveAs()

def saveAs():
    file = asksaveasfile(mode='w', defaultextension='.txt')
    if file:
        filename = file.name
        t = text.get(0.0, END)
        try:
            file.write(t.rstrip())
        except Exception as e:
            showerror(title="Oops!", message=f"Unable to save the file: {e}")
        finally:
            file.close()

def openFile():
    file = askopenfile(mode='r')
    if file:
        t = file.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        file.close()

root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
