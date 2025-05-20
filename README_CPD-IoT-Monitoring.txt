# CPD-IoT-Monitoring

Repositorio del Trabajo Fin de Máster en Internet de las Cosas (UNIR):  
**Transformación Digital de un Centro de Procesamiento de Datos mediante BIM, IoT y Simulación Energética**.

## 📌 Descripción

Este proyecto implementa una solución de monitorización ambiental en un CPD mediante sensores conectados a microcontroladores ESP32. Se registran y transmiten datos de temperatura, humedad y CO₂ en tiempo real a InfluxDB, y se visualizan mediante Grafana. Además, se incluye un script para exportar los datos a Excel.

## 🛠️ Contenido del repositorio

- `ESP32_Sensor_Temp_Humd_CO2.ino`: Código para ESP32 que lee sensores DHT11 y CCS811 y envía datos a InfluxDB usando HTTP.
- `influx_excel.py`: Script en Python que consulta datos recientes desde InfluxDB y los exporta a un archivo Excel.
- `docker-compose.yml`: Configuración para desplegar InfluxDB y Grafana con Docker.
- `scripts/datos_sensores.xlsx`: Archivo de Excel de destino para el script Python (debe crearse si no existe).
- `README.md`: Descripción del proyecto.

## 📦 Tecnologías utilizadas

- ESP32 (con Arduino IDE)
- Sensores DHT11 y CCS811
- InfluxDB
- Grafana
- Python 3 + openpyxl + influxdb-client
- Docker y Docker Compose

## 📄 Licencia

Este repositorio se distribuye bajo licencia MIT. Puedes reutilizar el código citando la fuente.

## 🔗 Cita recomendada (APA 7ª ed.)

Rincón Bolaño, O. (2025). *CPD-IoT-Monitoring* [Repositorio en GitHub]. https://github.com/tu_usuario/CPD-IoT-Monitoring


Autores:
- **Alba Lucía Núñez**
- **Otoniel Rincón Bolaño**
- **Ramón Rodríguez**