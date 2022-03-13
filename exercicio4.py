# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

pais1 = 80000
pais2 = 200000
ano = 0

while pais1 <= pais2:
    pais1 += pais1 * 0.03
    pais2 += pais2 * 0.015
    ano += 1

print(' O pais 1 ultrapassa ou iguala ao Pais 2 em %d' %ano)


