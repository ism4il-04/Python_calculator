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

c = 1

while c != '5':
    menu()
    match c:
        case '1':
            print(plus())
        case '2':
            print(moins())
        case '3':
            print(mult())
        case '4':
            print(div())
        case '5':
            print("au revoir :'(")
        case _:
            print("choix invalide")
        
