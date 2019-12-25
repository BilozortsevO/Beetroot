from graphics import *

col = ['Black', 'White']

l = [[1, 0, 0, 1, 0],
     [0, 0, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 1, 0, 0],
     [1, 1, 1, 1, 0]]

win = GraphWin("Life", 501, 501)

def life_point(x, y, color):
    
    obj = Rectangle(Point(x*100 + 1, y*100 + 1), Point(x*100 + 99, y*100 + 99))
    obj.setFill(color)
    obj.setOutline(color)
    obj.draw(win)

if __name__ == '__main__':
    for y in range(len(l)):
        for x in range(len(l[y])):
            if l[y][x] == 1:
                life_point(x, y, col[0])
                y += 1
            else:
                life_point(x, y, col[1])
                y += 1
            x += 1

    win.getMouse()
    win.close()