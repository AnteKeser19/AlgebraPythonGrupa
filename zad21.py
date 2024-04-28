# a = 5
# b = 7
# zbroj = a+b
# print(f'Zbroj {a} i {b} je {zbroj}')


# def zbroji1():
#     a = int(input('Unesi a: '))
#     b = int(input('Unesi b: '))
#     zbroj = a+b
#     print(f'Zbroj {a} i {b} je {zbroj}')

# zbroji1()
# zbroji1()

def zbroji2(a,b):
    zbroj = a+b
    print(f'Zbroj {a} i {b} je {zbroj}')

def zbroji3():
    zbroj = a+b
    print(f'Zbroj {a} i {b} je {zbroj}')

def zbroji4():
    a = int(input('Unesi a: '))
    b = int(input('Unesi b: '))
    zbroj = a+b
    # print(f'Zbroj {a} i {b} je {zbroj}')
    return zbroj

def zbroji5(a,b):
    zbroj = a+b
    return zbroj


zbroji2(5,4)
a = int(input('Unesi a: '))
b = int(input('Unesi b: '))
zbroji2(a,b)
zbr = zbroji4()
print(zbr)
print(f'Zbroj {a} i {b} je {zbr}')
zbr5 = zbroji5(a,b)
print(f'Zbroj {a} i {b} je {zbr5}')


