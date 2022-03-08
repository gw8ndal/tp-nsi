import requests as r
import csv
import folium as f

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
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lat, longitude = row['point_geo_ban'].split(',')
            lat = float(lat)
            longitude = float(longitude)
            build_school(row, map, lat, longitude)
    return map
            

def build_school(row, map, lat, longitude):
    html_code = f"{row['nom_et']}"
    icon_color = "red"
    return f.Marker([lat, longitude],popup = html_code, icon = f.Icon(color = icon_color)).add_to(map)

map = f.Map(location=[48.518042, -3.943186])
fichier = get_csv_data('https://www.data.gouv.fr/fr/datasets/r/a1075259-09ca-4c22-9e35-b2cd6bbf5c36', 'schools.csv')

school_data = read_data(fichier)

school_data.save('colleges.html')