from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import Selections as sel
from collections import Counter
from prettytable import PrettyTable


# Функция для прелбразования
def show_message1(p, q):
    data = str.split(p, " ")
    for i in range(len(data)):
        data[i] = float(data[i])

    if q:
        interval_dict, interval_dict_names = sel.convert_from_disk_to_inter(data, 4)
        plt.bar(interval_dict_names, interval_dict.values())
        plt.show()
    else:
        interval_dict = dict(Counter(data))
        plt.plot(interval_dict.keys(), interval_dict.values())
        plt.show()

    local_class = sel.Selectin(interval_dict)
    print(interval_dict)
    param = local_class.output()
    columns = ("dict",
    "size", "Mx", "Mx2", "Disp", "ASD", "corrected_D", "corrected_ASD", "asymmetry", "excess", "moda", "mediana")
    tree = ttk.Treeview(frame1, columns=columns, show="headings")
    tree.pack(side='top', fill='x')

    # определяем заголовки
    tree.heading("dict", text="dict")
    tree.heading("size", text="size")
    tree.heading("Mx", text="Mx")
    tree.heading("Mx2", text="Mx2")
    tree.heading("Disp", text="Disp")
    tree.heading("ASD", text="ASD")
    tree.heading("corrected_D", text="corrected_D")
    tree.heading("corrected_ASD", text="corrected_ASD")
    tree.heading("asymmetry", text="asymmetry")
    tree.heading("excess", text="excess")
    tree.heading("moda", text="moda")
    tree.heading("mediana", text="mediana")

    # добавляем данные
    tree.insert("", END, values=list(param.values()))

    s = sel.Shapiro_is_normal(local_class)

    lbl1 = Label(frame1, text=s)
    lbl1.pack(side='top', fill='x')



def show_message2(p, r, t, q):
    data1 = str.split(p, " ")
    for i in range(len(data1)):
        data1[i] = float(data1[i])

    data2 = str.split(r, " ")
    for i in range(len(data2)):
        data2[i] = float(data2[i])

    if q:
        interval_dict1, interval_dict_names1 = sel.convert_from_disk_to_inter(data1, 4)
        interval_dict2, interval_dict_names2 = sel.convert_from_disk_to_inter(data2, 4)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.bar(interval_dict_names1, interval_dict1.values())
        ax2.bar(interval_dict_names2, interval_dict2.values())
        plt.show()
    else:
        interval_dict1 = dict(Counter(data1))
        interval_dict2 = dict(Counter(data2))
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(interval_dict1.keys(), interval_dict1.values())
        ax2.plot(interval_dict2.keys(), interval_dict2.values())
        plt.show()

    first_class = sel.Selectin(interval_dict1)
    second_class = sel.Selectin(interval_dict2)

    param1 = first_class.output()
    param2 = second_class.output()

    columns = ("dict",
               "size", "Mx", "Mx2", "Disp", "ASD", "corrected_D", "corrected_ASD", "asymmetry", "excess", "moda",
               "mediana")
    tree = ttk.Treeview(frame2, columns=columns, show="headings")
    tree.pack(side='top', fill='x')

    # определяем заголовки
    tree.heading("dict", text="dict")
    tree.heading("size", text="size")
    tree.heading("Mx", text="Mx")
    tree.heading("Mx2", text="Mx2")
    tree.heading("Disp", text="Disp")
    tree.heading("ASD", text="ASD")
    tree.heading("corrected_D", text="corrected_D")
    tree.heading("corrected_ASD", text="corrected_ASD")
    tree.heading("asymmetry", text="asymmetry")
    tree.heading("excess", text="excess")
    tree.heading("moda", text="moda")
    tree.heading("mediana", text="mediana")

    # добавляем данные
    tree.insert("", END, values=list(param1.values()))
    tree.insert("", END, values=list(param2.values()))

    s = sel.Student(first_class, second_class, t)
    lbl1 = Label(frame2, text=s)
    lbl1.pack(side='top', fill='x')


