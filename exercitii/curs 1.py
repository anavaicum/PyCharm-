# def gaseste(caracter, word):
#     ct=0
#     for char in word:
#         if char == caracter:
#             ct+=1
#     return ct
#
# word="abcabbccab"
# caracter=input("caracter: ")
#
# print(gaseste(caracter,word))


# def schimb(sir):
#     vocale= "aeiouAEIOU"
#     for vocala in vocale:
#         sir=sir.replace(vocala,"?")
#     return sir
#
# sir="ahecoimnbe"
# print(schimb(sir))

def schimbare(sir):
    sirnou=[]
    vocale='aeiouAEIOU'
    for i in sir:
        if i in vocale:
            sirnou.append('?')
        else:
            sirnou.append(i)
    return ''.join(sirnou)

sir="ahecoimnbe"
print(schimbare(sir))
