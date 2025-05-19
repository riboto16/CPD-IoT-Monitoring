from influxdb_client import InfluxDBClient
from openpyxl import load_workbook
from datetime import datetime
import pytz
import time

# Conexión InfluxDB
url = "http://localhost:8086/"
token = "TOKEN CREADO EN INFLUX"
org = "ORGANIZACION DE INFLUX"
bucket = "NOMBRE_BUCKET_INFLUX"

# Dispositivos a consultar
devices = ["cpd_in", "cpd_RACK", "cpd_"]

# Ruta del archivo Excel
excel_path = "scripts/datos_sensores.xlsx"

# Zona horaria local
local_tz = pytz.timezone("Europe/Madrid")

# Conexión a InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

while True:
    wb = load_workbook(excel_path)
    sheet = wb.active

    for i, device in enumerate(devices):
        query = f'''
        from(bucket: "{bucket}")
          |> range(start: -1h)
          |> filter(fn: (r) => r["_measurement"] == "sensors")
          |> filter(fn: (r) => r["device"] == "{device}")
          |> filter(fn: (r) => r["_field"] == "temperature" or r["_field"] == "humidity" or r["_field"] == "co2")
          |> last()
        '''
        result = query_api.query(org=org, query=query)

        # Inicializar valores por defecto
        latest = {"temperature": 0, "humidity": 0, "co2": 0}
        timestamp = None

        for table in result:
            for record in table.records:
                field = record.get_field()
                value = record.get_value()
                latest[field] = value
                timestamp = record.get_time()

        hora_local_str = ""
        if timestamp:
            hora_local = timestamp.replace(tzinfo=pytz.UTC).astimezone(local_tz)
            hora_local_str = hora_local.strftime("%H:%M:%S")

        row = i + 2
        sheet[f"A{row}"] = device
        sheet[f"B{row}"] = latest["temperature"]
        sheet[f"C{row}"] = latest["humidity"]
        sheet[f"D{row}"] = latest["co2"]
        sheet[f"E{row}"] = hora_local_str

    wb.save(excel_path)
    print(f"Actualización completada: {datetime.now().strftime('%H:%M:%S')}")
    time.sleep(20)