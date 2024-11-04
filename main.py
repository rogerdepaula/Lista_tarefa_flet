import flet as ft

def main(page: ft.Page):
    tema = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary='blue',
            secondary='GREEN',
            background='WHITE',
        )
    )

    # Aplica o tema à página
    page.theme = tema
    page.bgcolor = tema.color_scheme.background  # Define a cor de fundo da página
    page.title = "App com Tema Verde e Branco" 

    button = ft.ElevatedButton(
        "Botão 01!",
        bgcolor=tema.color_scheme.primary,
        color=ft.colors.WHITE
    )

    button2 = ft.ElevatedButton(
        "Botão 02!",
        bgcolor=tema.color_scheme.primary,
        color="red"
    )

    button3 = ft.ElevatedButton(
        "Botão 03!",
        bgcolor=tema.color_scheme.primary,
        color=ft.colors.LIGHT_BLUE_ACCENT_400
    )

    # Evento do botão
    def on_button_click(e):
        page.add(ft.Text("Você clicou no botão!", color=tema.color_scheme.primary))

    button.on_click = on_button_click

    # Adiciona elementos à página
    page.add(button , button2 , button3)

# Inicia o app
ft.app(target=main)