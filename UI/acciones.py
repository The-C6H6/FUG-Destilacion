import flet as ft
from UI.cuadro_texto import cuadro_texto

def limpiar_todo(e, elementos_UI, controles_dinamicos):
        """Accion para boton limpiar; limpia dropdown, controles dinamicos, area de entradas y area de resultados"""
        elementos_UI["cantidad_dropdown"].value = None
        controles_dinamicos.clear()
        elementos_UI["area_entradas"].controls.clear()
        elementos_UI["area_resultados"].controls.clear()
        elementos_UI["cantidad_dropdown"].update()
        elementos_UI["area_entradas"].update()
        elementos_UI["area_resultados"].update()
        controles_dinamicos = []

def crear_entradas(e, controles_dinamicos, elementos_UI, crear_bloque_captura):
        """Accion para dropdown cantidad de sustancias; crea los controles 
            dinamicos necesarios segun la cantidad seleccionada,
            limpiando previamente cualquier captura o resultado existente."""
        controles_dinamicos.clear()
        elementos_UI["area_entradas"].controls.clear()
        elementos_UI["area_resultados"].controls.clear()

        if not elementos_UI["cantidad_dropdown"].value:
            elementos_UI["area_entradas"].update()
            elementos_UI["area_resultados"].update()
            return

        cantidad = int(elementos_UI["cantidad_dropdown"].value)

        for i in range(1, cantidad + 1):
            bloque = crear_bloque_captura(i, controles_dinamicos)
            elementos_UI["area_entradas"].controls.append(bloque)

        elementos_UI["area_entradas"].update()
        elementos_UI["area_resultados"].update()

def calcular_todo(e, elementos_UI, controles_dinamicos, calcular_composiciones):
        """Accion para boton calcular; Calcula la presión de vapor para cada captura, validando que se hayan seleccionado sustancias y temperaturas válidas. Muestra errores específicos para cada captura si hay problemas."""
        elementos_UI["area_resultados"].controls.clear()

        if not controles_dinamicos:
            elementos_UI["area_resultados"].controls.append(
                ft.Text("Primero selecciona cuántas sustancias deseas calcular.")
            )
        if not elementos_UI["presion_sistema_tf"].value:
            elementos_UI["area_resultados"].controls.append(
                ft.Text("Por favor ingresa la presión del sistema.")
            )

            elementos_UI["area_resultados"].update()
            return
        

        errores = validar_capturas(controles_dinamicos, elementos_UI["presion_sistema_tf"].value)
        if errores:
            for error in errores:
                elementos_UI["area_resultados"].controls.append(
                    ft.Text(error, color=ft.Colors.RED)
                )
            elementos_UI["area_resultados"].update()
            return
        

        composiciones= calcular_composiciones(controles_dinamicos)
        print(composiciones)
        #constantes,ecuacion_burbuja, ecuacion_rocio, resultado
        return


        elementos_UI["area_resultados"].controls.append(
                cuadro_texto("Constantes", constantes)
            )
        
        elementos_UI["area_resultados"].controls.append(
                cuadro_texto("Ecuación de Burbuja", ecuacion_burbuja)
            )
        
        elementos_UI["area_resultados"].controls.append(
                cuadro_texto("Ecuación de Rocío", ecuacion_rocio)
            )
        
        elementos_UI["area_resultados"].controls.append(
                cuadro_texto("Resultados", resultado)
            )


        elementos_UI["area_resultados"].update()




def validar_capturas(controles_dinamicos, presion_sistema=None):
    """
    Valida que cada captura tenga una sustancia seleccionada y valores numéricos
    válidos para alimentación, destilado y waste. También valida la presión del sistema.
    Devuelve una lista de errores encontrados.
    """
    errores = []

    # Validar presión una sola vez
    if presion_sistema is None or str(presion_sistema).strip() == "":
        errores.append("No se ha ingresado la presión del sistema.")
    else:
        try:
            presion_val = float(presion_sistema)
            if presion_val <= 0:
                errores.append("La presión del sistema debe ser un número positivo.")
        except ValueError:
            errores.append("La presión del sistema debe ser un número válido.")

    for i, captura in enumerate(controles_dinamicos, start=1):
        dropdown = captura["dropdown"]
        alimentacion = captura["alimentacion"]
        destilado = captura["destilado"]
        waste = captura["waste"]

        if not dropdown.value:
            errores.append(f"Captura {i}: No se ha seleccionado ninguna sustancia.")

        if not str(alimentacion.value).strip():
            errores.append(f"Captura {i}: No se ha ingresado la Alimentación.")
        else:
            try:
                alim_val = float(alimentacion.value)
                if alim_val <= 0:
                    errores.append(f"Captura {i}: La Alimentación debe ser mayor a 0.")
            except ValueError:
                errores.append(f"Captura {i}: La Alimentación debe ser un número válido.")

        if not str(destilado.value).strip():
            errores.append(f"Captura {i}: No se ha ingresado el Destilado.")
        else:
            try:
                desti_val = float(destilado.value)
                if desti_val <= 0:
                    errores.append(f"Captura {i}: El Destilado debe ser mayor a 0.")
            except ValueError:
                errores.append(f"Captura {i}: El Destilado debe ser un número válido.")

        if not str(waste.value).strip():
            errores.append(f"Captura {i}: No se ha ingresado el Waste.")
        else:
            try:
                waste_val = float(waste.value)
                if waste_val <= 0:
                    errores.append(f"Captura {i}: El Waste debe ser mayor a 0.")
            except ValueError:
                errores.append(f"Captura {i}: El Waste debe ser un número válido.")

    return errores