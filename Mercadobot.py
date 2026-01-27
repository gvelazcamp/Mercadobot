import streamlit as st

# =========================
# CONFIGURACIÓN NORMAL APP
# =========================
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# =========================
# FULL WIDTH STREAMLIT
# =========================
st.markdown(
    """
    <style>
    /* Eliminar TODO el padding y margin de Streamlit */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    section[data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }

    section.main > div {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Ocultar header, footer y toolbar */
    header[data-testid="stHeader"],
    .stAppHeader,
    footer,
    #MainMenu,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }

    /* Eliminar scroll horizontal */
    html, body, [data-testid="stAppViewContainer"], section.main {
        overflow-x: hidden !important;
        max-width: 100vw !important;
    }

    /* El iframe debe ocupar exactamente el espacio */
    iframe {
        width: 100% !important;
        border: none !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
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
# HTML COMPLETO
# =========================
HTML_BASE = """
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
}

html {
    overflow-x: hidden;
    width: 100%;
    height: 100%;
    background: #f6f7fb !important;
}

body {
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    background: #f6f7fb !important;
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden;
    min-height: 100vh;
}

.page-container {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
    background: #f6f7fb !important;
}

/* =========================
   HEADER
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 5%;
    width: 100%;
}

.logo {
    font-size: 22px;
    font-weight: 800;
    text-decoration: none;
    color: #000;
    white-space: nowrap;
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
    white-space: nowrap;
}

.nav a:hover {
    color: #f4b400;
}

.btn-login {
    background: #f4b400;
    padding: 8px 16px;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
}

/* =========================
   HERO IMPACT
========================= */
.hero-impact {
    background: linear-gradient(135deg, #2a2a2a 0%, #3d3d3d 100%);
    padding: 60px 5% 50px;
    text-align: center;
    color: #fff;
    position: relative;
    overflow: hidden;
}

.hero-impact::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 30% 50%, rgba(244, 180, 0, 0.08) 0%, transparent 50%);
    pointer-events: none;
}

.hero-impact-content {
    max-width: 900px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.hero-impact-title {
    font-size: 42px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 15px 0;
    letter-spacing: -0.02em;
}

.hero-impact-subtitle {
    display: block;
    font-size: 38px;
    background: linear-gradient(135deg, #f4b400 0%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 8px;
}

.hero-impact-text {
    font-size: 17px;
    color: rgba(255, 255, 255, 0.8);
    margin: 0 0 30px 0;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.hero-impact-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
}

.hero-impact-btn-primary {
    background: #f4b400;
    color: #000;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 6px 20px rgba(244, 180, 0, 0.3);
}

.hero-impact-btn-primary:hover {
    background: #ffd700;
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(244, 180, 0, 0.4);
}

.hero-impact-btn-secondary {
    background: transparent;
    color: #fff;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    border: 2px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease;
}

.hero-impact-btn-secondary:hover {
    border-color: #f4b400;
    color: #f4b400;
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .hero-impact {
        padding: 40px 5% 35px;
    }
    
    .hero-impact-title {
        font-size: 28px;
    }
    
    .hero-impact-subtitle {
        font-size: 26px;
    }
    
    .hero-impact-text {
        font-size: 15px;
    }
    
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary {
        font-size: 15px;
        padding: 12px 22px;
    }
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    padding: 40px 5%;
    align-items: center;
    width: 100%;
}

.hero-content {
    max-width: 600px;
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

.hero-image {
    text-align: center;
}

.hero-image img {
    max-width: 100%;
    width: auto;
    height: auto;
    max-height: 400px;
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
    white-space: nowrap;
}

.btn-primary:hover {
    background: #e5a500;
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #555;
    cursor: pointer;
    text-decoration: none;
    white-space: nowrap;
}

/* =========================
   NUEVO: HERO CHAT DEMO
   (solo agrega, no rompe)
========================= */
.hero-chat {
    background: #ffffff;
    border-radius: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    overflow: hidden;
    border: 1px solid rgba(0,0,0,0.06);
}

.chat-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 16px;
    background: linear-gradient(180deg, #ffffff, #f6f7fb);
    border-bottom: 1px solid rgba(0,0,0,0.06);
}

.chat-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 900;
    font-size: 13px;
    color: #111;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: #f4b400;
    box-shadow: 0 0 0 4px rgba(244,180,0,0.18);
}

.chat-pill {
    font-size: 12px;
    font-weight: 800;
    color: #7a5a00;
    background: rgba(244,180,0,0.18);
    border: 1px solid rgba(244,180,0,0.45);
    padding: 6px 10px;
    border-radius: 999px;
    white-space: nowrap;
}

.chat-body {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    min-height: 260px;
}

.bubble {
    max-width: 88%;
    padding: 10px 12px;
    border-radius: 14px;
    font-size: 13px;
    line-height: 1.35;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
}

.bubble.user {
    align-self: flex-end;
    background: #111;
    color: #fff;
    border-bottom-right-radius: 6px;
}

.bubble.bot {
    align-self: flex-start;
    background: #ffffff;
    color: #222;
    border: 1px solid rgba(0,0,0,0.06);
    border-bottom-left-radius: 6px;
}

.chat-meta {
    margin-top: 4px;
    font-size: 11px;
    color: #888;
}

.chat-input {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 14px 16px;
    border-top: 1px solid rgba(0,0,0,0.06);
    background: #fff;
}

.fake-input {
    flex: 1;
    background: #f6f7fb;
    border: 1px solid rgba(0,0,0,0.06);
    padding: 10px 12px;
    border-radius: 14px;
    font-size: 13px;
    color: #777;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.send-btn {
    background: #f4b400;
    border: none;
    padding: 10px 14px;
    border-radius: 14px;
    font-weight: 900;
    cursor: pointer;
}

.send-btn:hover {
    background: #e5a500;
}

.trust-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 14px;
}

.trust-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #fff;
    padding: 10px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
}

