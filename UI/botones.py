import flet as ft
  
def estilo_boton_calcular(calcular_todo):
    return ft.Button(
        "Calcular",
        on_click=calcular_todo
    )

def estilo_boton_limpiar(limpiar_todo): 
    return ft.OutlinedButton(
        "Limpiar todo",
        on_click=limpiar_todo,
        
    )   
