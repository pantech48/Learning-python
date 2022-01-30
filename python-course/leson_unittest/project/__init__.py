def calc_quadrantic_equation(a, b=0, c=0):
    """Возвращает корни квадратного уравнения"""
    d = b ** 2 - 4 * a * c

    if d < 0:
        return None

    if d == 0:
        return -b / (2 * a)

    return (-b + d ** .5) / (2 * a), (-b - d ** .5) / (2 * a)