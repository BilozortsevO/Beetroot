from tkinter import *
# Организация главного окна
'''
root = Tk() #пустое(базовое) окно
the_label = Label(root, text = 'Это всё очень просто!') #виджет с текстом
the_label.pack() # отображение виджета в окне
root.mainloop() #зациклить приложение(обязательно)
'''
'''
root = Tk()

top_frame = Frame(root) #объект (контейнер)
top_frame.pack() # по умолчанию без аргументов, pack размещает объект вверху

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button1 = Button(top_frame, text = 'Кнопка1', fg = 'red') #кнопки размещаются в контейнерах (frame)
button2 = Button(top_frame, text = 'Кнопка2', fg = 'blue')
button3 = Button(top_frame, text = 'Кнопка3', fg = 'green')
button4 = Button(bottom_frame, text = 'Кнопка4', fg = 'grey')
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

root.mainloop()
'''
# Упаковщик pack
'''
root = Tk()

one = Label(root, text = 'One', bg = 'red', fg = 'yellow') #bg - цвет фона, fg - цвет текста
one.pack()
two = Label(root, text = 'two', bg = 'blue', fg = 'white') #bg - цвет фона, fg - цвет текста
two.pack(fill = X) # fill - растягивает надпись по оси Х
three = Label(root, text = 'three', bg = 'green', fg = 'purple') #bg - цвет фона, fg - цвет текста
three.pack(side = LEFT, fill = Y)


root.mainloop()
'''
# Упаковщик grid
'''
root = Tk()

label_1 = Label(root, text = 'Name')
label_2 = Label(root, text = 'Password')

entry_1 = Entry(root) #поле ввода
entry_2 = Entry(root)

label_1.grid(row = 0, column = 0, sticky = E) #grid - пакует в таблицу, sticky - сдвигает надпись к нужному краю, стороны указываются как стороны света N,S,E,W
label_2.grid(row = 1, column = 0)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = 'Stay into the system') #окошко с галочкой, checkbox
c.grid(columnspan = 2) # указывает сколько колонок занимает объект

root.mainloop()
'''
# Метод bind
'''
def output (event):
    txt = entry_1.get()
    try:
        if int(txt)<18:
            label_1['text'] = 'Too young'
        else:
            label_1['text'] = 'Welcome'
    except ValueError:
        label_1['text'] = 'Wrong enter'
    
root = Tk()

root.title('Edge')

entry_1 = Entry(root, width = 3, font = 15) #font - размер шрифта
button_1 = Button(root, text = 'Check')
label_1 = Label(root, width = 27, font = 15)

entry_1.grid (row = 0, column = 0)
button_1.grid (row = 0, column = 1)
label_1.grid (row = 0, column = 2)

button_1.bind('<Button-1>', output) #по нажатию лкм - выполняется функция output

root.mainloop()
'''
# События мыши
'''
def left_click(event):
    frame_1.configure(bg = 'red')
    frame_2.configure(bg = 'white')
    frame_3.configure(bg = 'white')

def middle_click(event):
    frame_1.configure(bg = 'white')
    frame_2.configure(bg = 'red')
    frame_3.configure(bg = 'white')

def right_click(event):
    frame_1.configure(bg = 'white')
    frame_2.configure(bg = 'white')
    frame_3.configure(bg = 'red')

root = Tk()

root.configure(bg = 'black')

frame_1 = Frame(root, width = 250, heigh = 250, bg = 'white')
frame_2 = Frame(root, width = 250, heigh = 250, bg = 'white')
frame_3 = Frame(root, width = 250, heigh = 250, bg = 'white')

frame_1.grid(row = 0, column = 0)
frame_2.grid(row = 0, column = 1, padx = 1) # pad - бордюры (границы) по оси х толщиной 1
frame_3.grid(row = 0, column = 2)

root.bind('<Button-1>', left_click)
root.bind('<Button-2>', middle_click)
root.bind('<Button-3>', right_click)

root.mainloop()
'''
# События клавиатуры
'''
def print_char(event):
    label_1.configure(text = event.char)

def print_su(event):
    label_1.configure(text = 'Shift-Up')

def print_cd(event):
    label_1.configure(text = 'Control-Down')

root = Tk()

label_1 = Label(root, width = 12, font = ('Ubuntu', 100))
label_1.pack()

for i in range(65, 123):
    root.bind(chr(i), print_char)

root.bind('<Shift-Up>', print_su)
root.bind('<Control-Down>', print_cd)

root.mainloop()
'''
# Секундомер
'''
from datetime import datetime
temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label_1.configure(text = str(f_temp))
    temp += 1
    
def start_sw():
    btn_1.grid_forget()
    btn_2.grid(row = 1, columnspan = 2, sticky = 'ew')
    tick()

def stop_sw():
    btn_2.grid_forget()
    btn_3.grid(row = 1, column = 0, sticky = 'ew')
    btn_4.grid(row = 1, column = 1, sticky = 'ew')
    root.after_cancel(after_id)

def continue_sw():
    btn_3.grid_forget()
    btn_4.grid_forget()
    btn_2.grid(row = 1, columnspan = 2, sticky = 'ew')
    tick()

def reset_sw():
    global temp
    temp = 0
    label_1.configure(text = '00:00')
    btn_3.grid_forget()
    btn_4.grid_forget()
    btn_1.grid(row = 1, columnspan = 2, sticky = 'ew')
    
root= Tk()

root.title('Stopwatch')

label_1 = Label(root, width = 5, font = ('Ubuntu', 100), text = '00:00')
label_1.grid(row = 0, columnspan = 2)

btn_1 = Button(root, text = 'Start', font = ('Ubuntu', 30), command = start_sw)
btn_2 = Button(root, text = 'Stop', font = ('Ubuntu', 30), command = stop_sw)
btn_3 = Button(root, text = 'Continue', font = ('Ubuntu', 30), command = continue_sw)
btn_4 = Button(root, text = 'Reset', font = ('Ubuntu', 30), command = reset_sw)

btn_1.grid(row = 1, columnspan = 2, sticky = 'ew')

root.mainloop()
'''
# Использование ООП
'''
class Question:

    def __init__(self, main):

        self.entry_1 = Entry(main, width = 3, font = 15)
        self.button_1 = Button(main, text = 'Check')
        self.label_1 = Label(main, width = 27, font = 15)

        self.entry_1.grid(row = 0, column = 0)
        self.button_1.grid(row = 0, column = 1)
        self.label_1.grid(row = 0, column = 2)

        self.button_1.bind('<Button-1>', self.answer)

    def answer (self, event):
        txt = self.entry_1.get()
        try:
            if int(txt)<18:
                self.label_1['text'] = 'Too young!'
            else:
                self.label_1['text'] = 'Welcome'
        except ValueError:
            self.label_1['text'] = 'Wrong enter'

root = Tk()
root.title('Enter your edge')
q = Question(root)

root.mainloop()
''' 
# Выпадающее меню и Панель инструментов и статус бар
'''
def new_win():
    win = Toplevel(root) # Создание всплывающего окна
    label_1 = Label(win, text = 'Text of Top level window', font = 20)
    label_1.pack()

def exit_app():
    root.destroy() # Уничтожение окна и его потомков
    
root = Tk()

main_menu = Menu(root)
root.configure(menu = main_menu)

first_item = Menu (main_menu)
main_menu.add_cascade(label = 'File', menu = first_item)
first_item.add_command(label = 'New', command = new_win)
first_item.add_command(label = 'Exit', command = exit_app)

second_item = Menu (main_menu, tearoff = 0) # tearoff запрещает отрывать этот элемент меню от главного окна
main_menu.add_cascade(label = 'Edit', menu = second_item)
second_item.add_command(label = 'Item1')
second_item.add_command(label = 'Item2')
second_item.add_command(label = 'Item3')
second_item.add_separator()
second_item.add_command(label = 'Item4')

toolbar = Frame(root, bg = '#A1A1A1')
toolbar.pack (side = TOP, fill = X)

btn_1 = Button(toolbar, text = 'Cut')
btn_1.grid (row = 0, column = 0, padx = 2, pady = 2)

btn_2 = Button(toolbar, text = 'Copy')
btn_2.grid (row = 0, column = 1, padx = 2, pady = 2)

btn_3 = Button(toolbar, text = 'Paste')
btn_3.grid (row = 0, column = 2, padx = 2, pady = 2)

status_bar = Label(root, relief = SUNKEN, anchor = W, text = 'Mission complete') # relief - свойство, определяющее тип рамки элементаб anchor - привязка содержимого к краю
status_bar.pack(side = BOTTOM, fill = X)

root.mainloop()
'''
# Диалоговые окна 1
'''
from tkinter.messagebox import *

root = Tk()

btn_1 = Button (root, text = 'info', font = ('Ubuntu', 20), command = lambda:showinfo('Showinfo', 'Information'))
btn_1.grid (row = 0, column = 0, sticky = 'ew')

btn_2 = Button (root, text = 'Warning', font = ('Ubuntu', 20), command = lambda:showwarning('Showwarning', 'Warning'))
btn_2.grid (row = 1, column = 0, sticky = 'ew')

btn_3 = Button (root, text = 'Error', font = ('Ubuntu', 20), command = lambda:showerror('Showerror', 'Error'))
btn_3.grid (row = 2, column = 0, sticky = 'ew')

root.mainloop()
'''
# Диалоговые окна 2
'''
from tkinter.messagebox import *

def ask_question (event):
    answer = askquestion ('AskQuestion', 'First Question?')
    label_1.configure(text = answer)

def ask_ok (event):
    answer = askokcancel ('AskOkCancel', 'Second Question?')
    label_2.configure(text = answer)

def ask_YN (event):
    answer = askyesno ('AskYesNo', 'Third Question?')
    label_3.configure(text = answer)

def ask_RC (event):
    answer = askretrycancel ('AsRetryCancel', 'Fourth Question?')
    label_4.configure(text = answer)

root = Tk()

btn_1 = Button(root, text = 'AskQuestion', font = ('Ubuntu', 20), width = 12)
btn_1.grid (row = 0, column = 0, sticky = 'ew')
label_1 = Label(root, font = ('Ubuntu', 20), width = 12)
label_1.grid (row = 0, column = 1)
btn_1.bind('<Button-1>', ask_question)

btn_2 = Button(root, text = 'AskOkCancel', font = ('Ubuntu', 20), width = 12)
btn_2.grid (row = 1, column = 0, sticky = 'ew')
label_2 = Label(root, font = ('Ubuntu', 20), width = 12)
label_2.grid (row = 1, column = 1)
btn_2.bind('<Button-1>', ask_ok)

btn_3 = Button(root, text = 'AskYesNo', font = ('Ubuntu', 20), width = 12)
btn_3.grid (row = 2, column = 0, sticky = 'ew')
label_3 = Label(root, font = ('Ubuntu', 20), width = 12)
label_3.grid (row = 2, column = 1)
btn_3.bind('<Button-1>', ask_YN)

btn_4 = Button(root, text = 'AskRetryCancel', font = ('Ubuntu', 20), width = 12)
btn_4.grid (row = 3, column = 0, sticky = 'ew')
label_4 = Label(root, font = ('Ubuntu', 20), width = 12)
label_4.grid (row = 3, column = 1)
btn_4.bind('<Button-1>', ask_RC)

root.mainloop()
'''
# Диалоговые окна 3
'''
from tkinter.filedialog import *

def open_file ():
    of = askopenfilename()
    file = open (of, 'r')
    txt.insert (END, file.read())
    file.close

def save_file():
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END) # Чтение с 1 (нумерация с 1) строки и 0 столбца
    file = open (sf, 'w')
    file.write(final_text)
    file.close

def exit_app():
    root.quit()


root = Tk()

main_menu = Menu (root)
root.configure (menu = main_menu)

first_item = Menu (main_menu, tearoff = 0)
main_menu.add_cascade(label = 'File', menu= first_item)

first_item.add_command (label = 'Open', command = open_file)
first_item.add_command (label = 'Save', command = save_file)
first_item.add_command (label = 'Exit', command = exit_app)

txt = Text (root, width = 40, heigh = 40, font =12)
txt.pack(expand = YES, fill = BOTH)

root.mainloop()
'''
# Canvas и геометрические примитивы
'''
root = Tk()

c1 = Canvas (root, width = 500, heigh = 500, cursor = 'pencil', bg = 'white')
c1.pack()

c1.create_line(250, 0, 250, 500, width =3, fill = 'red', arrow = LAST)
c1.create_line(0, 250, 500, 250, width =3, fill = 'blue', arrow = BOTH)

c1.create_rectangle(10, 10, 240, 240, fill = 'green', outline = 'red')

c1.create_polygon (260, 10, 490, 10, 400, 125, 490, 240, 260, 240, 350, 125, fill = 'orange', smooth = 1)

c1.create_oval (10, 260, 240, 340, fill = 'yellow', outline = 'red', width = 3)

c1.create_arc (10, 350, 90, 430, start = 0, extent = 270, fill = '#0000cc')
c1.create_arc (160, 350, 240, 430, start = 0, extent = 270, fill = '#cc0099', style = 'chord')
c1.create_arc (80, 410, 160, 490, start = 0, extent = 270, style = 'arc', width = 3)


c1.create_text (275, 330, text = 'Tkinter - \nэто программа\n с оконным интерфейсом', font = 'Verdana 12', anchor ='w',
                justify = 'center', fill = 'orange')
root.mainloop()
'''
# Canvas статические изменения фигур
'''
def create_outline (event):
    c1.itemconfigure(oval_1, outline = 'blue', width = 3)

def change_fill (event):
    c1.itemconfigure(oval_2, fill = 'orange')
    c1.coords(oval_2, 250, 10, 390, 90)

def moove_ovals (event):
    c1.move ('ovals', 0, 260)

def clear_canvas (event):
    c1.delete ('all')

root = Tk()

c1 = Canvas(root, width = 400, heigh = 400, bg = 'white')
c1.pack()

oval_1 = c1.create_oval(10, 10, 90, 90, width = 0, fill = 'red', tag = 'ovals')
oval_2 = c1.create_oval(310, 10, 390, 90, width = 0, fill = 'blue', tag = 'ovals')
triangle_1 = c1.create_polygon(200, 200, 10, 390, 390, 390, fill = 'green')

c1.tag_bind(oval_1, '<Button-1>', create_outline)
c1.tag_bind(oval_2, '<Button-1>', change_fill)
c1.tag_bind(triangle_1, '<Button-1>', moove_ovals)

root.bind('<Button-3>', clear_canvas)

root.mainloop()
'''
# Анимированная отрисовка
from math import sin, cos
x = 0
def print_dot ():
    global x

    y1 = sin(x)
    y2 = cos(x)

    cvs.create_oval(25*x+10, 25*y1+100, 25*x+10, 25*y1+100, width = 1, outline = 'red')
    cvs.create_oval(25*x+10, 25*y2+100, 25*x+10, 25*y2+100, width = 1, outline = 'blue')
    x += 0.03

    root.after(5, print_dot)

root = Tk()

cvs = Canvas (root, width = 600, heigh = 200, bg = '#fff')
cvs.pack()

cvs.create_line(10, 0, 10, 200, width = 2, arrow = BOTH, fill = 'grey')
cvs.create_line(10, 100, 600, 100, width = 2, arrow = LAST, fill = 'grey')

print_dot()

root.mainloop()