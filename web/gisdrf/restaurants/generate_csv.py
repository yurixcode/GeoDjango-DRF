# Models
# from .models import Restaurant

# Utils
import csv

def generate_csv():

    data = [
        ['nombre', 'móvil', 'fijo'],
        ['aaaa', '39489843', '9999'],
        ['bbbb', '39489843', '9999'],
        ['cccc', '39489843', '9999'],
    ]

    with open('ejemplo_csv', 'w', newline='', encoding="utf8") as arq:
        writer = csv.writer(arq, delimiter=";")
        writer.writerows(data)


if __name__ == "__main__":
    generate_csv()
