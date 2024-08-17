import random
from datetime import time
from tkinter import *
import time


cl=False



def init():
    tab=[[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    i = random.randint(3, 8)
    j = random.randint(3, 8)
    while (tab[i][j] != 0 or not ((tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0 and
                                   tab[i - 3][j - 1] == 0 and tab[i - 3][j] == 0 and tab[i - 3][j + 1] and tab[i - 1][
                                       j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][
                                       j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
                                       j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][
                                       j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][
                                       j + 1] == 0 and tab[i - 2][j + 1] == 0) or (
                                          tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][j - 2] == 0 and
                                          tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and
                                          tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][j] == 0 and tab[i + 1][
                                              j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and
                                          tab[i + 1][j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0 and
                                          tab[i + 1][j - 3] == 0 and tab[i][j - 3] == 0 and tab[i - 1][j - 3] == 0 and
                                          tab[i + 1][j + 3] == 0 and tab[i][j + 3] == 0 and tab[i - 1][j + 3] == 0))):
        i = random.randint(3, 8)
        j = random.randint(3, 8)

    if ((tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0 and tab[i - 3][j - 1] == 0 and
         tab[i - 3][j] == 0 and tab[i - 3][j + 1] and tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][
             j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
             j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][
             j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0) and (
            tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][j - 2] == 0 and tab[i + 1][j - 1] == 0 and
            tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i + 1][
                j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0 and tab[i + 1][j - 3] == 0 and tab[i][
                j - 3] == 0 and tab[i - 1][j - 3] == 0 and tab[i + 1][j + 3] == 0 and tab[i][j + 3] == 0 and tab[i - 1][
                j + 3] == 0)):
        k = random.randint(1, 2)
        if k == 1:
            tab[i + 1][j] = 5
            tab[i][j] = 5
            tab[i - 1][j] = 5
            tab[i + 2][j] = 5
            tab[i - 2][j] = 5
        elif k == 2:
            tab[i][j + 1] = 5
            tab[i][j] = 5
            tab[i][j - 1] = 5
            tab[i][j + 2] = 5
            tab[i][j - 2] = 5
    elif (tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0 and tab[i - 3][j - 1] == 0 and
          tab[i - 3][j] == 0 and tab[i - 3][j + 1] and tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][
              j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
              j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][
              j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0):
        tab[i + 1][j] = 5
        tab[i][j] = 5
        tab[i - 1][j] = 5
        tab[i + 2][j] = 5
        tab[i - 2][j] = 5
    else:
        tab[i][j + 1] = 5
        tab[i][j] = 5
        tab[i][j - 1] = 5
        tab[i][j + 2] = 5
        tab[i][j - 2] = 5
    i = random.randint(2, 9)
    j = random.randint(2, 9)
    while (tab[i][j] != 0 or not ((tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0
                                        and tab[i - 1][
                                       j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][
                                       j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
                                       j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][
                                       j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][
                                       j + 1] == 0 and tab[i - 2][j + 1] == 0) or (
                                          tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][j - 2] == 0 and
                                          tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and
                                          tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][j] == 0 and tab[i + 1][
                                              j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and
                                          tab[i + 1][j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0 and
                                          tab[i + 1][j + 3] == 0 and tab[i][j + 3] == 0 and tab[i - 1][j + 3] == 0))):
        i = random.randint(2, 9)
        j = random.randint(2, 9)

    if ((tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0  and tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][
             j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
             j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][
             j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0) and (
            tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][j - 2] == 0 and tab[i + 1][j - 1] == 0 and
            tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i + 1][
                j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0  and tab[i + 1][j + 3] == 0 and tab[i][j + 3] == 0 and tab[i - 1][
                j + 3] == 0)):
        k = random.randint(1, 2)
        if k == 1:
            tab[i + 1][j] = 4
            tab[i][j] = 4
            tab[i - 1][j] = 4
            tab[i + 2][j] = 4

        elif k == 2:
            tab[i][j + 1] = 4
            tab[i][j] = 4
            tab[i][j - 1] = 4
            tab[i][j + 2] = 4

    elif (tab[i + 3][j - 1] == 0 and tab[i + 3][j] == 0 and tab[i + 3][j - 1] == 0 and tab[i - 3][j - 1] == 0 and
          tab[i - 3][j] == 0 and tab[i - 3][j + 1] and tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][
              j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][
              j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][
              j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0):
        tab[i + 1][j] = 4
        tab[i][j] = 4
        tab[i - 1][j] = 4
        tab[i + 2][j] = 4

    else:
        tab[i][j + 1] = 4
        tab[i][j] = 4
        tab[i][j - 1] = 4
        tab[i][j + 2] = 4

    for k in range(2):
        i = random.randint(2, 9)
        j = random.randint(2, 9)
        while (tab[i][j] != 0 or not ((tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and
                                       tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and
                                       tab[i - 2][j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][j] == 0 and
                                       tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
                                       tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0) or (
                                              tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][
                                          j - 2] == 0 and tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][
                                                  j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                                                  j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
                                              tab[i - 1][j + 1] == 0 and tab[i + 1][j + 2] == 0 and tab[i][
                                                  j + 2] == 0 and tab[i - 1][j + 2] == 0))):
            i = random.randint(2, 9)
            j = random.randint(2, 9)

        if ((tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][
            j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][j - 1] == 0 and tab[i + 2][j] == 0 and tab[i - 2][
                 j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][
                 j + 1] == 0 and tab[i - 2][j + 1] == 0) and (
                tab[i + 1][j - 2] == 0 and tab[i][j - 2] == 0 and tab[i - 1][j - 2] == 0 and tab[i + 1][j - 1] == 0 and
                tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                    j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i + 1][
                    j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0)):
            k = random.randint(1, 2)
            if k == 1:
                tab[i + 1][j] = 3
                tab[i][j] = 3
                tab[i - 1][j] = 3
            elif k == 2:
                tab[i][j + 1] = 3
                tab[i][j] = 3
                tab[i][j - 1] = 3
        elif (tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][j - 1] == 0 and
              tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i - 2][j - 1] == 0 and tab[i + 2][j] == 0 and
              tab[i - 2][j] == 0 and tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
              tab[i - 1][j + 1] == 0 and tab[i - 2][j + 1] == 0):
            tab[i + 1][j] = 3
            tab[i][j] = 3
            tab[i - 1][j] = 3
        else:
            tab[i][j + 1] = 3
            tab[i][j] = 3
            tab[i][j - 1] = 3
    for k in range(3):
        i = random.randint(1, 9)
        j = random.randint(1, 9)
        while (tab[i][j] != 0 or not ((tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and
                                       tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and
                                       tab[i + 2][j] == 0 and
                                       tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
                                       tab[i - 1][j + 1] == 0 ) or (
                                               tab[i + 1][j - 1] == 0 and tab[i][j - 1] == 0 and tab[i - 1][
                                                  j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                                                  j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
                                              tab[i - 1][j + 1] == 0 and tab[i + 1][j + 2] == 0 and tab[i][
                                                  j + 2] == 0 and tab[i - 1][j + 2] == 0))):
            i = random.randint(1, 9)
            j = random.randint(1, 9)

        if ((tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][j - 1] == 0 and tab[i][
            j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i + 2][j] == 0  and tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][
                 j + 1] == 0 ) and (
                  tab[i + 1][j - 1] == 0 and
                tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0 and tab[i + 1][j] == 0 and tab[i][j] == 0 and tab[i - 1][
                    j] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and tab[i - 1][j + 1] == 0 and tab[i + 1][
                    j + 2] == 0 and tab[i][j + 2] == 0 and tab[i - 1][j + 2] == 0)):
            k = random.randint(1, 2)
            if k == 1:
                tab[i + 1][j] = 2
                tab[i][j] = 2

            elif k == 2:
                tab[i][j + 1] = 2
                tab[i][j] = 2

        elif (tab[i - 1][j] == 0 and tab[i + 1][j] == 0 and tab[i + 2][j - 1] == 0 and tab[i + 1][j - 1] == 0 and
              tab[i][j - 1] == 0 and tab[i - 1][j - 1] == 0  and tab[i + 2][j] == 0 and
              tab[i + 2][j + 1] == 0 and tab[i + 1][j + 1] == 0 and tab[i][j + 1] == 0 and
              tab[i - 1][j + 1] == 0 ):
            tab[i + 1][j] = 2
            tab[i][j] = 2

        else:
            tab[i][j + 1] = 2
            tab[i][j] = 2

    for k in range (3):
        i = random.randint(1, 10)
        j = random.randint(1, 10)
        while(tab[i][j]!=0 or tab[i+1][j+1]!=0 or tab[i+1][j]!=0 or tab[i+1][j-1]!=0 or tab[i-1][j+1]!=0 or tab[i-1][j]!=0 or tab[i-1][j-1]!=0 or tab[i][j-1]!=0 or tab[i][j+1]!=0):
            i = random.randint(1, 10)
            j = random.randint(1, 10)
        tab[i][j]=1
    for i in range(12):
        for j in range(12):
            if (i==0 or i==11 or j==0 or j==11):
                tab[i][j]=9
    tab1=[[tab[i][j] for j in range (1,12)] for i in range (1,12)]


    return tab1

