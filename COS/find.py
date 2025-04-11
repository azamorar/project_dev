import requests
import json

# Endpoint genérico
GENERIC_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"

try:
    response = requests.get(GENERIC_ENDPOINT)
    data = response.json()  # Obtener la respuesta en formato JSON
    print(json.dumps(data, indent=4))  
except Exception as e:
    print("Error al llamar al endpoint genérico:", e)