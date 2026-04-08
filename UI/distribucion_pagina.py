import flet as ft
def distribucion_pagina(elementos_UI):
    return ft.Column(
            controls=[
                ft.Text(
                    "Cálculo Método Fenske-Underwood-Gilliland (FUG)",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    "Selecciona cuántas sustancias quieres calcular y la presión del sistema."
                ),
                ft.Divider(),
                elementos_UI["cantidad_dropdown"],
                elementos_UI["presion_sistema_tf"],
                elementos_UI["area_entradas"],
                
                ft.Row([elementos_UI["btn_calcular"], elementos_UI["btn_limpiar"]]),
                ft.Divider(),
                ft.Text(
                    "Resultados y procedimiento:",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                elementos_UI["area_resultados"],
            ],
            spacing=15,
        )