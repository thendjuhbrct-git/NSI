# Ce programme permet de passer n'import quel nombre d'une base 10 a une base <= 36

CARACTERES = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == '__main__':
    input_nombre = int(input("Entrez un nombre a convertir : "))
    input_base = int(input("Entrez la base dans laquelle vous voulez convertir ce nombre : "))

def changement_base(nombre: int, base: int) -> int:
    _nombre = nombre
    reste = ""

    if not 1 <= base <= 35:
        return print("La base doit être comprise entre 1 et 36")

    while nombre != 0:
        reste = CARACTERES[int(nombre % base)] + reste
        nombre = nombre // base

    return reste

if __name__ == '__main__':
    print('')
    print(f'{input_nombre} en base {input_base} est {changement_base(input_nombre, input_base)}')