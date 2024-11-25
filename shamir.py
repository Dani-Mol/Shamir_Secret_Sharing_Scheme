import random
from functools import reduce

def generar_polinomio(k, n, t):
    """
    Genera un polinomio de grado t-1 con el término independiente k.
    Args:
        k (int): Término independiente (secreto).
        n (int): Número de evaluaciones.
        t (int): Grado del polinomio + 1 (mínimo para reconstrucción).
    Returns:
        list: Lista de n pares (x, P(x)).
    """
    coeficientes = [k] + [random.randint(1, 2**256 - 1) for _ in range(t - 1)]
    puntos = [(x, evaluar_polinomio(coeficientes, x)) for x in range(1, n + 1)]
    return puntos

def evaluar_polinomio(coeficientes, x):
    """
    Evalúa un polinomio en un punto x.
    Args:
        coeficientes (list): Coeficientes del polinomio.
        x (int): Punto a evaluar.
    Returns:
        int: Resultado de P(x).
    """
    return sum(c * (x**i) for i, c in enumerate(coeficientes))

def reconstruir_secreto(puntos):
    """
    Reconstruye el término independiente de un polinomio usando interpolación de Lagrange.
    Args:
        puntos (list): Lista de pares (x, y).
    Returns:
        int: Secreto reconstruido.
    """
    def lagrange_interpolacion(i, x):
        numerador = reduce(lambda a, b: a * b, [x - puntos[j][0] for j in range(len(puntos)) if j != i], 1)
        denominador = reduce(lambda a, b: a * b, [puntos[i][0] - puntos[j][0] for j in range(len(puntos)) if j != i], 1)
        return numerador / denominador

    secreto = sum(y * lagrange_interpolacion(i, 0) for i, (x, y) in enumerate(puntos))
    return round(secreto)
