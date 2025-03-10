import random
import time

class EthernetIPSimulator:
    def __init__(self):
        self.device_id = "EthernetIP_Device_001"
        self.status = "OK"

    def start(self):
        print("Simulando Ethernet/IP...")
        while True:
            # Simula el cambio de estado del dispositivo
            self.status = random.choice(["OK", "Fault", "Warning"])
            print(f"Dispositivo Ethernet/IP {self.device_id} - Estado: {self.status}")
            time.sleep(20)  # Simula una nueva lectura cada 20 segundos
