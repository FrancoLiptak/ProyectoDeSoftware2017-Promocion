import json
import requests

class ResourceCollector:

    @staticmethod
    def getResource(url):
        response = requests.get(url)
        return response.json()

    @staticmethod
    def getTypeOfResource(url):
        a = requests.get(url).json()
        result = ((a[0]['nombre'], a[0]['nombre']),)
        for element in range(1, len(a)):
            result = result + ((a[element]['nombre'], a[element]['nombre']),)
        return result

    @staticmethod
    def getAllResources():
        resources = []

        resources.append(ResourceCollector.getResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-documento"))
        resources.append(ResourceCollector.getResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/obra-social"))
        resources.append(ResourceCollector.getResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-agua"))
        resources.append(ResourceCollector.getResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-vivienda"))
        resources.append(ResourceCollector.getResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-calefaccion"))

        return resources
