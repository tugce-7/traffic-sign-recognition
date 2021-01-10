import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from future.moves import tkinter


import numpy
from keras.models import load_model
model = load_model('traffic_classifier.h5')

classes = { 1:' Azami Hız (20km/h)',
            2:' Azami Hız (30km/h)',
            3:' Azami Hız (50km/h)',
            4:' Azami Hız (60km/h)',
            5:' Azami Hız (70km/h)',
            6:' Azami Hız (80km/h)',
            7:' Hız Limitinin Sonu (80km/h)',
            8:' Azami Hız (100km/h)',
            9:' Azami Hız (120km/h)',
           10:' Geçiş Yok ',
           11:' 3.5 Tondan Fazla Yüklü Taşıt Giremez ',
           12:' Kavşakta Geçiş Hakkı',
           13:' Ana Yol',
           14:' Yol Ver',
           15:' Dur',
           16:' Taşıt Trafiğine Kapalı Yol',
           17:' Kamyon Giremez ',
           18:' Giriş Olmayan Yol',
           19:' Dikkat',
           20:' Sola Tehlikeli Viraj',
           21:' Sağa Tehlikeli Viraj',
           22:' Tehlikeli Devamlı Virajlar',
           23:' Kasisli Yol',
           24:' Kaygan Yol',
           25:' Sağdan Daralan Yol',
           26:' Yolda Çalışma',
           27:' Trafik Işıkları',
           28:' Yaya Geçidi',
           29:' Okul Geçidi',
           30:' Bisiklet Geçidi',
           31:' Gizli Buzlanma ',
           32:' Vahşi Hayvan Geçebilir ',
           33:' Bütün Yasaklamaların Sonu ',
           34:' İleriden Sağa Mecburi Yön',
           35:' İleriden Sola Mecburi Yön',
           36:' İleri Mecburi Yön',
           37:' İleri ve Sağa Mecburi Yön',
           38:' İleri ve Sola Mecburi Yön',
           39:' Sağdan Gidiniz',
           40:' Soldan Gidiniz',
           41:' Ada Etrafında Dönünüz ',
           42:' Geçme Yasağı Sonu ',
           43:' 3.5 Tondan Fazla Taşıtların Geçme Yasağı Sonu' }
                 

top=tk.Tk()
top.geometry('800x600')
top.title('Trafik İşareti Sınıflandırma')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Sınıflandır",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Resim Seç",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Trafik İşaretlerini Öğren",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
