# main.py
import sys
sys.path.append(r'C:\Users\User\OneDrive\Documentos\Actividades\Operaciones')
import operaciones.matematica as mate
import operaciones.geometria as geo

print("Suma:", mate.suma(10,5))
print("Resta:", mate.resta(10, 5))
print("Multiplicación:", mate.multiplicacion(10, 5))
try:
    print("División:", mate.division(10, 5))
    print("División por cero:", mate.division(10, 0))  
except ValueError as e:
    print("Error:", e)

print("Área del rectángulo:", geo.area_rectangulo(10, 5))
print("Perímetro del rectángulo:", geo.perimetro_rectangulo(10, 5))