def show_message3(p, r, t, q):
    data1 = str.split(p, " ")
    for i in range(len(data1)):
        data1[i] = float(data1[i])

    data2 = str.split(r, " ")
    for i in range(len(data2)):
        data2[i] = float(data2[i])

    if q:
        interval_dict1, interval_dict_names1 = sel.convert_from_disk_to_inter(data1, 4)
        interval_dict2, interval_dict_names2 = sel.convert_from_disk_to_inter(data2, 4)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.bar(interval_dict_names1, interval_dict1.values())
        ax2.bar(interval_dict_names2, interval_dict2.values())
        plt.show()
    else:
        interval_dict1 = dict(Counter(data1))
        interval_dict2 = dict(Counter(data2))
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(interval_dict1.keys(), interval_dict1.values())
        ax2.plot(interval_dict2.keys(), interval_dict2.values())
        plt.show()

    first_class = sel.Selectin(interval_dict1)
    second_class = sel.Selectin(interval_dict2)

    param1 = first_class.output()
    param2 = second_class.output()

    columns = ("dict",
               "size", "Mx", "Mx2", "Disp", "ASD", "corrected_D", "corrected_ASD", "asymmetry", "excess", "moda",
               "mediana")
    tree = ttk.Treeview(frame3, columns=columns, show="headings")
    tree.pack(side='top', fill='x')

    # определяем заголовки
    tree.heading("dict", text="dict")
    tree.heading("size", text="size")
    tree.heading("Mx", text="Mx")
    tree.heading("Mx2", text="Mx2")
    tree.heading("Disp", text="Disp")
    tree.heading("ASD", text="ASD")
    tree.heading("corrected_D", text="corrected_D")
    tree.heading("corrected_ASD", text="corrected_ASD")
    tree.heading("asymmetry", text="asymmetry")
    tree.heading("excess", text="excess")
    tree.heading("moda", text="moda")
    tree.heading("mediana", text="mediana")

    # добавляем данные
    tree.insert("", END, values=list(param1.values()))
    tree.insert("", END, values=list(param2.values()))


    s = sel.Fisher(first_class, second_class, t)
    lbl1 = Label(frame3, text=s)
    lbl1.pack(side='top', fill='x')


def show_message4(p, r, t, q):
    data1 = str.split(p, " ")
    for i in range(len(data1)):
        data1[i] = float(data1[i])

    data2 = str.split(r, " ")
    for i in range(len(data2)):
        data2[i] = float(data2[i])

    if q:
        interval_dict1, interval_dict_names1 = sel.convert_from_disk_to_inter(data1, 4)
        interval_dict2, interval_dict_names2 = sel.convert_from_disk_to_inter(data2, 4)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.bar(interval_dict_names1, interval_dict1.values())
        ax2.bar(interval_dict_names2, interval_dict2.values())
        plt.show()
    else:
        interval_dict1 = dict(Counter(data1))
        interval_dict2 = dict(Counter(data2))
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(interval_dict1.keys(), interval_dict1.values())
        ax2.plot(interval_dict2.keys(), interval_dict2.values())
        plt.show()

    first_class = sel.Selectin(interval_dict1)
    second_class = sel.Selectin(interval_dict2)

    param1 = first_class.output()
    param2 = second_class.output()
    columns = ("dict",
               "size", "Mx", "Mx2", "Disp", "ASD", "corrected_D", "corrected_ASD", "asymmetry", "excess", "moda",
               "mediana")
    tree = ttk.Treeview(frame4, columns=columns, show="headings")
    tree.pack(side='top', fill='x')

    # определяем заголовки
    tree.heading("dict", text="dict")
    tree.heading("size", text="size")
    tree.heading("Mx", text="Mx")
    tree.heading("Mx2", text="Mx2")
    tree.heading("Disp", text="Disp")
    tree.heading("ASD", text="ASD")
    tree.heading("corrected_D", text="corrected_D")
    tree.heading("corrected_ASD", text="corrected_ASD")
    tree.heading("asymmetry", text="asymmetry")
    tree.heading("excess", text="excess")
    tree.heading("moda", text="moda")
    tree.heading("mediana", text="mediana")

    # добавляем данные
    tree.insert("", END, values=list(param1.values()))
    tree.insert("", END, values=list(param2.values()))

    s = sel.KS(first_class, second_class, t)
    lbl1 = Label(frame4, text=s)
    lbl1.pack(side='top', fill='x')


def show_message5(p, r, q):
    data1 = str.split(p, " ")
    for i in range(len(data1)):
        data1[i] = float(data1[i])

    data2 = str.split(r, " ")
    for i in range(len(data2)):
        data2[i] = float(data2[i])

    if q:
        interval_dict1, interval_dict_names1 = sel.convert_from_disk_to_inter(data1, 4)
        interval_dict2, interval_dict_names2 = sel.convert_from_disk_to_inter(data2, 4)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.bar(interval_dict_names1, interval_dict1.values())
        ax2.bar(interval_dict_names2, interval_dict2.values())
        plt.show()
    else:
        interval_dict1 = dict(Counter(data1))
        interval_dict2 = dict(Counter(data2))
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Horizontally stacked subplots')
        ax1.plot(interval_dict1.keys(), interval_dict1.values())
        ax2.plot(interval_dict2.keys(), interval_dict2.values())
        plt.show()

    first_class = sel.Selectin(interval_dict1)
    second_class = sel.Selectin(interval_dict2)

    param1 = first_class.output()
    param2 = second_class.output()

    columns = ("dict",
               "size", "Mx", "Mx2", "Disp", "ASD", "corrected_D", "corrected_ASD", "asymmetry", "excess", "moda",
               "mediana")
    tree = ttk.Treeview(frame5, columns=columns, show="headings")
    tree.pack(side='top', fill='x')

    # определяем заголовки
    tree.heading("dict", text="dict")
    tree.heading("size", text="size")
    tree.heading("Mx", text="Mx")
    tree.heading("Mx2", text="Mx2")
    tree.heading("Disp", text="Disp")
    tree.heading("ASD", text="ASD")
    tree.heading("corrected_D", text="corrected_D")
    tree.heading("corrected_ASD", text="corrected_ASD")
    tree.heading("asymmetry", text="asymmetry")
    tree.heading("excess", text="excess")
    tree.heading("moda", text="moda")
    tree.heading("mediana", text="mediana")

    # добавляем данные
    tree.insert("", END, values=list(param1.values()))
    tree.insert("", END, values=list(param2.values()))


    s = sel.Pirs(first_class, second_class)
    lbl1 = Label(frame5, text=s)
    lbl1.pack(side='top', fill='x')


