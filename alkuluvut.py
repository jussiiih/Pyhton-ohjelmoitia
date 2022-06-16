def alkuluvut():
    numero = 2
    while True:
        if onko_alkuluku(numero) == True:
            yield numero
        numero += 1
    
def onko_alkuluku (luku):
    if luku == 2:
            return True
    if luku > 2:
        jakaja = 2
        while jakaja < luku:
            if luku % jakaja == 0:
                return False
            else:
                jakaja += 1
        return True

            
if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))