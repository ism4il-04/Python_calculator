def plus():
    a = float(input("entrez premier nombre: "))
    b = float(input("entrez deuxiem nombre: "))
    return a + b

def moins():
    a = float(input("entrez premier nombre: "))
    b = float(input("entrez deuxiem nombre: "))
    return a - b

def mult():
    a = float(input("entrez premier nombre: "))
    b = float(input("entrez deuxiem nombre: "))
    return a * b

def div():
    a = float(input("entrez premier nombre: "))
    b = float(input("entrez deuxiem nombre: "))
    if b == 0:
        return "impossible de faire division sur 0"
    else:
        return a / b

def menu():
    print("<==========Python Calculator==========>")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    global c
    c = input("choisissez une operation ")

while 1 :
   
    menu()

    if c == '1':
        print(plus())
    elif c == '2':
        print(moins())
    elif c == '3':
        print(mult())
    elif c == '4':
        print(div())
    elif c == '5':
        print("Au revoir :)")
        break
    else:
        print("choix invalide")