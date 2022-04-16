import requests
from json import dumps
from threading import Thread


def get_units_information():
    """
    This function returns an array with all the microbuses units information from two APIs.
    Doesn't need parameters.
    """

    #Created/Updated units
    global data
    data = []

    #Gets the microbuses information provided by the CDMX API.
    #This information is outdated, then this is just an example.
    #The API requires the CDMX permission for getting the updated microbuses positions.
    cdmx_api_url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?' + \
            'resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=300'
    fetch_microbus_info = requests.get(url=cdmx_api_url).json()['result']['records']

    #Sets the relevant microbus unit information in a JSON and adds it to the data array.
    def unit_addition(microbus: dict):
        global data
        
        #Dictionary verifier
        if 'position_latitude' not in microbus:
            return None

        #Locality getter
        reverse_geocode_url = 'https://api.bigdatacloud.net/data/reverse-geocode-client?' + \
                'latitude={}&longitude={}&localityLanguage=es'.format(
                        microbus['position_latitude'],
                        microbus['position_longitude']
                    )
        try:
            locality = requests.get(url=reverse_geocode_url).json()
            locality = locality['localityInfo']['administrative'][2]['name']
        except:
            locality = 'Desconocido'

        #Microbus unit addition to the data array
        data.append({
            'label': microbus['vehicle_label'],
            'latitude': microbus['position_latitude'],
            'longitude': microbus['position_longitude'],
            'alcaldia': locality
        })

    #Threads for saving time between responses from the locality API
    unit_threads = {}
    for microbus in fetch_microbus_info:
        unit_threads[microbus['vehicle_label']] = Thread(
                target=unit_addition,
                args=(microbus,)
            )
        unit_threads[microbus['vehicle_label']].start()
    for unit in unit_threads:
        unit_threads[unit].join()

    return data