/* =========================
   NUEVO: CÓMO FUNCIONA (3 pasos)
========================= */
.steps {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
    max-width: 1200px;
    margin: 0 auto;
}

.step {
    background: #fff;
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    text-align: left;
}

.step-num {
    width: 34px;
    height: 34px;
    border-radius: 12px;
    background: rgba(244,180,0,0.20);
    border: 1px solid rgba(244,180,0,0.45);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    color: #7a5a00;
    margin-bottom: 12px;
}

.step h3 {
    font-size: 16px;
    margin-bottom: 8px;
}

.step p {
    font-size: 13px;
    color: #666;
    line-height: 1.45;
}

/* NUEVOS STEPS SIMPLES */
.steps-simple {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    max-width: 1200px;
    margin: 40px auto;
    flex-wrap: wrap;
}

.step-simple {
    background: #fff;
    border-radius: 24px;
    padding: 40px 30px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    flex: 1;
    min-width: 250px;
    max-width: 300px;
}

.step-icon {
    font-size: 64px;
    margin-bottom: 20px;
}

.step-simple h3 {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 12px;
    color: #000;
}

.step-simple p {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
}

.step-arrow {
    font-size: 32px;
    color: #f4b400;
    font-weight: 800;
}

@media (max-width: 768px) {
    .step-arrow {
        display: none;
    }
    
    .steps-simple {
        flex-direction: column;
        gap: 20px;
    }
}

/* =========================
   CATEGORÍAS
========================= */
.cats-block {
    text-align: center;
    padding: 20px 5%;
    width: 100%;
}

.cats {
    display: inline-flex;
    gap: 12px;
    background: #fff;
    padding: 10px 14px;
    border-radius: 999px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    flex-wrap: wrap;
}

.cat {
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 600;
    background: #f6f7fb;
    white-space: nowrap;
}

/* =========================
   SECTION
========================= */
.section {
    padding: 20px 5% 40px;
    width: 100%;
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
    max-width: 1400px;
    margin: 0 auto;
}

