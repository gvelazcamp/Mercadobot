import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stChatMessage { max-width: 900px; margin: 0 auto; }
    .stChatFloatingInputContainer { max-width: 900px; margin: 0 auto; }
    .custom-header {
        text-align: center; padding: 25px;
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        border-radius: 12px; margin-bottom: 30px; color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .custom-header h1 { margin: 0; font-size: 28px; font-weight: 600; }
    .custom-header p { margin: 10px 0 0 0; opacity: 0.9; font-size: 15px; }
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 10px; padding: 16px 24px; font-weight: 600;
        font-size: 15px; transition: all 0.3s ease; border: 2px solid #e5e7eb;
        background: white; color: #374151; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div[data-testid="column"] > div > div > button:hover {
        background: #4a90e2; border-color: #4a90e2; color: white;
        transform: translateY(-2px); box-shadow: 0 6px 16px rgba(74, 144, 226, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #4a90e2 0%, #5ba3f5 100%);
        color: white; padding: 10px 24px; border-radius: 25px; font-weight: 600; font-size: 14px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.4);">
        🎯 Imaginate este demo con tus datos - Tu agenda, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot - Reservá tu Turno</h1>
    <p>Sistema inteligente de gestión de turnos</p>
</div>
""", unsafe_allow_html=True)

BONUS = "Este asistente gestiona tu agenda automáticamente, envía recordatorios y reduce inasistencias hasta un 60%."

def maybe_bonus():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"💡 **{BONUS}**",
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """¡Hola! 👋 Soy tu asistente de turnos

**Reservá en 3 pasos:**
1️⃣ Elegí el día  
2️⃣ Seleccioná horario  
3️⃣ Confirmá datos

**Ventajas:**
⚡ Rápido (30 segundos)
🔔 Recordatorios automáticos
🌙 Disponible 24/7

¿Empezamos?""",
        "show_buttons": "inicial"
    }]

if "selected_date" not in st.session_state:
    st.session_state.selected_date = None
if "selected_time" not in st.session_state:
    st.session_state.selected_time = None
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

def add_msg(user, bot, btns=None, bonus=False):
    st.session_state.messages.append({"role": "user", "content": user})
    st.session_state.messages.append({"role": "assistant", "content": bot, "show_buttons": btns})
    if bonus:
        maybe_bonus()

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # VER CALENDARIO
    if any(k in p for k in ["calendario", "disponible", "turno", "reserva", "agenda", "ver"]):
        return {
            "content": """📅 **Turnos Disponibles - Próximos 14 Días**

**🟢 DÍAS CON MUCHOS TURNOS (6-9 espacios):**
• Lun 29 Ene - 8 turnos ✅
• Mar 30 Ene - 9 turnos ✅ ⭐ Mejor día
• Mié 31 Ene - 7 turnos ✅
• Jue 1 Feb - 8 turnos ✅
• Lun 5 Feb - 8 turnos ✅
• Mar 6 Feb - 9 turnos ✅
• Jue 8 Feb - 8 turnos ✅

**🟡 DÍAS CON POCOS TURNOS (3-5 espacios):**
• Vie 2 Feb - 6 turnos ⚡
• Sáb 3 Feb - 3 turnos ⚠️
• Vie 9 Feb - 6 turnos ⚡
• Sáb 10 Feb - 3 turnos ⚠️

**⚫ CERRADO:**
• Dom 4 Feb - Cerrado ❌
• Dom 11 Feb - Cerrado ❌

---

**💡 RECOMENDACIONES:**
✅ **Más disponibilidad:** Martes y Jueves
⚠️ **Reservá con anticipación:** Sábados
🌟 **Mejor día esta semana:** Martes 30 (9 turnos)

**🎯 PARA RESERVAR:**
Elegí un día usando los botones o escribí:
• "Quiero el martes 30"
• "Dame turno jueves 1"
• "El viernes 2"

👇 **Días más solicitados**""",
            "buttons": "fecha_rapida",
            "bonus_once": True
        }
    
    # SELECCIÓN DE DÍA
    if any(k in p for k in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado"]) or any(k in p for k in ["30", "31", "1", "2"]):
        
        if "martes" in p or "30" in p:
            fecha = "Martes 30 de Enero"
            emoji = "🟢"
            espacios = 9
        elif "miercoles" in p or "miércoles" in p or "31" in p:
            fecha = "Miércoles 31 de Enero"
            emoji = "🟢"
            espacios = 7
        elif "jueves" in p or "1" in p:
            fecha = "Jueves 1 de Febrero"
            emoji = "🟢"
            espacios = 8
        elif "viernes" in p or "2" in p:
            fecha = "Viernes 2 de Febrero"
            emoji = "🟡"
            espacios = 6
        else:
            fecha = "Martes 30 de Enero"
            emoji = "🟢"
            espacios = 9
        
        st.session_state.selected_date = fecha
        
        return {
            "content": f"""✅ **{emoji} {fecha}** ({espacios} espacios)

⏰ **Horarios Disponibles**

**🌅 TURNO MAÑANA (9:00 - 13:00)**

✅ Disponibles:
• 09:00 | 09:30 | 10:30 | 11:00
• 11:30 | 12:00 | 12:30

❌ Ocupados:
• 10:00

**🌇 TURNO TARDE (14:00 - 19:00)**

✅ Disponibles:
• 14:00 | 14:30 | 15:30 | 16:00
• 16:30 | 17:30 | 18:00

❌ Ocupados:
• 15:00 | 17:00

---

**💡 MENOS ESPERA:**
• Mañana: 9:00, 9:30, 11:00
• Tarde: 14:00, 14:30, 16:00

**🎯 ELEGÍ TU HORARIO:**
• "Quiero a las 9:30"
• "El de las 14:00"
• "15:30 por favor"

👇 **Horarios populares**""",
            "buttons": "horario_rapido"
        }
    
    # SELECCIÓN HORARIO
    if any(h in p for h in ["9:", "10:", "11:", "12:", "14:", "15:", "16:", "17:", "18:"]):
        if "9:30" in p or "930" in p:
            hora = "09:30"
        elif "14:00" in p or "1400" in p or "14" in p:
            hora = "14:00"
        elif "15:30" in p:
            hora = "15:30"
        elif "11" in p:
            hora = "11:00"
        else:
            hora = "14:00"
        
        st.session_state.selected_time = hora
        fecha = st.session_state.selected_date or "Martes 30 de Enero"
        
        return {
            "content": f"""🎉 **¡Turno Pre-Reservado!**

**📋 RESUMEN:**

📅 **Fecha:** {fecha}  
🕐 **Hora:** {hora}  
⏱️ **Duración:** 30-45 minutos  
📍 **Lugar:** Av. 18 de Julio 1850

---

**✅ PARA CONFIRMAR:**

Dame tus datos en este formato:
`Nombre, Teléfono, Email`

**Ejemplo:**
`Juan Pérez, 099123456, juan@email.com`

---

**🔔 AL CONFIRMAR RECIBIRÁS:**
✅ Email confirmación (inmediato)
✅ Recordatorio WhatsApp (24hs antes)
✅ SMS recordatorio (2hs antes)
✅ Link Google Calendar

**📋 TRAÉ:**
• Documento de identidad
• Credencial (si tenés)

💬 **Escribí tus datos**""",
            "buttons": "confirmar_directo"
        }
    
    # CONFIRMACIÓN
    if (any(k in p for k in ["confirmo", "confirmar", "ok"]) and ("@" in p or "099" in p or "098" in p)):
        return {
            "content": """✅ **¡TURNO CONFIRMADO!** 🎉

**📋 DETALLES:**

📅 Martes 30 de Enero 2024 - 14:00hs  
👤 Juan Pérez  
📱 099 123 456  
✉️ juan@email.com  
📍 Av. 18 de Julio 1850

🔖 **Código:** #TURNO-300124-1400

---

**📨 ENVIADO:**
✅ Email confirmación ✅  
✅ Google Calendar ✅  
⏰ WhatsApp 24hs antes (programado)  
⏰ SMS 2hs antes (programado)

---

**🗺️ CÓMO LLEGAR:**
🚇 Metro Tres Cruces (3 cuadras)  
🚌 Ómnibus 64, 180, 187  
🚗 Estacionamiento en la puerta

**📋 QUÉ TRAER:**
• Documento de identidad
• Credencial mutual (si tenés)
• Estudios previos

---

**¿Cambiar o cancelar?**
📱 Avisá con 24hs: 099 123 456

**¡Nos vemos el martes 30! 😊**""",
            "buttons": "post_confirmacion"
        }
    
    # CANCELAR/CAMBIAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

**Dame estos datos:**
• Tu nombre
• Fecha del turno
• Hora del turno

**Si es cambio, también:**
• Nueva fecha preferida

---

**📋 POLÍTICAS:**
✅ +48hs: Sin cargo, cambio libre  
✅ 24-48hs: Sin problema  
⚠️ -24hs: Avisá igual

**📱 CONTACTO:**
• WhatsApp: 099 123 456
• Tel: 2908 5555

**Ejemplo:**
"Juan Pérez, turno martes 30/1 a las 14:00, quiero cambiar al jueves 1/2"

¿Qué turno gestionar?""",
            "buttons": "gestion_turno"
        }
    
    # INFO
    if any(k in p for k in ["horario", "donde", "dónde", "ubicacion", "ubicación", "info"]):
        return {
            "content": """ℹ️ **Información del Consultorio**

**⏰ HORARIOS:**
• Lun-Vie: 9:00-13:00 y 14:30-19:00
• Sábados: 9:00-13:00
• Domingos: Cerrado

**📍 UBICACIÓN:**
Av. 18 de Julio 1850, Montevideo

**🚇 CÓMO LLEGAR:**
• Metro Tres Cruces (3 cuadras)
• Ómnibus 64, 180, 187

**📞 CONTACTO:**
• Tel: 2908 5555
• WhatsApp: 099 123 456

¿Reservar turno?""",
            "buttons": "info_acciones"
        }
    
    # DEFAULT
    return {
        "content": """❓ **¿Qué necesitás?**

📅 **Ver calendario** - Todos los días  
🔄 **Gestionar turno** - Cambiar/cancelar  
ℹ️ **Información** - Horarios/ubicación

**Escribí:**
• "Ver calendario"
• "Cambiar turno"
• "Información"

¿Qué hacemos?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        if msg.get("show_buttons"):
            bt = msg["show_buttons"]
            
            if bt == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver Calendario", key=f"cal_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"), r.get("bonus_once"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Información", key=f"info_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver información", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "fecha_rapida":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🟢 Mar 30 - 9 turnos", key=f"mar_{i}", use_container_width=True):
                        r = get_response("martes 30")
                        add_msg("Martes 30 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🟢 Jue 1 - 8 turnos", key=f"jue_{i}", use_container_width=True):
                        r = get_response("jueves 1")
                        add_msg("Jueves 1 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🟢 Mié 31 - 7 turnos", key=f"mie_{i}", use_container_width=True):
                        r = get_response("miércoles 31")
                        add_msg("Miércoles 31 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🟡 Vie 2 - 6 turnos", key=f"vie_{i}", use_container_width=True):
                        r = get_response("viernes 2")
                        add_msg("Viernes 2 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "horario_rapido":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🌅 09:30", key=f"h1_{i}", use_container_width=True):
                        r = get_response("9:30")
                        add_msg("09:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🌅 11:00", key=f"h2_{i}", use_container_width=True):
                        r = get_response("11:00")
                        add_msg("11:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("🌇 14:00", key=f"h3_{i}", use_container_width=True):
                        r = get_response("14:00")
                        add_msg("14:00", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🌇 15:30", key=f"h4_{i}", use_container_width=True):
                        r = get_response("15:30")
                        add_msg("15:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🌇 16:00", key=f"h5_{i}", use_container_width=True):
                        r = get_response("16:00")
                        add_msg("16:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("🌇 18:00", key=f"h6_{i}", use_container_width=True):
                        r = get_response("18:00")
                        add_msg("18:00", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Calendario", key=f"cal_h_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Info", key=f"info_h_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Info", r["content"], r.get("buttons"))
                        st.rerun()

# EJEMPLOS SIMPLES
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("**📅 Reservar:**")
    st.caption("• Ver calendario")
    st.caption("• Martes 30")
    st.caption("• A las 14:00")
    st.caption("• Confirmo")

with col2:
    st.caption("**🔄 Gestionar:**")
    st.caption("• Cambiar turno")
    st.caption("• Cancelar")
    st.caption("• No puedo ir")
    st.caption("• Reprogramar")

with col3:
    st.caption("**ℹ️ Info:**")
    st.caption("• Dónde queda")
    st.caption("• Horarios")
    st.caption("• Cómo llego")
    st.caption("• Teléfono")

# Input
if prompt := st.chat_input("Escribí tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    r = get_response(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": r["content"],
        "show_buttons": r.get("buttons")
    })
    if r.get("bonus_once"):
        maybe_bonus()
    st.rerun()

# Footer
st.divider()
st.caption("💡 Demo profesional - Sistema de turnos con recordatorios automáticos")
st.caption("🔌 En producción sincroniza con tu agenda, WhatsApp API y sistema de pagos")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
