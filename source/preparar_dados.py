import pandas as pd
import numpy as np

# Preparar os dados de consumo
def preparar_consumo():
    consumo = pd.read_csv('../data/building_consumption.csv')
    consumo['timestamp'] = pd.to_datetime(consumo['timestamp'])
    consumo['tipo_dia'] = np.where(consumo['timestamp'].dt.dayofweek >= 5,
                                   'Final de Semana', 'Dia Útil')
    consumo['hora'] = consumo['timestamp'].dt.hour
    return consumo

# Preparar os dados de clima
def preparar_clima():
    clima = pd.read_csv('../data/weather_data.csv')
    clima['timestamp'] = pd.to_datetime(clima['timestamp'])
    return clima