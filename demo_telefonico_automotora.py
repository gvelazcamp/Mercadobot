import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico - MercadoBot",
    page_icon="📞",
    layout="centered"
)

# CSS limpio
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: #f8f9fa;
    }
    
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 900px;
    }
    
    /* Métricas naranjas */
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        color: #ff6b00 !important;
        font-weight: bold !important;
    }
    
    /* Botones naranjas */
    .stButton > button, .stLinkButton > a {
        background: linear-gradient(135deg, #f4b400, #ff6b00) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2.5rem !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 0, 0.3) !important;
    }
    
    .stButton > button:hover, .stLinkButton > a:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 0, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# HEADER con imagen SVG inline
st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#f4b400;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#ff6b00;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="100%" height="200" rx="15" fill="url(#grad1)"/>
    <text x="50%" y="90" font-size="42" font-weight="bold" fill="white" text-anchor="middle" font-family="Arial, sans-serif">
        📞 Asistente Telefónico con IA
    </text>
    <text x="50%" y="130" font-size="18" fill="white" text-anchor="middle" font-family="Arial, sans-serif" opacity="0.95">
        Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.
    </text>
</svg>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# NÚMERO DE TELÉFONO - Usando SVG para que se vea perfecto
st.markdown("""
<svg width="100%" height="550" xmlns="http://www.w3.org/2000/svg">
    <!-- Fondo blanco principal -->
    <rect width="100%" height="550" rx="15" fill="white" filter="url(#shadow)"/>
    
    <!-- Sombra -->
    <defs>
        <filter id="shadow">
            <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
            <feOffset dx="0" dy="2" result="offsetblur"/>
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.1"/>
            </feComponentTransfer>
            <feMerge>
                <feMergeNode/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <linearGradient id="phoneGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#f4b400;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#ff6b00;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Título -->
    <text x="50%" y="50" font-size="28" font-weight="bold" fill="#333" text-anchor="middle" font-family="Arial, sans-serif">
        🎙️ Probalo Ahora
    </text>
    
    <!-- Subtítulo -->
    <text x="50%" y="85" font-size="16" fill="#666" text-anchor="middle" font-family="Arial, sans-serif">
        Llamá desde tu celular y conversá con el asistente.
    </text>
    <text x="50%" y="110" font-size="16" fill="#666" text-anchor="middle" font-family="Arial, sans-serif">
        Te va a sorprender lo natural que suena.
    </text>
    
    <!-- Box del teléfono con gradiente -->
    <rect x="10%" y="140" width="80%" height="280" rx="15" fill="url(#phoneGrad)"/>
    
    <!-- Ícono de teléfono -->
    <text x="50%" y="220" font-size="80" text-anchor="middle">📞</text>
    
    <!-- Número de teléfono -->
    <text x="50%" y="310" font-size="48" font-weight="bold" fill="white" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="2">
        +598 1234 5678
    </text>
    
    <!-- Instrucción -->
    <text x="50%" y="355" font-size="14" fill="white" text-anchor="middle" font-family="Arial, sans-serif" opacity="0.95">
        👆 Tap para llamar desde móvil
    </text>
    
    <!-- Badge disponibilidad -->
    <rect x="25%" y="450" width="50%" height="50" rx="25" fill="#e8f5e9"/>
    <circle cx="32%" cy="475" r="6" fill="#4caf50"/>
    <text x="50%" y="482" font-size="14" font-weight="600" fill="#2e7d32" text-anchor="middle" font-family="Arial, sans-serif">
        Disponible 24/7 · Llamá cuando quieras
    </text>
    
    <!-- Nota final -->
    <text x="50%" y="530" font-size="13" fill="#888" text-anchor="middle" font-family="Arial, sans-serif">
        💡 Es un demo gratuito. Probá todas las funciones sin costo.
    </text>
</svg>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CARACTERÍSTICAS - Con SVG para cards
st.markdown("""
<div style="text-align: center; margin: 40px 0 30px 0;">
    <h2 style="color: #333; font-size: 36px; font-weight: 700;">
        ✨ Qué Puede Hacer
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">🗣️</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Conversación Natural</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Habla como una persona real.</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">Entiende español argentino</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">perfectamente.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">💳</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Explica Financiación</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Detalla cuotas, tasas,</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">anticipo y formas de pago.</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">Calcula en el momento.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">🔄</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Tasa Usado</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Pregunta por tu auto y</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">coordina tasación sin cargo.</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">Toma marca, modelo, año.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">📝</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Califica Leads</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Identifica clientes reales.</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">Pregunta presupuesto,</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">urgencia y necesidades.</text>
    </svg>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">🚗</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Conoce el Stock</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Sabe todos los autos</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">disponibles, precios y</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">características al detalle.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">📅</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Agenda Test Drives</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Toma tus datos y coordina</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">visitas o pruebas de manejo</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">automáticamente.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">⏰</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">24/7 Disponible</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Nunca pierde una llamada.</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">Atiende de madrugada,</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">fines de semana, feriados.</text>
    </svg>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="180" rx="12" fill="white" filter="url(#cardShadow)"/>
        <line x1="0" y1="0" x2="0" y2="180" stroke="#ff6b00" stroke-width="4"/>
        <text x="20" y="60" font-size="40">🎯</text>
        <text x="20" y="100" font-size="18" font-weight="bold" fill="#333" font-family="Arial">Sin Errores</text>
        <text x="20" y="125" font-size="14" fill="#666" font-family="Arial">Siempre profesional.</text>
        <text x="20" y="145" font-size="14" fill="#666" font-family="Arial">Nunca se olvida información.</text>
        <text x="20" y="165" font-size="14" fill="#666" font-family="Arial">Consistencia garantizada.</text>
    </svg>
    """, unsafe_allow_html=True)

# Definir shadow para los cards
st.markdown("""
<svg width="0" height="0">
    <defs>
        <filter id="cardShadow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="2"/>
            <feOffset dx="0" dy="2" result="offsetblur"/>
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.08"/>
            </feComponentTransfer>
            <feMerge>
                <feMergeNode/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
</svg>
""", unsafe_allow_html=True)

# CONVERSACIÓN
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin: 40px 0 30px 0;">
    <h2 style="color: #333; font-size: 36px; font-weight: 700;">
        💬 Conversación Real
    </h2>
    <p style="color: #666; font-size: 16px;">
        Así suena una llamada típica con el asistente
    </p>
</div>
""", unsafe_allow_html=True)

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user", avatar="👤"):
    st.write("Busco un auto usado")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user", avatar="👤"):
    st.write("Unos 10 millones")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Genial. Tengo 2 opciones: un **Gol Trend 2020** a **$9.8 millones** o un **Focus 2019** a **$12.9 millones**. ¿Cuál te copa más?")

with st.chat_message("user", avatar="👤"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Claro! Te agendo el test drive. ¿Tu nombre completo?")

with st.chat_message("user", avatar="👤"):
    st.write("Juan Pérez")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Listo Juan, **cero nueve nueve, uno dos tres, cuatro cinco seis**. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos. ¡Gracias!")

# ESTADÍSTICAS
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin: 40px 0 30px 0;">
    <h2 style="color: #333; font-size: 36px; font-weight: 700;">
        📊 Resultados Comprobados
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Disponibilidad", value="24/7")

with col2:
    st.metric(label="Llamadas", value="100%", delta="+30%")

with col3:
    st.metric(label="Tiempo", value="3 min", delta="-5 min")

with col4:
    st.metric(label="Leads", value="85%", delta="+40%")

# CTA FINAL
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="200" rx="15" fill="white" filter="url(#shadow)"/>
    <text x="50%" y="60" font-size="32" font-weight="bold" fill="#333" text-anchor="middle" font-family="Arial">
        ¿Listo para Probarlo?
    </text>
    <text x="50%" y="95" font-size="16" fill="#666" text-anchor="middle" font-family="Arial">
        Llamá ahora y conversá con el asistente.
    </text>
    <text x="50%" y="120" font-size="16" fill="#666" text-anchor="middle" font-family="Arial">
        Es completamente gratis y podés probar todas las funciones.
    </text>
</svg>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# FOOTER
st.divider()
st.caption("💡 Este es un demo funcional. En producción se personaliza 100% con tu negocio.")
st.caption("🔒 IA de última generación (GPT-4 + ElevenLabs). Funcionamiento 24/7.")
st.caption("⚡ ROI: Se paga solo en 30 días. +40% conversión en llamadas.")
