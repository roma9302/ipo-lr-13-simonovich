import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
from tkinter import simpledialog
from PIL import Image, ImageTk
from .imageProcessor import ImageProcessor  


class ImageHandler(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.img = None  
        self.file_path = None  
        self.initUI()

    def initUI(self):
        self.pack()
        
        # Визуал кнопок для взаимодействия с обьектами  fill.x растягивание кнопки 
        ttk.Button(self, text='Файл', command=self.load_image).pack(fill=tk.X)
        ttk.Button(self, text='Размер', command=self.re_size).pack(fill=tk.X)
        ttk.Button(self, text='Сохранить', command=self.save_to_file).pack(fill=tk.X)
        ttk.Button(self, text='JPG', command=self.remake_format).pack(fill=tk.X)
        ttk.Button(self, text='Поворот на 45', command=self.turn).pack(fill=tk.X)
        ttk.Button(self, text='Резкость', command=self.sharpen_load).pack(fill=tk.X)
        ttk.Button(self, text='Рамка 15ph', command=self.border_load).pack(fill=tk.X)


    
        # Лейбл для вывода изображения при изменении/загрузке
        self.label_photo = ttk.Label(self)
        self.label_photo.pack(pady=10)


    #Метод для загрузки изображения
    def load_image(self):
        self.file_path = fd.askopenfilename(title="Выберите нужный вам формат", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")])  #окно переход в проводник для выбора нужного файла вручную
        try:
            self.img = Image.open(self.file_path)  # открытие файла  и обновление его глобально
            self.update_label(self.img)  # вывод на лейбл изображения
        except:
            showerror("Ошибка", "Файл не удалось открыть") # вывод при оштбке


    #метод обновления лейбла
    def update_label(self, img):
        self.img_tk = ImageTk.PhotoImage(img)  # метод ткинтера
        self.label_photo.config(image=self.img_tk)  # обновление лейбла


    # изменение размера изображения
    def re_size(self):
        width = simpledialog.askinteger("Ширина", "Введите ширину") #Ввод через диалоговое окно ширины
        height = simpledialog.askinteger("Высота", "Введите высоту") #Ввод через диалоговое окно высоты
        
        try:  
            self.img = self.img.resize((width, height))  # Изменение размера
            self.update_label(self.img)  # изменение лейбла
        except:
            showerror("Ошибка", "Не удалось изменить изображение") # вывод при ошибке


    # метод сохранения в файл
    def save_to_file(self):
            try:
                self.img.save(self.file_path)  # обновление старого файла на новый
            except:
                showerror("Ошибка", "Файл не удалось сохранить") # вывод при ошибке


    # изменение формата на jpg
    def remake_format(self):
        try:
            jpg_path = f"{self.file_path.split('.', 1)[0]}.jpg" # разделяем файл на 2 части получается список из 2 элементов где 1 это пусть файла 2 это .png и добавляем к 1 элементу jpg второй убираем
            self.img.save(jpg_path)
        except:
            showerror("Ошибка", "Не удалось изменить формат изображения") # вывод при ошибке

        
    #метод поворота на 45 градусов
    def turn(self):
        try:
            self.img  = self.img.rotate(45) # повторот и присвоение обьекту
            self.update_label(self.img)  # сохранение на лейбл
        except:
            showerror("Ошибка", "Не удалось изменить ориентацию изображения") # вывод при ошибке


    # метод повышения резкости изображения
    def sharpen_load(self):
            filter = ImageProcessor(self.img)  #  экземпляр дочернего класса
            try:
                self.img = filter.sharpen()  # повышение резкости
                self.update_label(self.img)  # меняем лейбл
            except:
                showerror("Ошибка", "Не удалось  применить фильтр резкости") # вывод при ошибке


    def border_load(self):
        try:
            filter = ImageProcessor(self.img)  #  экземпляр дочернего класса
            self.img = filter.border()  # создание рамки 15ph
            self.update_label(self.img) # меняем лейбл
        except:
            showerror("Ошибка", "Не удалось создать рамку изображению") # вывод при ошибке


