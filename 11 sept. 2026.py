# Ce programme permet de vérifier si un mot est un palindrome

user_input_mot = str(input('Entrer une chaine de charactères : '))
input_mot = user_input_mot.lower().replace(' ', '').replace('é', 'e').replace('è', 'e').replace('ç', 'c').replace('à', 'a')
print('')

def is_palindrome(mot: str) -> bool:
    lenght = len(input_mot)

    if lenght % 2 == 0: return False

    for i in range(len(mot)):
        letter_a = mot[i]
        letter_b = mot[(lenght - i) - 1]

        if letter_a != letter_b:
            return False

    return True     

if is_palindrome(input_mot):
    print(f'{user_input_mot} est un palindrome')
else:
    print(f'{user_input_mot} n\'est pas un palindrome')

# Ce proramme permet de compter les voyelles d'un mot

def count_vowels(mot: str) -> list:
    VOWELS = "aeiouy"
    vowels_count = 0
    conson_count = 0

    for i in range(len(mot)):
        if mot[i] in VOWELS:
            vowels_count += 1
        else:
            conson_count += 1
    
    return [vowels_count, conson_count]

count = count_vowels(input_mot)
print(f'Il y a {count[0]} voyelle(s) et {count[1]} consone(s) dans {user_input_mot}')