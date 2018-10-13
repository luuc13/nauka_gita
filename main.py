#imie = 'LUKASZ'
#marka = 'fiat 126p'
#ilosc_drzwi = 2

#pojemnosc = 1.5

#marka_l = marka.lower()
#marka_h = marka.upper()

#print('witaj' + ' ' + imie)
#print('najlepszy na swiecie jest' + ' ' + marka + ' ' + 'ktora ma' + ' ' + str(ilosc_drzwi) + ' ' + 'drzwi')
#print(marka.upper())
#print(imie.lower())

#for s in samoloty:
#    print(s)

#for il in ilosc_miejsc:
#    print(il)

#samoloty = ['boing', 'f16']
#ilosc_miejsc = [300, 2]

#print('Dlugosc: {0}'.format(len(samoloty)))

#for idx in range (len(samoloty)):
#     print( "idx:" + str(idx) + ":" + samoloty[idx])
#     print(samoloty[idx] + ' ' + "ma ilosc miejsc" + ' ' + str(ilosc_miejsc[idx]))

#quad = {'name': 'kawassaki',
#        'przebieg': 1000,
#        'liczba_miejsc': 1}

#print(quad['name'])

#for key, value in quad.iteritems():
#    print("{0}:{1}".format(key, value))

#for key in quad:
#    print("{0}:{1}".format(key, quad[key]))


def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key, value))

if __name__ == "__main__":
    quad = {'name': 'kawassaki',
            'przebieg': 1000,
            'liczba_miejsc': 1}

    print_dict(quad)
    print_dict(quad)
