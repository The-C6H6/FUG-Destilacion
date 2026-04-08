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

    return {
        "alimentado_total": alimentado_total,
        "destilado_total": destilado_total,
        "waste_total": waste_total,
        "Zf": alimentado_individual,
        "Xd": destilado_individual,
        "Xw": waste_individual,
    }
    

        
    