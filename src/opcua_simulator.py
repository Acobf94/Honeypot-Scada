import random
import time

class OpcuaSimulator:
    def __init__(self):
        self.node_id = "ns=1;s=Temperature"
        self.value = 22.0  # Valor inicial de temperatura

    def start(self):
        print("Simulando OPC UA...")
        while True:
            # Simula la actualización de un valor en el nodo OPC UA
            self.value = random.uniform(20.0, 30.0)
            print(f"Servidor OPC UA - Nodo {self.node_id}: {self.value:.2f}°C")
            time.sleep(15)  # Simula una nueva lectura cada 15 segundos
