import keyboard

def yazdir(konum):
    metin = ""
    for i in range(1, konum):
        metin += " "
    metin += "|"
    print(metin)

konum=0

while True:
    try:
        if keyboard.is_pressed("ç"):
            print("ç tuşuna basıldığı için !")
            break
        elif keyboard.read_key()=="right":
            konum += 1
            yazdir(konum)
        elif keyboard.read_key()=="left":
            konum -= 1
            yazdir(konum)
        elif keyboard.read_key()=="up":
            yazdir(konum)
        elif keyboard.read_key()=="down":
            yazdir(konum)
    except:
        break