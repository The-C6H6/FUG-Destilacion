import math
from sympy import symbols, Eq, exp, nsolve




SUSTANCIAS = {
    "Acetona": {"formula": "C3H6O", "A": 14.3145, "B": 2756.22, "C": 228.060, "t_min": -26, "t_max": 77},
    "Ácido acético": {"formula": "C2H4O2", "A": 15.0717, "B": 3580.80, "C": 224.650, "t_min": 24, "t_max": 142},
    "Acetonitrilo": {"formula": "C2H3N", "A": 14.8950, "B": 3413.10, "C": 250.523, "t_min": -27, "t_max": 81},
    "Benceno": {"formula": "C6H6", "A": 13.7819, "B": 2726.81, "C": 217.572, "t_min": 6, "t_max": 104},
    "iso-Butano": {"formula": "C4H10", "A": 13.8254, "B": 2181.79, "C": 248.870, "t_min": -83, "t_max": 7},
    "n-Butano": {"formula": "C4H10", "A": 13.6608, "B": 2154.70, "C": 238.789, "t_min": -73, "t_max": 19},
    "1-Butanol": {"formula": "C4H10O", "A": 15.3144, "B": 3212.43, "C": 182.739, "t_min": 37, "t_max": 138},
    "2-Butanol": {"formula": "C4H10O", "A": 15.1989, "B": 3026.03, "C": 186.500, "t_min": 25, "t_max": 120},
    "iso-Butanol": {"formula": "C4H10O", "A": 14.6047, "B": 2740.95, "C": 166.670, "t_min": 30, "t_max": 128},
    "tert-Butanol": {"formula": "C4H10O", "A": 14.8445, "B": 2658.29, "C": 177.650, "t_min": 10, "t_max": 101},
    "Tetracloruro de carbono": {"formula": "CCl4", "A": 14.0572, "B": 2914.23, "C": 232.148, "t_min": -14, "t_max": 101},
    "Clorobenceno": {"formula": "C6H5Cl", "A": 13.8635, "B": 3174.78, "C": 211.700, "t_min": 29, "t_max": 159},
    "1-Clorobutano": {"formula": "C4H9Cl", "A": 13.7965, "B": 2723.73, "C": 218.265, "t_min": -17, "t_max": 79},
    "Cloroformo": {"formula": "CHCl3", "A": 13.7324, "B": 2548.74, "C": 218.552, "t_min": -23, "t_max": 84},
    "Ciclohexano": {"formula": "C6H12", "A": 13.6568, "B": 2723.44, "C": 220.618, "t_min": 9, "t_max": 105},
    "Ciclopentano": {"formula": "C5H10", "A": 13.9727, "B": 2653.90, "C": 234.510, "t_min": -35, "t_max": 71},
    "n-Decano": {"formula": "C10H22", "A": 13.9748, "B": 3442.76, "C": 193.858, "t_min": 65, "t_max": 203},
    "Diclorometano": {"formula": "CH2Cl2", "A": 13.9891, "B": 2463.93, "C": 223.240, "t_min": -38, "t_max": 60},
    "Éter dietílico": {"formula": "C4H10O", "A": 14.0735, "B": 2511.29, "C": 231.200, "t_min": -43, "t_max": 55},
    "1,4 Dioxeno": {"formula": "C4H8O2", "A": 15.0967, "B": 3579.78, "C": 240.337, "t_min": 20, "t_max": 105},
    "n-Eicosano": {"formula": "C20H42", "A": 14.4575, "B": 4680.46, "C": 132.100, "t_min": 208, "t_max": 379},
    "Etanol": {"formula": "C2H6O", "A": 16.8958, "B": 3795.17, "C": 230.918, "t_min": 3, "t_max": 96},
    "Etilbenceno": {"formula": "C8H10", "A": 13.9726, "B": 3259.93, "C": 212.300, "t_min": 33, "t_max": 163},
    "Etilenglicol": {"formula": "C2H6O2", "A": 15.7567, "B": 4187.46, "C": 178.650, "t_min": 100, "t_max": 222},
    "n-Heptano": {"formula": "C7H16", "A": 13.8622, "B": 2910.26, "C": 216.432, "t_min": 4, "t_max": 123},
    "n-Hexano": {"formula": "C6H14", "A": 13.8193, "B": 2696.04, "C": 224.317, "t_min": -19, "t_max": 92},
    "Metanol": {"formula": "CH4O", "A": 16.5785, "B": 3638.27, "C": 239.500, "t_min": -11, "t_max": 83},
    "Acetato de metilo": {"formula": "C3H6O2", "A": 14.2456, "B": 2662.78, "C": 219.690, "t_min": -23, "t_max": 78},
    "Metil etil cetona": {"formula": "C4H8O", "A": 14.1334, "B": 2838.24, "C": 218.690, "t_min": -8, "t_max": 103},
    "Nitrometano": {"formula": "CH3NO2", "A": 14.7513, "B": 3331.70, "C": 227.600, "t_min": 56, "t_max": 146},
    "n-Nonano": {"formula": "C9H20", "A": 13.9854, "B": 3311.19, "C": 202.694, "t_min": 46, "t_max": 178},
    "iso-Octano": {"formula": "C8H18", "A": 13.6703, "B": 2896.31, "C": 220.767, "t_min": 2, "t_max": 125},
    "n-Octano": {"formula": "C8H18", "A": 13.9346, "B": 3123.13, "C": 209.635, "t_min": 26, "t_max": 152},
    "n-Pentano": {"formula": "C5H12", "A": 13.7667, "B": 2451.88, "C": 232.014, "t_min": -45, "t_max": 58},
    "Fenol": {"formula": "C6H6O", "A": 14.4387, "B": 3507.80, "C": 175.400, "t_min": 80, "t_max": 208},
    "1-Propanol": {"formula": "C3H8O", "A": 16.1154, "B": 3483.67, "C": 205.807, "t_min": 20, "t_max": 116},
    "2-Propanol": {"formula": "C3H8O", "A": 16.6796, "B": 3640.20, "C": 219.610, "t_min": 8, "t_max": 100},
    "Tolueno": {"formula": "C7H8", "A": 13.9320, "B": 3056.96, "C": 217.625, "t_min": 13, "t_max": 136},
    "Agua": {"formula": "H2O", "A": 16.3872, "B": 3885.70, "C": 230.170, "t_min": 0, "t_max": 200},
    "o-Xileno": {"formula": "C8H10", "A": 14.0415, "B": 3358.79, "C": 212.041, "t_min": 40, "t_max": 172},
    "m-Xileno": {"formula": "C8H10", "A": 14.1387, "B": 3381.81, "C": 216.120, "t_min": 35, "t_max": 166},
    "p-Xileno": {"formula": "C8H10", "A": 14.0579, "B": 3331.45, "C": 214.627, "t_min": 35, "t_max": 166},
}