def click(e):
    global cl
    cl=True
    print(cl)

def callback(e):
    global cl
    #m = -1
    #n = -1
    size=50
    a=e.x
    b=e.y
    #root.bind('<1>', click)

    #root.update()



    #for i in range(10):
        #for j in range(10):

            #if a>j*size and b>i*size and a<j*size+size and b<i*size+size and cl==True:
                #m=j
                #n=i

                #cl=False
                #print(n,m)
    if cl == False:

        for i in range(10):
            for j in range(10):
                if a > j * size and b > i * size and a < j * size + size and b < i * size + size:
                #m=j
                #n=i
                    if tab[i][j] == 1:
                        tab[i][j]=8
                    elif tab[i][j]==2 or tab[i][j]==3 or tab[i][j]==4 or tab[i][j]==5 :
                        tab[i][j]=8
                    elif tab[i][j]==0:
                        tab[i][j]=9

                    cl=False

            #if i==n and j==m:
                #if tab[i][j] == 1:
                    #tab[i][j]=8
                #elif tab[i][j]==2 or tab[i][j]==3 or tab[i][j]==4 or tab[i][j]==5 :
                    #tab[i][j]=8
                #elif tab[i][j]==0:
                    #tab[i][j]=9


#def saisir_coord(tab):
    #n=int(input("Give i"))
    #m=int(input("Give j"))
    #root.bind('<Motion>', callback)
    #for i in range(10):
        #for j in range(10):
            #if (i==n and j==m):
                #if tab[i][j] == 1:
                    #tab[i][j]=8
                #elif tab[i][j]==2 or tab[i][j]==3 or tab[i][j]==4 or tab[i][j]==5 :
                    #tab[i][j]=8
                #else:
                    #tab[i][j]=9









