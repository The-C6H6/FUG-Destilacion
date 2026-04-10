import flet as ft
from antoine import SUSTANCIAS  


##Dropdown inicial para cantidad de sustancias a calcular
def estilo_cantidad_sustancias(crear_entradas):
    return ft.Dropdown(
            label="¿Cuántas sustancias quieres calcular?",
            width=300,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_select=crear_entradas,
        )



##Dropdown dinámico 
def opciones_sustancias():
    return [
        ft.dropdown.Option(
            key=nombre,
            text=f"{nombre} ({datos['formula']})"
        )
        for nombre, datos in SUSTANCIAS.items()
    ]

def crear_bloque_captura(indice, controles_dinamicos: list = []):
        """Genera Dropdown para seleccionar sustancia y temperatura, 
        agregando estos controles a la lista de controles dinámicos."""

        dd_sustancia = ft.Dropdown(
            label=f"Sustancia {indice}",
            width=420,
            options=opciones_sustancias(),
        )

        tf_alimentacion = ft.TextField(
            label=f" Alimentación {indice}",
            width=220,
            hint_text="Ejemplo: 100Kmol/h",
        )

        tf_destilado = ft.TextField(
            label=f" Destilado {indice}",
            width=220,
            hint_text="Ejemplo: 100Kmol/h",
        )

        tf_waste = ft.TextField(
            label=f" Waste {indice}",
            width=220,
            hint_text="Ejemplo: 100Kmol/h",
        )

        controles_dinamicos.append(
            {
                "dropdown": dd_sustancia,
                "alimentacion":tf_alimentacion,
                "destilado": tf_destilado,
                "waste": tf_waste

            }
        )

        

        return ft.Card(
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            f"Captura {indice}",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Row(
                            controls=[dd_sustancia, tf_alimentacion, tf_destilado, tf_waste],
                            wrap=True,
                        ),
                    ],
                    spacing=10,
                ),
            )
        )


