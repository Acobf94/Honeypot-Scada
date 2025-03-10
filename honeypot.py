import time
import threading
from simulators.modbus_simulator import ModbusSimulator
from simulators.opcua_simulator import OpcuaSimulator
from simulators.ethernet_ip_simulator import EthernetIPSimulator

class Honeypot:
    def __init__(self):
        self.modbus_simulator = ModbusSimulator()
        self.opcua_simulator = OpcuaSimulator()
        self.ethernet_ip_simulator = EthernetIPSimulator()

    def start(self):
        print("Iniciando el Honeypot SCADA...")

        threading.Thread(target=self.modbus_simulator.start, daemon=True).start()
        threading.Thread(target=self.opcua_simulator.start, daemon=True).start()
        threading.Thread(target=self.ethernet_ip_simulator.start, daemon=True).start()

        while True:
            time.sleep(60)

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()
