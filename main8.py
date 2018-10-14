import pprint

def get_pozycje():
    p = [
        {'produkty': 'ziemniaki0', 'id': 1, 'masa': 10, 'ilosc': 10, 'cena': 15.40},
        {'produkty': 'ziemniaki1', 'id': 2, 'masa': 20, 'ilosc': 20, 'cena': 16.40},
        {'produkty': 'ziemniaki2', 'id': 3, 'masa': 30, 'ilosc': 30, 'cena': 17.40},
        {'produkty': 'ziemniaki3', 'id': 4, 'masa': 40, 'ilosc': 40, 'cena': 18.40},
        {'produkty': 'ziemniaki4', 'id': 5, 'masa': 50, 'ilosc': 50, 'cena': 19.40},
        {'produkty': 'ziemniaki5', 'id': 6, 'masa': 45, 'ilosc': 60, 'cena': 20.40},
        {'produkty': 'ziemniaki6', 'id': 7, 'masa': 44, 'ilosc': 70, 'cena': 25.40},
        {'produkty': 'ziemniaki7', 'id': 8, 'masa': 21, 'ilosc': 80, 'cena': 23.40},
        {'produkty': 'ziemniaki8', 'id': 9, 'masa': 14, 'ilosc': 90, 'cena': 24.40}        
    ]
    return p


def main():
        pozycje = get_pozycje()

        total_cena = 0.0
        total_ilosc = 0
        total_masa = 0

        for poz in pozycje:
            total_cena = total_cena + poz['cena']
            total_ilosc = total_ilosc + poz['ilosc']
            total_masa = total_masa + poz['masa']

        print("Cena za wszystkie produkty: " + str(total_cena))
        print(" ")
        print("Ilosc wszystkich produktow: " + str(total_ilosc))      
        print(" ")
        print("Masa wszystkich produktow: " + str(total_masa))      
        print(" ")

if __name__ == "__main__":
    main()
