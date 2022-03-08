import requests as r
import csv

def get_csv_data(url, filename):
    """
    Récupère toutes les données à partir d'une URL et les met dans un fichier csv
    """
    assert type(url) == str, "The URL should be a string but is a %s" % (type(url))
    assert type(filename) == str, "The name should be a string but is a %s" % (type(filename))

    response = r.get(url)
    local_file = filename
    with open(local_file, 'wb') as csvfile:
        csvfile.write(response.content)
    return local_file


def read_data(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


fichier = get_csv_data('https://www.data.gouv.fr/fr/datasets/r/a1075259-09ca-4c22-9e35-b2cd6bbf5c36', 'schools.csv')
print(fichier)
read_data(fichier)