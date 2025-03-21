import time
import threading
import logging
import os
from simulators.modbus_simulator import ModbusSimulator
from simulators.opcua_simulator import OpcuaSimulator
from simulators.ethernet_ip_simulator import EthernetIPSimulator

os.makedirs('/home/nombredeusuario/honeypot/logs', exist_ok=True)

logging.basicConfig(
    filename='/home/nombredeusuario/honeypot/logs/honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Honeypot:
    def __init__(self):
        self.modbus_simulator = ModbusSimulator()
        self.opcua_simulator = OpcuaSimulator()
        self.ethernet_ip_simulator = EthernetIPSimulator()

    def start(self):
        logger.info("Iniciando el Honeypot SCADA...")

        threading.Thread(target=self.modbus_simulator.start, daemon=True).start()
        threading.Thread(target=self.opcua_simulator.start, daemon=True).start()
        threading.Thread(target=self.ethernet_ip_simulator.start, daemon=True).start()

        while True:
            time.sleep(60)

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()
