import itertools, os
from tkinter import *

os.chdir (r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\Life')

f = open ('INPUT')
line = f.readline()
win_size = line.split(' ')
win_width = int(win_size[0])
win_height = int(win_size[1])
root = Tk()
root.title('It\'s a beautiful life')
#win_width = 350
#win_height = 370
config_string = "{0}x{1}".format(win_width, win_height + 32)
fill_color = "green"
root.geometry(config_string)

canvas = Canvas(root, height=win_height)
canvas.pack(fill=BOTH)	

line = f.readline()
field_size = line.split(' ')
f.close()

field_h = int(field_size[0])
field_w = int(field_size[1])
dot_w = (win_width//field_h)-2
dot_h = (win_height//field_w)-2

def draw_a(x, y):
    canvas.itemconfig(cell_matrix[x][y], state=NORMAL, tags='vis')

def advance():
    for i in range(len(cell_matrix)):
        for j in range(len(cell_matrix[i])):
            n = 0
            for i_shift in range(-1, 2):
                for j_shift in range(-1, 2):
                    if canvas.gettags(cell_matrix[(i + i_shift)%len(cell_matrix)] [(j + j_shift)%len(cell_matrix[i])])[0] == 'vis'  and (i_shift != 0 or j_shift != 0):              
                        n += 1		
            if n == 3 or (n == 2 and canvas.gettags(cell_matrix[i][j])[0] == 'vis'):
                psevdo_matrix[i][j] = 1
            else:
                psevdo_matrix[i][j] = 0        

def glider():
    clear()
    canvas.itemconfig(cell_matrix[10][10], state=NORMAL, tags='vis')
    canvas.itemconfig(cell_matrix[11][10], state=NORMAL, tags='vis')
    canvas.itemconfig(cell_matrix[12][10], state=NORMAL, tags='vis')
    canvas.itemconfig(cell_matrix[10][11], state=NORMAL, tags='vis')
    canvas.itemconfig(cell_matrix[11][12], state=NORMAL, tags='vis')

def step():
    advance()
    repaint()

def stop():
    root.after_cancel(after_id)

def clear():  
    for i in range(field_h):
        for j in range(field_w):
            canvas.itemconfig(cell_matrix[i][j], state=HIDDEN, tags='hid')
    
def repaint():
    for i in range(field_h):
        for j in range(field_w):			
            if psevdo_matrix[i][j] == 0:
                canvas.itemconfig(cell_matrix[i][j], state=HIDDEN, tags='hid')
            if psevdo_matrix[i][j] == 1:
                canvas.itemconfig(cell_matrix[i][j], state=NORMAL, tags='vis')

def auto():
    global after_id
    step()
    after_id = root.after(200, auto)

after_id = ''        

cell_matrix = []
psevdo_matrix = []
for i in range(field_h):
    sub_cell_matrix = []
    sub_psevdo_matrix = []
    for j in range(field_w):
        sub_psevdo_matrix.append(0)
        square = canvas.create_rectangle(dot_w*j, dot_h*i, dot_w + dot_w*j, dot_h + dot_h*i, fill=fill_color, outline = 'black', width = 1)
        canvas.itemconfig(square, state=HIDDEN, tags='hid')
        sub_cell_matrix.append(square)
    cell_matrix.append(sub_cell_matrix)
    psevdo_matrix.append(sub_psevdo_matrix)

frame = Frame(root)
btn1 = Button(frame, text='Eval', command = step)
btn2 = Button(frame, text='Clear', command = clear)
btn3 = Button(frame, text='Auto', command= auto)
btn4 = Button(frame, text='Glider', command= glider)
btn5 = Button(frame, text = 'Stop', command = stop)
btn1.pack(side='left')
btn2.pack(side='right')
btn3.pack(side='right')
btn4.pack(side='left')
btn5.pack(side = 'right')
frame.pack(side='bottom')

#canvas.bind('<B1-Motion>', draw_a)
#canvas.bind('<ButtonPress>', draw_a)

root.mainloop()
