import threading
import time

contador = 0
parar = True

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  (self.filosofosNum + 1) % 5 #Se corrigio esta variable
   
    def hilosFilosofos(self):
        global contador
        global parar
        while parar:
            print("Filosofo iniciando", self.filosofosNum)
            time.sleep(2)
            print("Filosofo ", self.filosofosNum, "pasando tenedor del lado izquierdo")
            time.sleep(2)
            self.tenedores[self.filosofosNum].acquire()
            print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
            time.sleep(2)
            self.tenedores[self.datoTemporal].acquire()
            print("Filosofo ", self.filosofosNum, "libre derecho")
            time.sleep(2)
            self.tenedores[self.datoTemporal].release()  
            print("Filosofo ", self.filosofosNum, "libre izquierdo")
            time.sleep(2)
            self.tenedores[self.filosofosNum].release()
            contador = contador + 1
            if contador >= self.filosofosNum:
                parar =False    #Variable para terminar el ciclo
              
    def run(self):
        global parar
        self.hilosFilosofos()
        


tenedores = [1,1,1,1,1] #Se cambio el nombre del arreglo

for i in range(0,5):
    #print("for uno: ", i)
    tenedores[i] = threading.BoundedSemaphore(1)

for i in range(0,5):
    #print("for dos: ", i)
    total = TenedorFilosofo(tenedores,i)
    total.start()
    time.sleep(2)   #Se agrego aquí un tiempo de espera