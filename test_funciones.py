def test_calcular_promedio(lista):
    """Calcula el promedio de una lista de números."""
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    promedio = suma / len(lista)
    return promedio

def test_dividir(a, b):
    return a / b

def test_buscar_elemento(lista, x):
    """Busca un elemento en la lista y devuelve True/False."""
    for elemento in lista:
        if elemento == x:
            return True
    return False

def test_obtener_mayor(numeros):
    mayor = 0
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor

def test_es_par(numero):
    """Verifica si un numero es par."""
    if numero % 2 == 0:
        return True
    else:
        return False

def test_contar_vocales(texto):
    """Cuenta cuántas vocales hay en un texto."""
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador


lista = [10, 20, 30]
print(calcular_promedio(lista))
print(dividir(10, 2))
print(buscar_elemento(lista, 20))
print(obtener_mayor([-5, -3, -10]))
print(es_par(7))
print(contar_vocales("Hola mundo"))