# Функция нажатия на кнопку
def click():
    global parametrs1
    parametrs1 = entry.get()
    print(parametrs1)


#Критерий Пирсона
def form5(num_lines):
    frame_table5 = ttk.LabelFrame(frame5, text="заполните таблицы (разделитель пробел)")
    frame_table5.pack(side='top', fill='x')
    list5 = list()
    entry1 = ttk.Entry(frame_table5, background="red")
    entry1.pack(side='top', fill='x')
    entry2 = ttk.Entry(frame_table5, background="red")
    entry2.pack(side='top', fill='x')
    chk5 = Checkbutton(frame_table5, text='Интервальная выборка или нет', var=chk_state)
    chk5.pack(side='top', fill='x')
    resultButton5 = ttk.Button(frame_table5, text='Get Result', width=20, command=lambda: show_message5(entry1.get(), entry2.get(), chk_state.get()))
    resultButton5.pack(side='left')


def creat5(lines):
    form5(lines)


# Функция для создания входных параметров
def form4(num_lines):
    frame_table4 = ttk.LabelFrame(frame4, text="заполните таблицы (разделитель пробел)")
    frame_table4.pack(side='top', fill='x')
    list4 = list()
    entry1 = ttk.Entry(frame_table4, background="red")
    entry1.pack(side='top', fill='x')
    entry2 = ttk.Entry(frame_table4, background="red")
    entry2.pack(side='top', fill='x')
    r_var4 = StringVar()
    r_var4.set(0)
    r1 = Radiobutton(frame_table4,text='0.05',
                     variable=r_var4, value='0.05')
    r1.pack(side='top', fill='x')
    r2 = Radiobutton(frame_table4, text='0.01',
                     variable=r_var4, value='0.01')
    r2.pack(side='top', fill='x')
    chk4 = Checkbutton(frame_table4, text='Интервальная выборка или нет', var=chk_state)
    chk4.pack(side='top', fill='x')
    resultButton4 = ttk.Button(frame_table4, text='Get Result', width=20, command=lambda: show_message4(entry1.get(), entry2.get(), r_var4.get(), chk_state.get()))
    resultButton4.pack(side='left')


def creat4(lines):
    form4(lines)


# Функция для создания входных параметров
def form3(num_lines):
    frame_table3 = ttk.LabelFrame(frame3, text="заполните таблицы (разделитель пробел)")
    frame_table3.pack(side='top', fill='x')
    list3 = list()
    entry1 = ttk.Entry(frame_table3, background="red")
    entry1.pack(side='top', fill='x')
    entry2 = ttk.Entry(frame_table3, background="red")
    entry2.pack(side='top', fill='x')
    list3.append(entry.get())
    r_var3 = StringVar()
    r_var3.set(0)
    r1 = Radiobutton(frame_table3,text='0.05',
                     variable=r_var3, value='0.05')
    r1.pack(side='top', fill='x')
    r2 = Radiobutton(frame_table3, text='0.01',
                     variable=r_var3, value='0.01')
    r2.pack(side='top', fill='x')
    chk3 = Checkbutton(frame_table3, text='Интервальная выборка или нет', var=chk_state)
    chk3.pack(side='top', fill='x')
    resultButton3 = ttk.Button(frame_table3, text='Get Result', width=20,  command=lambda: show_message3(entry1.get(), entry2.get(), r_var3.get(), chk_state.get()))
    resultButton3.pack(side='left')


def creat3(lines):
    form3(lines)


