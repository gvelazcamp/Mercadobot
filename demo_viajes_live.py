import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo Viajes - MercadoBot",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilos del chat */
    .stChatMessage {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .stChatFloatingInputContainer {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Header personalizado */
    .custom-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #f4b400, #ff6b00);
        border-radius: 15px;
        margin-bottom: 30px;
        color: white;
    }
    
    .custom-header h1 {
        margin: 0;
        font-size: 32px;
    }
    
    .custom-header p {
        margin: 10px 0 0 0;
        opacity: 0.95;
    }
    
    /* Botones de sugerencias */
    .suggestion-buttons {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
        margin: 20px 0;
    }
    
    .suggestion-btn {
        background: #f4b400;
        color: #000;
        padding: 8px 16px;
        border-radius: 20px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.3s;
    }
    
    .suggestion-btn:hover {
        background: #ff6b00;
        color: white;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <h1>🌍 Demo Live - Asistente de Viajes</h1>
    <p>Probá el chatbot en vivo. Hacele las preguntas que quieras.</p>
</div>
""", unsafe_allow_html=True)

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": """¡Hola! 👋 Te ayudo a encontrar tu viaje perfecto.

**Decime:**
• ¿Playa o montaña?
• ¿Aventura o relax?
• ¿Presupuesto? (económico/medio/premium)
• ¿Cuándo querés viajar?

💡 **Trending ahora:** Bariloche nieve ❄️ | Caribe playas 🏝️ | Europa cultura 🏛️"""
        }
    ]

# Botones de sugerencias (solo al inicio)
if len(st.session_state.messages) == 1:
    st.markdown("**💡 Probá con estas preguntas:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏖️ Playa en marzo", use_container_width=True):
            st.session_state.temp_input = "Busco playa, relax, presupuesto medio, en marzo"
            st.rerun()
    
    with col2:
        if st.button("✈️ ¿Cuánto sale Cancún?", use_container_width=True):
            st.session_state.temp_input = "¿Cuánto sale Cancún?"
            st.rerun()
    
    with col3:
        if st.button("💳 Formas de pago", use_container_width=True):
            st.session_state.temp_input = "¿Puedo pagar en cuotas?"
            st.rerun()

# Mostrar historial de mensajes
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Función para obtener respuesta del bot
def get_bot_response(prompt):
    p = prompt.lower()
    
    # Respuesta 1: Consulta inicial de destino
    if any(word in p for word in ["playa", "relax", "marzo", "verano"]):
        return """¡Perfecto! 🏖️ Te recomiendo:

**OPCIÓN 1 — Cancún, México 🇲🇽**
• Vuelo + Hotel 5★ (7 días): USD 1.200/persona
• Todo incluido (comidas + bebidas)
• Playa turquesa + vida nocturna
⚠️ Quedan solo **3 paquetes** a este precio para marzo

**OPCIÓN 2 — Punta Cana 🇩🇴**
• Vuelo + Resort (7 días): USD 1.350
• All inclusive premium
• Excursiones incluidas

**OPCIÓN 3 — Florianópolis 🇧🇷**
• Vuelo + Hotel boutique (5 días): USD 800
• Playas paradisíacas
• Más económico, cerca

¿Cuál te llama más? 😊"""
    
    # Respuesta 2: Detalles de Cancún
    elif "cancun" in p or "cancún" in p or "méxico" in p or "cuanto" in p:
        return """¡Excelente elección! 🇲🇽

**Paquete Cancún Premium incluye:**
✅ Vuelos directos Buenos Aires → Cancún
✅ Hotel 5★ frente al mar (7 noches)
✅ All inclusive (desayuno, almuerzo, cena, bar)
✅ Traslados aeropuerto ↔ hotel
✅ Excursión a Chichén Itzá GRATIS
✅ Snorkel en cenotes GRATIS

**Salidas disponibles:**
• 5 de marzo → USD 1.200
• 12 de marzo → USD 1.280
• 19 de marzo → USD 1.350

💡 Reservando HOY: **$50 USD descuento + upgrade de habitación**

¿Para cuántas personas es?"""
    
    # Respuesta 3: Consulta de personas
    elif any(num in p for num in ["2", "dos", "3", "tres", "4", "cuatro", "persona"]):
        return """Perfecto! Para 2 personas: **USD 2.400 total** ✈️

**¿Querés agregar experiencias VIP?**
🌊 Nado con delfines — USD 120/persona
🏛️ Tour privado Tulum + cenote — USD 150/persona
🍽️ Cena romántica en la playa — USD 80 para 2
🎉 Fiesta en catamarán — USD 90/persona

🔥 **Promo:** Contratando 2 experiencias → 3ra al 50% OFF

¿Te sumo alguna? 😊"""
    
    # Respuesta 4: Formas de pago
    elif any(word in p for word in ["cuotas", "pago", "financ", "tarjeta", "efectivo"]):
        return """¡Claro! 💳

**Formas de pago:**
💵 **Efectivo/Transferencia:** 5% descuento adicional
💳 **Tarjeta de crédito:**
   • 3 cuotas sin interés
   • 6 cuotas sin interés
   • 12 cuotas (TNA 48%)
🌎 **Mercado Pago:** Hasta 18 cuotas

**Ejemplo para 2 personas (USD 2.400):**
→ 6 cuotas de **USD 400** sin interés
→ 12 cuotas de **USD 220** c/interés

¿Cómo preferís pagar?"""
    
    # Respuesta 5: Cambios de fecha
    elif any(word in p for word in ["cambio", "fecha", "cancelar", "flexible"]):
        return """Buena pregunta! 🗓️

**Opciones de flexibilidad:**
📌 **Estándar:** Cambio de fecha con 30 días anticipación — Cargo USD 100
📌 **Flex:** Cambio GRATIS hasta 15 días antes — +USD 150
📌 **Total Flex:** Cambio o cancelación hasta 48hs antes, reembolso 100% — +USD 280

La mayoría elige **Flex** para viajar tranquilo.
¿Cuál preferís?"""
    
    # Respuesta 6: Visa y requisitos
    elif any(word in p for word in ["visa", "pasaporte", "documento", "requisito"]):
        return """No 🎉 **Argentinos NO necesitan visa para México**

**Requisitos:**
✅ Pasaporte válido (mínimo 6 meses)
✅ Formulario migratorio (te lo damos)
✅ Seguro de viaje (obligatorio, lo incluimos)

**¿No tenés pasaporte?**
Te ayudamos a tramitarlo:
• Turno online → 15 días
• Entrega en 10-15 días hábiles

🔔 **Importante:** Arrancar YA para viajar en marzo.
¿Ya tenés pasaporte vigente?"""
    
    # Respuesta 7: Seguro de viaje
    elif any(word in p for word in ["seguro", "cobertura", "salud"]):
        return """Buena pregunta! 🛡️

**Seguro Básico (incluido):**
✅ Gastos médicos hasta USD 50.000
✅ Equipaje perdido USD 1.000
✅ Cancelación por enfermedad

**Seguro Premium (+USD 80):**
✅ Gastos médicos USD 150.000
✅ COVID cubierto 100%
✅ Deportes extremos
✅ Equipaje USD 3.000
✅ Cancelación por CUALQUIER motivo
✅ Asistencia 24/7 en español

💡 El 70% de nuestros clientes elige **Premium** para viajar tranquilo.
¿Lo sumamos?"""
    
    # Respuesta 8: Urgencia
    elif any(word in p for word in ["pienso", "duda", "después", "mañana"]):
        return """¡Perfecto! 😊 Te entiendo.

⚠️ **Datos importantes:**
• Este precio es válido solo **hasta mañana 18hs**
• Quedan **2 habitaciones** disponibles para 5 de marzo
• Los vuelos directos se agotan rápido en temporada alta

🎁 **Si reservás HOY:**
→ Te guardamos el precio 24hs SIN pagar
→ Upgrade de habitación GRATIS (vista al mar)
→ Late check-out incluido

¿Te lo reservo mientras pensás? (sin compromiso)"""
    
    # Respuesta 9: Comparación con competencia
    elif any(word in p for word in ["otra agencia", "más barato", "encontré", "vi"]):
        return """Buenísimo que compares! 👍

**¿Qué incluye ese otro paquete?**
Muchas veces no incluyen:
❌ Traslados (USD 80)
❌ Tasas e impuestos (USD 150)
❌ Seguro de viaje (USD 60)
❌ Excursiones

**Nuestro precio INCLUYE TODO:**
✅ Sin cargos ocultos
✅ Sin sorpresas al pagar
✅ Precio final USD 2.400

Pasame el link y te hago el breakdown exacto 😊
Seguro que nuestro paquete tiene más valor."""
    
    # Respuesta 10: Grupos/familias
    elif any(word in p for word in ["familia", "niños", "hijos", "grupo", "6 personas"]):
        return """¡Genial viaje en familia! 👨‍👩‍👧‍👦

**Paquete Familiar Cancún:**
💰 **Precio:** USD 5.400 total (USD 900/adulto, niños 50% OFF)
🏨 **Habitaciones:** 2 conectadas con vista al mar
🍽️ **All inclusive** para toda la familia
🎠 **Kids club** incluido (4-12 años)

**BONUS familiar:**
🎁 1 adulto GRATIS en grupos de 6+
🎢 Parque acuático 1 día GRATIS
📸 Sesión de fotos familiar incluida

¿Los niños qué edad tienen? (importante para los servicios)"""
    
    # Respuesta 11: Luna de miel
    elif any(word in p for word in ["luna de miel", "casamiento", "boda", "romántico"]):
        return """¡¡¡FELICITACIONES!!! 💍🥂

**Paquete Luna de Miel Cancún:**
✨ Todo lo del paquete normal +
🍾 Champagne + fresas en la habitación
🌹 Decoración romántica (pétalos de rosa)
🍽️ Cena romántica en la playa (1 noche)
💆 Masaje de pareja en el spa
📸 Sesión de fotos profesional
🛏️ Upgrade automático a suite

**Precio:** USD 2.600 (solo USD 200 más)

🎁 **Regalo especial:** Álbum digital de la luna de miel

¿Para cuándo es la boda? 😍"""
    
    # Respuesta 12: Aventura/solo
    elif any(word in p for word in ["solo", "aventura", "mochilero", "backpacker"]):
        return """¡Perfecto! 🎒 Te armo algo épico.

**Ruta Aventura México (10 días):**
🏛️ **Día 1-2:** CDMX (Teotihuacán, museos)
🏖️ **Día 3-5:** Playa del Carmen (buceo, cenotes)
🌴 **Día 6-7:** Tulum (ruinas, playa)
🏔️ **Día 8-10:** Chiapas (selva, cascadas)

**Incluye:**
✅ Vuelos internos
✅ Hostels/hoteles
✅ Todas las excursiones
✅ Grupo de viajeros solos (conocés gente)

**Precio:** USD 1.800 (todo incluido)

¿Te copa este estilo o preferís más playa?"""
    
    # Respuesta 13: Reservar/comprar
    elif any(word in p for word in ["reservar", "comprar", "quiero", "dale", "sí", "si"]):
        return """¡GENIAAAL! 🎉

**Para confirmar necesito:**
📝 Datos de los pasajeros (nombre completo, DNI, fecha nac.)
📧 Email de contacto
📱 WhatsApp

**Opciones para continuar:**
💬 **Opción 1:** Seguimos por WhatsApp (+54 9 11 1234-5678)
   → Te mando formulario + link de pago

📞 **Opción 2:** Te llamo en 5 minutos
   → Cerramos todo por teléfono

📧 **Opción 3:** Te mando todo por email

¿Cuál preferís? 😊"""
    
    # Respuesta 14: Otras opciones
    elif any(word in p for word in ["punta cana", "brasil", "florianopolis", "floripa"]):
        return """¡Excelente opción también! 🏝️

**Punta Cana:**
• 7 días all inclusive: USD 1.350/persona
• Resort 5 estrellas
• Playa Bávaro

**Florianópolis:**
• 5 días hotel boutique: USD 800/persona
• 42 playas diferentes
• Vida nocturna
• Más económico

¿Querés que te arme un paquete detallado de alguno?"""
    
    # Respuesta por defecto
    else:
        return """Interesante pregunta! 🤔

Puedo ayudarte con:
• 🌍 Destinos y paquetes
• 💰 Precios y formas de pago
• 📋 Requisitos (visa, pasaporte)
• 🛡️ Seguros de viaje
• 🔄 Cambios y cancelaciones
• 👨‍👩‍👧‍👦 Paquetes familiares
• 💍 Luna de miel
• 🎒 Viajes de aventura

¿Sobre qué querés saber más?"""

# Procesar input del usuario o botón de sugerencia
if "temp_input" in st.session_state:
    prompt = st.session_state.temp_input
    del st.session_state.temp_input
    
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Obtener respuesta
    response = get_bot_response(prompt)
    
    # Agregar respuesta del bot
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Input del chat
if prompt := st.chat_input("Escribí tu pregunta..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtener respuesta del bot
    response = get_bot_response(prompt)
    
    # Agregar respuesta del bot
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.markdown(response)

# Footer
st.divider()
st.caption("💡 **Este es un demo interactivo.** El bot responde con información de ejemplo.")
st.caption("🔒 En producción conecta con tu base de datos real y APIs de viajes.")

# Botón para resetear conversación
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": """¡Hola! 👋 Te ayudo a encontrar tu viaje perfecto.

**Decime:**
• ¿Playa o montaña?
• ¿Aventura o relax?
• ¿Presupuesto? (económico/medio/premium)
• ¿Cuándo querés viajar?

💡 **Trending ahora:** Bariloche nieve ❄️ | Caribe playas 🏝️ | Europa cultura 🏛️"""
            }
        ]
        st.rerun()
