import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS SUPER VISUAL
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
    
    /* Calendario super visual */
    .calendar-wrapper {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 20px 0;
    }
    
    .calendar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid #e5e7eb;
    }
    
    .calendar-title {
        font-size: 20px;
        font-weight: 700;
        color: #1f2937;
    }
    
    .calendar-legend {
        display: flex;
        gap: 15px;
        font-size: 12px;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 10px;
        margin-top: 15px;
    }
    
    .calendar-day {
        aspect-ratio: 1;
        padding: 12px 8px;
        text-align: center;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 90px;
    }
    
    .calendar-day:hover {
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 8px 25px rgba(74, 144, 226, 0.25);
        z-index: 10;
    }
    
    /* Estilos por disponibilidad */
    .day-excellent {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border: 2px solid #22c55e;
        color: #166534;
    }
    
    .day-excellent:hover {
        background: linear-gradient(135deg, #bbf7d0 0%, #86efac 100%);
        border-color: #16a34a;
    }
    
    .day-good {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
        border: 2px solid #0ea5e9;
        color: #075985;
    }
    
    .day-good:hover {
        background: linear-gradient(135deg, #bae6fd 0%, #7dd3fc 100%);
        border-color: #0284c7;
    }
    
    .day-few {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 2px solid #f59e0b;
        color: #92400e;
    }
    
    .day-few:hover {
        background: linear-gradient(135deg, #fde68a 0%, #fcd34d 100%);
        border-color: #d97706;
    }
    
    .day-closed {
        background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
        border: 2px solid #d1d5db;
        color: #9ca3af;
        cursor: not-allowed;
        opacity: 0.6;
    }
    
    .day-closed:hover {
        transform: none;
        box-shadow: none;
    }
    
    .day-number {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 4px;
        line-height: 1;
    }
    
    .day-name {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
        opacity: 0.8;
    }
    
    .day-slots {
        font-size: 12px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Horarios visuales */
    .time-slots-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
        gap: 10px;
        margin: 20px 0;
    }
    
    .time-slot-btn {
        padding: 14px;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
        font-size: 15px;
        cursor: pointer;
        transition: all 0.2s;
        border: 2px solid #e5e7eb;
        background: white;
    }
    
    .time-slot-available {
        border-color: #4a90e2;
        color: #4a90e2;
    }
    
    .time-slot-available:hover {
        background: #4a90e2;
        color: white;
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
    }
    
    .time-slot-taken {
        background: #f3f4f6;
        border-color: #d1d5db;
        color: #9ca3af;
        cursor: not-allowed;
        text-decoration: line-through;
    }
    
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 10px; padding: 16px 24px; font-weight: 600;
        font-size: 15px; transition: all 0.3s ease; border: 2px solid #e5e7eb;
        background: white; color: #374151; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    div[data-testid="column"] > div > div > button:hover {
        background: #4a90e2; border-color: #4a90e2; color: white;
        transform: translateY(-2px); box-shadow: 0 6px 16px rgba(74, 144, 226, 0.3);
    }
    
    .section-header {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 4px solid #4a90e2;
        padding: 12px 16px;
        border-radius: 8px;
        margin: 20px 0 15px 0;
        font-weight: 600;
        color: #075985;
    }
</style>
""", unsafe_allow_html=True)

# Badge
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #4a90e2 0%, #5ba3f5 100%);
        color: white; padding: 10px 24px; border-radius: 25px; font-weight: 600; font-size: 14px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.4);">
        🎯 Imaginate este demo con tus datos - Tu agenda, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot - Reservá tu Turno</h1>
    <p>Sistema inteligente de gestión de turnos - Simple, rápido y efectivo</p>
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

**Reservá en 3 simples pasos:**
1️⃣ Elegí el día en el calendario
2️⃣ Seleccioná el horario
3️⃣ Confirmá tus datos

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

def get_calendar_visual():
    """Genera calendario SUPER visual con CSS"""
    today = datetime.now()
    
    # Disponibilidad simulada
    availability = {
        0: ("excellent", 8, "🟢"),  # Lunes
        1: ("excellent", 9, "🟢"),  # Martes
        2: ("good", 7, "🔵"),        # Miércoles
        3: ("excellent", 8, "🟢"),  # Jueves
        4: ("few", 6, "🟡"),         # Viernes
        5: ("few", 3, "🟡"),         # Sábado
        6: ("closed", 0, "⚫"),      # Domingo
    }
    
    html = """
    <div class="calendar-wrapper">
        <div class="calendar-header">
            <div class="calendar-title">📅 Calendario de Turnos - Próximos 14 Días</div>
            <div class="calendar-legend">
                <div class="legend-item"><span>🟢</span> Muchos turnos</div>
                <div class="legend-item"><span>🔵</span> Disponible</div>
                <div class="legend-item"><span>🟡</span> Pocos turnos</div>
                <div class="legend-item"><span>⚫</span> Cerrado</div>
            </div>
        </div>
        <div class="calendar-grid">
    """
    
    day_names = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    
    for i in range(14):
        date = today + timedelta(days=i)
        day_num = date.day
        day_name = day_names[date.weekday()]
        month = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"][date.month - 1]
        
        style_class, slots, emoji = availability[date.weekday()]
        
        if slots == 0:
            status_text = "Cerrado"
        else:
            status_text = f"{slots} turnos"
        
        html += f"""
            <div class="calendar-day day-{style_class}">
                <div class="day-name">{day_name}</div>
                <div class="day-number">{day_num}</div>
                <div style="font-size: 10px; opacity: 0.7; margin-bottom: 4px;">{month}</div>
                <div class="day-slots">{emoji} {status_text}</div>
            </div>
        """
    
    html += """
        </div>
        <p style="text-align: center; margin-top: 20px; color: #6b7280; font-size: 13px;">
            💡 <strong>Tip:</strong> Clickeá en un día para ver los horarios disponibles o usá los botones de acceso rápido abajo
        </p>
    </div>
    """
    
    return html

def get_time_slots_visual(fecha):
    """Genera horarios visuales"""
    morning = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30"]
    afternoon = ["14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"]
    
    occupied = ["10:00", "15:00", "17:00"]
    
    html = f"""
    <div style="background: white; padding: 24px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <div style="text-align: center; margin-bottom: 20px;">
            <h3 style="margin: 0; color: #1f2937; font-size: 22px;">⏰ Horarios Disponibles</h3>
            <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 14px;">{fecha}</p>
        </div>
        
        <div class="section-header">🌅 Turno Mañana (9:00 - 13:00)</div>
        <div class="time-slots-grid">
    """
    
    for slot in morning:
        if slot in occupied:
            html += f'<div class="time-slot-btn time-slot-taken">{slot}</div>'
        else:
            html += f'<div class="time-slot-btn time-slot-available">{slot}</div>'
    
    html += """
        </div>
        
        <div class="section-header">🌇 Turno Tarde (14:00 - 19:00)</div>
        <div class="time-slots-grid">
    """
    
    for slot in afternoon:
        if slot in occupied:
            html += f'<div class="time-slot-btn time-slot-taken">{slot}</div>'
        else:
            html += f'<div class="time-slot-btn time-slot-available">{slot}</div>'
    
    html += """
        </div>
        
        <div style="background: #f0f9ff; border-radius: 8px; padding: 12px; margin-top: 20px;">
            <p style="margin: 0; color: #0369a1; font-size: 13px; text-align: center;">
                💡 <strong>Menos espera:</strong> 9:00am, 11:00am y 14:30pm | 
                <strong>Más pedidos:</strong> 10:00am, 15:00pm, 17:00pm
            </p>
        </div>
    </div>
    """
    
    return html

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # VER CALENDARIO
    if any(k in p for k in ["calendario", "disponible", "turno", "reserva", "agenda", "ver", "mostrar"]):
        calendar_html = get_calendar_visual()
        
        return {
            "content": f"""{calendar_html}

**🎯 Para reservar tu turno:**

Usá los botones de acceso rápido abajo o escribí directamente:
- "Quiero el martes 30"
- "Dame turno para el jueves"
- "El viernes 2"

👇 **Días más solicitados**""",
            "buttons": "fecha_rapida",
            "bonus_once": True
        }
    
    # SELECCIÓN DE DÍA
    if any(k in p for k in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado"]) or any(k in p for k in ["30", "31", "1", "2", "3"]):
        
        if "martes" in p or "30" in p:
            fecha = "Martes 30 de Enero"
        elif "miercoles" in p or "miércoles" in p or "31" in p:
            fecha = "Miércoles 31 de Enero"
        elif "jueves" in p or "1" in p:
            fecha = "Jueves 1 de Febrero"
        elif "viernes" in p or "2" in p:
            fecha = "Viernes 2 de Febrero"
        else:
            fecha = "Martes 30 de Enero"
        
        st.session_state.selected_date = fecha
        
        time_html = get_time_slots_visual(fecha)
        
        return {
            "content": f"""✅ **¡Perfecto! Elegiste {fecha}**

{time_html}

**Para elegir tu horario:**

Seleccioná con los botones rápidos o escribí:
- "Quiero a las 9:30"
- "El de las 14:00"  
- "15:30 por favor"

👇 **Horarios populares**""",
            "buttons": "horario_rapido"
        }
    
    # SELECCIÓN HORARIO
    if any(h in p for h in ["9:", "10:", "11:", "12:", "14:", "15:", "16:", "17:", "18:"]):
        if "9:30" in p or "930" in p:
            hora = "09:30"
        elif "14:00" in p or "1400" in p or "14" in p:
            hora = "14:00"
        elif "15:30" in p or "1530" in p:
            hora = "15:30"
        elif "11" in p:
            hora = "11:00"
        else:
            hora = "14:00"
        
        st.session_state.selected_time = hora
        fecha = st.session_state.selected_date or "Martes 30 de Enero"
        
        return {
            "content": f"""🎉 **¡Turno Pre-Reservado!**

<div style="background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); border-radius: 16px; padding: 24px; border-left: 6px solid #0ea5e9; margin: 20px 0;">
    <h3 style="margin: 0 0 15px 0; color: #075985;">📋 Resumen de Tu Turno</h3>
    <div style="display: grid; gap: 10px;">
        <div style="display: flex; gap: 10px; align-items: center;">
            <span style="font-size: 20px;">📅</span>
            <div><strong>Fecha:</strong> {fecha}</div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <span style="font-size: 20px;">🕐</span>
            <div><strong>Hora:</strong> {hora}</div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <span style="font-size: 20px;">⏱️</span>
            <div><strong>Duración:</strong> 30-45 minutos</div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <span style="font-size: 20px;">📍</span>
            <div><strong>Lugar:</strong> Av. 18 de Julio 1850</div>
        </div>
    </div>
</div>

**✅ Para CONFIRMAR necesito tus datos:**

Por favor escribí en este formato:
`Nombre completo, Teléfono, Email`

**Ejemplo:**
`Juan Pérez, 099123456, juan@email.com`

---

**🔔 Al confirmar recibirás:**
✅ Email de confirmación inmediata
✅ Recordatorio WhatsApp 24hs antes
✅ SMS 2 horas antes del turno
✅ Link para agregar a tu calendario

**📋 Recordá traer:**
• Documento de identidad
• Credencial (si tenés)
• Estudios previos

💬 **Escribí tus datos para confirmar**""",
            "buttons": "confirmar_directo"
        }
    
    # CONFIRMACIÓN
    if (any(k in p for k in ["confirmo", "confirmar", "ok"]) and ("@" in p or "099" in p or "098" in p)):
        return {
            "content": """✅ **¡TURNO CONFIRMADO!** 🎉

<div style="background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); border-radius: 16px; padding: 32px; text-align: center; border: 3px solid #22c55e; margin: 20px 0;">
    <div style="font-size: 48px; margin-bottom: 10px;">✓</div>
    <h2 style="margin: 0; color: #166534;">¡Tu turno está confirmado!</h2>
    <p style="margin: 10px 0 0 0; color: #166534; font-size: 16px;">Código: <strong>#TURNO-300124-1400</strong></p>
</div>

**📋 DETALLES:**

<div style="background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 15px 0;">
    <div style="display: grid; gap: 12px;">
        <div style="border-left: 4px solid #4a90e2; padding-left: 12px;">
            <div style="color: #6b7280; font-size: 12px;">FECHA Y HORA</div>
            <div style="font-size: 18px; font-weight: 600; color: #1f2937;">Martes 30 de Enero - 14:00hs</div>
        </div>
        <div style="border-left: 4px solid #4a90e2; padding-left: 12px;">
            <div style="color: #6b7280; font-size: 12px;">PACIENTE</div>
            <div style="font-size: 16px; font-weight: 600; color: #1f2937;">Juan Pérez</div>
        </div>
        <div style="border-left: 4px solid #4a90e2; padding-left: 12px;">
            <div style="color: #6b7280; font-size: 12px;">CONTACTO</div>
            <div style="font-size: 16px; color: #1f2937;">📱 099 123 456 | ✉️ juan@email.com</div>
        </div>
        <div style="border-left: 4px solid #4a90e2; padding-left: 12px;">
            <div style="color: #6b7280; font-size: 12px;">UBICACIÓN</div>
            <div style="font-size: 16px; color: #1f2937;">Av. 18 de Julio 1850, Montevideo</div>
        </div>
    </div>
</div>

**📨 YA TE ENVIAMOS:**

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 15px 0;">
    <div style="background: #f0fdf4; padding: 12px; border-radius: 8px; text-align: center;">
        <div style="font-size: 24px;">📧</div>
        <div style="font-size: 13px; font-weight: 600; color: #166534;">Email Enviado ✅</div>
    </div>
    <div style="background: #f0f9ff; padding: 12px; border-radius: 8px; text-align: center;">
        <div style="font-size: 24px;">📅</div>
        <div style="font-size: 13px; font-weight: 600; color: #075985;">Google Calendar ✅</div>
    </div>
    <div style="background: #fef3c7; padding: 12px; border-radius: 8px; text-align: center;">
        <div style="font-size: 24px;">📱</div>
        <div style="font-size: 13px; font-weight: 600; color: #92400e;">WhatsApp 24hs ⏰</div>
    </div>
    <div style="background: #f3e8ff; padding: 12px; border-radius: 8px; text-align: center;">
        <div style="font-size: 24px;">💬</div>
        <div style="font-size: 13px; font-weight: 600; color: #6b21a8;">SMS 2hs ⏰</div>
    </div>
</div>

**🗺️ CÓMO LLEGAR:**

🚇 Metro Tres Cruces (3 cuadras)
🚌 Ómnibus 64, 180, 187, 121
🚗 Estacionamiento en la puerta

**📋 QUÉ TRAER:**

✓ Documento de identidad
✓ Credencial mutual (si tenés)
✓ Estudios previos
✓ Lista de medicamentos

---

**¿Necesitás cambiar o cancelar?**
Avisá con 24hs: 📱 099 123 456

**¡Nos vemos el martes 30! 😊**""",
            "buttons": "post_confirmacion"
        }
    
    # CANCELAR/CAMBIAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

**¿QUÉ NECESITÁS HACER?**

Usá los botones o escribí directamente

**Para cambiar o cancelar dame:**
• Tu nombre
• Fecha del turno
• Hora del turno

**Ejemplo:**
"Juan Pérez, turno martes 30/1 a las 14:00, quiero cambiar al jueves 1/2"

---

**📋 POLÍTICAS:**

✅ +48hs: Cambio/Cancelación gratis
✅ 24-48hs: Sin problema
⚠️ -24hs: Avisá igual

**📱 Contacto rápido:**
WhatsApp: 099 123 456
Tel: 2908 5555""",
            "buttons": "gestion_turno"
        }
    
    # INFO
    if any(k in p for k in ["horario", "donde", "dónde", "ubicacion", "ubicación", "info"]):
        return {
            "content": """ℹ️ **Información del Consultorio**

**⏰ HORARIOS:**
• Lun-Vie: 9:00-13:00 y 14:30-19:00
• Sábados: 9:00-13:00

**📍 UBICACIÓN:**
Av. 18 de Julio 1850, Montevideo

**🚇 CÓMO LLEGAR:**
• Metro Tres Cruces (3 cuadras)
• Ómnibus 64, 180, 187

**📞 CONTACTO:**
• Tel: 2908 5555
• WhatsApp: 099 123 456

¿Querés reservar un turno?""",
            "buttons": "info_acciones"
        }
    
    # DEFAULT
    return {
        "content": """❓ **¿Qué necesitás?**

**Elegí una opción:**

📅 **Ver calendario** - Mirá todos los días disponibles
🔄 **Gestionar turno** - Cambiar o cancelar
ℹ️ **Información** - Horarios y ubicación

**O escribí directamente:**
"Ver calendario"
"Cambiar mi turno"
"Dónde queda"

¿Qué hacemos?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)
        
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
                    if st.button("🔵 Mié 31 - 7 turnos", key=f"mie_{i}", use_container_width=True):
                        r = get_response("miércoles 31")
                        add_msg("Miércoles 31 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🟢 Jue 1 - 8 turnos", key=f"jue_{i}", use_container_width=True):
                        r = get_response("jueves 1")
                        add_msg("Jueves 1 de Febrero", r["content"], r.get("buttons"))
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
                    if st.button("📅 Ver Calendario", key=f"cal_h_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Info", key=f"info_h_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Info", r["content"], r.get("buttons"))
                        st.rerun()

# EJEMPLOS
st.markdown("---")
st.markdown("**💬 Probá estas consultas:**")

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
st.caption("💡 Demo con calendario visual interactivo - Sistema profesional de turnos")
st.caption("🔌 En producción sincroniza con tu agenda, WhatsApp API y sistema de pagos")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
