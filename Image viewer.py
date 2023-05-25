from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image veiwer")
root.geometry("800x800")
root.configure(background="darkslate grey")

label_image= Label(root, bg="white", highlightthickness=5)
label_image.place(relx=0.5, rely=0.42, anchor=CENTER)


img_path=""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Text File", filetype=[("Image Files","*.jpg, *.gif; *.jpg;;*.png;*.txt")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_img["image"] = img
    img.close()
    
def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = imageTk.phtoImage(im.rotate(90))
    label_image["image"] = img
    print(img_path)
    img.close()
         

button=Button(root, text="Open Image", command=openFile, relief=RIDGE)
button.place(relx=0.5, rely=0.1, anchor=CENTER)

button1=Button(root, text="Rotate Image", command=rotateImage, relief=RIDGE)
button1.place(relx=0.5,rely=0.85, anchor=CENTER)


root.mainloop()