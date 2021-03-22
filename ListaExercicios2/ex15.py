'''Faça um programa que leia três valores que representam os lados de um triângulo. Primeiramente,
verifique se os lados podem formar um triângulo ( a soma de dois lados não pode ser menor que o
terceiro lado ). Caso possa formar um triângulo, indique se este é equilátero, isósceles ou escaleno.'''

x, y, z = float(input('Informe x: ')), float(
    input('Informe y: ')), float(input('Informe z: '))
if x+y > z and x+z > y and y+z > x:
    print('forma um triangulo')
elif x+y == z and x+z == y and y+z == x:
    print('triangulo eqüilátero')
elif x+y == z and x+z == y and y+z != x:
    print('triangulo Isóscelos')
elif x+y != z and x+z != y and y+z != x:
    print('triangulo Escaleno')