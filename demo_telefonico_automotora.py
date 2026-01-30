import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS con naranjas y diseño profesional
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%) !important;
}

.main .block-container {
    padding: 2rem 1rem;
}

/* Títulos blancos */
h1, h2, h3 {
    color: white !important;
}

/* Métricas naranjas */
div[data-testid="stMetricValue"] {
    color: #ff6b00 !important;
    font-size: 2.5rem !important;
    font-weight: bold !important;
}

/* Botón naranja grande */
.stButton > button, .stLinkButton > a {
    background: white !important;
    color: #ff6b00 !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    padding: 1.2rem 3rem !important;
    border-radius: 12px !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
}

.stButton > button:hover, .stLinkButton > a:hover {
    background: #fff5e6 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("📞 Asistente Telefónico con IA")
st.subheader("Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.")

st.write("")
st.write("")

# NÚMERO DESTACADO
st.header("🎙️ Probalo Ahora")
st.write("Llamá desde tu celular y conversá con el asistente. Te va a sorprender lo natural que suena.")

st.write("")
st.markdown("## 📞")
st.markdown("# **+598 1234 5678**")
st.caption("👆 Tap para llamar desde móvil")

st.success("✅ **Disponible 24/7** · Llamá cuando quieras")
st.info("💡 Es un demo gratuito. Probá todas las funciones sin costo.")

st.write("")
st.write("")

# CARACTERÍSTICAS
st.header("✨ Qué Puede Hacer")
st.write("")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("### 🗣️ Conversación Natural")
        st.write("Habla como una persona real. Entiende español argentino perfectamente con todas sus expresiones.")
    
    st.write("")
    
    with st.container():
        st.markdown("### 💳 Explica Financiación")
        st.write("Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles. Calcula las cuotas en el momento.")
    
    st.write("")
    
    with st.container():
        st.markdown("### 🔄 Tasa Usado")
        st.write("Pregunta por tu auto usado y coordina la tasación sin cargo. Toma marca, modelo, año y kilómetros.")
    
    st.write("")
    
    with st.container():
        st.markdown("### 📝 Califica Leads")
        st.write("Identifica clientes reales preguntando presupuesto, urgencia y necesidades. Filtra curiosos automáticamente.")

with col2:
    with st.container():
        st.markdown("### 🚗 Conoce el Stock")
        st.write("Sabe todos los autos disponibles, precios y características al detalle. Nunca se confunde con el inventario.")
    
    st.write("")
    
    with st.container():
        st.markdown("### 📅 Agenda Test Drives")
        st.write("Toma tus datos y coordina visitas o pruebas de manejo automáticamente. Confirma fechas disponibles.")
    
    st.write("")
    
    with st.container():
        st.markdown("### ⏰ 24/7 Disponible")
        st.write("Nunca pierde una llamada. Atiende de madrugada, fines de semana y feriados. Siempre profesional.")
    
    st.write("")
    
    with st.container():
        st.markdown("### 🎯 Sin Errores")
        st.write("Siempre profesional, nunca se olvida información, nunca tiene un mal día. Consistencia garantizada.")

st.write("")
st.write("")

# CONVERSACIÓN
st.header("💬 Conversación Real")
st.caption("Así suena una llamada típica con el asistente")
st.write("")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user", avatar="👤"):
    st.write("Busco un auto usado")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user", avatar="👤"):
    st.write("Unos 10 millones")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Genial. Tengo 2 opciones excelentes: un **Gol Trend 2020** a **$9.8 millones** con 55 mil km, único dueño, service al día. O un **Focus 2019** a **$12.9 millones** con 65 mil km. ¿Cuál te copa más?")

with st.chat_message("user", avatar="👤"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Claro que sí! Te agendo el test drive del Gol Trend. ¿Cuál es tu nombre completo?")

with st.chat_message("user", avatar="👤"):
    st.write("Juan Pérez")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Perfecto Juan. ¿Y tu número de teléfono?")

with st.chat_message("user", avatar="👤"):
    st.write("099 123 456")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Listo Juan, confirmo: **cero nueve nueve, uno dos tres, cuatro cinco seis**. Agendé tu test drive del Gol Trend 2020. Un vendedor te va a contactar en los próximos 10 minutos para confirmar el día y horario que mejor te venga. ¡Muchas gracias por comunicarte con AutoCenter!")

st.write("")
st.write("")

# ESTADÍSTICAS
st.header("📊 Resultados Comprobados")
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Disponibilidad", value="24/7")

with col2:
    st.metric(label="Llamadas Atendidas", value="100%", delta="vs. humanos 70%")

with col3:
    st.metric(label="Tiempo Promedio", value="3 min", delta="-5 min vs. humanos")

with col4:
    st.metric(label="Leads Calificados", value="85%", delta="+40% vs. humanos")

st.write("")
st.write("")

# CTA FINAL
st.header("¿Listo para Probarlo?")
st.write("Llamá ahora y conversá con el asistente. Es completamente **gratis** y podés probar todas las funciones.")

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.write("")
st.write("")

# FOOTER
st.divider()
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo. En producción se personaliza 100% con tu negocio, stock real y precios actualizados.")
st.caption("🔒 Todas las llamadas son procesadas con IA de última generación (GPT-4 + ElevenLabs). Funcionamiento garantizado 24/7. Integración con CRM disponible.")
st.caption("⚡ **ROI Promedio:** El sistema se paga solo en 30 días. Clientes reportan aumento del 40% en conversión de llamadas.")
