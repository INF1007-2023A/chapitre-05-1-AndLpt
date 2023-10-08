#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >= 0:
        return number
    else:
        return -1 * number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for i in range(len(prefixes)):
        name = prefixes[i] + suffixe
        names.append(name)
    return names


def prime_integer_summation() -> int:
    liste_nombre = [2, 3, 5]
    num = 6
    # comment définir nombre premier # j'ai créé une fonction dans une fonction
    def prime_number(num):
        if num == 1:
            return False
        for i in range(2, int(num / 2) + 1):
            if (num % i == 0):
                return False
        else: 
            return True
    
    while (len(liste_nombre) < 100):
        if prime_number(num):
            liste_nombre.append(num)
        num += 1
    return sum(liste_nombre)


def factorial(number: int) -> int:
    if number == 1:
        return 1
    elif number == 2: 
        return 2
    else:
        return number * factorial(number - 1)
    


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)
    


def verify_ages(groups: List[List[int]]) -> List[bool]:
    final_list = []
    for i in range(len(groups)):
        if len(groups[i]) > 10 or len(groups[i]) <= 3:
            final_list.append(False)
            continue
        elif 25 in groups[i]:
            final_list.append(True)
        elif min(groups[i]) < 18 or (max(groups[i]) > 70 and 50 in groups[i]):
            final_list.append(False)
        else:
            final_list.append(True)
    return final_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    groups = [[15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
                  [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
                  [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]]
    print(verify_ages(groups))
