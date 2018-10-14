def calculate_vat(netto, rate):
    return float(netto * rate) / 100


def prepare_report(pozycje, wybory):
    total_netto = 0
    total_brutto = 0

    for poz in pozycje:
        if poz['produkt'] in wybory:
            total_netto = total_netto + poz['cena']
            total_brutto = total_brutto + poz['cena'] +  calculate_vat(poz['cena'], poz['vat_procent'])
    return total_netto, total_brutto


def export_to_file(netto, brutto):
    print("netto,{0}".format(netto))
    print("brutto,{0}".format(brutto))


def retrieve_data(client_id, user_id):
    pozycje = [
        {'produkt': 'wyklady', 'cena': 121.10, 'vat_procent': 50},
        {'produkt': 'sprzatanie', 'cena': 199.10, 'vat_procent': 8.5},
        {'produkt': 'samochod', 'cena': 10921, 'vat_procent': 8},
        {'produkt': 'masaz', 'cena': 219, 'vat_procent': 25}        
    ]
    return pozycje


def main():
   
    pozycje = retrieve_data("exampleCompany", "maciej.kot")
    wybory = [ 'wyklady', 'samochod' ]

    netto, brutto = prepare_report(pozycje, wybory)

    export_to_file(netto, brutto)

if __name__ == "__main__":
    main()











def prepere_report(pozycje):
        total_cena = 0.0
        total_ilosc = 0
        total_kg = 0.0

        for poz in pozycje:
                total_cena = total_cena + poz['Cena']
                total_ilosc = total_ilosc + poz['Ilosc']
                total_kg = total_kg + poz['KG']
        return total_cena
