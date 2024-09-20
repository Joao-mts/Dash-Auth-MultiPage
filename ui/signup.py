from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

def get_signup_layout(imagem):
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
                    dmc.Title("Create an account", ta="center"),
                    dmc.Text("Fill with your personal information.", ta="center", size="sm"),
                    dmc.Space(h=20),
                    dmc.TextInput(
                        placeholder="Full name",
                        w=400,
                        id='signin-name-input',
                        leftSection=DashIconify(icon="mdi:identification-card-outline")
                    ),
                    dmc.TextInput(
                        placeholder="Email",
                        w=400,
                        id='signin-email-input',
                        leftSection=DashIconify(icon="mdi:email-outline")
                    ),
                    dmc.PasswordInput(
                        placeholder="Password",
                        w=400,
                        id='signin-password-input',
                        leftSection=DashIconify(icon="material-symbols:lock-outline")
                    ),
                    dmc.PasswordInput(
                        placeholder="Confirm password",
                        w=400,
                        id='signin-confirm-password-input',
                        leftSection=DashIconify(icon="material-symbols:lock-outline")
                    ),
                    dmc.Button("Create", size="sm", style={"background-color": "#000"}, w=400, className='login-button', id='create-account-button'),
                ],
                align="center",
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
