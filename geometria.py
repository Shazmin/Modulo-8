# geometria.py
import math
def area_circulo(radio):
    """
    Devuelve el área de un círculo dado su radio.
    """
    return math.pi * radio**2

def perimetro_circulo(radio):
    """
    Devuelve el perímetro de un círculo dado su radio.
    """
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    """
    Devuelve el área de un rectángulo dada su base y altura.
    """
    return base * altura

def perimetro_rectangulo(base, altura):
    """
    Devuelve el perímetro de un rectángulo dada su base y altura.
    """
    return 2 * (base + altura)
