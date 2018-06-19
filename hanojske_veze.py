win = False
pole = []
def game_setup():
      global pole
      pocet = int(input("Počet disků:"))
      for i in range(0, pocet):
            pole.append([0,0,0])
      I = 1
      for a in pole:
            a[0] = I
            I += 1

def tah():
      global pocet
      pohyb = input("-->").split()
      start = int(pohyb[0])
      cil = int(pohyb[1])
      print(start,cil)

      for y in range(0, pocet):
            try:
                  if pole[cil][y+1] == 0:
                        pass
                  else:
                        pole[cil][y] =













while True:
      game_setup()
      while not win:
            tah()
            if pole[0][2] == 1:
                  win = True

      print("Vyhrál jsi")