'''Escreva um programa que 
peça ao usuário para digitar uma frase e, 
em seguida, 
conte quantos vogais (a, e, i, o, u) existem na frase utilizando um loop "for"'''

frase = input("Digite uma frase")
total_a, total_e, total_i, total_o, total_u = 0,0,0,0,0

for letra in frase:
    
    if letra == "a":
        total_a += 1
    elif letra == "e":
        total_e += 1
    elif letra == "i":
        total_i += 1
    elif letra == "o":
        total_o += 1
    elif letra == "u":
        total_u += 1

print("0 total de vogais é:", total_a)
print("0 total de vogais é:", total_e)
print("0 total de vogais é:", total_i)
print("0 total de vogais é:", total_o)
print("0 total de vogais é:", total_u)