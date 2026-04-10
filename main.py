import math
import flet as ft
from composiciones import calcular_composiciones    
from UI import (
    crear_bloque_captura, 
    estilo_cantidad_sustancias, 
    estilo_boton_calcular, 
    estilo_boton_limpiar, 
    estilo_boton_underwood,
    limpiar_todo, 
    calcular_todo, 
    crear_entradas, 
    distribucion_pagina,
    underwood_evento

)


def main(page: ft.Page):
    page.title = "Calculadora de presión de vapor"
    page.window_width = 950
    page.window_height = 850
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    controles_dinamicos = []    
    almacen_variables={}

    elementos_UI={
        "area_entradas": ft.Column(spacing=12),
        "area_resultados": ft.Column(spacing=12),
        "cantidad_dropdown": estilo_cantidad_sustancias(lambda e: crear_entradas(e, controles_dinamicos, elementos_UI, crear_bloque_captura)),
        "presion_sistema_tf": ft.TextField(label="Presión del sistema (kPa)", width=300, hint_text="Ejemplo: 101.325"),
        "btn_calcular": estilo_boton_calcular(lambda e: calcular_todo(e, elementos_UI, controles_dinamicos, calcular_composiciones, almacen_variables)),
        "btn_limpiar": estilo_boton_limpiar(lambda e: limpiar_todo(e, elementos_UI, controles_dinamicos)),
        "q_textfield" : ft.TextField(label="q= 1-fv", width=300, hint_text="Ejemplo: 0.5", border_color="#00efee"),
        "r_min_textfield" : ft.TextField(label="R min", width=300, hint_text="Ejemplo: 2.0", border_color="#00efee"),
        "boton_uderwood":estilo_boton_underwood(lambda e: underwood_evento(e,almacen_variables, elementos_UI))
    }


    page.add(
        distribucion_pagina(elementos_UI)
    )


ft.run(main)