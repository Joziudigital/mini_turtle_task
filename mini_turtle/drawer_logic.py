position_x = 0
position_y = 0

def adelante(pasos):
    global position_x, position_y
    print(" " * position_x + "-" * pasos + ">")
    position_x += pasos

def abajo(pasos):
    global position_x, position_y
    for i in range(pasos):
        print(" " * position_x + "|")
    print(" " * position_x + "V")
    position_y += pasos

def reiniciar():
    global position_x, position_y
    position_x = 0
    position_y = 0
