from tkinter import filedialog
from tkinter import *
from image_handler import ImageHandler

# Making TKinter window

window = Tk()
window.geometry('600x600')
window.title('Watermark')
window.config(bg="#3C3A3B")

# Functions
file_path = ""
save_path = ""
def open_file():
    global file_path
    file_path = filedialog.askopenfilename()

def save_file():
    global save_path,inp_text,file_path
    save_path = filedialog.asksaveasfile(filetypes=[("png", "*.png")], defaultextension="png")
    processing = ImageHandler(file_path,inp_text.get(),save_path.name)
    window.quit()

file_loc = Button(window, text="Select File", command=open_file,height=3,width=20)
t1= Label(text="What text you want to write?",font=("Arial",15),bg="#3C3A3B",fg="white")
inp_text = StringVar()
inp = Entry(window,textvariable=inp_text,font=("Arial",20),width=10)
save_loc = Button(window, text="Save File", command=save_file,height=3,width=20)

file_loc.grid(row=0, columnspan=2,column=1,padx=50,pady=50)
t1.grid(row=1, column=1,padx=50)
inp.grid(row=1, column=2,padx= 20)
save_loc.grid(row=3, column=1,columnspan = 2,padx=50,pady=50)


window.mainloop()









