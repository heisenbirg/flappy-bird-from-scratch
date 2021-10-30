import random
import time
import keyboard as k
def draw(px,py,yh,by,bx):

    height,width=25,25
    gameover=False

    

    for y in range(height+1):
        for x in range(width+1):
            if y==height or x==width or y==0 or x==0:
                print("*",end=" ")
            else:

                if(bx==x and by==y):
                    print("$")

                elif  px==x:
                    if y==yh+1 or y==yh or y==yh-1:
                        print(" ",end=" ")
                    else:
                        print("#"*1,end=" ")

                else:
                    print(" ",end=" ")
                
        print("")
    return width

def pipes():
    yh=random.randint(2,23)

    return yh

px=0
py=0
yh=3
by=12
bx=20
gameover=False
while(not gameover):
    width=draw(px,py,yh,by,bx)
    px+=1
    if(px>width):
        px=0
    if px==width:
        yh=pipes()
    if k.is_pressed("up"):
        by -= 1
    elif k.is_pressed("down"):
        by += 1
    elif k.is_pressed("left"):
        bx=bx-1
    elif k.is_pressed("right"):
        bx=bx+1
    if bx==px and (by <yh-1 or by>yh+1):
        gameover = True
        
        break
    time.sleep(0.3)
