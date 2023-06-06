import tkinter as tk

def SortByFirstEl(Array):
    return Array[0]

def SortBySecondEl(Array):
    return Array[1]

def Encrypt():

    KeyWord = entry1.get()
    Rows = int(entry1_1.get())
    Columns = int(entry1_2.get())
    Text = list(text_box.get("1.0", tk.END))
    ArrayColumnElements_WithKey = [0] * Columns
    IndNumb = [0] * Columns
    ArrayColumnElements = []
    ChipherText = ''
    OpenText = ''

    for i in range(Columns):
        ColumnElements = []
        for j in range(Rows):
            ColumnElements.append(Text[i * Rows + j])
        ArrayColumnElements.append(ColumnElements)
    #     print(ColumnElements, '\b')
    # print(ArrayColumnElements, '\b')

    for i in range(Columns):        #добавление по букве кл слова
           ArrayColumnElements_WithKey[i] = list(KeyWord[i]) + ArrayColumnElements[i]
    # print(ArrayColumnElements_WithKey, '\b')

    ArrayColumnElements_WithKey.sort(key = SortByFirstEl)     #сортировка по 1-ым буквам кл слова
    # print(ArrayColumnElements_WithKey, '\b')

    for i in range(Columns):    #удаление 1-ых букв кл слова
           ArrayColumnElements_WithKey[i].pop(0)
    # print(ArrayColumnElements_WithKey, '\b')

    for i in range(Rows):
        for j in range(Columns):
            ChipherText+= ArrayColumnElements_WithKey[j][i]
    # print('Шифртекст:', ChipherText)

    file = open('result.txt', 'w', encoding ='UTF-8')
    file.write(ChipherText)

    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", ChipherText)

def Decrypt():
    KeyWord = entry1.get()
    Rows = int(entry1_1.get())
    Columns = int(entry1_2.get())
    Text = list(text_box.get("1.0", tk.END))
    ArrayColumnElements_WithKey = [0] * Columns
    IndNumb = [0] * Columns
    ArrayColumnElements = []
    ChipherText = ''
    OpenText = ''

    for i in range(Columns):
        ColumnElements = []
        for j in range(Rows):
            ColumnElements.append(Text[j * Columns + i])
        ArrayColumnElements.append(ColumnElements)
    #     print(ColumnElements, '\b')
    # print(ArrayColumnElements, '\b')

    for i in range(Columns):    #добавление по цифре(индексу) кл слова
           IndNumb[i] = str(i)
    # print(IndNumb, '\b')

    for i in range(Columns):
           ArrayColumnElements_WithKey[i] = list(IndNumb[i] + KeyWord[i])
    # print(ArrayColumnElements_WithKey,'\b')
    ArrayColumnElements_WithKey.sort(key=SortBySecondEl)    #сортировка по букве кл слова
    # print(ArrayColumnElements_WithKey, '\b')

    for i in range(Columns):
           IndNumb[i] = list(ArrayColumnElements_WithKey[i]) + ArrayColumnElements[i]
    # print(IndNumb, '\b')
    IndNumb.sort(key=SortByFirstEl)     #сортировка по индексу кл слова
    # print(IndNumb, '\b')

    for i in range(Columns):
           IndNumb[i].pop(0)
           IndNumb[i].pop(0)
    # print(IndNumb, '\b')

    for i in range(Columns):
        for j in range(Rows):
            OpenText+= IndNumb[i][j]
    # print('Открытый текст:', OpenText)

    file = open('result.txt', 'w', encoding='UTF-8')
    file.write(OpenText)

    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", OpenText)

windows = tk.Tk()
windows.title('Одиночная перестановка')

label1 = tk.Label(
    master = windows,
    text = 'Введите ключевое слово: ',
    fg = "#FFFFFF",
    bg = "#696969",
    width = 30,
    height = 1
)

entry1 = tk.Entry(master=windows, bg="#DED9C4", width=12)

# entry1.pack()

label1_1=tk.Label(
    master=windows,
    text='Введите размер таблицы: ',
    fg="#FFFFFF",
    bg="#696969",
    width=30,
    height=1
)
# label1_1.pack()

frame1 = tk.Frame()

frame2 = tk.Frame()

entry1_1 = tk.Entry(master=frame1,bg="#DED9C4", width=5)

# entry1_1.pack()

label1_2=tk.Label(
    master=frame1,
    text='x',
    fg="#000000",
    bg="#D0CAB2",
    width=1,
    height=1
)
# label1_2.pack()

entry1_2 = tk.Entry(master=frame1,bg="#DED9C4", width=5)

# entry1_2.pack()

label2=tk.Label(
    master=windows,
    text='Текст: ',
    fg="#FFFFFF",
    bg="#696969",
    width=30,
    height=1
)
# label2.pack()

text_box = tk.Text(width=50, height=4,fg="#000000",bg="#DED9C4")
# text_box.pack()

button1 = tk.Button(
    master=frame2,
    text="Зашифровать",
    width=12,
    height=1,
    bg="#696969",
    fg="#FFFFFF",
    command = Encrypt
)
# button1.pack()

button2 = tk.Button(
    master=frame2,
    text="Расшифровать",
    width=12,
    height=1,
    bg="#696969",
    fg="#FFFFFF",
    command= Decrypt
)
# button2.pack()

label1.pack()
entry1.pack()
label1_1.pack()
entry1_2.pack(side = tk.RIGHT)
label1_2.pack(side = tk.RIGHT)
entry1_1.pack(side = tk.RIGHT)
frame1.pack()
label2.pack()
text_box.pack()
button1.pack(side = tk.RIGHT)
button2.pack(side = tk.LEFT)
frame2.pack()

file = open('text.txt', encoding='UTF-8')
text = file.read()
text_box.insert("1.0", text)

windows.mainloop()