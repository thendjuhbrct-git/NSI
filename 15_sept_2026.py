from _8_sept_2026 import changement_base

user_input = int(input('Entrez une durée en secondes (un nombre entier) : '))
print('')

# Cette fonction permet de passer une durée en secondes vers une durée en minutes / secondes

def sec_to_min_sec(sec: int) -> tuple[int, int]:
    return (sec//60, sec%60)

# Cette fonction permet de passer d'une durée en secondes vers une durée en heures / minutes / secondes

def sec_to_h_min_sec(sec: int) -> tuple[int, int, int]:
    h = sec//3600
    return (h,) + sec_to_min_sec(sec%3600)

# Cette fonction permet de passer d'une durée en secondes vers une durée en jours/ heures / minutes / secondes

def sec_to_d_h_min_sec(sec: int) -> tuple[int, int, int, int]:
    d = sec//86400
    return (d,) + sec_to_h_min_sec(sec%86400)

###

d_h_min_sec = sec_to_d_h_min_sec(user_input)
print(f'Il y a {d_h_min_sec[0]} jour(s), {d_h_min_sec[1]} heure(s), {d_h_min_sec[2]} minute(s) et {d_h_min_sec[3]} seconde(s) dans {user_input} seconde(s)')
print('')

###

d_user_input = int(input('Entrez une durée en jours (un nombre entier) : '))
h_user_input = int(input('Entrez une durée en heures (un nombre entier) : '))
min_user_input = int(input('Entrez une durée en minutes (un nombre entier) : '))
sec_user_input = int(input('Entrez une durée en secondes (un nombre entier) : '))
print('')

d_h_min_sec = (d_user_input, h_user_input, min_user_input, sec_user_input)

# Cette fonction permet de passer d'une durée en jours / heures / minutes / secondes en secondes

def in_sec(d_h_min_sec: tuple[int, int, int, int]) -> int:
    return int(86400 * d_h_min_sec[0] + 3600 * d_h_min_sec[1] + 60 * d_h_min_sec[2] + d_h_min_sec[3])

result = in_sec(d_h_min_sec)
print(f'Il y a {result} seconde(s) dans {d_user_input} jour(s), {h_user_input} heure(s), {min_user_input} minute(s), {sec_user_input} seconde(s)')
print(f'{result} en décimal correspond a {changement_base(result, 2)} en binaire et {changement_base(result, 16)} en hexadécimal')
