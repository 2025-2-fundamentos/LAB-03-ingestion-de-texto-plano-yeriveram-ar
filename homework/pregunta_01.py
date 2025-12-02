"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd
    import re
	
    header_parts = dict()
    values = []
    entry_buffer = []
    with open('./files/input/clusters_report.txt') as file:
        for index, line in enumerate(file):
            if index < 4:
                # Catch header
                header_matches = re.finditer(r'\w+(?:\s\w+)*', line)
                for match in header_matches:
                    index = match.start()
                    if index not in header_parts:
                        header_parts[index] = []
                    header_parts[index].append(match.group(0).lower())
            else:
                # Catch entry
                num_matches = re.findall(r'\d+,*\d?', line)
                if num_matches:
                    entry_buffer = []
                    nums = [int(num) for num in num_matches[:2]] + [float(num_matches[2].replace(',', '.'))]
                    entry_buffer += nums + ['']
                text_match = re.findall(r'[a-zA-Z].+\n', line)
                if text_match:
                    entry_buffer[-1] += text_match[0][:-1] + ' '
                else:
                    values.append(entry_buffer)
    
    headers = [' '.join(header_list) for header_list in header_parts.values()]
    values = list(map(lambda x: x[:-1] + [' '.join(x[-1].split()).replace('.', '')], values))
    headers = list(map(lambda h: '_'.join(h.split()), headers))
    df = pd.DataFrame(values, columns=headers)

    return df