from math import gcd

def simplify(a):
    d= gcd(a[0], a[1])

    return a[0]//d, a[1]//d

def test_simplify():
    assert simplify((2,2))==((1,1))

# def add(a,b):
#     return simplify((a[0]*b[1]+a[1]*b[0], a[1]*b[1]))

def sub(a,b):
    x= gcd(a[1],b[1])
    return simplify(((a[0]*x/a[1])-b[0]*x/b[1]), x)
# def test_add():
#     assert add((1,2),(2,3))==(7,6)
#     assert add((1, 2), (1, 2)) == (4, 4)

# def add_frac(fracs, frac):
#     fracs.append(frac)
def sub_frac(fracs, frac):
    fracs.append(frac)
# def sum_fracs(fracs):
#     s=0, 1
#     for frac in fracs:
#         s= add(s, frac)
#     return s
def sub_fracs(fracs):
    di=0, 1
    for frac in fracs:
        di= sub(di, frac)
    return di

# def test_sum_fracs():
#     assert sum_fracs([(1, 2), (2, 3), (1, 2)]) == (20, 12)
#     assert sum_fracs([(1, 2),  (1, 2)]) == (4,4)

def test_sub_fracs():
    assert sub_fracs([(3, 2), (1, 5)]) == (13, 10)
    assert sub_fracs([(4, 2),  (3, 2)]) == (1,2)

def menu():
    return """
    1 - add frac
    2- sum frac
    3- sub frac
    0- exit
    """

def main():
    fracs=[]
    while True:
        print(menu())
        opt=int(input('opt='))

        if opt ==1:
            n= int(input('n= '))
            m= int(input('m= '))
            sub_frac(fracs,(n,m))
        # if opt ==2:
        #     s=sum_fracs(fracs)
        #     print('sum= ',s)
        if opt==3:
            di=sub_fracs(fracs)
            print('sub= ',d)
        if opt==0:
            break
# test_sum_fracs()
# test_add()
test_sub_fracs()
test_sub()
test_simplify()
main()