def calcular_temperatura_burbuja(controles_dinamicos, presion_sistema):
    
    T = symbols("T")
    sustancias_seleccionadas = [i["dropdown"].value for i in controles_dinamicos]
    composiciones = [float(i["composicion"].value) for i in controles_dinamicos]       
    A=[SUSTANCIAS[sustancia]["A"] for sustancia in sustancias_seleccionadas]
    B=[SUSTANCIAS[sustancia]["B"] for sustancia in sustancias_seleccionadas]
    C=[SUSTANCIAS[sustancia]["C"] for sustancia in sustancias_seleccionadas]
    suma_presiones_burbuja = (1/presion_sistema)*sum([composiciones[i] * ecuacion_antoine(A[i], B[i], C[i], T) for i in range(len(sustancias_seleccionadas))])
    suma_presiones_rocio = presion_sistema*sum([composiciones[i] /ecuacion_antoine(A[i], B[i], C[i], T) for i in range(len(sustancias_seleccionadas))])
    temperatura_burbuja_valor = encontrar_temperaturas(suma_presiones_burbuja, T)
    temperatura_rocio_valor = encontrar_temperaturas(suma_presiones_rocio, T)

    resultado = ""
    constantes = ""
    presiones_suma_burbuja = ""
    presiones_suma_rocio = ""
    #Se mantiene igual
    for i in range(len(sustancias_seleccionadas)):
        constantes += f"Sustancia {i+1}: {sustancias_seleccionadas[i]}\n"
        constantes += f"x{i+1} = {composiciones[i]}\n"
        constantes += f"A{i+1} = {A[i]}\n"
        constantes += f"B{i+1} = {B[i]}\n"
        constantes += f"C{i+1} = {C[i]}\n\n"


        presiones_suma_burbuja += f"{composiciones[i]}*exp[{A[i]} - ({B[i]}/(T + {C[i]}))]/{presion_sistema}\n"
        presiones_suma_burbuja += " + " if i < len(sustancias_seleccionadas)-1 else ""

        presiones_suma_rocio += f"[{presion_sistema}*{composiciones[i]}]/exp[{A[i]} - ({B[i]}/(T + {C[i]}))]\n"
        presiones_suma_rocio += " + " if i < len(sustancias_seleccionadas)-1 else ""


    ecuacion_burbuja = "Ecuación final de burbuja:\n"
    ecuacion_burbuja += f"{presiones_suma_burbuja} = 1\n\n\n"
    ecuacion_rocio = "Ecuación final de rocio:\n"
    ecuacion_rocio += f"{presiones_suma_rocio} = 1"



    if isinstance(temperatura_burbuja_valor, str):
        resultado += f"{temperatura_burbuja_valor}\n"
    else:
        resultado += f"Temperatura de burbuja: {float(temperatura_burbuja_valor):.2f} °C\n"

    if isinstance(temperatura_rocio_valor, str):
        resultado += f"{temperatura_rocio_valor}\n" 
    else:
        resultado += f"Temperatura de rocío: {float(temperatura_rocio_valor):.2f} °C\n"

    return constantes,ecuacion_burbuja, ecuacion_rocio,resultado






def ecuacion_antoine(A, B, C, T=symbols("T")):
    """Ecuación de Antoine en forma simbólica o numérica."""
    return exp(A - (B / (T + C)))




def encontrar_temperaturas(suma_presiones, T=symbols("T")):
    ecuacion = Eq(suma_presiones, 1)
    solucion = nsolve(ecuacion, (-270, 1000), solver="bisect")
    return solucion if solucion else "Solución no encontrada"