def stop(tab):
    stop=True
    for i in range (10):
        for j in range (10):
            if tab[i][j]!=0 and tab[i][j]!=9 and tab[i][j]!=8:
                stop=False
    return stop

root = Tk()

root.title("GAME")
root.geometry("500x500")
root.configure(bg="white")
S_Canvas = Canvas(root,width=500,height=500,bg="white")
S_Canvas.pack()


def draw(tab):
    size=50
    for i in range (10):
        for j in range (10):
            x1, y1, x2, y2 = j * size, i * size, j * size + size, i * size + size
            if tab[i][j] == 9:
                rectangle=S_Canvas.create_rectangle(x1, y1, x2, y2, fill='blue')
            elif tab[i][j] == 8:
                rectangle=S_Canvas.create_rectangle(x1, y1, x2, y2, fill='brown')
            else:
                rectangle=S_Canvas.create_rectangle(x1, y1, x2, y2, fill='red')



def draw_tab(tab):
    for i in range (10):
        for j in range (10):
            print(tab[i][j], end=" ")
        print('')


tab=init()
draw(tab)



while True:
    #S_Canvas.delete("all")

    #root.bind('<1>', click)
    draw(tab)
    root.bind('<1>', callback)
    root.update()

    if stop(tab) == True:
        for i in range(10):
            for j in range(10):
                if tab[i][j] == 0:
                    tab[i][j] = 9
        draw(tab)
        #time.sleep(3)
        
        tab = init()

    #root.update()
    #draw_tab(tab)










    #saisir_coord(tab)



root.mainloop()











