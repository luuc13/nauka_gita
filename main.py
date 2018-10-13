#samochody = ['syrena', 'garbus', 'maluch', 'mini']
#ilosc = [3,2,2,2]

#for nr in range( len(samochody) ) :
#	print("nr" + " " + str(nr) + ":" + " " + samochody[nr])
#	print(samochody[nr] + " ma ilosc drzwi " + str(ilosc[nr])) 


li=['syrena', 'garbus', 'maluch', 'mini']
for i in li:
	marka_samochodu=raw_input("Podaj marke samochodu:")
	if marka_samochodu in li:
		        print("znam ja")
        else:
	        li.append(marka_samochodu)
		print("nie znam")touch 
