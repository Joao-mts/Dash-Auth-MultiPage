import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html
import dash

def get_initials(name: str) -> str:
    # Remove leading/trailing whitespace and split the name into words
    words = name.strip().split()
    
    # Check if there's at least one word
    if not words:
        return ""
    
    # Get the first initial
    first_initial = words[0][0].upper()
    
    # Get the last initial if there's more than one word
    last_initial = words[-1][0].upper() if len(words) > 1 else ""
    
    return first_initial + last_initial



def get_navbar(initials):
    return html.Nav(
        className="navbar",
        children=[
            html.Div(
                className="wrapper",
                style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"},
                children=[
                    html.Div(
                        className="logo",
                        children=[
                            html.A("Logo", href="#")
                        ]
                    ),
                    # Simulação de radio buttons com divs e classes
                    html.Div(id="menu-btn"),
                    html.Div(id="close-btn"),
                    html.Ul(
                        className="nav-links",
                        style={"display": "flex", "alignItems": "center"},
                        children=[
                            html.Label(
                                html.I(className="fas fa-times"),
                                htmlFor="close-btn",
                                className="btn close-btn"
                            ),
                            html.Li(html.A("Home", href="#")),
                            html.Li(html.A("About", href="#")),
                            html.Li(
                                children=[
                                    html.A("Dropdown Menu", href="#", className="desktop-item"),
                                    # html.Div(id="showDrop"),
                                    # html.Label("Dropdown Menu", htmlFor="showDrop", className="mobile-item"),
                                    html.Ul(
                                        className="drop-menu",
                                        children=[
                                            html.Li(html.A("Drop menu 1", href="#")),
                                            html.Li(html.A("Drop menu 2", href="#")),
                                            html.Li(html.A("Drop menu 3", href="#")),
                                            html.Li(html.A("Drop menu 4", href="#")),
                                        ]
                                    )
                                ]
                            ),
                            html.Li(
                                children=[
                                    html.A("Mega Menu", href="#", className="desktop-item"),
                                    # html.Div(id="showMega"),
                                    # html.Label("Mega Menu", htmlFor="showMega", className="mobile-item"),
                                    html.Div(
                                        className="mega-box",
                                        children=[
                                            html.Div(
                                                className="content",
                                                children=[
                                                    html.Div(
                                                        className="row",
                                                        children=[
                                                            html.Img(src="https://fadzrinmadu.github.io/hosted-assets/responsive-mega-menu-and-dropdown-menu-using-only-html-and-css/img.jpg", alt="")
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="row",
                                                        children=[
                                                            html.Header("Design Services"),
                                                            html.Ul(
                                                                className="mega-links",
                                                                children=[
                                                                    html.Li(html.A("Graphics", href="#")),
                                                                    html.Li(html.A("Vectors", href="#")),
                                                                    html.Li(html.A("Business cards", href="#")),
                                                                    html.Li(html.A("Custom logo", href="#")),
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="row",
                                                        children=[
                                                            html.Header("Email Services"),
                                                            html.Ul(
                                                                className="mega-links",
                                                                children=[
                                                                    html.Li(html.A("Personal Email", href="#")),
                                                                    html.Li(html.A("Business Email", href="#")),
                                                                    html.Li(html.A("Mobile Email", href="#")),
                                                                    html.Li(html.A("Web Marketing", href="#")),
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="row",
                                                        children=[
                                                            html.Header("Security Services"),
                                                            html.Ul(
                                                                className="mega-links",
                                                                children=[
                                                                    html.Li(html.A("Site Seal", href="#")),
                                                                    html.Li(html.A("VPS Hosting", href="#")),
                                                                    html.Li(html.A("Privacy Seal", href="#")),
                                                                    html.Li(html.A("Website design", href="#")),
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                            html.Li(html.A("Feedback", href="#")),
                        ]
                    ),
                   
                    # Adicionando o Avatar no canto direito
                    html.Div(
                        style={"display": "flex", "alignItems": "center"},
                        children=[
                            dmc.Menu(
                                [
                                    dmc.MenuTarget(dmc.Avatar(initials, radius="xl", className="hover-pointer", color='black', bg='white')),
                                    dmc.MenuDropdown(
                                        [   
                                            dmc.MenuItem(
                                                "Perfil", leftSection=DashIconify(icon="mdi:account-outline")
                                            ),
                                            dmc.MenuItem(
                                                "Configurações", leftSection=DashIconify(icon="material-symbols:settings-outline")
                                            ),
                                            dmc.MenuDivider(),
                                            dmc.MenuItem(
                                                "Sair",
                                                leftSection=DashIconify(icon="material-symbols:logout"),
                                                color="red",
                                                id='logout-button',
                                            ),
                                        ]
                                    ),
                                ],
                                trigger="hover",
                                
                            )
                        ]
                    ),
                    html.Label(html.I(className="fas fa-bars"), htmlFor="menu-btn", className="btn menu-btn"),
                ]
            )
        ]
    )




def get_main_layout(image, info):
    initials = get_initials(info.get('name'))
    email = info.get('email')
    return [html.Div([
    get_navbar(initials),
    html.Div(children=dash.page_container)
], style={'margin': '0', 'padding': '0'})]


