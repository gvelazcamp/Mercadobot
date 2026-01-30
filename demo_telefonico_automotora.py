import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS mínimo
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("📞 Asistente Telefónico con IA")
st.write("Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.")

st.divider()

# TARJETA PRINCIPAL
st.header("🎙️ Probalo Ahora")
st.write("Llamá desde tu celular y conversá con el asistente. Te va a sorprender lo natural que suena.")

st.markdown("### 📞 **+598 1234 5678**")
st.caption("👆 Tap para llamar desde móvil")

st.success("✅ Disponible 24/7 · Llamá cuando quieras")

st.info("💡 Es un demo gratuito. Probá todas las funciones sin costo.")

st.divider()

# CARACTERÍSTICAS
st.header("✨ Qué Puede Hacer")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🗣️ Conversación Natural")
    st.write("Habla como una persona real. Entiende español argentino perfectamente.")
    
    st.markdown("#### 💳 Explica Financiación")
    st.write("Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles.")
    
    st.markdown("#### 🔄 Tasa Usado")
    st.write("Pregunta por tu auto usado y coordina la tasación sin cargo.")

with col2:
    st.markdown("#### 🚗 Conoce el Stock")
    st.write("Sabe todos los autos disponibles, precios y características al detalle.")
    
    st.markdown("#### 📅 Agenda Test Drives")
    st.write("Toma tus datos y coordina visitas o pruebas de manejo automáticamente.")
    
    st.markdown("#### ⏰ 24/7 Disponible")
    st.write("Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.")

st.divider()

# CONVERSACIÓN DE EJEMPLO
st.header("💬 Ejemplo de Conversación Real")

with st.chat_message("assistant"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user"):
    st.write("Busco un auto usado")

with st.chat_message("assistant"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user"):
    st.write("Unos 10 millones")

with st.chat_message("assistant"):
    st.write("Genial. Tengo 2 opciones: un Gol Trend 2020 a 9.8 millones o un Focus 2019 a 12.9 millones. ¿Cuál te copa más?")

with st.chat_message("user"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant"):
    st.write("¡Claro! Te agendo el test drive. ¿Tu nombre completo?")

with st.chat_message("user"):
    st.write("Juan Pérez")

with st.chat_message("assistant"):
    st.write("Perfecto Juan. ¿Tu teléfono?")

with st.chat_message("user"):
    st.write("099 123 456")

with st.chat_message("assistant"):
    st.write("Listo Juan, cero nueve nueve, uno dos tres, cuatro cinco seis. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos para confirmar día y horario. ¡Gracias por llamar!")

st.divider()

# ESTADÍSTICAS
st.header("📊 Resultados Reales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Disponibilidad", value="24/7")

with col2:
    st.metric(label="Llamadas Atendidas", value="100%")

with col3:
    st.metric(label="Tiempo Promedio", value="3 min")

with col4:
    st.metric(label="Leads Calificados", value="85%")

st.divider()

# CTA FINAL
st.header("¿Listo para Probarlo?")
st.write("Llamá ahora y conversá con el asistente. Es completamente gratis y podés probar todas las funciones.")

# Botón para llamar
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.divider()

# FOOTER
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo.")
st.caption("🔒 Todas las llamadas son procesadas con IA. Funcionamiento garantizado 24/7.")
