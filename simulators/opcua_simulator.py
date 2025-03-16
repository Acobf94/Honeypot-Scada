import random
import time
import logging
import os
from opcua import Server

os.makedirs('/home/abonilla/honeypot/logs', exist_ok=True)

logging.basicConfig(
    filename='/home/abonilla/honeypot/logs/honeypot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class OpcuaSimulator:
    def __init__(self):
        self.server = Server()
        self.server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
        self.idx = self.server.register_namespace("http://example.org")

    def start(self):
        logger.info("Simulador OPC UA iniciado en el puerto 4840.")
        objects = self.server.get_objects_node()
        temperature_node = objects.add_variable(self.idx, "Temperature", 0.0)
        temperature_node.set_writable()

        self.server.start()
        try:
            while True:
                value = round(random.uniform(20.0, 30.0), 2)
                temperature_node.set_value(value)
                logger.info(f"Servidor OPC UA - Nodo ns=1;s=Temperature: {value}°C")
                time.sleep(10)
        finally:
            self.server.stop()
            logger.info("Servidor OPC UA detenido.")
