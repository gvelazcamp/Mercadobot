import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<style>
* {
    box-sizing: border-box;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background: #f6f7fb;
    margin: 0;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 60px;
}

.logo {
    font-size: 22px;
    font-weight: 800;
}
.logo span { color: #f4b400; }

.nav {
    display: flex;
    gap: 32px;
    font-weight: 500;
    color: #555;
}

.btn-login {
    background: #f4b400;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 600;
}

.hero {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 40px;
    padding: 60px;
    align-items: center;
}

.hero h1 { font-size: 48px; line-height: 1.1; }
.hero p { font-size: 18px; color: #555; margin: 20px 0; }

.section {
    padding: 60px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}

.card {
    background: #fff;
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 12px 40px rgba(0,0,0,0.06);
}

.card img {
    width: 100%;
    max-height: 180px;
    object-fit: contain;
}

.card h3 { margin-top: 20px; }
.card p { color: #666; font-size: 14px; }

.card button {
    margin-top: 16px;
    background: #f4b400;
    border: none;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 700;
}
</style>

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
        <p>Automatizá tu negocio con asistentes virtuales inteligentes.</p>
    </div>
    <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistente.png">
</div>

<div class="section">
    <h2 style="text-align:center;">Asistentes IA</h2>

    <div class="cards">
        <div class="card">
            <img src="https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/Asistentefutbol.png">
            <h3>Fútbol</h3>
            <p>Datos y estadísticas</p>
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
"""

components.html(html, height=1600, scrolling=True)
