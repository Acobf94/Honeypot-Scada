import random
import time
import logging
import os

os.makedirs('/home/nombredeusuario/honeypot/logs', exist_ok=True)

logging.basicConfig(
    filename='/home/nombredeusuario/honeypot/logs/honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EthernetIPSimulator:
    def __init__(self):
        self.device_id = "EthernetIP_Device_001"
        self.status = "OK"

    def start(self):
        logger.info("Simulador Ethernet/IP iniciado.")
        while True:
            self.status = random.choice(["OK", "Fault", "Warning"])
            logger.info(f"Dispositivo Ethernet/IP {self.device_id} - Estado: {self.status}")
            time.sleep(20)
