import math

def triangulo(base, altura):
    area = (base * altura) / 2
    return area

def rectangulo(lado1, lado2):
    area = lado1 * lado2
    return area

def circulo(radio):
    area = math.pi * (radio ** 2)
    return area
