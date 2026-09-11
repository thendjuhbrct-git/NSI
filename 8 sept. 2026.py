# Ce programme permet de passer n'import quel nombre d'une base 10 a une base <= 36

CHARACTERES = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_nombre = int(input("Entrez un nombre a convertir : "))
input_base = int(input("Entrez la base dans laquelle vous voulez convertir ce nombre : "))

def changement_base(nombre: int, base: int) -> None:
    _nombre = nombre
    reste = ""
    
    print('')

    if not 1 <= base <= 35:
        return print("La base doit être comprise entre 1 et 36")

    while nombre != 0:
        reste = CHARACTERES[int(nombre % base)] + reste
        nombre = nombre // base
        
        print(reste)

    print('')
    return print(f'{_nombre} en base {base} est {reste}')

changement_base(input_nombre, input_base)