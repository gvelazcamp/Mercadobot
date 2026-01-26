import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<style>
/* =========================
   BASE
========================= */
* {
    box-sizing: border-box;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background: #f6f7fb;
    margin: 0;
}

/* =========================
   WRAPPER
========================= */
.wrapper {
    max-width: 1200px;
    margin: 0 auto;
}

/* =========================
   HEADER
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
}

.logo {
    font-size: 22px;
    font-weight: 800;
}
.logo span {
    color: #f4b400;
}

.nav {
    display: flex;
    gap: 28px;
    font-weight: 500;
    color: #555;
}

.btn-login {
    background: #f4b400;
    padding: 8px 16px;
    border-radius: 10px;
    font-weight: 600;
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    padding: 40px;
    align-items: center;
}

.hero h1 {
    font-size: 38px;
    line-height: 1.15;
}

.hero p {
    font-size: 16px;
    color: #555;
    margin: 18px 0;
}

.hero img {
    max-width: 460px;
    width: 100%;
    margin-left: auto;
}

/* =========================
   SECTION
========================= */
.section {
    padding: 40px;
}

.section h2 {
    text-align: center;
    font-size: 32px;
    margin-bottom: 10px;
}

/* =========================
   CARDS
========================= */
.cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
    margin-top: 40px;
}

.card {
    background: #fff;
    border-radius: 22px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
}

.card img {
    width: 100%;
    max-height: 130px;
    object-fit: contain;
}

.card h3 {
    margin-top: 18px;
    font-size: 18px;
}

.card p {
    font-size: 13px;
    color: #666;
}

.card button {
    margin-top: 14px;
    background: #f4b400;
    border: none;
    padding: 8px 16px;
    border-radius: 10px;
    font-weight: 700;
    cursor: pointer;
}

/* =========================
   FOOTER
========================= */
.footer {
    padding: 30px 40px;
    color: #888;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
}
</style>

<div class="wrapper">

    <div class="header">
        <div class="logo">MERCADO<span>BOT</span></div>
        <div class="nav">
            <div>Inicio</div>
            <div>Asistentes</div>
            <div>Precios</div>
            <div>Soporte</div>
        </div>
        <div class="btn-login">Iniciar sesión</div>
    </div>

    <div class="hero">
        <div>
            <h1>El marketplace<br>de asistentes IA</h1>
            <p>
                Automatizá tu negocio con asistentes virtuales inteligentes
                que responden, informan y venden por vos.
            </p>
        </div>

        <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistente.png">
    </div>

    <div class="section">
        <h2>Asistentes IA</h2>

        <div class="cards">
            <div class="card">
                <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistentefutbol.png">
                <h3>Fútbol</h3>
                <p>Datos, estadísticas y análisis</p>
                <button>Ver</button>
            </div>

            <div class="card">
                <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistentecocina.png">
                <h3>Cocina</h3>
                <p>Recetas inteligentes</p>
                <button>Ver</button>
            </div>

            <div class="card">
                <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistenteecommerce.png">
                <h3>Ecommerce</h3>
                <p>Ventas automáticas</p>
                <button>Ver</button>
            </div>

            <div class="card">
                <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistentefinanzas.png">
                <h3>Finanzas</h3>
                <p>Análisis financiero</p>
                <button>Ver</button>
            </div>
        </div>
    </div>

    <div class="footer">
        <div>Política de privacidad · Términos · Contacto</div>
        <div>Facebook · Twitter · LinkedIn</div>
    </div>

</div>
"""

components.html(html, height=1400, scrolling=True)
