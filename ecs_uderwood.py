from sympy import symbols, Eq, exp, nsolve


def underwood(volatilidad_relativa, zif, q, alfa_clcp):
    theta = symbols('theta')
    suma_ecuacion_theta = 0
    terminos = []

    for i in range(len(zif)):
        termino = volatilidad_relativa[i] * zif[i] / (volatilidad_relativa[i] - theta)
        suma_ecuacion_theta += termino
        terminos.append(
            f'{volatilidad_relativa[i]:.4f}*{zif[i]:.4f}/({volatilidad_relativa[i]:.4f} - θ)'
        )

    texto_ecuacion = "Ecuación para encontrar el valor de θ\n\n"
    texto_ecuacion += "Suma θ:\n\n"
    texto_ecuacion += " +\n".join(terminos)
    texto_ecuacion += f"\n={1-q:.4f}\n"

    valor_theta = encontrar_theta(suma_ecuacion_theta, q, alfa_clcp, theta)
    if isinstance(valor_theta, str):
        texto_ecuacion += f"{valor_theta}\n" 
    else:
        texto_ecuacion += f"\nθ = {float(valor_theta):.6f}"

    return texto_ecuacion, valor_theta
    



def encontrar_theta(suma_ecuaciones, q, alfa,  theta=symbols("theta")):
    expresion = suma_ecuaciones - (1 - q)

    eps = 1e-6
    a = 1 + eps
    b = alfa - eps

    try:
        solucion = nsolve(expresion, theta, (a, b), solver="bisect")
        return solucion if solucion else "No se encontró solución"
    except ValueError:
        return "No se encontró solución en el intervalo dado"
    except ZeroDivisionError:
        return "El intervalo toca una singularidad de la ecuación"

def R_min(theta, volatilidad_relativa, xid:list):
    suma_ecuacion_theta = 0
    terminos = []

    for i in range(len(xid)):
        termino = volatilidad_relativa[i] * xid[i] / (volatilidad_relativa[i] - theta)
        suma_ecuacion_theta += termino
        terminos.append(
            f'{volatilidad_relativa[i]:.4f}*{xid[i]:.4f}/({volatilidad_relativa[i]:.4f} - {theta:.4f})'
        )
    r=suma_ecuacion_theta-1
    texto_ecuacion = "Ecuación para encontrar el valor de Rmin\n\n"
    texto_ecuacion += "Suma Rmin:\n\n"
    texto_ecuacion += " +\n".join(terminos)
    texto_ecuacion += f"\n=1+Rmin\n\n"
    texto_ecuacion+=f"Rmin = {r}"


    return texto_ecuacion