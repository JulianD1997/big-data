import csv
import pprint
path = "data/subvenciones.csv"
path2 = "data/subvenciones_2.csv"
with open(path, encoding='latin1') as file, open(path2,'w', encoding='latin1') as file2:
    reader = csv.DictReader(file)
    fields = reader.fieldnames + ['Justificación requerida', 'Justificación recibida']
    writer = csv.DictWriter(file2, fieldnames=fields)
    writer.writeheader()
    for line in reader:
        if not float(line['Importe']) > 300:
            line['Justificación requerida'] = "No"
            continue
        line['Justificación requerida'] = "Si"
        line['Justificación recibida'] = "No"
        writer.writerow(line)