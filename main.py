import sys
sys.path.append(r'C:\Users\User\OneDrive\Documentos\geometria\geometriaa\geometria')

import geometria.circulo  as cir
import geometria.rectangulo as re
import geometria.triangulo as tri

radio = 5
print(f"Área del círculo con radio {radio}: {cir.area_circulo(radio)}")

base_rectangulo = 10
altura_rectangulo = 4
print(f"Área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo}: {re.area_rectangulo(base_rectangulo, altura_rectangulo)}")

base_triangulo = 6
altura_triangulo = 8
print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo}: {tri.area_triangulo(base_triangulo, altura_triangulo)}")
