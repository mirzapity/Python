import sys
entrada = input("Tecleame: ")
acertar = "Pepe"
salida = "Salida"
while entrada != acertar and entrada != salida:
    entrada = input("Sigue Probando: ")
if (entrada == acertar):
    print("Acertaste")
else:
    sys.exit()
