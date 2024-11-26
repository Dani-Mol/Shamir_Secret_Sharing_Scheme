import random
from functools import reduce

# Define un módulo grande (primo mayor a los coeficientes)
MODULO = 2**256 - 189  # Un primo cercano a 2^256

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
    coeficientes = [k] + [random.randint(1, MODULO - 1) for _ in range(t - 1)]
    puntos = [(x, evaluar_polinomio(coeficientes, x)) for x in range(1, n + 1)]
    return puntos

def evaluar_polinomio(coeficientes, x):
    """
    Evalúa un polinomio en un punto x usando aritmética modular.
    Args:
        coeficientes (list): Coeficientes del polinomio.
        x (int): Punto a evaluar.
    Returns:
        int: Resultado de P(x).
    """
    return sum(c * pow(x, i, MODULO) for i, c in enumerate(coeficientes)) % MODULO

def reconstruir_secreto(puntos):
    """
    Reconstruye el término independiente de un polinomio usando interpolación de Lagrange.
    Args:
        puntos (list): Lista de pares (x, y).
    Returns:
        int: Secreto reconstruido.
    """
    def mod_inverse(a, p):
        """
        Calcula el inverso modular de a módulo p usando el algoritmo extendido de Euclides.
        """
        return pow(a, p - 2, p)  # Solo válido si p es primo

    def lagrange_interpolacion(x, puntos):
        secreto = 0
        for i, (xi, yi) in enumerate(puntos):
            numerador = reduce(lambda a, b: a * b % MODULO, [x - puntos[j][0] for j in range(len(puntos)) if j != i], 1)
            denominador = reduce(lambda a, b: a * b % MODULO, [xi - puntos[j][0] for j in range(len(puntos)) if j != i], 1)
            inverso_denominador = mod_inverse(denominador, MODULO)
            termino = yi * numerador * inverso_denominador % MODULO
            secreto = (secreto + termino) % MODULO
        return secreto

    return lagrange_interpolacion(0, puntos)


