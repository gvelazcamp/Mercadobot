import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# =========================
# FULL WIDTH STREAMLIT
# =========================
st.markdown(
    """
    <style>
    .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    section.main > div {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    section.main {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Ocultar completamente header y toolbar de Streamlit */
    header[data-testid="stHeader"] { 
        display: none !important; 
        visibility: hidden !important; 
        height: 0px !important;
        min-height: 0px !important;
    }
    .stAppHeader {
        display: none !important;
    }
    #MainMenu { 
        visibility: hidden !important;
        display: none !important; 
    }
    footer { 
        visibility: hidden !important; 
        height: 0px !important; 
    }
    [data-testid="stToolbar"] { 
        visibility: hidden !important; 
        height: 0px !important;
        display: none !important; 
    }
    .stToolbar {
        display: none !important;
    }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stStatusWidget"] { display: none !important; }
    
    /* Eliminar scrollbars de Streamlit */
    iframe {
        display: block;
        overflow: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# VISTA
# =========================
try:
    vista = st.query_params.get("vista", "home")
except Exception:
    qp = st.experimental_get_query_params()
    vista = qp.get("vista", ["home"])[0]

BASE_URL = "https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/"

# =========================
# HTML + CSS (BASE)
# =========================
CSS_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    background: #f6f7fb;
}

body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* =========================
   WRAPPER
========================= */
.wrapper {
    width: 100%;
    max-width: 100vw;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
}

/* =========================
   HEADER
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    width: 100%;
}

.logo {
    font-size: 22px;
    font-weight: 800;
    text-decoration: none;
    color: #000;
}
.logo span { color: #f4b400; }

.nav {
    display: flex;
    gap: 28px;
    font-weight: 500;
    color: #555;
    align-items: center;
}

.nav a {
    text-decoration: none;
    color: #555;
    cursor: pointer;
}

.btn-login {
    background: #f4b400;
    padding: 8px 16px;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    padding: 40px 40px;
    align-items: center;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
}

.hero h1 {
    font-size: 38px;
    line-height: 1.15;
    margin: 0 0 18px 0;
}

.hero p {
    font-size: 16px;
    color: #555;
    margin: 0 0 22px 0;
}

.hero img {
    max-width: 100%;
    width: 100%;
    height: auto;
    display: block;
}

.hero-actions {
    display: flex;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
}

.btn-primary {
    background: #f4b400;
    color: #000;
    padding: 12px 22px;
    border-radius: 14px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    border: none;
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #555;
    cursor: pointer;
    text-decoration: none;
}

/* =========================
   CATEGORÍAS
========================= */
.cats-block {
    text-align: center;
    padding: 20px 40px;
    width: 100%;
}

.cats {
    display: inline-flex;
    gap: 12px;
    background: #fff;
    padding: 10px 14px;
    border-radius: 999px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.cat {
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 600;
    background: #f6f7fb;
}

/* =========================
   SECTION
========================= */
.section {
    padding: 20px 40px 40px 40px;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
}

.section h2 {
    text-align: center;
    font-size: 32px;
    margin: 0 0 10px 0;
}

.subtitle {
    text-align: center;
    font-size: 14px;
    color: #777;
    margin: 0 0 30px 0;
}

/* =========================
   CARDS
========================= */
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 22px;
    width: 100%;
}

.card {
    background: #fff;
    border-radius: 22px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

.card img {
    width: 100%;
    max-height: 130px;
    object-fit: contain;
}

.card h3 {
    margin: 16px 0 10px 0;
    font-size: 18px;
}

.card p {
    font-size: 13px;
    color: #666;
    min-height: 70px;
    margin: 0 0 14px 0;
}

.card button {
    background: #f4b400;
    border: none;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 700;
    cursor: pointer;
}

/* =========================
   PRECIOS
========================= */
.pricing {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 22px;
    margin-top: 10px;
    width: 100%;
}

.plan {
    background: #fff;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    text-align: left;
    position: relative;
}

.plan.pro {
    border: 2px solid rgba(244, 180, 0, 0.9);
    transform: translateY(-6px);
}

.badge {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(244, 180, 0, 0.16);
    border: 1px solid rgba(244, 180, 0, 0.55);
    color: #7a5a00;
    font-weight: 800;
    font-size: 12px;
    padding: 6px 10px;
    border-radius: 999px;
}

.plan-name {
    font-size: 18px;
    font-weight: 800;
    margin: 0;
}

.plan-desc {
    margin-top: 6px;
    font-size: 13px;
    color: #777;
}

.plan-price {
    margin-top: 14px;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: -0.02em;
}

.plan-price span {
    font-size: 13px;
    font-weight: 700;
    color: #777;
    margin-left: 6px;
}

.plan-note {
    margin-top: 6px;
    font-size: 13px;
    color: #777;
}

.plan-list {
    list-style: none;
    padding: 0;
    margin: 16px 0 0 0;
}

.plan-list li {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    padding: 9px 0;
    border-bottom: 1px solid #f2f2f2;
    font-size: 13px;
    color: #555;
}

.plan-btn {
    margin-top: 16px;
    width: 100%;
    text-align: center;
}

.setup {
    margin-top: 22px;
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    border-radius: 22px;
    padding: 22px;
    text-align: left;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.setup h3 {
    margin: 0 0 10px 0;
    font-size: 18px;
}

.setup p {
    margin: 0;
    font-size: 13px;
    color: #666;
}

.mini-note {
    margin-top: 14px;
    font-size: 12px;
    color: #888;
    text-align: center;
}

/* =========================
   CTA FINAL
========================= */
.cta {
    margin: 40px 40px 20px;
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    border-radius: 40px;
    padding: 40px;
    text-align: center;
    width: calc(100% - 80px);
    max-width: 1320px;
    margin-left: auto;
    margin-right: auto;
}

.cta h2 {
    font-size: 32px;
    margin: 0 0 10px 0;
}

.cta p {
    font-size: 14px;
    color: #666;
    margin: 0 0 20px 0;
}

.cta button {
    background: #f4b400;
    padding: 14px 28px;
    border-radius: 16px;
    font-weight: 800;
    border: none;
    cursor: pointer;
}

/* =========================
   FEATURES
========================= */
.features {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 24px;
    flex-wrap: wrap;
}

.feature {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #fff;
    padding: 10px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
}

/* =========================
   FOOTER
========================= */
.footer {
    border-top: 1px solid #eee;
    padding: 20px 40px;
    font-size: 13px;
    color: #888;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: auto;
}

/* =========================
   RESPONSIVE
========================= */
@media (max-width: 1100px) {
    .hero {
        grid-template-columns: 1fr;
        text-align: center;
    }
    .hero img {
        margin: 0 auto;
        max-width: 400px;
    }
    .hero-actions {
        justify-content: center;
    }
    .cards {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    }
}

@media (max-width: 640px) {
    .header { 
        padding: 16px;
        flex-wrap: wrap;
        gap: 10px;
    }
    .nav { 
        gap: 14px;
        font-size: 14px;
    }
    .hero { 
        padding: 20px 16px;
        gap: 20px;
    }
    .hero h1 {
        font-size: 28px;
    }
    .section { 
        padding: 20px 16px;
    }
    .cta { 
        margin: 30px 16px 16px;
        padding: 30px 20px;
        width: calc(100% - 32px);
    }
    .cards { 
        grid-template-columns: 1fr;
    }
    .footer { 
        padding: 16px;
        flex-direction: column;
        gap: 10px;
        text-align: center;
    }
    .pricing {
        grid-template-columns: 1fr;
    }
}
</style>
</head>
<body>
"""

# =========================
# HEADER (COMÚN)
# =========================
HEADER = """
<div class="wrapper">
    <!-- HEADER -->
    <div class="header">
        <a class="logo" href="?vista=home">MERCADO<span>BOT</span></a>
        <div class="nav">
            <a href="?vista=home">Inicio</a>
            <a href="?vista=asistentes">Asistentes</a>
            <a href="?vista=precios">Precios</a>
            <a href="?vista=home#soporte">Soporte</a>
        </div>
        <div class="btn-login">Iniciar sesión</div>
    </div>
"""

FOOTER = """
    <!-- FOOTER -->
    <div class="footer">
        <div>Política de privacidad · Términos y condiciones · Contacto</div>
        <div>Facebook · Twitter · LinkedIn</div>
    </div>
</div>
</body>
</html>
"""

# =========================
# HOME
# =========================
HTML_HOME = f"""{CSS_BASE}
{HEADER}

    <!-- HERO -->
    <div class="hero">
        <div>
            <h1>El marketplace<br>de asistentes IA</h1>
            <p>Automatizá tu negocio con asistentes virtuales inteligentes.</p>
            <div class="hero-actions">
                <a class="btn-primary" href="?vista=asistentes">Explorar asistentes</a>
                <a class="btn-secondary" href="#demo">▶ Ver demo en vivo</a>
            </div>
        </div>
        <img src="{BASE_URL}Asistente.png" alt="Asistente IA">
    </div>

    <!-- CATEGORÍAS -->
    <div class="cats-block">
        <div class="cats">
            <div class="cat">⚽ Fútbol</div>
            <div class="cat">👨‍🍳 Cocina</div>
            <div class="cat">🛒 Ecommerce</div>
            <div class="cat">💰 Finanzas</div>
        </div>
    </div>

    <!-- ASISTENTES (HOME) -->
    <div class="section">
        <h2>Asistentes IA listos para potenciar tu negocio</h2>
        <div class="subtitle">Explorá, elegí e instalá asistentes inteligentes según tus necesidades.</div>

        <div class="cards">
            <div class="card">
                <img src="{BASE_URL}Asistentefutbol.png" alt="Asistente de Fútbol">
                <h3>Asistente de Fútbol</h3>
                <p>Resultados, noticias y estadísticas del mundo del fútbol.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentecocina.png" alt="Asistente de Cocina">
                <h3>Asistente de Cocina</h3>
                <p>Recetas rápidas, consejos de cocina y conversiones de ingredientes.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Asistente de Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Respuestas automáticas sobre productos, pedidos y envíos.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Asistente de Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Información financiera, cotizaciones y análisis de inversiones.</p>
                <button>Ver asistente</button>
            </div>
        </div>
    </div>

    <!-- CTA FINAL -->
    <div class="cta">
        <h2>Integra en minutos</h2>
        <p>Instalá un asistente virtual IA en tu web fácilmente con un simple código.</p>
        <button>Probar gratis</button>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Totalmente configurable</div>
            <div class="feature">🔒 Seguro y escalable</div>
            <div class="feature">💬 Soporte incluido</div>
        </div>
    </div>

{FOOTER}
"""

# =========================
# ASISTENTES
# =========================
HTML_ASISTENTES = f"""{CSS_BASE}
{HEADER}

    <div class="section">
        <h2>Todos los asistentes IA</h2>
        <div class="subtitle">Estos son los asistentes disponibles en MercadoBot.</div>

        <div class="cards">
            <div class="card">
                <img src="{BASE_URL}Asistentefutbol.png" alt="Asistente de Fútbol">
                <h3>Asistente de Fútbol</h3>
                <p>Resultados, noticias y estadísticas del mundo del fútbol.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentecocina.png" alt="Asistente de Cocina">
                <h3>Asistente de Cocina</h3>
                <p>Recetas, consejos y conversiones de ingredientes.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Asistente de Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Soporte para productos, pedidos, envíos y postventa.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Asistente de Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Cotizaciones, reportes y análisis financiero básico.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentestock.png" alt="Asistente de Stock">
                <h3>Asistente de Stock</h3>
                <p>Control de inventario, consumos y alertas de reposición.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteinmobiliaria.png" alt="Asistente Inmobiliario">
                <h3>Asistente Inmobiliario</h3>
                <p>Consultas de propiedades, disponibilidad y agendado.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteagendas.png" alt="Asistente de Turnos">
                <h3>Asistente de Turnos / Agenda</h3>
                <p>Reserva de turnos, confirmaciones y recordatorios.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentedental.png" alt="Asistente Dental">
                <h3>Asistente Dental</h3>
                <p>Turnos, precios orientativos y preparación previa.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentedeviaje.png" alt="Asistente de Viaje">
                <h3>Asistente de Viaje</h3>
                <p>Itinerarios, recomendaciones y ayuda en reservas.</p>
                <button>Ver asistente</button>
            </div>
        </div>
    </div>

    <!-- CTA FINAL -->
    <div class="cta">
        <h2>Integra en minutos</h2>
        <p>Instalá un asistente virtual IA en tu web fácilmente con un simple código.</p>
        <button>Probar gratis</button>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Totalmente configurable</div>
            <div class="feature">🔒 Seguro y escalable</div>
            <div class="feature">💬 Soporte incluido</div>
        </div>
    </div>

{FOOTER}
"""

# =========================
# PRECIOS
# =========================
HTML_PRECIOS = f"""{CSS_BASE}
{HEADER}

    <div class="section">
        <h2>Precios</h2>
        <div class="subtitle">Elegí un plan según la cantidad de asistentes y el nivel de soporte que necesites.</div>

        <div class="pricing">
            <div class="plan">
                <div class="plan-name">Starter</div>
                <div class="plan-desc">Para probar 1 asistente en tu web</div>

                <div class="plan-price">US$ 49<span>/mes</span></div>
                <div class="plan-note">1 asistente · 1 sitio</div>

                <ul class="plan-list">
                    <li>✅ Widget embebible (iframe)</li>
                    <li>✅ Personalización básica (colores/logo)</li>
                    <li>✅ 1 fuente de datos / integración simple</li>
                    <li>✅ Soporte por email</li>
                </ul>

                <a class="btn-primary plan-btn" href="?vista=asistentes">Elegir plan</a>
            </div>

            <div class="plan pro">
                <div class="badge">Más popular</div>
                <div class="plan-name">Pro</div>
                <div class="plan-desc">Para negocios que quieren escalar</div>

                <div class="plan-price">US$ 99<span>/mes</span></div>
                <div class="plan-note">3 asistentes · 1 sitio</div>

                <ul class="plan-list">
                    <li>✅ Todo lo de Starter</li>
                    <li>✅ Hasta 3 asistentes (catálogo)</li>
                    <li>✅ Configuración avanzada de prompts</li>
                    <li>✅ Reporte mensual básico</li>
                    <li>✅ Soporte prioritario</li>
                </ul>

                <a class="btn-primary plan-btn" href="?vista=asistentes">Elegir plan</a>
            </div>

            <div class="plan">
                <div class="plan-name">Enterprise</div>
                <div class="plan-desc">Para empresas con necesidades a medida</div>

                <div class="plan-price">A medida<span></span></div>
                <div class="plan-note">Asistentes ilimitados · Multi-sitio</div>

                <ul class="plan-list">
                    <li>✅ Integraciones (CRM / ERP / APIs)</li>
                    <li>✅ Roles, permisos y auditoría</li>
                    <li>✅ SLA y soporte dedicado</li>
                    <li>✅ Seguridad/escala</li>
                    <li>✅ Onboarding y capacitación</li>
                </ul>

                <a class="btn-primary plan-btn" href="?vista=home#contacto">Hablar con ventas</a>
            </div>
        </div>

        <div class="setup">
            <h3>Instalación & Setup (pago único)</h3>
            <p>
                Incluye: configuración inicial, carga de tu branding, seteo del asistente, publicación y pruebas en tu web.
                Ideal para arrancar rápido sin tocar código.
            </p>
            <div style="margin-top:14px; font-weight:900; font-size:22px;">US$ 150</div>
            <div style="margin-top:6px; font-size:13px; color:#777;">Pago único · Puede variar según integraciones.</div>
        </div>

        <div class="mini-note">Los precios son orientativos. Si querés, definimos 3 planes finales con tus límites reales (asistentes, sitios, soporte, integraciones).</div>
    </div>

    <!-- CTA FINAL -->
    <div class="cta">
        <h2>Integra en minutos</h2>
        <p>Instalá un asistente virtual IA en tu web fácilmente con un simple código.</p>
        <button>Probar gratis</button>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Totalmente configurable</div>
            <div class="feature">🔒 Seguro y escalable</div>
            <div class="feature">💬 Soporte incluido</div>
        </div>
    </div>

{FOOTER}
"""

# =========================
# RENDER CON ALTURAS OPTIMIZADAS
# =========================
if vista == "asistentes":
    components.html(HTML_ASISTENTES, height=2000, scrolling=False)
elif vista == "precios":
    components.html(HTML_PRECIOS, height=1850, scrolling=False)
else:
    components.html(HTML_HOME, height=1700, scrolling=False)
