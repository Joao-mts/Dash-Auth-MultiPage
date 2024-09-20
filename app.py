from auth.deps import login_for_access_token, validate_token, create_user
from dash import html, dcc, Input, Output, State, callback
from ui.conta_criada import get_conta_criada_layout
from ui.main_layout import get_main_layout
from dash.exceptions import PreventUpdate
from ui.signup import get_signup_layout
from ui.login import get_login_layout
import base64
import dash
import re
import dash_mantine_components as dmc

from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, title='Dash Auth', update_title=None)

server = app.server

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

Logo = encode_image('assets/image.png')

app.layout = dmc.MantineProvider(html.Div(children=[
    dcc.Store(id="auth_token", storage_type='session'),
        dcc.Loading(
        custom_spinner=html.Div(className="custom-spinner"),
        id="loading-spinner",
        children=html.Div(
            id='main-div',
            ),
        overlay_style={"visibility":"visible", "filter": "blur(2px)"},
        type="default",
        fullscreen=False,
        delay_show=1000,
    ),
        ])
)
@callback(
    [Output("main-div", "children")],
    [Input('auth_token', 'data')],
)
def auth_check(auth:dict):
    if not auth:
        return get_login_layout(Logo)
    
    token = auth.get('access_token')

    user_info = validate_token(token)

    if not user_info:
        return get_login_layout(Logo)
    
    return get_main_layout(Logo, user_info)


@callback(
    [Output("main-div", "children", allow_duplicate=True)],
    [Input('signin-button', 'n_clicks')],
    prevent_initial_call='initial_duplicate'
)
def redirect_to_signin(n_clicks):
    if not n_clicks:
        raise PreventUpdate
    return get_signup_layout(Logo)

@callback(
    Output("auth_token", "data", allow_duplicate=True),
    Input('logout-button', 'n_clicks'),
    prevent_initial_call='initial_duplicate'
)
def logout(clicks):
    if not clicks:
        raise PreventUpdate
    return {"acces_token":None}

@callback(
    [Output("auth_token", "data"), Output('user-input', 'error'), Output('password-input', 'error')],
    [Input('login-button', 'n_clicks')],
    [State('user-input', 'value'), State('password-input', 'value')],
    prevent_initial_call=True,
    running=[(Output("login-button", "loading"), True, False)]
)
def login(n_clicks, usuario, senha):
    if not n_clicks:
        raise PreventUpdate
    if not usuario or not senha:
        return dash.no_update, True, "Preencha com email e senha"
    
    auth_token:dict = login_for_access_token(usuario, senha)
    
    if not auth_token:
        return dash.no_update, True, "Usuário ou senha incorretos"
    
    return auth_token, False, False
    
def is_valid_email(email):
    # Verificação simples de email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.callback(
    [Output("main-div", "children", allow_duplicate=True), Output('signin-name-input', 'error'),
    Output('signin-email-input', 'error'), Output('signin-password-input', 'error'), Output('signin-confirm-password-input', 'error')],
    Input('create-account-button', 'n_clicks'),
    [State('signin-name-input', 'value'),State('signin-email-input', 'value'),
     State('signin-password-input', 'value'),State('signin-confirm-password-input', 'value')],
    prevent_initial_call='initial_duplicate',
    running=[(Output("create-account-button", "loading"), True, False)]
)
def create_account(n_clicks, name, email, password, confirm_password):
    if n_clicks is None:
        raise PreventUpdate

    if not name or not email or not password or not confirm_password:
        return dash.no_update, not bool(name), not bool(email), not bool(password), not bool(confirm_password),

    if not is_valid_email(email):
        return dash.no_update, False, "Email inválido", False, False

    # Verificação de senha
    if len(password) < 8:
        return dash.no_update, False, False, True, "A senha deve ter ao menos 8 carateres"
    if password != confirm_password:
        return dash.no_update, False, False, True, "As senhas não correspondem"
    

    if not create_user(name=name, email=email, password=password):
        return dash.no_update, False,  "Algo deu errado, tente novamente.", False, False
    return get_login_layout(Logo), True, True, True, True

if __name__ == '__main__':
    app.run_server(debug=True)
