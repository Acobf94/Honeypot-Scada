import time
from modbus_simulator import ModbusSimulator
from opcua_simulator import OpcuaSimulator
from ethernet_ip_simulator import EthernetIPSimulator

class Honeypot:
    def __init__(self):
        self.modbus_simulator = ModbusSimulator()
        self.opcua_simulator = OpcuaSimulator()
        self.ethernet_ip_simulator = EthernetIPSimulator()

    def start(self):
        print("Iniciando el Honeypot SCADA...")
        
        # Simulación de protocolos
        self.modbus_simulator.start()
        self.opcua_simulator.start()
        self.ethernet_ip_simulator.start()

        while True:
            time.sleep(60)  # Mantén el honeypot corriendo

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()
