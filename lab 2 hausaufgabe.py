#1
def elim_dupli(numere):
    new_num=[]
    for nr in numere:
        if nr not in new_num:
            new_num.append(nr)
    return new_num

#2

def perechi(numbers):
    count=0
    for i in range (0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]%10 == numbers[j]//10%10:
                if numbers[i]//10%10==numbers[j]%10:
                    count +=1
    return count



#3
def numar_maxim(numere):
    num_max=0
    lista_noua=sorted(numere, reverse=True)

    for i in lista_noua:
        num_max=num_max*100+i
    return num_max

#4
def ori_encrypt(numbers):
     key = int(numbers[0])
     encrypted_num = [(int(num) * key) for num in numbers]
     return encrypted_num


#5
def filtare_num(numere):
      lista_filtrate = []
      for nr in numere:
            x=nr//10
            y=nr%10
            if x == y * 3:
                lista_filtrate.append(nr)
            if y//x == 2:
                lista_filtrate.append(nr)
      return lista_filtrate

#6
def secventa_domino(numar1, numar2):

    return numar1 % 10 == numar2 // 10 or numar1 // 10 == numar2 %10

def secventa_maxima(numere):
    max_l = 1
    max_start_ind = 0
    current_l = 1
    current_ind = 0

    for i in range(1, len(numere)):
        if secventa_domino(numere[i - 1], numere[i]):
            current_l += 1
        else:
            if current_l > max_l:
                max_l = current_l
                max_start_ind = current_ind
            current_l = 1
            current_ind = i

    if current_l > max_l:
        max_l = current_l
        max_start_ind = current_ind

    if max_l > 1:
        return numere[max_start_ind:max_start_ind + max_l]
    else:
        return None

#7
def cmmdc(a,b):
    while (a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def cmmmc(a,b):
    return a * b // cmmdc(a,b)
def gaseste(l,fom,to):
    return cmmmc(l[fom],l[to])


numbers = [55, 61, 16, 77, 55, 88, 66,77,56, 65, 65]
lista_numere=[13, 28, 36, 31, 13, 63, 11]
print(elim_dupli(lista_numere))
print(perechi(numbers))
print(numar_maxim(lista_numere))
print(ori_encrypt(lista_numere))
print(filtare_num(lista_numere))
print(secventa_maxima(lista_numere))
print(gaseste([5,6,3,12,24,48],3,5))