.card {
    background: #fff;
    border-radius: 22px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.card img {
    width: 100%;
    max-width: 200px;
    height: 130px;
    object-fit: contain;
    margin: 0 auto;
    display: block;
}

.card h3 {
    margin: 16px 0 10px 0;
    font-size: 18px;
}

.card p {
    font-size: 13px;
    color: #666;
    margin: 0 0 14px 0;
    flex-grow: 1;
}

.card button {
    background: #f4b400;
    border: none;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 700;
    cursor: pointer;
    margin-top: auto;
}

.card button:hover {
    background: #e5a500;
}

/* =========================
   PRECIOS
========================= */
.pricing {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    max-width: 1200px;
    margin: 20px auto 0 auto;
    align-items: stretch;
}

.plan {
    background: #ffffff;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
}

.plan.pro {
    border: 2px solid rgba(244,180,0,0.9);
}

.badge {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(244,180,0,0.15);
    border: 1px solid rgba(244,180,0,0.6);
    color: #7a5a00;
    font-weight: 800;
    font-size: 12px;
    padding: 6px 12px;
    border-radius: 999px;
}

.plan-name {
    font-size: 18px;
    font-weight: 800;
}

.plan-desc {
    font-size: 13px;
    color: #777;
    margin-top: 6px;
    min-height: 34px;
}

.plan-price {
    margin-top: 16px;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: -0.02em;
    min-height: 44px;
}

.plan-price span {
    font-size: 13px;
    font-weight: 700;
    color: #777;
    margin-left: 6px;
}

.plan-note {
    font-size: 13px;
    color: #777;
    margin-top: 6px;
    min-height: 18px;
}

.plan-list {
    list-style: none;
    padding: 0;
    margin: 18px 0 0 0;
    flex: 1;
}

.plan-list li {
    display: flex;
    gap: 10px;
    padding: 9px 0;
    font-size: 13px;
    color: #555;
    border-bottom: 1px solid #f2f2f2;
}

.plan-btn {
    margin-top: auto;
    width: 100%;
    text-align: center;
}

/* =========================
   TESTIMONIOS
========================= */
.testimonios {
    padding: 60px 5% 40px;
    background: #fff;
}

.testimonios h2 {
    font-size: 36px;
    text-align: center;
    margin: 0 0 50px 0;
}

.testimonios-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
}

.testimonio-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.testimonio-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}

.testimonio-quote {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    margin: 0 0 20px 0;
    font-style: italic;
}

.testimonio-author {
    display: flex;
    align-items: center;
    gap: 12px;
}

.testimonio-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400 0%, #ffd700 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    color: #000;
    font-size: 18px;
}

.testimonio-info h4 {
    margin: 0 0 4px 0;
    font-size: 15px;
    font-weight: 700;
    color: #000;
}

.testimonio-info p {
    margin: 0;
    font-size: 13px;
    color: #666;
}

.testimonio-stat {
    display: inline-block;
    background: rgba(244, 180, 0, 0.1);
    color: #c29400;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-top: 15px;
}

@media (max-width: 768px) {
    .testimonios-grid {
        grid-template-columns: 1fr;
    }
}

