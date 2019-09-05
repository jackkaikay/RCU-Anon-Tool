
import csv


with open('Deprivation_Band_Lookup.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == 'BB1 1ZZ':
            dep_band_final = row[1]
            print(dep_band_final)