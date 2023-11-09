def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



def longest_prim(vector):
    max_l = 0  # definim 4 contoare
    max_start_ind = -1
    current_l = 0
    current_ind = -1

    for i in range(
            len(vector)):  # Aceast for parcurge vectorul și verifica pentru fiecare element dacă este prim folosind funcția isprime
        if isprime(vector[i]):
            current_l += 1  # daca elementul este prim, contorul nostru curent creste
            if current_ind == -1:  # daca indexul contorului este -1 atunci indexul devine pozitia curenta a elementului prim gasit adica i
                current_ind = i
        else:  # in cazul in care elementul gasit nu este numar prim verificam daca contorul curent este mai mare decat contorul maxim
            if current_l > max_l:
                max_l = current_l  # in caz afirmativ, contorul maxim ia valoarea contorului curent
                max_start_ind = current_ind  # si indexul maxim ia valoarea indexului curent i
            current_l = 0  # la final resetam contoarele curente si bucla se repeta
            current_ind = -1

    if current_l > max_l:
        max_l = current_l
        max_start_ind = current_ind

    if max_start_ind >= 0:  # verificam daca secventa maxima este mai mare decat 0 , in caz afirmativ returnam secventa
        return vector[max_start_ind:max_start_ind + max_l]
    else:
        return None  # in caz negativ returnam None


num = input("Introduceti numerele vectorului:")
num_list = [int(x) for x in num.split(",")]
result = longest_prim(num_list)

print(result)