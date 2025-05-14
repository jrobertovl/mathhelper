def add(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtract(a, b):
    """Retorna a subtração de b de a."""
    return a - b

def multiply(a, b):
    """Retorna o produto de a e b."""
    return a * b

def divide(a, b):
    """Retorna a divisão de a por b. Lança erro se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b