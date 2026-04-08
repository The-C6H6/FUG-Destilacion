import flet as ft



def cuadro_texto(titulo, contenido):
    return ft.Card(
        content=ft.Container(
                    width=900,
                    padding=15,
                    content=ft.Column(
                            controls=[
                                ft.Text(f"{titulo}:",size=18,weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                                ft.Text(contenido, selectable=True, size=15, font_family="Courier New", weight=ft.FontWeight.BOLD),
                            ],
                            spacing=10,
                        )
                    )
                )