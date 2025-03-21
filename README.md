# Honeypot SCADA

Este proyecto implementa un honeypot SCADA desde cero, diseñado para simular los protocolos OPC UA, Modbus y Ethernet/IP con el fin de estudiar y detectar posibles ataques en sistemas industriales. El proyecto está dirigido a la investigación en ciberseguridad, específicamente en la protección de infraestructuras críticas.

## Descripción

El honeypot SCADA simula dispositivos y comunicaciones de sistemas de control industrial para atraer y detectar intrusiones, ataques o actividades maliciosas. El sistema incluye:

- Simulación de **Modbus**, **OPC UA** y **Ethernet/IP**.
- **Integración con Wazuh** para la detección avanzada de ataques y análisis en tiempo real.
  
Este proyecto tiene como objetivo crear un ambiente controlado para la detección y análisis de ataques a dispositivos SCADA.

## Requisitos

El honeypot ha sido probado en **Ubuntu 22.04**, y las siguientes dependencias son necesarias para su funcionamiento:

- Python 3.8 o superior
- Pip (para la instalación de dependencias)
- Systemd (para gestionar el servicio del honeypot)
- Wazuh (para la monitorización y gestión de logs)

## Instalación

Sigue los pasos a continuación para montar el honeypot en tu sistema Ubuntu 22.04.

### Paso 1: Clonar el Repositorio

Primero, clona este repositorio en tu máquina:

```bash
git clone https://github.com/nombredeusuario/Honeypot-Scada.git
cd Honeypot-Scada
```

### Paso 2: Instalar Dependencias

Asegúrate de tener `pip` instalado en tu sistema. Luego, instala las dependencias necesarias listadas en el archivo `requirements.txt`:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Paso 3: Configurar el Servicio con systemd

Para ejecutar el honeypot como un servicio en Ubuntu, sigue estos pasos:

1. Copia el archivo `honeypot.service` en el directorio de systemd:

   ```bash
   sudo cp systemd/honeypot.service /etc/systemd/system/
   ```

2. Recarga el demonio de systemd para que reconozca el nuevo servicio:

   ```bash
   sudo systemctl daemon-reload
   ```

3. Habilita el servicio para que se inicie automáticamente al arrancar el sistema:

   ```bash
   sudo systemctl enable honeypot.service
   ```

4. Inicia el servicio:

   ```bash
   sudo systemctl start honeypot.service
   ```

5. Verifica el estado del servicio:

   ```bash
   sudo systemctl status honeypot.service
   ```

### Paso 4: Configuración de los Simuladores

El proyecto incluye simuladores de diferentes protocolos SCADA. Asegúrate de que cada simulador esté configurado correctamente. Los simuladores se encuentran en el directorio `simulators`.

- Modbus: El archivo principal es `modbus_simulator.py`. Asegúrate de que la configuración de puertos y direcciones IP sea la adecuada para tu red.

```bash
cd simulators
python3 modbus_simulator.py
```

### Paso 5: Configuración de Wazuh

Si deseas integrar el honeypot con Wazuh para la gestión de logs y la detección de ataques, sigue estos pasos:

1. Instala Wazuh en tu máquina siguiendo [esta guía oficial](https://documentation.wazuh.com/current/installation-guide/index.html).
2. Configura Wazuh para monitorear los logs generados por el honeypot.

### Paso 6: Monitorización y Análisis

Una vez que el honeypot esté funcionando y Wazuh esté configurado, los ataques y eventos serán registrados en los logs del sistema y podrás analizarlos a través de la interfaz de Wazuh o cualquier otra herramienta que utilices para analizar logs.

## Uso

Para ejecutar el honeypot manualmente, puedes usar el siguiente comando:

```bash
python3 honeypot.py
```

El script escuchará los puertos configurados para los protocolos SCADA (Modbus, OPC UA, Ethernet/IP) y generará logs con los ataques detectados.

## Contribuciones

Si deseas contribuir al proyecto, por favor abre un "pull request" con las mejoras o correcciones que desees hacer. Si encuentras algún error o tienes sugerencias, no dudes en abrir un "issue".

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo [LICENSE](LICENSE).
