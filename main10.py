file = open("zwierzeta.txt", "r")

zwierzeta = []
for l  in file:
    zwierzeta.append(l.strip())
file.close()
#print(zwierzeta)

zwierze=raw_input("podaj zwierzaka: ")
if zwierze in zawiera:
   print("y")
else:
   print("nie znane")

print(zwierzeta)
