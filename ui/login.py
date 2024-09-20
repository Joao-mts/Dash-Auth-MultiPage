import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

def get_login_layout(image):
    return [html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src=image, style={"position": "absolute", "top": "10px", "left": "10px", "width": "150px"}),
            ],
        ),
        dmc.Center(
            dmc.Stack(
                [
                    dmc.Title("Login", ta="center"),
                    dmc.Space(h=7),
                    dmc.TextInput(
                        placeholder="Email",
                        w=400,
                        id='user-input',
                        leftSection=DashIconify(icon="mdi:account-outline"),
                        # type='email'
                    ),
                    dmc.PasswordInput(
                        placeholder="Password",
                        w=400,
                        id='password-input',
                        leftSection=DashIconify(icon="material-symbols:lock-outline")
                    ),
                    dmc.Button("Sign In", size="sm", style={"background-color": "#000"}, w=400, className='login-button', id='login-button'),
                    dmc.Anchor("Forgot password?", href="mailto:alamos@alamosgestao.com.br", style={"color": "black"}),
                    dmc.Space(h=2),
                    dmc.Divider(label="Dont have an account?", labelPosition="center", w=400),
                    dmc.Space(h=2),
                    dmc.Button("Sign Up", size="sm", color='gray', w=400, className='login-button', variant='outline', id = 'signin-button'),
                ],
                ta="left",
                # spacing="xs",
                justify='left'
            )
        ),
    ],
    style={
        'position': 'relative',
        'display': 'flex',
        'justify-content': 'center',
        'ta-items': 'center',
        'height': '80vh',
        'padding': '20px'
    }
)]
