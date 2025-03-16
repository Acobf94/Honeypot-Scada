import random
import time
import logging
import os
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

os.makedirs('/home/abonilla/honeypot/logs', exist_ok=True)

logging.basicConfig(
    filename='/home/abonilla/honeypot/logs/honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ModbusSimulator:
    def __init__(self):
        self.store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*100),
            co=ModbusSequentialDataBlock(0, [0]*100),
            hr=ModbusSequentialDataBlock(0, [0]*100),
            ir=ModbusSequentialDataBlock(0, [0]*100))
        self.context = ModbusServerContext(slaves=self.store, single=True)

    def update_values(self):
        while True:
            address = random.randint(0, 99)
            value = random.randint(0, 255)
            self.store.setValues(3, address, [value])
            logger.info(f"Dispositivo Modbus 1 - Registro {address}: {value}")
            time.sleep(10)

    def start(self):
        logger.info("Simulador Modbus iniciado en el puerto 502.")
        StartTcpServer(self.context, address=("0.0.0.0", 502), defer_start=True)
        self.update_values()