/* =========================
   CTA FINAL
========================= */
.cta {
    margin: 40px 5% 20px;
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    border-radius: 40px;
    padding: 40px;
    text-align: center;
    max-width: 1200px;
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

.cta-form {
    display: flex;
    gap: 12px;
    justify-content: center;
    align-items: center;
    max-width: 600px;
    margin: 0 auto 30px;
    flex-wrap: wrap;
}

.cta-form input {
    flex: 1;
    min-width: 200px;
    padding: 14px 18px;
    border-radius: 12px;
    border: 2px solid #e0e0e0;
    font-size: 15px;
    font-family: inherit;
}

.cta-form input:focus {
    outline: none;
    border-color: #f4b400;
}

.cta-form button {
    background: #f4b400;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 800;
    border: none;
    cursor: pointer;
    font-size: 15px;
    white-space: nowrap;
}

.cta-form button:hover {
    background: #e5a500;
}

.cta button {
    background: #f4b400;
    padding: 14px 28px;
    border-radius: 16px;
    font-weight: 800;
    border: none;
    cursor: pointer;
}

.cta button:hover {
    background: #e5a500;
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
   FAQ
========================= */
.faq-section {
    padding: 60px 5%;
    background: #fff;
    max-width: 1200px;
    margin: 0 auto;
}

.faq-section h2 {
    text-align: center;
    font-size: 36px;
    margin-bottom: 50px;
}

.faq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 25px;
}

.faq-item {
    background: #f6f7fb;
    padding: 25px;
    border-radius: 16px;
    border-left: 4px solid #f4b400;
}

.faq-question {
    font-size: 16px;
    font-weight: 700;
    color: #000;
    margin-bottom: 10px;
}

.faq-answer {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
}

/* =========================
   INTEGRACIONES
========================= */
.integrations-section {
    padding: 60px 5%;
    background: linear-gradient(180deg, #f6f7fb, #fff);
    text-align: center;
}

.integrations-section h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.integrations-subtitle {
    font-size: 16px;
    color: #666;
    margin-bottom: 40px;
}

.integrations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 30px;
    max-width: 900px;
    margin: 0 auto;
}

.integration-logo {
    background: #fff;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    transition: transform 0.3s ease;
}

.integration-logo:hover {
    transform: translateY(-5px);
}

.integration-logo p {
    margin-top: 10px;
    font-size: 14px;
    font-weight: 600;
    color: #333;
}

/* =========================
   FOOTER
========================= */
.footer {
    border-top: 1px solid #eee;
    padding: 20px 5%;
    font-size: 13px;
    color: #888;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 20px;
}

/* =========================
   RESPONSIVE
========================= */
@media (max-width: 1100px) {
    .hero {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .hero-content {
        max-width: 100%;
    }

    .hero-actions {
        justify-content: center;
    }

    .trust-row {
        justify-content: center;
    }

    .steps {
        grid-template-columns: 1fr;
    }

    .hero-chat {
        text-align: left;
    }
}

@media (max-width: 768px) {
    /* FORZAR FONDO GRIS EN MOBILE - TODO EXCEPTO HERO-IMPACT */
    html, body {
        background: #f6f7fb !important;
        background-color: #f6f7fb !important;
    }
    
    .page-container,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .hero,
    .hero-content,
    .section,
    .steps,
    .step,
    .cards,
    .card,
    .features,
    .feature,
    .testimonios,
    .testimonios-grid,
    .trust-row,
    .trust-pill,
    .cat,
    .chat-body,
    main,
    section {
        background: #f6f7fb !important;
        background-color: #f6f7fb !important;
    }
    
    /* FORZAR COLORES DE TEXTO OSCUROS PARA QUE SE LEAN */
    h1, h2, h3, h4, h5, h6, p, span, div, a {
        color: #333 !important;
    }
    
    .cta h2 {
        color: #000 !important;
        font-weight: 800 !important;
    }
    
    .cta p {
        color: #666 !important;
    }
    
    .footer,
    .footer a {
        color: #666 !important;
    }
    
    /* BOTONES CON MENOS BORDER-RADIUS Y COLOR AMARILLO EN MOBILE */
    button,
    .btn-primary,
    .btn-login,
    .hero-impact-btn-primary,
    .cta button,
    a button,
    .card button,
    input[type="submit"],
    input[type="button"],
    .stButton button,
    [class*="button"],
    [class*="Button"],
    [class*="btn"]:not(.btn-secondary) {
        border-radius: 8px !important;
        background: #f4b400 !important;
        background-color: #f4b400 !important;
        color: #000 !important;
        border: none !important;
    }
    
    /* Link "Explorar asistentes" más visible en mobile */
    .btn-secondary,
    a.btn-secondary,
    .hero-actions .btn-secondary {
        background: transparent !important;
        background-color: transparent !important;
        color: #000 !important;
        font-weight: 700 !important;
        border: none !important;
        text-decoration: underline !important;
    }
    
    /* Elementos con fondos específicos que NO deben cambiar */
    .hero-impact {
        background: linear-gradient(135deg, #2a2a2a 0%, #3d3d3d 100%) !important;
    }
    
    .hero-impact h1,
    .hero-impact p,
    .hero-impact span {
        color: #fff !important;
    }
    
    .cta {
        background: linear-gradient(180deg, #eef2f7, #ffffff) !important;
    }
    
    .testimonio-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%) !important;
    }
    
    .hero-chat,
    .chat-topbar,
    button,
    .btn-primary,
    .btn-secondary,
    .btn-login,
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary,
    .bubble,
    .demo-bubble {
        background: revert !important;
        color: revert !important;
    }
    
    button, .btn-primary {
        color: #000 !important;
    }
    
    /* BURBUJAS DEL CHAT CON COLORES CORRECTOS EN MOBILE */
    .bubble.user {
        background: #111 !important;
        background-color: #111 !important;
        color: #fff !important;
    }
    
    .bubble.bot {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #222 !important;
        border: 1px solid rgba(0,0,0,0.06) !important;
    }
    
    .header {
        flex-direction: column;
        gap: 15px;
        padding: 16px 4%;
        background: #f6f7fb !important;
    }

    .nav {
        gap: 16px;
        font-size: 14px;
    }

    .hero {
        padding: 20px 4%;
    }

    .hero h1 {
        font-size: 28px;
    }

    .section {
        padding: 20px 4%;
    }

    .section h2 {
        font-size: 26px;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .cta {
        margin: 30px 4% 20px;
        padding: 30px 20px;
    }

    .footer {
        flex-direction: column;
        gap: 10px;
        text-align: center;
        padding: 20px 4%;
    }

    .pricing {
        grid-template-columns: 1fr;
    }
}

/* =========================
   CHATBOT FLOTANTE
========================= */
#chatbot-button {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(244, 180, 0, 0.5);
    display: flex !important;
    align-items: center;
    justify-content: center;
    z-index: 999999 !important;
    transition: all 0.3s ease;
}

#chatbot-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 25px rgba(244, 180, 0, 0.6);
}

#chatbot-button svg {
    width: 30px !important;
    height: 30px !important;
    fill: white !important;
    display: block !important;
}

