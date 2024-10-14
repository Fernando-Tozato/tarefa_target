"""
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
além de informar a quantidade de vezes em que ela ocorre.
"""

# O que eu faria no trabalho
def find_a_2(text: str) -> int:
    return text.count('a') + text.count('A')

# O que eu faria na faculdade
def find_a(text: str) -> int:
    text = text.lower()
    if not 'a' in text:
        return 0
    count = 0
    for char in text:
        if char == 'a':
            count += 1
    return count

def main():
    text = input('Digite um texto: ')
    print(f'A letra \'a\' aparece {find_a(text)} vezes no texto.')

if __name__ == '__main__':
    main()