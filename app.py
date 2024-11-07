import streamlit as st
import base64
import random
import string
import time
from pathlib import Path

st.set_page_config(
    page_title="Soccer Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicialización de variables de estado
if 'registered_users' not in st.session_state:
    st.session_state.registered_users = {}
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'registration_mode' not in st.session_state:
    st.session_state.registration_mode = False
if 'recovery_mode' not in st.session_state:   
    st.session_state.recovery_mode = False

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(8))

def register_user(email, password):
    """Registra un nuevo usuario en el sistema"""
    st.session_state.registered_users[email] = password
    st.success(f"""
        ✅ Registro exitoso! 
        
        Tus credenciales de acceso son:
        Usuario: {email}
        Contraseña: {password}
        
        Por favor, guarda estas credenciales para iniciar sesión.
    """)
    return True

def authenticate_user(username, password):
    """Verifica las credenciales del usuario"""
    if username == "admin" and password == "admin":
        return True
    return (username in st.session_state.registered_users and 
            st.session_state.registered_users[username] == password)
    
def recover_password(email):
    """Recupera la contraseña de un usuario registrado"""
    if email in st.session_state.registered_users:
        password = st.session_state.registered_users[email]
        st.success(f"""
            ✅ Recuperación exitosa! 
            
            Tus credenciales son:
            Usuario: {email}
            Contraseña: {password}
            
            Por favor, guarda estas credenciales para futuros accesos.
        """)
        return True
    else:
        st.error("No se encontró ninguna cuenta asociada a este email")
        return False    

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.85)), url("data:image/jpg;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Configurar el fondo
set_background('Imagenes/datos-med-1024x601.jpg')

# Definir rutas de imágenes (rutas relativas)
ANALYTICS_ICON = "Imagenes/th (1).jpeg"
COMPARE_ICON = "Imagenes/6652080.png"
INSIGHTS_ICON = "Imagenes/shutterstock_488322949.jpg"
LEFT_SIDE_IMAGE = "Imagenes/aipowered-digital-soccer-ball-futuristic-technology-theme-virtual-field-artificial-intelligence-317209934.webp"
RIGHT_SIDE_IMAGE = "Imagenes/7u87cocj.png"

# Convertir imágenes a base64
analytics_icon_b64 = get_image_base64(ANALYTICS_ICON)
compare_icon_b64 = get_image_base64(COMPARE_ICON)
insights_icon_b64 = get_image_base64(INSIGHTS_ICON)
left_image_b64 = get_image_base64(LEFT_SIDE_IMAGE)
right_image_b64 = get_image_base64(RIGHT_SIDE_IMAGE)

# Estilos CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Orbitron:wght@400;500;600;700&display=swap');

    body {{
        font-family: 'JetBrains Mono', monospace;
        overflow-x: hidden;
    }}

    .side-image-container {{
        position: fixed;
        top: 50%;
        transform: translateY(-50%);
        height: 80vh;
        width: 300px;
        z-index: 0;
        opacity: 0.6;
        pointer-events: none;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }}

    .side-image-left {{
        left: -50px;
        background-image: url("data:image/webp;base64,{left_image_b64}");
        mask-image: linear-gradient(to right, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
        -webkit-mask-image: linear-gradient(to right, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
    }}

    .side-image-right {{
        right: -50px;
        background-image: url("data:image/png;base64,{right_image_b64}");
        mask-image: linear-gradient(to left, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
        -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
    }}

    .container {{
        position: relative;
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        padding: 2vh 2rem;
        z-index: 1;
    }}

    .big-font {{
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem !important; /* Tamaño para móvil */
        font-weight: 700;
        background: linear-gradient(135deg, #A8D9FD, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: 3px;
        animation: glow 2s ease-in-out infinite alternate;
        margin-bottom: 1rem;
    }}

    @media (min-width: 768px) {{
        .big-font {{
            font-size: 5rem !important;
        }}
    }}

    @keyframes glow {{
        from {{
            text-shadow: 0 0 20px rgba(168, 217, 253, 0.3),
                         0 0 30px rgba(168, 217, 253, 0.3),
                         0 0 40px rgba(168, 217, 253, 0.3);
        }}
        to {{
            text-shadow: 0 0 30px rgba(168, 217, 253, 0.5),
                         0 0 40px rgba(168, 217, 253, 0.5),
                         0 0 50px rgba(168, 217, 253, 0.5);
        }}
    }}

    .description {{
        text-align: center;
        color: #FFFFFF;
        font-size: 0.9rem;
        max-width: 800px;
        margin: 0 auto 1.5rem auto;
        line-height: 1.6;
        padding: 1rem;
        background: rgba(20, 30, 48, 0.3);
        border-radius: 5px;
        font-family: 'JetBrains Mono', monospace;
    }}

    @media (min-width: 768px) {{
        .description {{
            font-size: 1.1rem;
        }}
    }}

    .description::before {{
        content: '>';
        color: #A8D9FD;
        margin-right: 0.5rem;
    }}

    .features {{
        display: flex;
        flex-direction: column;  /* Por defecto en columna para móvil */
        gap: 1rem;
        margin: 0 auto 1rem auto;
        padding: 0 10px;
        width: 100%;
    }}

    @media (min-width: 768px) {{
        .features {{
            flex-direction: row;  /* En desktop se muestran en fila */
            gap: 2rem;
            padding: 0 20px;
            justify-content: center;
        }}
    }}

    .feature-item {{
        text-align: center;
        padding: 1rem;
        background: rgba(20, 30, 48, 0.6);
        border-radius: 8px;
        border: 1px solid rgba(168, 217, 253, 0.2);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
        margin: 0 auto;
        width: 100%;  /* Ancho completo en móvil */
    }}

    @media (min-width: 768px) {{
        .feature-item {{
            padding: 1.5rem;
            flex: 1;
            min-width: 0;
            width: auto;  /* Auto width en desktop */
        }}
    }}

    .feature-item:hover {{
        transform: translateY(-5px);
        border-color: rgba(168, 217, 253, 0.4);
        box-shadow: 0 5px 15px rgba(168, 217, 253, 0.1);
    }}

    .custom-icon {{
        width: 64px;  /* Tamaño más grande para móvil ya que hay más espacio vertical */
        height: 64px;
        object-fit: cover;
        border-radius: 50%;
        margin: 0 auto 1rem;
        display: block;
        border: 2px solid rgba(168, 217, 253, 0.3);
    }}

    .feature-title {{
        color: #A8D9FD;
        font-size: 1.1rem;  /* Tamaño más grande para móvil */
        margin-bottom: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 600;
    }}

    .feature-text {{
        color: #FFFFFF;
        font-size: 0.9rem;  /* Tamaño más grande para móvil */
        opacity: 0.8;
        line-height: 1.4;
    }}

    @media (min-width: 768px) {{
        .feature-text {{
            font-size: 0.9rem;
        }}
    }}

    div[data-testid="stForm"] {{
        background: rgba(20, 30, 48, 0.8);
        padding: 2rem;
        border-radius: 8px;
        border: 1px solid rgba(168, 217, 253, 0.2);
        position: relative;
        z-index: 2;
    }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(168, 217, 253, 0.3) !important;
        color: #FFFFFF !important;
        font-family: 'JetBrains Mono', monospace !important;
    }}

    .stButton button {{
        background: linear-gradient(135deg, #A8D9FD, #7BC5FF) !important;
        color: #000000 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: bold !important;
        border: none !important;
        transition: all 0.3s ease !important;
        padding: 0.75rem 1.5rem !important;
    }}

    .stButton button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(168, 217, 253, 0.2);
    }}

    .register-text {{
        text-align: center;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 1rem;
        font-size: 0.9rem;
    }}

    .form-header {{
        color: #A8D9FD;
        text-align: center;
        margin-bottom: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
    }}

    @media (max-width: 768px) {{
        .side-image-container {{
            display: none;
        }}
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>

    <div class="side-image-container side-image-left"></div>
    <div class="side-image-container side-image-right"></div>
""", unsafe_allow_html=True)

if not st.session_state.authenticated:
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # Cabecera - siempre visible
    st.markdown('<h1 class="big-font">Soccer Analytics</h1>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="description">
            Plataforma avanzada de análisis de datos futbolísticos con tecnología de última generación
        </div>
        
        <div class="features">
            <div class="feature-item">
                <img src="data:image/jpeg;base64,{analytics_icon_b64}" class="custom-icon" alt="Analytics">
                <div class="feature-title">> Analytics.Pro</div>
                <div class="feature-text">Análisis exhaustivo de métricas futbolísticas: rendimiento físico, 
                táctico y técnico. Seguimiento en tiempo real de posesión, pases, tiros, duelos y más.</div>
            </div>
            <div class="feature-item">
                <img src="data:image/png;base64,{compare_icon_b64}" class="custom-icon" alt="Compare">
                <div class="feature-title">> Smart.Compare</div>
                <div class="feature-text">Sistema avanzado de comparación entre jugadores y equipos. 
                Análisis detallado de estilos de juego, rendimiento histórico y proyecciones futuras.</div>
            </div>
            <div class="feature-item">
                <img src="data:image/jpeg;base64,{insights_icon_b64}" class="custom-icon" alt="Insights">
                <div class="feature-title">> Data.Insight</div>
                <div class="feature-text">Generación automática de reportes PDF personalizados. 
                Visualizaciones interactivas y dashboards dinámicos para análisis profundo.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Formularios de login/registro/recuperación
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        if not st.session_state.registration_mode and not st.session_state.recovery_mode:
            with st.form("login_form"):
                username = st.text_input("Usuario")
                password = st.text_input("Contraseña", type="password")
                col1, col2 = st.columns(2)
                with col1:
                    submit = st.form_submit_button("INICIAR SESIÓN")
                with col2:
                    register = st.form_submit_button("REGISTRARSE")
                
                forgot_password = st.form_submit_button("¿Olvidaste tu contraseña?")
                
                if submit:
                    if authenticate_user(username, password):
                        st.session_state.authenticated = True
                        st.rerun()
                    else:
                        st.error("Usuario o contraseña incorrectos")
                
                if register:
                    st.session_state.registration_mode = True
                    st.rerun()
                    
                if forgot_password:
                    st.session_state.recovery_mode = True
                    st.rerun()
                    
        elif st.session_state.recovery_mode:
            with st.form("recovery_form"):
                st.markdown('<div class="form-header"><h3>Recuperar Contraseña</h3></div>', unsafe_allow_html=True)
                st.markdown('<p class="form-text">Introduce tu email para recuperar tus credenciales</p>', unsafe_allow_html=True)
                email = st.text_input("Email")
                col1, col2 = st.columns(2)
                with col1:
                    submit = st.form_submit_button("RECUPERAR")
                with col2:
                    back = st.form_submit_button("VOLVER")
                
                if submit and email:
                    if '@' in email and '.' in email:
                        recover_password(email)
                    else:
                        st.error("Por favor, introduce un email válido")
                
                if back:
                    st.session_state.recovery_mode = False
                    st.rerun()
                    
        else:
            with st.form("register_form"):
                st.markdown('<div class="form-header"><h3>Registro de Usuario</h3></div>', unsafe_allow_html=True)
                st.markdown('<p class="form-text">Introduce tu email para recibir tus credenciales de acceso</p>', unsafe_allow_html=True)
                email = st.text_input("Email")
                col1, col2 = st.columns(2)
                with col1:
                    submit = st.form_submit_button("ENVIAR")
                with col2:
                    back = st.form_submit_button("VOLVER")
                
                if submit and email:
                    if '@' in email and '.' in email:
                        if email in st.session_state.registered_users:
                            st.error("Este email ya está registrado")
                        else:
                            password = generate_password()
                            if register_user(email, password):
                                time.sleep(10)
                                st.session_state.registration_mode = False
                                st.rerun()
                    else:
                        st.error("Por favor, introduce un email válido")
                
                if back:
                    st.session_state.registration_mode = False
                    st.rerun()

else:
    st.markdown("<h1 class='big-font'>¡Bienvenido a Soccer Analytics!</h1>", unsafe_allow_html=True)
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.clear()
        st.rerun()