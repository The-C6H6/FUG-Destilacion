import flet as ft

def main(page: ft.Page):
    page.title = "Tabla editable tipo Excel"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    filas = 5
    columnas = 6

    headers = [f"Col {i+1}" for i in range(columnas)]

    # matriz inicial
    data = [[f"" for _ in range(columnas)] for _ in range(filas)]

    # aquí guardamos referencias a cada celda
    celdas = []

    def crear_celda(valor=""):
        tf = ft.TextField(
            value=valor,
            width=120,
            height=42,
            text_size=14,
            content_padding=10,
            border=ft.InputBorder.NONE,
        )
        return ft.Container(
            content=tf,
            border=ft.border.all(1, ft.Colors.GREY_400),
            padding=0,
        ), tf

    def obtener_datos(e=None):
        matriz = []
        for fila in celdas:
            matriz.append([celda.value for celda in fila])

        resultado.value = str(matriz)
        page.update()

    # encabezados
    fila_headers = ft.Row(
        spacing=0,
        controls=[
            ft.Container(
                content=ft.Text(h, weight=ft.FontWeight.BOLD),
                width=120,
                height=42,
                alignment=ft.Alignment.CENTER,
                bgcolor=ft.Colors.BLUE_100,
                border=ft.border.all(1, ft.Colors.GREY_400),
            )
            for h in headers
        ],
    )

    filas_ui = [fila_headers]

    # celdas editables
    for i in range(filas):
        fila_refs = []
        controles_fila = []
        for j in range(columnas):
            contenedor, tf = crear_celda(data[i][j])
            fila_refs.append(tf)
            controles_fila.append(contenedor)

        celdas.append(fila_refs)
        filas_ui.append(ft.Row(spacing=0, controls=controles_fila))

    tabla = ft.Row(
        scroll=ft.ScrollMode.AUTO,   # scroll horizontal
        controls=[
            ft.Column(
                spacing=0,
                controls=filas_ui,
            )
        ],
    )

    resultado = ft.Text(selectable=True)

    page.add(
        ft.Text("Tabla editable n x m", size=22, weight=ft.FontWeight.BOLD),
        tabla,
        ft.Row(
            controls=[
                ft.ElevatedButton("Leer datos", on_click=obtener_datos),
            ]
        ),
        resultado
    )

ft.run(main)