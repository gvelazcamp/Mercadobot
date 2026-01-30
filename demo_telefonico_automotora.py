import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
}

.main .block-container {
    padding: 2rem 1rem;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div style="background: white; padding: 40px 20px; border-radius: 20px; text-align: center; margin-bottom: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
    <h1 style="margin: 0; font-size: 42px; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        📞 Asistente Telefónico con IA
    </h1>
    <p style="margin: 15px 0 0 0; color: #666; font-size: 18px;">
        Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.
    </p>
</div>
""", unsafe_allow_html=True)

# TARJETA PRINCIPAL
st.markdown("""
<div style="background: white; padding: 50px 30px; border-radius: 25px; text-align: center; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 32px; color: #333; margin-bottom: 15px;">🎙️ Probalo Ahora</h2>
    <p style="font-size: 18px; color: #666; margin-bottom: 30px;">
        Llamá desde tu celular y conversá con el asistente.<br>
        Te va a sorprender lo natural que suena.
    </p>
    
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 50px 30px; border-radius: 20px; margin: 30px 0;">
        <div style="font-size: 80px; margin-bottom: 20px;">📞</div>
        <div style="font-size: 48px; font-weight: bold; color: white; letter-spacing: 3px; margin: 20px 0;">
            <a href="tel:+5981234567" style="color: white; text-decoration: none;">+598 1234 5678</a>
        </div>
        <p style="color: white; opacity: 0.9; font-size: 16px; margin-top: 15px;">
            Tap para llamar desde móvil
        </p>
    </div>
    
    <div style="background: #e8f5e9; padding: 15px 25px; border-radius: 50px; display: inline-block; margin: 20px 0; font-weight: 600; color: #2e7d32;">
        <span style="display: inline-block; width: 10px; height: 10px; background: #4caf50; border-radius: 50%; margin-right: 10px;"></span>
        Disponible 24/7 · Llamá cuando quieras
    </div>
    
    <p style="margin-top: 30px; font-size: 14px; color: #888;">
        💡 Es un demo gratuito. Probá todas las funciones sin costo.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CARACTERÍSTICAS
st.markdown("""
<div style="background: white; padding: 40px 30px; border-radius: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 28px; color: #333; margin-bottom: 30px; text-align: center;">
        ✨ Qué Puede Hacer
    </h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">🗣️</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">Conversación Natural</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Habla como una persona real. Entiende español argentino perfectamente.
            </div>
        </div>
        
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">🚗</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">Conoce el Stock</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Sabe todos los autos disponibles, precios y características al detalle.
            </div>
        </div>
        
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">💳</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">Explica Financiación</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles.
            </div>
        </div>
        
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">📅</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">Agenda Test Drives</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Toma tus datos y coordina visitas o pruebas de manejo automáticamente.
            </div>
        </div>
        
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">🔄</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">Tasa Usado</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Pregunta por tu auto usado y coordina la tasación sin cargo.
            </div>
        </div>
        
        <div style="background: #f8f9ff; padding: 25px; border-radius: 15px;">
            <div style="font-size: 36px; margin-bottom: 15px;">⏰</div>
            <div style="font-size: 18px; font-weight: 700; color: #333; margin-bottom: 10px;">24/7 Disponible</div>
            <div style="font-size: 14px; color: #666; line-height: 1.6;">
                Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CONVERSACIÓN
st.markdown("""
<div style="background: white; padding: 40px 30px; border-radius: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 28px; color: #333; margin-bottom: 30px; text-align: center;">
        💬 Ejemplo de Conversación Real
    </h2>
    
    <div style="max-width: 600px; margin: 0 auto;">
        <div style="margin: 15px 0; text-align: left;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">ASISTENTE</div>
            <div style="background: #f0f0f0; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; border-bottom-left-radius: 5px;">
                ¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: right;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">CLIENTE</div>
            <div style="background: #667eea; color: white; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; display: inline-block; border-bottom-right-radius: 5px;">
                Busco un auto usado
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: left;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">ASISTENTE</div>
            <div style="background: #f0f0f0; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; border-bottom-left-radius: 5px;">
                Dale, perfecto. ¿Qué presupuesto tenés más o menos?
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: right;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">CLIENTE</div>
            <div style="background: #667eea; color: white; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; display: inline-block; border-bottom-right-radius: 5px;">
                Unos 10 millones
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: left;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">ASISTENTE</div>
            <div style="background: #f0f0f0; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; border-bottom-left-radius: 5px;">
                Genial. Tengo 2 opciones: un Gol Trend 2020 a 9.8 millones o un Focus 2019 a 12.9 millones. ¿Cuál te copa más?
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: right;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">CLIENTE</div>
            <div style="background: #667eea; color: white; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; display: inline-block; border-bottom-right-radius: 5px;">
                El Gol. ¿Puedo hacer un test drive?
            </div>
        </div>
        
        <div style="margin: 15px 0; text-align: left;">
            <div style="font-size: 11px; font-weight: 600; color: #888; margin-bottom: 5px;">ASISTENTE</div>
            <div style="background: #f0f0f0; padding: 15px 20px; border-radius: 18px; font-size: 15px; line-height: 1.5; border-bottom-left-radius: 5px;">
                ¡Claro! Te agendo el test drive. ¿Tu nombre completo?
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ESTADÍSTICAS
st.markdown("""
<div style="background: white; padding: 40px 30px; border-radius: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 28px; color: #333; margin-bottom: 30px; text-align: center;">
        📊 Resultados Reales
    </h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; text-align: center;">
        <div>
            <div style="font-size: 42px; font-weight: bold; color: #667eea; margin-bottom: 8px;">24/7</div>
            <div style="font-size: 13px; color: #666; font-weight: 600;">Disponibilidad</div>
        </div>
        
        <div>
            <div style="font-size: 42px; font-weight: bold; color: #667eea; margin-bottom: 8px;">100%</div>
            <div style="font-size: 13px; color: #666; font-weight: 600;">Llamadas Atendidas</div>
        </div>
        
        <div>
            <div style="font-size: 42px; font-weight: bold; color: #667eea; margin-bottom: 8px;">3 min</div>
            <div style="font-size: 13px; color: #666; font-weight: 600;">Tiempo Promedio</div>
        </div>
        
        <div>
            <div style="font-size: 42px; font-weight: bold; color: #667eea; margin-bottom: 8px;">85%</div>
            <div style="font-size: 13px; color: #666; font-weight: 600;">Leads Calificados</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# CTA FINAL
st.markdown("""
<div style="background: white; padding: 50px 30px; border-radius: 25px; text-align: center; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 32px; font-weight: 700; color: #333; margin-bottom: 15px;">
        ¿Listo para Probarlo?
    </h2>
    <p style="font-size: 18px; color: #666; margin-bottom: 30px; line-height: 1.6;">
        Llamá ahora y conversá con el asistente. Es completamente gratis y podés probar todas las funciones.
    </p>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.divider()
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo.")
st.caption("🔒 Todas las llamadas son procesadas con IA. Funcionamiento garantizado 24/7.")
