with open("fisier.txt", 'r') as f:
     C=f.read()

lista=C.split()

cuvant_vechi=input("Scrie cuvantul pe care vrei sa il inlocuiesti: " )
cuvant_nou=input("Scrie cuvantul pe care vrei sa il adaugi: " )
cnt=0
for i in range(len(lista)):
     if lista[i]==cuvant_vechi:
         cnt += 1
         lista.pop(i)
         lista.insert(i,cuvant_nou)



with open("fisier.txt", 'w')as f:
    tfinal= ' '.join(lista)
    f.write(tfinal)


if cnt==0:
    print("Nu exitsas cuvant de inlocuit")
else:
    print("Cuvantul a fost inlocuit de", cnt, "ori")
