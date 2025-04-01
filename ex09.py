# Faça um contador de minutos e segundos com 02 casas decimais de
# formatação se assemelhando ao mostrador de um relógio XX:XX. O programa deve durar 
# 1 minuto e os segundos do dia de seu aniversário. Pesquise uma forma de apagar o 
# console através de comando no interpretador python para que funcione da seguinte 
# forma:
# 00:00 ==> 1 segundo ==> apaga ==> 00:01 ==> 1 segundo ==> apaga ==> 00:02 ...

#Bibliotecas
import time
import os

#Entradas
min = -1
sec = -1

try:
    for x in range (2):
        min = min + 1
        for y in range (60):
            print(f"{min:02d}:{sec:02d}")
            time.sleep(1)
            os.system('cls')
            sec = sec + 1
            
            if sec == 59:
                sec = 0
            if min == 1 and sec == 31:
                break
except KeyboardInterrupt:
    print("Programa finalizado pelo usuário")