def calcular_composiciones(controles_dinamicos):
    destilado_total = 0
    waste_total = 0
    alimentado_total = 0

    alimentado_individual = []
    destilado_individual = []
    waste_individual = []

    for captura in controles_dinamicos:
        a = float(captura["alimentacion"].value)
        d = float(captura["destilado"].value)
        w = float(captura["waste"].value)


    

        alimentado_individual.append(a)
        destilado_individual.append(d)
        waste_individual.append(w)

        alimentado_total += a
        destilado_total += d
        waste_total += w

    if alimentado_total != 0:
        alimentado_individual = [x / alimentado_total for x in alimentado_individual]

    if destilado_total != 0:
        destilado_individual = [x / destilado_total for x in destilado_individual]

    if waste_total != 0:
        waste_individual = [x / waste_total for x in waste_individual]

    D_cl=None
    W_cl=None
    indice_cl=None
    for i, composicion in enumerate(destilado_individual, start=-1):
            if i ==-1:
                continue
            if composicion <0.08:
                indice_cl=i
                D_cl=destilado_individual[i]
                W_cl=waste_individual[i]
                break

    W_cp=None
    D_cp=None
    indice_cp=None
    for i, composicion in enumerate(waste_individual, start=0):
            if composicion >0.08:
                indice_cp=i
                W_cp=waste_individual[i]
                D_cp=waste_individual[i]
                break

    

    return {
        "alimentado_total": alimentado_total,
        "destilado_total": destilado_total,
        "waste_total": waste_total,
        "Zf": alimentado_individual,
        "Xd": destilado_individual,
        "Xw": waste_individual,
        "indice_cl":indice_cl,
        "D_cl":D_cl,
        "W_cl":W_cl,
        "indice_cp":indice_cp,
        "W_cp":W_cp,
        "D_cp":D_cp,



        
    }
    






def texto_composiciones(composiciones: dict):
    alimentado_total = composiciones.get("alimentado_total", 0)
    destilado_total = composiciones.get("destilado_total", 0)
    waste_total = composiciones.get("waste_total", 0)

    zf = composiciones.get("Zf", [])
    xd = composiciones.get("Xd", [])
    xw = composiciones.get("Xw", [])

    def bloque(nombre_corriente, simbolo, total, fracciones):
        lineas = []
        lineas.append(f"{nombre_corriente.upper()}")
        lineas.append(f"Total = {total:.6f}")

        lineas.append("Procedimiento matemático:")
        for i, fraccion in enumerate(fracciones, start=1):
            flujo_individual = fraccion * total
            lineas.append(
                f"{simbolo}{i} = {flujo_individual:.6f} / {total:.6f} = {fraccion:.6f}"
            )

        lineas.append("")
        lineas.append("Valores finales:")
        for i, fraccion in enumerate(fracciones, start=1):
            lineas.append(f"{simbolo}{i} = {fraccion:.6f}")

        lineas.append("")
        lineas.append(
            f"Suma de fracciones = {' + '.join(f'{x:.6f}' for x in fracciones)} = {sum(fracciones):.6f}"
        )
        lineas.append("-" * 50)
        return "\n".join(lineas)

    texto = []
    
    texto.append("=" * 50)
    texto.append(f"Alimentado total = {alimentado_total:.6f}")
    texto.append(f"Destilado total = {destilado_total:.6f}")
    texto.append(f"Waste total = {waste_total:.6f}")
    texto.append("-" * 50)

    texto.append(bloque("Alimentación", "Zf", alimentado_total, zf))
    texto.append(bloque("Destilado", "Xd", destilado_total, xd))
    texto.append(bloque("Waste", "Xw", waste_total, xw))

    texto.append(f"Sustancia clave ligero:{composiciones.get('indice_cl',0)+1}")
    texto.append(f"Sustancia clave pesado:{composiciones.get('indice_cp',0)+1}")

    return "\n".join(texto)
        
    