#chatbot-button svg path {
    fill: white !important;
}

#chatbot-container {
    position: fixed !important;
    bottom: 100px !important;
    right: 20px !important;
    width: 380px;
    height: 550px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    display: none;
    flex-direction: column;
    z-index: 999998 !important;
    overflow: hidden;
    animation: slideIn 0.3s ease;
}

#chatbot-container.open {
    display: flex !important;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.chat-header {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.chat-header-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.chat-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.chat-header-text h3 {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 2px;
}

.chat-header-text p {
    font-size: 12px;
    opacity: 0.9;
}

.close-button {
    background: none;
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
    padding: 0;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: background 0.2s;
}

.close-button:hover {
    background: rgba(255,255,255,0.2);
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background: #f8f9fa;
}

.message {
    margin-bottom: 16px;
    display: flex;
    gap: 10px;
}

.message.bot {
    flex-direction: row;
}

.message.user {
    flex-direction: row-reverse;
}

.message-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}

.message.bot .message-avatar {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
}

.message.user .message-avatar {
    background: #e9ecef;
}

.message-content {
    max-width: 70%;
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 14px;
    line-height: 1.5;
}

.message.bot .message-content {
    background: white;
    color: #333;
    border-bottom-left-radius: 4px;
}

.message.user .message-content {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
    border-bottom-right-radius: 4px;
}

.typing-indicator {
    display: flex;
    gap: 4px;
    padding: 12px 16px;
    background: white;
    border-radius: 18px;
    border-bottom-left-radius: 4px;
    width: fit-content;
}

.typing-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #f4b400;
    animation: typing 1.4s infinite;
}

