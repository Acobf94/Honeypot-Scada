# Honeypot SCADA

Este proyecto implementa un honeypot SCADA desde cero, diseñado para simular los protocolos OPC UA, Modbus y Ethernet/IP con el fin de estudiar y detectar posibles ataques en sistemas industriales. El proyecto está dirigido a la investigación en ciberseguridad, específicamente en la protección de infraestructuras críticas.

## Descripción

El honeypot SCADA simula dispositivos y comunicaciones de sistemas de control industrial para atraer y detectar intrusiones, ataques o actividades maliciosas. El sistema incluye:

- Simulación de **Modbus**, **OPC UA** y **Ethernet/IP**.
- **Integración con Wazuh** para la detección avanzada de ataques y análisis en tiempo real.
- Despliegue y configuración sencilla en **AWS** o **Azure**.
  
Este proyecto tiene como objetivo crear un ambiente controlado para la detección y análisis de ataques a dispositivos SCADA.

## Estructura del Proyecto

### src/
Contiene el código fuente principal del honeypot SCADA:
- `honeypot.py`: El archivo principal que gestiona la simulación y la interacción con los protocolos.
- `modbus_simulator.py`: Código que simula un dispositivo Modbus.
- `opcua_simulator.py`: Código que simula un servidor OPC UA.
- `ethernet_ip_simulator.py`: Código que simula un dispositivo Ethernet/IP.

### config/
Archivos de configuración para el honeypot y su integración con Wazuh:
- `honeypot_config.yaml`: Configuración general del honeypot.
- `wazuh_config.json`: Configuración de reglas y alertas en Wazuh.

### scripts/
Contiene scripts útiles para desplegar y monitorear el honeypot:
- `deploy_aws.sh`: Script para desplegar el honeypot en AWS.
- `monitor_honeypot.sh`: Script para monitorear el estado del honeypot.

### logs/
Carpeta que contiene logs generados durante la ejecución del honeypot. Esta carpeta no se sube a GitHub, pero es útil para la revisión del funcionamiento del sistema.

### requirements.txt
Este archivo contiene las dependencias necesarias para ejecutar el proyecto. Para instalar las dependencias, simplemente ejecuta:

```bash
pip install -r requirements.txt
