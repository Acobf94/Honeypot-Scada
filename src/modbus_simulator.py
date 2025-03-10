import random
import time

class ModbusSimulator:
    def __init__(self):
        self.device_id = 1
        self.registers = {100: 0, 101: 0, 102: 0}  # Registros Modbus simples

    def start(self):
        print("Simulando Modbus...")
        while True:
            # Simula la lectura/escritura de registros
            register = random.choice(list(self.registers.keys()))
            value = random.randint(0, 255)
            self.registers[register] = value
            print(f"Dispositivo Modbus {self.device_id} - Registro {register}: {value}")
            time.sleep(10)  # Simula una nueva lectura cada 10 segundos
