import datetime
import pandas as pd
from generalModule.models import Actividad
pd.set_option('display.max_columns', 500)

df = pd.read_csv('Actividades.csv')


def str_object_datetime(obj):
    month, year = obj.split('-')
    obj = f'01-04-{year} 00:00:00'
    print(obj)
    return datetime.datetime.strptime(obj, '%d-%m-%y %H:%M:%S')


df['fechaDoc'] = df['fechaDoc'].apply(lambda x: str_object_datetime(x))
df['fechaZafra'] = df['fechaZafra'].apply(lambda x: 1)


actividades_lista = list()

for idx, row in df.iterrows():
    num_actividad, fecha_doc, fecha_zafra, actividad, duracion = row

    actividades_lista.append(
        Actividad(
            num_actividad=num_actividad,
            fechadoc=fecha_doc,
            fechazafra_id=fecha_zafra,
            nombre_actividad=actividad,
            duracion=duracion
        )
    )


Actividad.objects.bulk_create(actividades_lista)