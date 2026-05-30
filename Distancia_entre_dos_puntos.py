#Problema: Hallar la distancia entre dos puntos en el plano cartesiano,
#con las cordenas indicadas por el usuario.

#Solucion: implementar un programa que calcule la distancia entre los dos puntos con
#la formula euclidiana: d = ((x2 - x1)^2 + (y2 - y1)^2)^0.5

#Pedir al usuario las coordenadas de los dos puntos
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"distance={d:.2f}")

