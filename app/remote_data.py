# Code to get remote data
import requests
import json
from .constants import (COUNTRY, API_KEY, METHOD_TOP_ARTISTS, METHOD_TOP_TRACKS,
                        JSON_DATA_KEY_TOP_ARTISTS, JSON_DATA_KEY_TOP_TRACKS, 
                        JSON_DATA_ROOT_KEY_TOP_ARTISTS, JSON_DATA_ROOT_KEY_TOP_TRACKS)


BASE_URL = "http://ws.audioscrobbler.com/2.0/?method={0}&country={1}&api_key={2}&format=json"


def obtenerDatosDelJson(function):
    def wrapperFunction(*args, **kwargs):
        result = function(*args, **kwargs)
        if result.status_code == 200:
            jsonData = json.loads(result.content)
            if args[0] == METHOD_TOP_ARTISTS:
                return jsonData[JSON_DATA_ROOT_KEY_TOP_ARTISTS][JSON_DATA_KEY_TOP_ARTISTS]
            if args[0] == METHOD_TOP_TRACKS:
                return jsonData[JSON_DATA_ROOT_KEY_TOP_TRACKS][JSON_DATA_KEY_TOP_TRACKS]
            else:
                return jsonData
        else:
            return None
    return wrapperFunction


@obtenerDatosDelJson
def descargaDatos(method):
    url = BASE_URL.format(method,COUNTRY, API_KEY)
    response = requests.get(url)
    return response

