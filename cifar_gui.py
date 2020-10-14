# importing libraries

import tkinter as tk
from tkinter import *
# import PIL
from tkinter import filedialog

import numpy
from PIL import Image, ImageTk
from keras.models import load_model

# importing model

model = load_model('cifar_model.h5')

classes = {
    0: 'Aerolplane',
    1: 'Automobile',
    2: 'Bird',
    3: 'Cat',
    4: 'Deer',
    5: 'Dog',
    6: 'Frog',
    7: 'Horse',
    8: 'Ship',
    9: 'truck'
}


def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width() / 2.25, (top.winfo_height() / 2.25))))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text=' ')
    show_classify_button(file_path)


def show_classify_button(file_path):
    classify_btn = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_btn.configure(background="#364156", foreground="white", font=('arial', 10, 'bold'))
    classify_btn.place(relx=0.79, rely=0.46)


def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#011638', text=sign)


# initialize GUI
top = tk.Tk()  # calling the constructor or creating the object of tk class
top.geometry('800x600')  # set height and width
top.title("Image Classification CIFAR10")
top.configure(background="#CDCDCD")

# set Heading

heading = Label(top, text="Image Classification CIFAR10", pady=20, font=('arial', 20, 'bold'))
heading.configure(background="#CDCDCD", foreground='#364156')
heading.pack()

upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
heading.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)

# upload image
sign_image = Label(top)
sign_image.pack(side=BOTTOM, expand=True)

# predicted class

label = Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
label.pack(side=BOTTOM, expand=True)

top.mainloop()
