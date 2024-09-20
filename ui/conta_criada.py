import dash_mantine_components as dmc
from dash import html

def get_conta_criada_layout(imagem):
    return [html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src=imagem, style={"position": "absolute", "top": "10px", "left": "10px", "width": "150px"}),
            ],
        ),
        dmc.Center(
            dmc.Stack(
                [
                        dmc.Title("Conta criada com sucesso!", align="center"),
                        dmc.Space(h=20),

                        dmc.Text(
                            "Sua conta foi criada e está aguardando aprovação.",
                            align="center",
                            size="md"
                        ),
                        dmc.Text(
                            "Por favor, aguarde enquanto processamos sua solicitação.",
                            align="center",
                            size="md"
                        ),
                        dmc.Text(
                            [
                                "Qualquer dúvida, entre em contato: ",
                                html.A("alamos@alamosgestao.com.br", href="mailto:alamos@alamosgestao.com.br", style={"color": "blue", "text-decoration": "underline"})
                            ],
                            align="center",
                            size="md"
                        ),
                ],
                align="center",
                spacing="xs",
            )
        ),
    ],
    style={
        'position': 'relative',
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'height': '80vh',
        'padding': '20px'
    }
)]