.typing-dot:nth-child(2) {
    animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes typing {
    0%, 60%, 100% {
        transform: translateY(0);
    }
    30% {
        transform: translateY(-10px);
    }
}

.chat-input {
    padding: 20px;
    background: white;
    border-top: 1px solid #e9ecef;
    display: flex;
    gap: 10px;
}

.chat-input input {
    flex: 1;
    padding: 12px 16px;
    border: 1px solid #e9ecef;
    border-radius: 24px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s;
}

.chat-input input:focus {
    border-color: #f4b400;
}

.send-button {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    border: none;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
}

.send-button:hover {
    transform: scale(1.05);
}

.send-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.send-button svg {
    width: 20px;
    height: 20px;
    fill: white;
}

@media (max-width: 768px) {
    #chatbot-container {
        width: calc(100vw - 40px);
        height: calc(100vh - 140px);
        bottom: 90px;
    }
}

.chat-messages::-webkit-scrollbar {
    width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.chat-messages::-webkit-scrollbar-thumb {
    background: #f4b400;
    border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
    background: #ff6b00;
}
</style>
</head>
<body>
<div class="page-container">
"""

HEADER = """
    <div class="header">
        <a class="logo" href="?vista=home">MERCADO<span>BOT</span></a>
        <div class="nav">
            <a href="?vista=home">Inicio</a>
            <a href="?vista=asistentes">Asistentes</a>
            <a href="?vista=precios">Precios</a>
            <a href="?vista=home#soporte">Soporte</a>
        </div>
    </div>
"""

# FOOTER SIN CIERRE (para st.html) - el body/html se cierra en FOOTER_CHATBOT
FOOTER = """
    <div class="footer" style="display: none;">
    </div>
</div>
</body>
</html>
"""

# FOOTER SIMPLE SIN CHATBOT
FOOTER_SIMPLE = """
<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
    background: #1a1a2e !important; 
    font-family: Inter, system-ui, -apple-system, sans-serif;
}

.footer-section {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 60px 5% 30px;
    color: white;
}

.footer-content {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 40px;
    max-width: 900px;
    margin-bottom: 40px;
}

.footer-col h3 {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #f4b400;
}

.footer-col p {
    font-size: 14px;
    color: rgba(255,255,255,0.8);
    line-height: 1.6;
    margin-bottom: 12px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    font-size: 14px;
    color: rgba(255,255,255,0.8);
}

.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 20px;
    text-align: center;
    font-size: 13px;
    color: rgba(255,255,255,0.5);
}

@media (max-width: 768px) {
    .footer-content {
        grid-template-columns: 1fr;
        gap: 30px;
    }
}
</style>
</head>
<body>

<div class="footer-section">
    <div class="footer-content">
        <div class="footer-col">
            <h3>MercadoBot</h3>
            <p>Automatizá tu atención al cliente con IA conversacional avanzada.</p>
            <p>Respondé 24/7, aumentá conversiones y liberá tiempo para tu equipo.</p>
        </div>
        
        <div class="footer-col">
            <h3>Contacto</h3>
            <div class="contact-item">
                <span>📧</span>
                <span>hola@mercadobot.com</span>
            </div>
            <div class="contact-item">
                <span>📱</span>
                <span>+54 9 11 1234-5678</span>
            </div>
            <div class="contact-item">
                <span>📍</span>
                <span>Buenos Aires, Argentina</span>
            </div>
        </div>
        
        <div class="footer-col">
            <h3>Seguinos</h3>
            <div class="contact-item">
                <span>🔗</span>
                <span>LinkedIn</span>
            </div>
            <div class="contact-item">
                <span>📘</span>
                <span>Facebook</span>
            </div>
            <div class="contact-item">
                <span>📷</span>
                <span>Instagram</span>
            </div>
        </div>
    </div>
    
    <div class="footer-bottom">
        <p>© 2025 MercadoBot. Todos los derechos reservados.</p>
    </div>
</div>

</body>
</html>
"""
# CSS para overflow visible
st.markdown("""
<style>
div[data-testid="element-container"]:has(iframe[height="550"]) {
    overflow: visible !important;
}
div[data-testid="element-container"]:has(iframe[height="550"]) iframe {
    overflow: visible !important;
}
</style>
""", unsafe_allow_html=True)

# Footer simple sin chatbot
components.html(FOOTER_SIMPLE, height=400)