# Функция для создания входных параметров
def form2(num_lines):
    frame_table2 = ttk.LabelFrame(frame2, text="заполните таблицы (разделитель пробел)")
    frame_table2.pack(side='top', fill='x')
    entry1 = ttk.Entry(frame_table2, background="red")
    entry1.pack(side='top', fill='x')
    entry2 = ttk.Entry(frame_table2, background="red")
    entry2.pack(side='top', fill='x')
    r_var2 = StringVar()
    r_var2.set(0)
    r1 = Radiobutton(frame_table2,text='0.05',
                     variable=r_var2, value='0.05')
    r1.pack(side='top', fill='x')
    r2 = Radiobutton(frame_table2, text='0.01',
                     variable=r_var2, value='0.01')
    r2.pack(side='top', fill='x')
    chk2 = Checkbutton(frame_table2, text='Интервальная выборка или нет', var=chk_state)
    chk2.pack(side='top', fill='x')
    resultButton2 = ttk.Button(frame_table2, text='Get Result', width=20, command=lambda: show_message2(entry1.get(), entry2.get(), r_var2.get(), chk_state.get()))
    resultButton2.pack(side='left')


def creat2(lines):
    form2(lines)


master = Tk()
master.title("МатСтат - лучший предмет! Группа у стены.")
master.geometry("850x600")

# создание переменных
message1 = StringVar()
chk_state = BooleanVar()
chk_state = IntVar()
chk_state.set(0)
chk_state.set(1)
col_strok = 1

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook, name="1")
frame2 = ttk.Frame(notebook, name="2")
frame3 = ttk.Frame(notebook, name="3")
frame4 = ttk.Frame(notebook, name="4")
frame5 = ttk.Frame(notebook, name="5")

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
frame4.pack(fill=BOTH, expand=True)
frame5.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Проверка распределения")
notebook.add(frame2, text="t-Стьюдента")
notebook.add(frame3, text="F-Фишера")
notebook.add(frame4, text="Колмогорова-Смирнова")
notebook.add(frame5, text="Критерий Пирсона")

# проверка распределения:
frame_table = ttk.LabelFrame(frame1, text="Заполните таблицы (разделитель пробел):")
frame_table.pack(side='top', fill='x')
entry= ttk.Entry(frame_table, background="red", textvariable=message1)
entry.pack(side='top', fill='x')
chk = Checkbutton(frame_table, text='Интервальная выборка или нет', var=chk_state)
chk.pack(side='top', fill='x')
resultButton = ttk.Button(frame_table, text='Get Result', width=20, command=lambda: show_message1(entry.get(), chk_state.get()))
resultButton.pack(side='left')

# t-Стьюдента:
frame_col_viborok_2 = LabelFrame(frame2, text="Кол. выборок:")
frame_col_viborok_2.pack(side='top', fill='x')
spin_lines2 = Spinbox(frame_col_viborok_2, from_=1, to=5)
spin_lines2.pack(side='top', fill='x')
# кнопка создания выборок
resultButton = ttk.Button(frame_col_viborok_2, text='Создать', width=20, command=lambda: creat2(spin_lines2.get()))
resultButton.pack(side='left')

# F-Фишера:
frame_col_viborok_3 = LabelFrame(frame3, text="Кол. выборок:")
frame_col_viborok_3.pack(side='top', fill='x')
spin_lines3 = Spinbox(frame_col_viborok_3, from_=1, to=5)
spin_lines3.pack(side='top', fill='x')
# кнопка создания выборок
resultButton = ttk.Button(frame_col_viborok_3, text='Создать', width=20, command=lambda: creat3(spin_lines3.get()))
resultButton.pack(side='left')

# Колмогорова-Смирнова:
frame_col_viborok_4 = LabelFrame(frame4, text="Кол. выборок:")
frame_col_viborok_4.pack(side='top', fill='x')
spin_lines4 = Spinbox(frame_col_viborok_4, from_=1, to=5)
spin_lines4.pack(side='top', fill='x')
# кнопка создания выборок
resultButton = ttk.Button(frame_col_viborok_4, text='Создать', width=20, command=lambda: creat4(spin_lines4.get()))
resultButton.pack(side='left')

# Критерий Пирсона:
frame_col_viborok_5 = LabelFrame(frame5, text="Кол. выборок:")
frame_col_viborok_5.pack(side='top', fill='x')
spin_lines5 = Spinbox(frame_col_viborok_5, from_=1, to=5)
spin_lines5.pack(side='top', fill='x')
# кнопка создания выборок
resultButton = ttk.Button(frame_col_viborok_5, text='Создать', width=20, command=lambda: creat5(spin_lines5.get()))
resultButton.pack(side='left')


# frame_table = ttk.LabelFrame(frame2, text="Заполните таблицы (разделитель пробел):")
# frame_table.pack(side='top', fill='x')
# entry = ttk.Entry(frame_table, background="red", textvariable=message1)
# entry.pack(side='top', fill='x')

master.mainloop()
